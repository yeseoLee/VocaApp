import sqlite3
import os

DB_PATH = "voca.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    c = conn.cursor()
    
    # Create sentences table
    c.execute('''
        CREATE TABLE IF NOT EXISTS sentences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_text TEXT NOT NULL,
            translated_text TEXT,
            pdf_source TEXT,
            difficulty TEXT
        )
    ''')
    
    # Create words table
    c.execute('''
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sentence_id INTEGER,
            original_word TEXT NOT NULL,
            translated_meaning TEXT,
            position_index INTEGER,
            FOREIGN KEY (sentence_id) REFERENCES sentences (id)
        )
    ''')
    
    conn.commit()
    conn.close()
