import sys
import os
from .db import init_db
from .etl import run_etl
from .quiz import start_quiz

def main():
    if len(sys.argv) < 2:
        print("Usage: python -m src.main [etl|quiz]")
        return

    command = sys.argv[1]
    
    # Ensure DB is initialized
    init_db()

    if command == "etl":
        # Default to data folder
        data_dir = os.path.join(os.getcwd(), "data")
        pdf_file = "Intern Script.pdf" # Hardcoded for now based on request, or scan folder
        pdf_path = os.path.join(data_dir, pdf_file)
        
        if not os.path.exists(pdf_path):
            print(f"Error: {pdf_path} not found.")
            return
            
        run_etl(pdf_path)
        
    elif command == "quiz":
        try:
            num = int(input("How many words do you want to study? "))
            start_quiz(num)
        except ValueError:
            print("Please enter a valid number.")
            
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
