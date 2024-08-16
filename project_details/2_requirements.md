## Requirements

### Functional Requirements
- **Expense Logging:**
   -  The bot must allow users to log expenses by specifying the amount paid, payment method, and date.
   - The bot must prompt the user to specify what expense they are going to pay from a predefined list:
     - Acueducto
     - Claro
     - Gas natural (VANTI)
     - ENEL Codensa
     - Administración
     - Plan complementario Diego B
     - EPS Mary Espitia
     - Plan complementario Mary E
     - Spotify
     - Microsoft
     - Movil Data
     - Amazon Prime
     - Disney + | Star +
   - The bot must handle cases where users input incorrect expense names by suggesting the closest matching predefined category and asking for confirmation.
   
- **Add New Expense Category:** The bot must allow users to add new expense categories to the predefined list.
- **Expense Listing** The bot must provide a command to retrieve and display a list of all logged expenses, including details such as the amount, payment method, description, and date.
- **Expense Deletion:** The bot must allow users to delete specific expenses by providing the unique ID of the expense entry.
- **Database Management:** The bot must store and manage expense data in an SQLite database, ensuring data integrity and accessibility.
- **Expense Reporting:** 
   - The bot must provide a command to generate a report summarizing the logged expenses.
   - The report should use basic generative AI and NLU to analyze and summarize the data.

### Non-Functional Requirements
- **Usability:** The bot's commands must be intuitive and easy to use, requiring minimal user input for maximum functionality.
- **Performance:** The bot must respond to commands promptly, with minimal latency.
- **Reliability:** The bot must perform consistently under normal operating conditions without crashing or producing errors.
- **Maintainability:** The code must be well-documented and modular to allow for easy updates and maintenance.

### Software Requirements
- **Programming Language:** Python 3.x
- **Development Environment:** Visual Studio Code

### Technical Requirements
- **Discord API:** The bot must utilize the Discord API for interacting with users on Discord.
- **SQLite:** The bot must use SQLite for local data storage and management.
- **Generative AI and NLU:** Integrate basic generative AI and NLU capabilities to analyze and summarize expense data for reporting.
- **Hosting:** Initially developed on a local machine; optional cloud hosting (e.g., AWS, Heroku) for deployment.

### Libraries
- **discord.py:** For interacting with the Discord API.
- **sqlite3:** For database management.
- **NLTK or SpaCy:**  For natural language understanding and processing.
- **OpenAI GPT (or similar):**  For generative AI to create summary reports.

### Testing Requirements
- **Unit Testing:** The bot’s functions must be unit tested to ensure they perform as expected.
- **Integration Testing:** Test the bot's interaction with the Discord API and SQLite database to ensure seamless integration.
- **User Acceptance Testing:** Perform testing with actual users to validate that the bot meets user needs and functional requirements.

### Quality Assurance Requirements
- **Code Review:** Conduct code reviews to ensure adherence to coding standards and best practices.
- **Documentation:** Ensure comprehensive documentation is provided for setup, usage, and maintenance.

### Security Requirements
- **Token Management:** Securely store and manage the Discord bot token to prevent unauthorized access.
- **Data Security:** Ensure that expense data stored in the SQLite database is secure and not accessible to unauthorized users.
- **Input Validation:** Implement input validation to prevent SQL injection and other security vulnerabilities.
## Refined Project Plan Additions

### Command Aliases
- **Objective:** Enhance usability by providing shorter or alternative command options.
- **Example:** `!log` as an alias for `!log_expense`.
- **Implementation:** Introduce an alias system within the command structure. Ensure that the bot recognizes both the full command and its alias.

### Expense Categorization
- **Objective:** Help users organize their expenses better by introducing categories.
- **Example:** Allow users to tag expenses with categories like “utilities,” “subscriptions,” etc.
- **Implementation:** Add a tagging system when logging expenses, allowing users to assign categories. Update the database schema to accommodate categories.

### Monthly Summary Command
- **Objective:** Provide a quick overview of expenses without the need for a full report.
- **Example:** `!monthly_summary` command that displays total spending by category for the current month.
- **Implementation:** Implement a command that aggregates expenses by category and displays the totals for the current month.

### Data Backup/Export Feature
- **Objective:** Ensure users don’t lose their data and can export it for external use.
- **Example:** `!export_data` command to export data to a CSV file.
- **Implementation:** Add a feature to export the SQLite database entries to a CSV file, which can be triggered by the user through a command.

### Basic Budgeting Feature
- **Objective:** Allow users to compare expenses against budget limits.
- **Example:** Users can set a monthly budget for categories, and the bot can notify them when they're close to or exceed their limits.
- **Implementation:** Add budget setting commands and track expenses against these budgets, with automated notifications.

### Customization of Responses
- **Objective:** Personalize the user experience by allowing customization of the bot’s tone.
- **Example:** Users can choose between formal, casual, or humorous responses.
- **Implementation:** Add user settings to select response styles and modify command responses based on user preference.

### Automated Data Cleaning
- **Objective:** Maintain data integrity with minimal user intervention.
- **Example:** Regular prompts to correct or confirm duplicate or suspicious entries.
- **Implementation:** Implement checks for duplicates or anomalies in the data and notify users for confirmation or correction.

## Refined Project Plan Removals or Simplifications

### Generative AI for Reports
- **Why:** Simplifying the bot to provide structured, text-based reports without the complexity of AI.
- **Alternative:** Focus on clear, structured summaries with key statistics.

### Natural Language Processing (NLP)
- **Why:** Avoid potential complexity and unreliability in interpreting user inputs.
- **Alternative:** Use a structured input format with command suggestions to reduce ambiguity.

### Integration with External APIs
- **Why:** Maintain simplicity by avoiding unnecessary external dependencies unless clearly justified.
- **Alternative:** Keep all functionalities local to the bot for better control and reliability.

## Refined Project Plan Enhancements to Existing Features

### Improved Error Handling
- **Objective:** Simplify debugging and enhance the user experience.
- **Example:** Provide detailed and helpful error messages, including corrective suggestions.
- **Implementation:** Update error handling across all commands to offer more user-friendly feedback.

### Interactive Setup Process
- **Objective:** Simplify the onboarding experience.
- **Example:** Guide new users through the initial setup and demonstrate command usage.
- **Implementation:** Add an interactive tutorial that activates on first use, guiding users through setting up and using basic commands.

### More Robust Testing Framework
- **Objective:** Ensure the bot remains stable as new features are added.
- **Example:** Expand test coverage, focusing on edge cases and various user input scenarios.
- **Implementation:** Enhance the testing framework to cover more scenarios, including edge cases, user input variations, and database integrity.
