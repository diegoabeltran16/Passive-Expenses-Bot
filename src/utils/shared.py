# src/utils/shared.py

from src.utils.db import connect_db

def set_user_language(user_id, language):
    """
    Sets the user's preferred language in the database.
    If the user already has a language set, it updates the language.
    """
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO user_language (user_id, language)
                VALUES (?, ?)
                ON CONFLICT(user_id) DO UPDATE SET language=excluded.language
            ''', (user_id, language))
            conn.commit()
        except Exception as e:
            print(f"Error setting user language: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database.")

def get_user_language(user_id):
    """
    Retrieves the user's preferred language from the database.
    If no language is set, defaults to English ('en').
    """
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT language FROM user_language WHERE user_id = ?', (user_id,))
            result = cursor.fetchone()
            if result:
                return result[0]
        except Exception as e:
            print(f"Error retrieving user language: {e}")
        finally:
            conn.close()
    else:
        print("Failed to connect to the database.")
        
    return 'en'  # Default to English if no language is set
