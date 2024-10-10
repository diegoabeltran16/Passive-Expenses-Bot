# src/utils/lang.py

## General Description
The main goal of this script is to provide a multilingual translation system for a bot, allowing it to support multiple languages when generating responses. It contains a dictionary of translation templates for different messages in English and Spanish, and a function that retrieves and formats these messages based on the user-specified language and message parameters.

## Pseudocode
```
1. **Define a Translation Dictionary**
   - Create a dictionary named `translations`.
   - Define keys for supported languages (e.g., "en" for English, "es" for Spanish).
   - Store translation templates for various messages like "expense_logged", "expense_deleted", etc.
   - Each template contains placeholders (e.g., `{id}`, `{amount}`) for formatting.

2. **Function to Retrieve Translated Message**
   - Define a function named `translate` that takes the following parameters:
     - `message_key`: The key representing the message to translate.
     - `language`: The language in which the message should be translated (default is "en").
     - `**kwargs`: Additional arguments used to format the message placeholders.
   - **Log the Translation Request**
     - Print a log statement for debugging purposes that shows which message is being translated to which language, along with values to be formatted.
   - **Check if the Language is Supported**
     - If the provided language is not available in the `translations` dictionary, default to English.
   - **Retrieve and Format the Message**
     - Use the `message_key` to get the appropriate message template from the `translations` dictionary for the specified language.
     - Format the message using `**kwargs` to replace placeholders.
   - **Return the Translated Message**
```

## Code

```
# lang.py

# Translation dictionary for supported languages
translations = {
    "en": {
        "expense_logged": "Expense logged with ID {id}: {amount} for {description}.",
        "expense_deleted": "Expense with ID {id} deleted.",
        "no_expenses_found": "No expenses found.",
        "here_are_your_expenses": "Here are your expenses:",
        "expense_updated": "Expense with ID {id} has been updated with amount {amount} and description '{description}'.",
        "update_failed": "Failed to update expense: {error}",
        "language_set": "Language has been set to {language_value}.",  # Updated placeholder name
        "report_generated": "Expense report for {start_date} to {end_date}:",
        "category_total": "- {category}: {total_spent}",
        "no_report_data": "No expenses found for the given period.",
        "budget_exceeded": "You have exceeded your budget for {category}! Total spent: {total_spent}, Budget: {budget}.",
        "within_budget": "You are within your budget for {category}. Total spent: {total_spent}, Budget: {budget}.",
        "no_budget_set": "No budget set for this category."
    },
    "es": {
        "expense_logged": "Gasto registrado con ID {id}: {amount} por {description}.",
        "expense_deleted": "Gasto con ID {id} eliminado.",
        "no_expenses_found": "No se encontraron gastos.",
        "here_are_your_expenses": "Aquí están tus gastos:",
        "expense_updated": "Gasto con ID {id} se ha actualizado con la cantidad {amount} y descripción '{description}'.",
        "update_failed": "No se pudo actualizar el gasto: {error}",
        "language_set": "El idioma ha sido establecido a {language_value}.",  # Updated placeholder name
        "report_generated": "Informe de gastos desde {start_date} hasta {end_date}:",
        "category_total": "- {category}: {total_spent}",
        "no_report_data": "No se encontraron gastos para el periodo dado.",
        "budget_exceeded": "Has excedido tu presupuesto para {category}! Total gastado: {total_spent}, Presupuesto: {budget}.",
        "within_budget": "Estás dentro de tu presupuesto para {category}. Total gastado: {total_spent}, Presupuesto: {budget}.",
        "no_budget_set": "No se ha establecido un presupuesto para esta categoría."
    }
}

# Function to retrieve the translated message
def translate(message_key, language="en", **kwargs):
    print(f"Translating '{message_key}' to '{language}' with values {kwargs}")
    if language not in translations:
        language = "en"
    message_template = translations[language].get(message_key, "")
    return message_template.format(**kwargs)

```
## Testing 
tests/test_lang.py

**Main Goal:**
The main goal of this code is to test the functionality of the `translate` function, which is responsible for providing translations for different messages in English and Spanish. The tests ensure that the `translate` function works as expected for valid translations and handles invalid keys appropriately.

### Testing Pseudocode
```
1. Import the necessary modules:
    - Import `unittest` for testing framework.
    - Import `sys` and `os` to manipulate system paths.
    - Import `translate` from `utils.lang` to be tested.

2. Define a class `TestTranslation` that inherits from `unittest.TestCase`.

3. Define the method `test_translation_to_english` to verify English translations:
    - Call `translate` with parameters:
        - message_key: "expense_logged"
        - language: "en"
        - id: 1, amount: 100, description: "Lunch"
    - Assert that the result matches the expected English message: 
      "Expense logged with ID 1: 100 for Lunch."

4. Define the method `test_translation_to_spanish` to verify Spanish translations:
    - Call `translate` with parameters:
        - message_key: "expense_logged"
        - language: "es"
        - id: 1, amount: 100, description: "Almuerzo"
    - Assert that the result matches the expected Spanish message:
      "Gasto registrado con ID 1: 100 por Almuerzo."

5. Define the method `test_invalid_translation_key` to verify handling of invalid translation keys:
    - Call `translate` with parameters:
        - message_key: "invalid_key"
        - language: "en"
    - Assert that the result is an empty string, indicating no matching translation found.

6. Run the test cases using `unittest.main()` to execute the defined test cases when the script is run.
```

### Testing Code
```
import unittest
import sys
import os

# Add the 'src' directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from utils.lang import translate

class TestTranslation(unittest.TestCase):

    def test_translation_to_english(self):
        """Test translating a message to English."""
        result = translate("expense_logged", "en", id=1, amount=100, description="Lunch")
        self.assertEqual(result, "Expense logged with ID 1: 100 for Lunch.")

    def test_translation_to_spanish(self):
        """Test translating a message to Spanish."""
        result = translate("expense_logged", "es", id=1, amount=100, description="Almuerzo")
        self.assertEqual(result, "Gasto registrado con ID 1: 100 por Almuerzo.")

    def test_invalid_translation_key(self):
        """Test handling of invalid translation keys."""
        result = translate("invalid_key", "en")
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()

```
