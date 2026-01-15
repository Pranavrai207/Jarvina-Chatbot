import os
from tinydb import TinyDB, Query
from datetime import datetime

class Database:
    """
    Handles all database operations for the chatbot using TinyDB.
    Manages both conversation history and user-saved notes.
    """
    def __init__(self, db_folder='database'):
        """
        Initializes the databases, creating the folder if it doesn't exist.
        """
        # Ensure the database directory exists
        if not os.path.exists(db_folder):
            os.makedirs(db_folder)
            print(f"Created directory: {db_folder}")

        # Initialize chat history database
        history_db_path = os.path.join(db_folder, 'chat_history.json')
        self.history_db = TinyDB(history_db_path)
        print(f"Chat history database initialized at: {history_db_path}")
        
        # Initialize notes database
        notes_db_path = os.path.join(db_folder, 'notes.json')
        self.notes_db = TinyDB(notes_db_path)
        print(f"Notes database initialized at: {notes_db_path}")


    def add_conversation(self, role: str, content: str):
        """
        Adds a new conversation entry to the chat history database.
        """
        if not isinstance(role, str) or not isinstance(content, str):
            print("Error: Role and content must be strings.")
            return

        self.history_db.insert({
            'role': role,
            'content': content,
            'timestamp': datetime.now().isoformat()
        })
        print(f"Saved message from '{role}' to the chat history.")

    def add_note(self, content: str):
        """
        Adds a new note to the notes database.
        """
        if not isinstance(content, str):
            print("Error: Note content must be a string.")
            return

        self.notes_db.insert({
            'note': content,
            'timestamp': datetime.now().isoformat()
        })
        print(f"Saved note to the database: '{content[:50]}...'")

    def get_conversations(self, limit: int = 20):
        """
        Retrieves the most recent conversations from the chat history database.
        """
        all_conversations = self.history_db.all()
        return all_conversations[-limit:]
    
    def get_notes(self, limit: int = 20):
        """
        Retrieves the most recent notes from the notes database.
        """
        all_notes = self.notes_db.all()
        return all_notes[-limit:]


    def clear_history_database(self):
        """
        Clears all entries from the chat history database.
        """
        self.history_db.truncate()
        print("Chat history database has been cleared.")
        
    def clear_notes_database(self):
        """
        Clears all entries from the notes database.
        """
        self.notes_db.truncate()
        print("Notes database has been cleared.")

# Example of how to use the updated Database class
if __name__ == '__main__':
    db = Database()

    # Clear databases for a fresh start
    db.clear_history_database()
    db.clear_notes_database()

    # Add some sample conversations
    db.add_conversation('user', 'Hello, how are you?')
    db.add_conversation('assistant', 'I am doing well, thank you!')

    # Add a sample note
    db.add_note('This is an important piece of information to remember.')

    # Retrieve and print recent conversations
    print("\n--- Recent Conversations ---")
    recent_chats = db.get_conversations(limit=5)
    for chat in recent_chats:
        print(f"[{chat['timestamp']}] {chat['role'].title()}: {chat['content']}")

    # Retrieve and print recent notes
    print("\n--- Recent Notes ---")
    recent_notes = db.get_notes(limit=5)
    for note in recent_notes:
        print(f"[{note['timestamp']}] Note: {note['note']}")

