# src/utils/shared.py

from src.utils.db import connect_db

def set_user_language(user_id, language):
    """
    Sets the user's preferred language in the database.
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

def get_user_language(user_id):
    """
    Retrieves the user's preferred language from the database. Defaults to 'en' if not set.
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
    return 'en'  # Default to English if no language is set
