# Diccionario de traducción para inglés y español
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

# Función para obtener el mensaje traducido
def translate(message_key, language="en", **kwargs):
    """
    Traduce un mensaje basado en la preferencia de idioma del usuario.

    Parámetros:
    -----------
    message_key : str
        La clave que identifica el mensaje en el diccionario de traducción.
    language : str
        El idioma al que se traducirá el mensaje ('en' para inglés, 'es' para español).
    kwargs : dict
        Cualquier valor adicional que se necesite para formatear la cadena traducida 
        (por ejemplo, 'amount', 'description', 'id').

    Retorna:
    --------
    str:
        El mensaje traducido con los valores formateados.
    """
    # Mensaje de depuración para verificar que la función de traducción está siendo invocada
    print(f"Translating '{message_key}' to '{language}' with values {kwargs}")

    # Verifica si el idioma solicitado está en el diccionario de traducciones
    if language not in translations:
        language = "en"  # Si el idioma no está soportado, se utiliza inglés por defecto

    # Obtiene la plantilla de mensaje para la clave y el idioma especificados
    message_template = translations[language].get(message_key, "")
    
    # Mensaje de depuración para confirmar la traducción que se va a retornar
    print(f"Translation result: {message_template.format(**kwargs)}")
    
    # Retorna el mensaje traducido con los valores formateados
    return message_template.format(**kwargs)
