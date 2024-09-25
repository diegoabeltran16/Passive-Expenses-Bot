# Cycle 1 - Implementing the Passive Expenses Bot

## Abstract
The primary objectives for cycle #1 were to build a foundational Passive Expenses Bot with essential functionality, focusing on four key goals: configuring the project directory structure, setting up and integrating SQLite for expense management, developing basic CRUD operations, and implementing multilingual support for more inclusive user interactions. Throughout this process, we aimed to ensure the bot could log, list, update, and delete expenses while allowing users to switch between English and Spanish seamlessly. This cycle provided the groundwork for a robust and extendable bot, preparing us for more advanced features in the next stages.

## Development Process and Problem-Solving

1. Configuring the Project Directory Structure

We began by establishing a clean and well-organized project structure, critical for the scalability and maintainability of the Passive Expenses Bot. The directory setup included separate folders for commands, utils, config, and others. Each module had a dedicated purpose:

commands housed the individual features (e.g., log_expense, delete_expense),
utils contained utility files like db.py and lang.py,
config stored the config.yaml file with the bot's configuration details.
This structure allowed us to maintain clarity and separation of concerns, which is vital in a growing project. One challenge encountered during this step was ensuring all dependencies and modules could be correctly imported across the different folders. We resolved this by thoroughly testing the import paths and adjusting our PYTHONPATH to match the project hierarchy.

2. Implementing SQLite Database and CRUD Operations

The next milestone was setting up the SQLite database, which provided a lightweight solution for managing expenses. We created a dedicated db.py file in the utils directory, where we wrote functions to handle database interactions, such as connect_db(), create_expenses_table(), add_expense(), list_expenses(), update_expense(), and delete_expense().

One issue encountered was ensuring the database file (expenses.db) was correctly created and accessible within the project structure. Additionally, integrating the CRUD operations with the Discord bot commands required careful handling of asynchronous function calls, as SQLite operations are synchronous. We resolved this by maintaining efficient and straightforward function structures and using proper error handling to avoid potential crashes or data inconsistencies.

The CRUD functionality testing was another challenge, but we used SQLite extensions within Visual Studio Code to validate data entries directly, ensuring our commands correctly interacted with the database.

3. Developing Command Modules and Handling User Interactions

To manage expenses, we developed command modules within the commands directory for log_expense, delete_expense, list_expenses, and update_expense. Each module was designed as a Discord Cog, allowing us to modularize functionality. We ensured the commands were correctly registered with the bot and could interact with the SQLite database.

One significant obstacle was ensuring the bot correctly processed each command and interacted with the database without errors. We experienced issues such as "command not found" errors and data inconsistency problems. These were resolved by carefully debugging the command registration process, testing each CRUD operation, and refining the database interaction functions.

4. Implementing Multilingual Support

The final objective of cycle #1 was to introduce multilingual support for user interactions, enabling the bot to respond in either English or Spanish based on user preferences. This involved creating a lang.py file in the utils directory, which contained a translation dictionary and a translate() function. We developed a set_language command that allowed users to set their preferred language, stored in a shared user_language dictionary.

The most significant hurdle in this stage was ensuring that the bot correctly remembered the user's language preference across different commands. Initially, we noticed that the language setting wasn't being retained, which led to responses defaulting to English. We resolved this by creating a shared.py module to store and share the user_language dictionary across different command modules, thus maintaining the user’s language preference throughout their session.

We thoroughly tested the multilingual feature, confirming that the bot's responses adapted correctly based on user settings. Debugging statements helped us trace the flow of data and ensured that translations were accurately applied.

## Conclusion
Cycle #1 has successfully established the Passive Expenses Bot as a functional, multilingual expense management tool within Discord. By integrating SQLite for data persistence, implementing core CRUD operations, and enabling multilingual support, we have created a strong foundation for a versatile and user-friendly bot. The challenges we faced, particularly with maintaining consistent language settings and integrating database functionality, provided valuable insights into managing a scalable Discord bot project.

## Next Steps: Preparing for Cycle #2
In the next cycle, we aim to introduce more advanced features, such as generating expense reports, setting budgets, and integrating natural language understanding to allow more intuitive user interactions. The work accomplished in cycle #1 will be pivotal as it ensures a robust command structure, data handling capability, and a flexible language setting mechanism. This foundation will allow us to seamlessly build upon existing functionality and introduce more complex features, ensuring that the Passive Expenses Bot continues to evolve into a more comprehensive financial management tool.

By leveraging the solid groundwork laid in cycle #1, we can now confidently approach the advanced objectives planned for the upcoming cycle, enhancing the bot's intelligence, efficiency, and overall user experience.