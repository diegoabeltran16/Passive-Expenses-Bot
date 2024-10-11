# Translation dictionary for supported languages
translations = {
    "en": {
        "expense_logged": "Expense logged with ID {id}: {amount} for {description}.",
        "expense_deleted": "Expense with ID {id} deleted.",
        "no_expenses_found": "No expenses found.",
        "here_are_your_expenses": "Here are your expenses:",
        "expense_updated": "Expense with ID {id} has been updated with amount {amount} and description '{description}'.",
        "update_failed": "Failed to update expense: {error}",
        "language_set": "Language has been set to {language_value}.",
        "report_generated": "Expense report for {start_date} to {end_date}:",
        "category_total": "- {category}: {total_spent}",
        "no_report_data": "No expenses found for the given period.",
        "budget_exceeded": "You have exceeded your budget for {category}! Total spent: {total_spent}, Budget: {budget}.",
        "within_budget": "You are within your budget for {category}. Total spent: {total_spent}, Budget: {budget}.",
        "no_budget_set": "No budget set for this category.",
        "reports_table_created": "Reports table created successfully.",
        "error_creating_table": "Error creating reports table: {error}",
        "reports_table_dropped": "Reports table dropped successfully.",
        "error_dropping_table": "Error dropping reports table: {error}",
        "error_connecting_db": "Error connecting to the database: {error}",
        "report_inserted": "Report inserted with ID {id}.",
        "error_inserting_report": "Error inserting report: {error}",
        "reports_retrieved": "Reports retrieved for user {user_id}.",
        "error_retrieving_reports": "Error retrieving reports: {error}",
        "report_deleted": "Report with ID {id} deleted.",
        "error_deleting_report": "Error deleting report: {error}",
        # New translations for report commands
        "report_logged": "Report '{name}' logged with file path '{file_path}'.",
        "no_reports_found": "No reports found for your account.",
        "reports_listed": "Your reports:\n{reports}",
        "report_deleted_confirmation": "Report with ID {id} has been deleted successfully.",
        "error_logging_report": "An error occurred while logging the report: {error}",
        "error_deleting_report": "An error occurred while deleting the report: {error}",
        # New translations for report generator
        "report_generated": "Report generated successfully.",
        "report_generation_failed": "Failed to generate the report.",
        "report_format_not_supported": "The report format '{format}' is not supported.",
        "report_no_data": "No data available for the selected filters.",
        "report_file_saved": "Report saved at: {file_path}",
        # New translations for file manager
        "file_saved": "File saved at: {file_path}.",
        "file_retrieved": "File retrieved: {file_path}.",
        "file_deleted": "File deleted successfully.",
        "file_not_found": "File not found at: {file_path}.",
        "error_saving_file": "Error saving file: {error}",
        "error_retrieving_file": "Error retrieving file: {error}",
        "error_deleting_file": "Error deleting file: {error}",
        # Translations for generate_report command
        "pdf_report_generated": "PDF report generated: {file_path}",
        "text_report_generated": "Text report generated successfully.",
        "report_format_not_supported": "The report format '{format}' is not supported.",
        "report_generation_failed": "Failed to generate report: {error}",

    },
    "es": {
        "expense_logged": "Gasto registrado con ID {id}: {amount} por {description}.",
        "expense_deleted": "Gasto con ID {id} eliminado.",
        "no_expenses_found": "No se encontraron gastos.",
        "here_are_your_expenses": "Aquí están tus gastos:",
        "expense_updated": "Gasto con ID {id} se ha actualizado con la cantidad {amount} y descripción '{description}'.",
        "update_failed": "No se pudo actualizar el gasto: {error}",
        "language_set": "El idioma ha sido establecido a {language_value}.",
        "report_generated": "Informe de gastos desde {start_date} hasta {end_date}:",
        "category_total": "- {category}: {total_spent}",
        "no_report_data": "No se encontraron gastos para el periodo dado.",
        "budget_exceeded": "Has excedido tu presupuesto para {category}! Total gastado: {total_spent}, Presupuesto: {budget}.",
        "within_budget": "Estás dentro de tu presupuesto para {category}. Total gastado: {total_spent}, Presupuesto: {budget}.",
        "no_budget_set": "No se ha establecido un presupuesto para esta categoría.",
        "reports_table_created": "La tabla de informes se ha creado con éxito.",
        "error_creating_table": "Error al crear la tabla de informes: {error}",
        "reports_table_dropped": "La tabla de informes se ha eliminado con éxito.",
        "error_dropping_table": "Error al eliminar la tabla de informes: {error}",
        "error_connecting_db": "Error al conectar con la base de datos: {error}",
        "report_inserted": "Informe insertado con ID {id}.",
        "error_inserting_report": "Error al insertar informe: {error}",
        "reports_retrieved": "Informes recuperados para el usuario {user_id}.",
        "error_retrieving_reports": "Error al recuperar informes: {error}",
        "report_deleted": "Informe con ID {id} eliminado.",
        "error_deleting_report": "Error al eliminar informe: {error}",
        # New translations for report commands
        "report_logged": "Informe '{name}' registrado con ruta de archivo '{file_path}'.",
        "no_reports_found": "No se encontraron informes para tu cuenta.",
        "reports_listed": "Tus informes:\n{reports}",
        "report_deleted_confirmation": "Informe con ID {id} ha sido eliminado con éxito.",
        "error_logging_report": "Ocurrió un error al registrar el informe: {error}",
        "error_deleting_report": "Ocurrió un error al eliminar el informe: {error}",
        # New translations for report generator
        "report_generated": "Informe generado con éxito.",
        "report_generation_failed": "No se pudo generar el informe.",
        "report_format_not_supported": "El formato de informe '{format}' no es compatible.",
        "report_no_data": "No hay datos disponibles para los filtros seleccionados.",
        "report_file_saved": "Informe guardado en: {file_path}",
        # New translations for file manager
        "file_saved": "Archivo guardado en: {file_path}.",
        "file_retrieved": "Archivo recuperado: {file_path}.",
        "file_deleted": "Archivo eliminado con éxito.",
        "file_not_found": "Archivo no encontrado en: {file_path}.",
        "error_saving_file": "Error al guardar el archivo: {error}",
        "error_retrieving_file": "Error al recuperar el archivo: {error}",
        "error_deleting_file": "Error al eliminar el archivo: {error}",
        # Translations for generate_report command
        "pdf_report_generated": "Informe PDF generado: {file_path}",
        "text_report_generated": "Informe de texto generado con éxito.",
        "report_generation_failed": "No se pudo generar el informe: {error}",

    }
}

# Function to retrieve the translated message
def translate(message_key, language="en", **kwargs):
    print(f"Translating '{message_key}' to '{language}' with values {kwargs}")
    if language not in translations:
        language = "en"
    message_template = translations[language].get(message_key, "")
    return message_template.format(**kwargs)
