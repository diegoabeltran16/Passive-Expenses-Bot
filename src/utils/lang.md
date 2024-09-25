# lang

## Descripción general
Este módulo proporciona un sistema de traducción para el bot, permitiendo que los mensajes se generen en inglés o español según la preferencia del usuario. Incluye un diccionario de traducciones para ambas lenguas y una función translate que obtiene la traducción correcta basada en una clave y el idioma especificado.

## Codigo

```
# Diccionario de traducción para inglés y español
translations = {
    "en": {
        "expense_logged": "Expense logged with ID {id}: {amount} for {description}.",
        "expense_deleted": "Expense with ID {id} deleted.",
        "no_expenses_found": "No expenses found.",
        "here_are_your_expenses": "Here are your expenses:",
        "expense_updated": "Expense with ID {id} has been updated with amount {amount} and description '{description}'.",
        "update_failed": "Failed to update expense: {error}"
    },
    "es": {
        "expense_logged": "Gasto registrado con ID {id}: {amount} por {description}.",
        "expense_deleted": "Gasto con ID {id} eliminado.",
        "no_expenses_found": "No se encontraron gastos.",
        "here_are_your_expenses": "Aquí están tus gastos:",
        "expense_updated": "Gasto con ID {id} se ha actualizado con la cantidad {amount} y descripción '{description}'.",
        "update_failed": "No se pudo actualizar el gasto: {error}"
    }
}

# Función para traducir mensajes con soporte de valores dinámicos
def translate(message_key, language="en", **kwargs):
    """
    Traduce un mensaje basado en la clave proporcionada y el idioma especificado.

    Esta función busca la traducción correspondiente a la clave `message_key` en el idioma indicado por `language`.
    Si la traducción no se encuentra para el idioma especificado, se utilizará el inglés ("en") como idioma predeterminado.
    En caso de que la clave de traducción no esté presente en el diccionario, la función retornará un mensaje de
    advertencia para indicar que la traducción no fue encontrada.

    Parámetros:
    -----------
    message_key : str
        La clave que identifica el mensaje en el diccionario de traducción.
    language : str, opcional
        El idioma al que se desea traducir el mensaje. Por defecto es "en" (inglés).
    kwargs : dict
        Cualquier valor adicional que se necesite para formatear la cadena traducida (por ejemplo, 'amount', 
        'description', 'id', etc.).

    Retorna:
    --------
    str
        El mensaje traducido y formateado con los valores proporcionados. Si la clave de traducción no se encuentra,
        retorna un mensaje indicando que la traducción no está disponible.

    Ejemplo de uso:
    ---------------
    translate("expense_logged", "es", id=1, amount=100.0, description="Compra de supermercado")
    -> "Gasto registrado con ID 1: 100.0 por Compra de supermercado"
    """
    # Mensaje de depuración para verificar que la función de traducción está siendo invocada
    print(f"Traduciendo '{message_key}' al idioma '{language}' con los valores {kwargs}")

    # Verifica si el idioma solicitado está en el diccionario de traducciones
    if language not in translations:
        language = "en"  # Si el idioma no está soportado, se utiliza inglés por defecto

    # Obtiene la plantilla de mensaje para la clave y el idioma especificados
    message_template = translations[language].get(message_key, None)

    # Verifica si la plantilla de mensaje existe
    if not message_template:
        # Mensaje de advertencia si la clave de traducción no se encuentra
        print(f"Clave de traducción '{message_key}' no encontrada. Usando un mensaje por defecto.")
        return f"Traducción para '{message_key}' no encontrada."

    # Mensaje de depuración para confirmar la traducción que se va a retornar
    print(f"Resultado de la traducción: {message_template.format(**kwargs)}")

    # Retorna el mensaje traducido con los valores formateados
    return message_template.format(**kwargs)


```

## Pseudocodigo

```
# Definir el diccionario de traducción para los idiomas inglés y español
# Cada idioma tiene claves de mensaje con sus traducciones correspondientes
crear diccionario "translations" que contenga:
    "en" (inglés):
        "expense_logged": "Mensaje de gasto registrado con ID, cantidad y descripción."
        "expense_deleted": "Mensaje de gasto eliminado por ID."
        "no_expenses_found": "Mensaje de que no se encontraron gastos."
        "here_are_your_expenses": "Mensaje indicando que se listarán los gastos."
        "expense_updated": "Mensaje confirmando que un gasto ha sido actualizado con cantidad y descripción."
        "update_failed": "Mensaje indicando que la actualización del gasto falló con el error correspondiente."
    "es" (español):
        "expense_logged": "Mensaje de gasto registrado con ID, cantidad y descripción en español."
        "expense_deleted": "Mensaje de gasto eliminado por ID en español."
        "no_expenses_found": "Mensaje de que no se encontraron gastos en español."
        "here_are_your_expenses": "Mensaje indicando que se listarán los gastos en español."
        "expense_updated": "Mensaje confirmando que un gasto ha sido actualizado con cantidad y descripción en español."
        "update_failed": "Mensaje indicando que la actualización del gasto falló con el error correspondiente en español."

# Definir la función para traducir mensajes basada en el idioma y las claves de mensaje
definir función "translate" con parámetros (message_key, language="en", **kwargs):
    # Imprimir un mensaje de depuración para mostrar los valores que se intentan traducir
    imprimir "Traduciendo la clave de mensaje con el idioma y los valores específicos proporcionados"
    
    # Verificar si el idioma especificado está en el diccionario de traducciones
    si el idioma no está en el diccionario "translations":
        establecer idioma a "en"  # Usar inglés como idioma predeterminado si el idioma solicitado no es soportado
    
    # Obtener la plantilla de mensaje correspondiente al idioma y la clave de mensaje
    obtener "message_template" de "translations[language]" usando "message_key"
    
    # Verificar si la plantilla de mensaje existe
    si "message_template" es nulo o no encontrado:
        imprimir "Clave de traducción no encontrada. Usando un mensaje por defecto."
        retornar "Mensaje indicando que la traducción no fue encontrada para esa clave"
    
    # Imprimir un mensaje de depuración mostrando el resultado de la traducción
    imprimir "Resultado de la traducción con los valores proporcionados formateados"

    # Retornar la plantilla de mensaje formateada con los valores específicos proporcionados en kwargs
    retornar "message_template" formateada con "kwargs"


```




