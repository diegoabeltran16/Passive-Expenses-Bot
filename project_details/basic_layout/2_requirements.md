# Project Details

## Functional Requirements
- **Expense Logging:**
   - The bot must allow users to log expenses by specifying the amount paid, payment method, and date.
   - The bot must support both structured command inputs and natural language inputs in multiple languages (English and Spanish).
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
   - The bot must handle multilingual input and provide responses in the user's preferred language (English or Spanish).
   
- **Add New Expense Category:** The bot must allow users to add new expense categories to the predefined list.
- **Expense Listing:** The bot must provide a command to retrieve and display a list of all logged expenses, including details such as the amount, payment method, description, and date.
- **Expense Deletion:** The bot must allow users to delete specific expenses by providing the unique ID of the expense entry.
- **Database Management:** The bot must store and manage expense data in an SQLite database, ensuring data integrity and accessibility.
- **Expense Reporting:**
   - The bot must provide a command to generate a report summarizing the logged expenses.
   - The report should be clear and structured, providing key statistics without relying on complex AI analysis, though basic generative AI can be used if needed.
   - Reports should be available in both English and Spanish.

- **Monthly Summary Command:** The bot must allow users to quickly view total spending by category for the current month, without generating a full report.
- **Data Backup/Export:** The bot must support exporting expense data to a CSV file, ensuring that users don’t lose their data and can use it outside of Discord.
- **Basic Budgeting Feature:** The bot should allow users to set a monthly budget for different categories and notify them when they are close to or exceed their limits.
- **Customization of Responses:** The bot must allow users to customize the tone of its responses, with options for formal, casual, or humorous styles, in both English and Spanish.
- **Automated Data Cleaning:** The bot should regularly prompt users to correct or confirm duplicate or suspicious entries, maintaining data integrity.

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
- **NLTK or SpaCy:** For natural language understanding and processing.
- **OpenAI GPT (or similar):** For generative AI to create summary reports.

### Testing Requirements
- **Unit Testing:** The bot’s functions must be unit tested to ensure they perform as expected.
- **Integration Testing:** Test the bot's interaction with the Discord API and SQLite database to ensure seamless integration.
- **User Acceptance Testing:** Perform testing with actual users to validate that the bot meets user needs and functional requirements.
- **Input Variability:** The bot must be tested with a wide range of inputs, including both structured and unstructured language in English and Spanish, to ensure reliable performance across different interaction styles.
- **Natural Language Understanding:** The bot’s ability to understand and correctly interpret natural language inputs must be rigorously tested, ensuring that common phrases and variations are accurately processed.

### Quality Assurance Requirements
- **Code Review:** Conduct code reviews to ensure adherence to coding standards and best practices.
- **Documentation:** Ensure comprehensive documentation is provided for setup, usage, and maintenance.

### Security Requirements
- **Token Management:** Securely store and manage the Discord bot token to prevent unauthorized access.
- **Data Security:** Ensure that expense data stored in the SQLite database is secure and not accessible to unauthorized users.
- **Input Validation:** Implement input validation to prevent SQL injection and other security vulnerabilities.
