# Translation dictionary for English and Spanish
translations = {
    "en": {
        "expense_logged": "Expense logged with ID {id}: {amount} for {description}.",
        "expense_deleted": "Expense with ID {id} deleted.",
        "no_expenses_found": "No expenses found.",
        "here_are_your_expenses": "Here are your expenses:",
    },
    "es": {
        "expense_logged": "Gasto registrado con ID {id}: {amount} por {description}.",
        "expense_deleted": "Gasto con ID {id} eliminado.",
        "no_expenses_found": "No se encontraron gastos.",
        "here_are_your_expenses": "Aquí están tus gastos:",
    }
}

# Function to get translated message
def translate(message_key, language="en", **kwargs):
    """
    Translate a message based on the language preference.

    Parameters:
    -----------
    message_key : str
        The key to identify the message in the translation dictionary.
    language : str
        The language to translate the message into ('en' for English, 'es' for Spanish).
    kwargs : dict
        Any values to format into the translated string (e.g., amount, description, id).

    Returns:
    --------
    str:
        The translated message with values formatted.
    """
    # Debug print to check if translation function is working
    print(f"Translating '{message_key}' to '{language}' with values {kwargs}")

    if language not in translations:
        language = "en"  # Default to English if language not supported

    message_template = translations[language].get(message_key, "")
    
    # Another debug print to verify what is being returned
    print(f"Translation result: {message_template.format(**kwargs)}")
    
    return message_template.format(**kwargs)
