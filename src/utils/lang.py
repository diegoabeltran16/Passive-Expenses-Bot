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
