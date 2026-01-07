import sqlite3
from .db import get_connection
import random

def start_quiz(num_questions):
    conn = get_connection()
    c = conn.cursor()
    
    # Fetch words with their sentences
    c.execute('''
        SELECT w.original_word, w.translated_meaning, s.original_text, s.translated_text 
        FROM words w
        JOIN sentences s ON w.sentence_id = s.id
        ORDER BY RANDOM()
        LIMIT ?
    ''', (num_questions,))
    
    questions = c.fetchall()
    conn.close()
    
    if not questions:
        print("No words found in DB. Run ETL first.")
        return

    params = []
    # Structure: (word, meaning, sentence, sentence_trans)
    
    # Store questions in a list to manage retries
    quiz_queue = list(questions)
    
    while quiz_queue:
        q = quiz_queue.pop(0)
        word, meaning, sentence, s_trans = q
        
        print("\n" + "="*30)
        # Create blank
        question_sentence = sentence.replace(word, "______")
        print(f"Sentence: {question_sentence}")
        print(f"Meaning: {s_trans}")
        print(f"Word Meaning: {meaning}")
        
        user_input = input("Enter the missing word: ").strip()
        
        if user_input.lower() == word.lower():
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was: {word}")
            print("Adding back to queue...")
            quiz_queue.append(q)
            
    print("\nQuiz Completed! Great job.")
