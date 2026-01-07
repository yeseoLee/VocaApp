import pdfplumber
import re
from deep_translator import GoogleTranslator
from .db import get_connection

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    
    # Clean text: replace newlines with spaces and collapse multiple spaces
    text = text.replace('\n', ' ')
    text = re.sub(r'\s+', ' ', text)
    return text

def process_text(text):
    # Simple sentence splitting
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    filtered = []
    for s in sentences:
        s = s.strip()
        # Filter too short or garbage sentences
        if len(s.split()) > 3 and len(s) < 300:
             filtered.append(s)
    return filtered

def analyze_difficulty(sentence):
    # Placeholder for difficulty analysis
    length = len(sentence.split())
    if length > 20:
        return "Hard"
    elif length > 10:
        return "Medium"
    else:
        return "Easy"

def translate_text(text):
    try:
        return GoogleTranslator(source='auto', target='ko').translate(text)
    except Exception as e:
        print(f"Translation error: {e}")
        return None

def run_etl(pdf_path):
    print(f"Extracting from {pdf_path}...")
    raw_text = extract_text_from_pdf(pdf_path)
    sentences = process_text(raw_text)
    
    conn = get_connection()
    c = conn.cursor()
    
    print(f"Found {len(sentences)} sentences. Processing...")
    
    count = 0
    for s in sentences:  
        try:
            trans_s = translate_text(s)
            diff = analyze_difficulty(s)
            
            c.execute('INSERT INTO sentences (original_text, translated_text, pdf_source, difficulty) VALUES (?, ?, ?, ?)',
                      (s, trans_s, pdf_path, diff))
            sentence_id = c.lastrowid
            
            # Simple word extraction: pick a random word or longest word for quiz
            words = s.split()
            if words:
                # Pick the longest word as a candidate for the quiz
                target_word = max(words, key=len) 
                target_word_clean = re.sub(r'[^\w]', '', target_word) # clean punctuation
                
                if len(target_word_clean) > 3:
                     trans_w = translate_text(target_word_clean)
                     # Find position
                     try:
                         pos = words.index(target_word)
                     except ValueError:
                         pos = 0 # Fallback
                     
                     c.execute('INSERT INTO words (sentence_id, original_word, translated_meaning, position_index) VALUES (?, ?, ?, ?)',
                               (sentence_id, target_word_clean, trans_w, pos))
            
            count += 1
            if count % 5 == 0:
                print(f"Processed {count} sentences...")
                conn.commit()
                
        except Exception as e:
            print(f"Error processing sentence: {e} - skipping")
    
    conn.commit()
    conn.close()
    print("ETL Compelted.")
