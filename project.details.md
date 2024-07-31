# Passive Expenses Bot
Provide a simple tool for logging, viewing, and managing expenses, suitable for personal use and showcasing in a portfolio.

## Scope
The Passive Expenses Discord Bot is designed to help users manage and organize their passive expenses through a simple and intuitive interface within Discord. This project aims to provide a practical tool for logging, viewing, and managing expenses, tailored for personal use but robust enough to showcase in a portfolio. The bot leverages the Discord API and SQLite for seamless integration and reliable data management.

## Objectives
- Create a Discord bot that allows users to log, list, and delete their passive expenses through simple commands.
- Implement SQLite for secure and reliable data storage, ensuring that all expense data is accurately logged and easily retrievable.
- Design an intuitive command structure that allows users to interact with the bot effortlessly, making the process of logging and managing expenses straightforward.
- Showcase proficiency in Python programming, API integration with Discord, and database management through clear, well-documented code and functionality.
- Build the bot with a scalable architecture that allows for future enhancements, such as categorizing expenses, generating summary reports, and setting up notifications and alerts for recurring expenses.
- Provide comprehensive documentation that details the setup process, command usage, and includes examples of the bot in action, ensuring that the project is easy to understand and replicate.
- Thoroughly test the bot in a local Discord environment to identify and resolve any issues, ensuring that all commands work correctly and the bot performs reliably.

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

## Best Practices
### Project Organization
- **Structured Directory Layout:**
  - Organize the project into clear, separate directories for src, tests, docs, and configs.
  - Place source code files (bot.py, database.py) in the src directory.
  - Keep configuration files like requirements.txt and environment variable files in the configs directory.
- **Version Control:**
Use Git for version control.
Maintain a clean commit history with meaningful commit messages.
Use branches to develop new features and merge them into the main branch after thorough testing.
- **Documentation:**
  - Maintain comprehensive documentation in the docs directory.
  - Include setup instructions, usage guidelines, and API references.

### Coding Standards
- **Consistent Style:**
  - Follow PEP 8 guidelines for Python code.
  - Use a linter like flake8 to ensure code consistency.
- **Modular Code:**
  - Write modular code with functions and classes encapsulating specific functionalities.
  - Keep functions short and focused on a single task.
- **Code Comments:**
  - Use docstrings to document functions and classes.
  - Add comments to explain complex logic and algorithms.

### Error Handling and Logging
- **Comprehensive Error Handling:**
  - Use try-except blocks to handle potential errors gracefully.
  - Provide informative error messages to help with debugging.
- **Logging:**
  - Implement logging using Python’s logging module.
  - Log important events, errors, and user interactions at appropriate levels (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL).

### Database Management
- **Schema Design:**
  - Design a simple and effective database schema.
  - Use appropriate data types for each field.
- **Data Integrity:**
  - Ensure data integrity with constraints (e.g., NOT NULL, UNIQUE).
  - Regularly back up the database.
- **Efficient Queries:**
  - Optimize SQL queries for performance.
  - Use indexing where necessary.

### NLU Model
- **Model Selection:**
  - Choose a lightweight NLU model suitable for simple text processing, such as SpaCy.
  - Ensure the model is capable of handling the specific needs of the project.
- **Training and Fine-Tuning:**
  - Fine-tune the model with relevant data if necessary.
  - Continuously improve the model with new data.

### Generative AI Capabilities
- **Model Selection:**
  - Use a reliable generative AI model like OpenAI’s GPT for text generation.
  - Ensure the model can generate coherent and relevant summaries.
- **API Integration:**
  - Integrate the model through API calls.
  - Handle API responses effectively and ensure they are formatted correctly.

### Automation
- **Task Automation:**
  - Automate repetitive tasks such as database backups and report generation.
  - Use tools like cron jobs for scheduling tasks.
- **CI/CD Pipeline:**
  - Implement a CI/CD pipeline to automate testing and deployment.
  - Use platforms like GitHub Actions or Travis CI.

### Security Best Practices
- **Token Management:**
  - Securely store and manage the Discord bot token and other sensitive credentials.
  - Use environment variables to manage secrets.
- **Input Validation:**
  - Validate all user inputs to prevent SQL injection and other attacks.
  - Sanitize data before processing.
- **Data Encryption:**
  - Encrypt sensitive data stored in the database.
  - Use HTTPS for secure API communication.

### Testing and Development
- **Unit Testing:**
  - Write unit tests for individual functions and components.
  - Use a testing framework like pytest.
- **Integration Testing:**
  - Test the integration of different components such as the bot, database, and NLU model.
  - Ensure end-to-end functionality.
- **Test Coverage:**
  - Aim for high test coverage to ensure reliability.
  - Regularly run tests and fix any issues promptly.

### User Experience
- **User-Friendly Commands:**
  - Design intuitive commands that are easy to remember and use.
  - Provide clear instructions and feedback for each command.
- **Error Messages:**
  - Provide helpful error messages that guide the user on how to correct their input.
  - Avoid technical jargon in user-facing messages.
-**Report Generation:**
  - Ensure generated reports are clear, concise, and easy to understand.
  - Use formatting to enhance readability.

## Architecture
The Passive Expenses Discord Bot will be designed using a multi-layered architecture to ensure modularity, maintainability, and scalability. The architecture will consist of the following layers: Client Layer, Application Layer, Data Layer, and Integration Layer.

### Client Layer
- **Description:** This layer represents the user interface where users interact with the bot through Discord. It handles user commands and responses.
- **Components:** Discord Client: The interface through which users interact with the bot using Discord commands.
- **Responsibilities:**
  - Receive and interpret user commands.
  - Display responses and information to users.
  - Provide user feedback and error messages.
- **Breakdown**
  - Discord Client:
    - Utilizes discord.py to connect to Discord.
    - Handles events such as receiving messages and commands.
    - Sends responses back to the Discord server.

### Application Layer
- **Description:** This layer contains the core logic and functionality of the bot, including command handling, business logic, and interactions with other layers.
- **Components:**
  - **Command Handler:** Manages the various commands issued by the users and routes them to the appropriate functions.
  - **Business Logic:** Implements the core functionalities such as logging expenses, generating reports, and validating inputs.

- **Responsibilities:**
  - Process user commands and execute corresponding actions.
  - Handle business logic for expense management.
  - Ensure proper flow of data between the client layer and the data layer.
- **Breakdown:**
  - **Command Handler:**
    - Maps user commands to functions.
    - Validates user input and handles errors.
    - Coordinates with the business logic for processing commands.
  - **Business Logic:**
    - Implements expense logging by interacting with the data layer.
    - Generates reports by fetching data from the database and using generative AI.
    - Adds new expense categories and ensures they are stored correctly.

### Data Layer
- **Description:** This layer is responsible for data storage, retrieval, and management. It interacts with the database to perform CRUD operations.
- **Components:**
  - Database (SQLite): Stores expense data and other relevant information.
  - Data Access Objects (DAO): Interfaces for interacting with the database.

- **Responsibilities:**
  - Store and retrieve expense data.
  - Ensure data integrity and security.
  - Manage database schema and perform necessary migrations.

- **Breakdown:**
  - **Database (SQLite):**
    - Stores user expenses, categories, and other metadata.
    - Uses tables with fields such as id, amount, description, payment_method, and date.
  - **Data Access Objects (DAO):**
    - Provides methods for CRUD operations.
    - Ensures data is stored and retrieved efficiently.
    - Handles database connections and queries.

### Integration Layer
- **Description:** This layer handles integration with external services such as generative AI for report generation and NLU for understanding user input.
- **Components:**
  - Generative AI (OpenAI GPT): Generates summary reports and insights from expense data.
  - NLU Model (SpaCy or NLTK): Processes and understands user inputs for better interaction.
- **Responsibilities:**
  - Integrate with external APIs and services.
  - Process and analyze data using AI and NLU models.
  - Ensure seamless communication between the application layer and external services.
- **Breakdown:**
  - **Generative AI (OpenAI GPT):**
    - Generates natural language reports based on expense data.
    - Integrates via API calls, processing data and returning summaries.

  - **NLU Model (SpaCy or NLTK):**
    - Processes user inputs to understand and correct errors in expense names.
    - Enhances user interaction by providing accurate responses based on natural language understanding.

### Diagram Representation (Textual)
```
+-------------------+         +-------------------+         +-------------------+
|  Client Layer     | <----> | Application Layer  | <----> |   Data Layer       |
|  (Discord Client) |        | (Command Handler)  |        | (SQLite Database)  |
|                   |        | (Business Logic)   |        | (Data Access Obj.) |
+-------------------+         +-------------------+         +-------------------+
        ^                           ^
        |                           |
        v                           v
+-----------------------------------------------------+
|                  Integration Layer                  |
|   (Generative AI, NLU Model)                        |
|                                                     |
+-----------------------------------------------------+


```

## Components

### Discord Bot Interface
- Description: The main interface for user interaction, allowing users to issue commands and receive responses.
- Responsibilities:
  - Receive user commands through Discord.
  - Display responses and feedback to users.
  - Handle events such as message reception and command execution.

### NLU Component

- Description: Processes and understands user inputs to enhance interaction and correct potential errors in expense names.
- Responsibilities:
  - Use natural language processing (NLP) to interpret user inputs.
  - Suggest correct expense names if the input is incorrect.
  - Improve the user experience by understanding the context of inputs.

### Generative AI Component

- Description: Generates natural language reports and insights based on logged expense data.
- Responsibilities:
  - Create summaries and reports from the expense data.
  - Use generative AI models (e.g., OpenAI GPT) to produce coherent and relevant text.
  - Integrate via API calls to process and return data.

### User Input Analysis Component

- Description: Analyzes user inputs for accuracy and relevance.
- Responsibilities:
  - Validate user inputs to ensure they conform to expected formats.
  - Use NLU to interpret and correct user inputs.
  - Provide real-time feedback to users about the validity of their inputs.

### Prediction Component

- Description: Predicts user needs and provides intelligent suggestions based on historical data.
- Responsibilities:
  - Analyze past expense data to predict future expenses.
  - Suggest possible expenses based on user input patterns.
  - Enhance user interaction by providing context-aware suggestions.

### Database Management Component

- Description: Manages the storage, retrieval, and integrity of expense data.
- Responsibilities:
  - Store expense data securely in an SQLite database.
  - Perform CRUD (Create, Read, Update, Delete) operations.
  - Ensure data integrity and handle database schema migrations.

### Automation and Scheduling Component

- Description: Automates repetitive tasks and schedules regular operations.
- Responsibilities:
  - Automate database backups and maintenance tasks.
  - Schedule regular reports and notifications.
  - Use tools like cron jobs for task scheduling.

### Logging and Error Handling Component

- Description: Manages logging of system activities and handles errors gracefully.
- Responsibilities:
  - Log important events and errors using Python’s logging module.
  - Provide detailed error messages for debugging purposes.
  - Implement try-except blocks to catch and handle exceptions.

## Interaction Flow
The interaction less computerized and more interactive, we can incorporate more conversational elements, natural language responses, and a touch of personality to the bot. This can be achieved by using a mix of friendly prompts, confirmations, and feedback, making the interaction feel more like a natural conversation.

### Main Interaction Screen
- Description: The primary interface where users interact with the bot using conversational commands.
- Components:
  - Command Input: Area where users type commands.
  - Response Display: Area where the bot's responses are shown.

```
+--------------------------------------+
| Discord Interface                    |
|--------------------------------------|
| User: Hey bot, I need to log an      |
| expense                              |
|--------------------------------------|
| Bot: Sure thing! What did you spend  |
| on?                                  |
|--------------------------------------|
| User: Spotify                        |
|--------------------------------------|
| Bot: Got it! How much did you pay?   |
|--------------------------------------|
| User: 9.99                           |
|--------------------------------------|
| Bot: And how did you pay for it?     |
|--------------------------------------|
| User: Credit Card                    |
|--------------------------------------|
| Bot: Awesome! When was this? (YYYY-MM|
| -DD)                                 |
|--------------------------------------|
| User: 2024-07-29                     |
|--------------------------------------|
| Bot: Great! I’ve logged Spotify - $9.|
| 99 - Credit Card - 2024-07-29 for you|
+--------------------------------------+


```
### Logging an Expense
- Description: The sequence of interactions for logging an expense using conversational prompts.
- Components:
  - Prompts: Bot prompts for expense details.
  - User Inputs: User provides details in response to prompts.

```
+--------------------------------------+
| Discord Interface                    |
|--------------------------------------|
| User: Hey bot, I need to log an      |
| expense                              |
|--------------------------------------|
| Bot: Sure thing! What did you spend  |
| on?                                  |
|--------------------------------------|
| User: Spotify                        |
|--------------------------------------|
| Bot: Got it! How much did you pay?   |
|--------------------------------------|
| User: 9.99                           |
|--------------------------------------|
| Bot: And how did you pay for it?     |
|--------------------------------------|
| User: Credit Card                    |
|--------------------------------------|
| Bot: Awesome! When was this? (YYYY-MM|
| -DD)                                 |
|--------------------------------------|
| User: 2024-07-29                     |
|--------------------------------------|
| Bot: Great! I’ve logged Spotify - $9.|
| 99 - Credit Card - 2024-07-29 for you|
+--------------------------------------+


```

### Listing Expenses
- Description: The interaction for listing all logged expenses with a conversational command.
- Components:
  - Command Input: Area where the user types the list command.
  - Expense List Display: Area where the bot displays the list of expenses

```
+--------------------------------------+
| Discord Interface                    |
|--------------------------------------|
| User: Can you show me my expenses?   |
|--------------------------------------|
| Bot: Here’s what I have:             |
| 1. Spotify - $9.99 - Credit Card -   |
| 2024-07-29                           |
| 2. ENEL Codensa - $45.00 - Debit Card|
| - 2024-07-25                         |
| 3. Claro - $30.00 - Cash - 2024-07-20|
+--------------------------------------+


```
### Deleting an Expense
- Description: The interaction for deleting a specific expense using a conversational command.
- Components:
  - Command Input: Area where the user types the delete command.
  - Confirmation Display: Area where the bot confirms the deletion.

```
+--------------------------------------+
| Discord Interface                    |
|--------------------------------------|
| User: Can you remove expense number 2|
|--------------------------------------|
| Bot: No problem! I’ve removed the    |
| expense: ENEL Codensa - $45.00 - 2024|
| -07-25                               |
+--------------------------------------+


```
### Generating a Report
- Description: The interaction for generating an expense report with a conversational command.
- Components:
  - Command Input: Area where the user types the report command.
  - Report Display: Area where the bot displays the generated report.

```
+--------------------------------------+
| Discord Interface                    |
|--------------------------------------|
| User: Can you give me a report?      |
|--------------------------------------|
| Bot: Sure! Let me pull up your       |
| report...                            |
|--------------------------------------|
| Bot:                                 |
| Here’s your expense summary:         |
| - Total expenses this month: $84.99  |
| - Most frequently used payment method|
| : Credit Card                        |
| - Highest single expense: ENEL Codensa|
| - $45.00                             |
| - Categories with most expenses:     |
|   1. Utilities: $75.00               |
|   2. Subscriptions: $9.99            |
|--------------------------------------|
| You’ve spent $84.99 on 3 expenses    |
| this month. Keep an eye on your      |
| spending to manage your budget better|
+--------------------------------------+


```

## Algorithms and Mathematics for the Passive Expenses Discord Bot

### Natural Language Understanding (NLU)
- Algorithms:
  - Tokenization: Breaking down text into words or tokens.
  - Part-of-Speech Tagging (POS): Assigning parts of speech to each token.
  - Named Entity Recognition (NER): Identifying and classifying named entities in text.
- Mathematics:
  - Statistical Language Models: Calculating probabilities for token sequences.

### String Matching for Expense Names
- Algorithms:
  - Levenshtein Distance: Calculating the minimum number of single-character edits needed to change one word into another.
  - Fuzzy String Matching: Finding close matches between input strings and predefined categories.
- Mathematics:
  - Edit Distance Calculation: Computing the number of edits (insertions, deletions, substitutions) between strings.
  - Cosine Similarity: Measuring similarity between two non-zero vectors.

### Generative AI for Report Generation
- Algorithms:
  - Transformer Models (e.g., GPT): Using self-attention mechanisms to process input sequences and generate text.
  - Probabilistic Text Generation: Generating text based on learned probability distributions.
- Mathematics:
  - Attention Mechanisms: Calculating attention weights for each token in a sequence.
  - Probability Distributions: Generating text based on the likelihood of token sequences.

### Prediction and Analysis
- Algorithms:
  - Time Series Analysis: Analyzing data points ordered in time to identify trends and patterns.
  - Moving Averages: Smoothing out short-term fluctuations to identify long-term trends.
- Mathematics:
  - Statistical Analysis: Computing averages, trends, and patterns over time.
  - Trend Identification: Using mathematical models to identify and forecast trends.

### Database Operations
- Algorithms:
  - CRUD Operations: Performing Create, Read, Update, and Delete operations on the database.
  - Indexing: Creating indexes to speed up data retrieval.
- Mathematics:
  - Basic Set Operations: Handling data insertion, deletion, and queries.
  - Database Normalization: Organizing data to reduce redundancy and improve integrity.

### Automation and Scheduling
- Algorithms:
  - Task Scheduling: Automating repetitive tasks and scheduling regular operations.
- Mathematics:None.

### Logging and Error Handling
- Algorithms:
  - Exception Handling: Managing errors and exceptions gracefully.
  - Log Management: Logging system activities for monitoring and debugging.
- Mathematics: None.

### Security
- Algorithms:
  - Encryption: Securing data through cryptographic techniques.
  - Secure Storage: Managing tokens and sensitive data securely.
- Mathematics:
  - Cryptographic Algorithms: Encrypting and decrypting data to ensure security.

## Development Plan
We will structure the development into cycles of pre-co-requisite programming blocks, moving from the simplest to the most complex. Each cycle will be developed in a separate Git branch, ensuring each phase is independently tested before merging into the main branch. This approach will facilitate continuous integration, incremental improvements, and a robust, scalable, user-friendly bot.

### Cycle 1: Basic Setup and Initial Features
- Branch Name: cycle-1-basic-setup
- Objectives:
  - Set up the basic project structure.
  - Implement basic command handling.
  - Establish the SQLite database and CRUD operations.

- Tasks:
  - Project Setup:
    - Create the project directory structure.
    - Initialize Git repository.
    - Set up requirements.txt with necessary libraries (discord.py, sqlite3).

  - Basic Command Handling:
    - Create a Discord bot.
    - Implement basic command for testing connectivity (e.g., !ping).

  - Database Setup:
    - Design the database schema.
    - Implement CRUD operations (Create, Read, Update, Delete).

  - Math and Algorithms:
    - CRUD Operations: SQL queries.
    - Basic Set Operations: Insert, Update, Delete records.

### Cycle 2: Logging and Listing Expenses
- Branch Name: cycle-2-expense-logging
- Objectives:
  - Implement expense logging feature.
  - Implement expense listing feature.

- Tasks:
  - Expense Logging:
    - Develop the command to log expenses (log expense).
    - Validate user input (amount, date, payment method).

  - Expense Listing:
    - Develop the command to list expenses (show expenses).
    - Display expenses in a user-friendly format.

  - Math and Algorithms:
    - Input Validation: Basic arithmetic checks.
    - Data Retrieval: SQL queries.

### Cycle 3: Deleting and Correcting Expenses
- Branch Name: cycle-3-expense-deletion
- Objectives:
  - Implement expense deletion feature.
  - Enhance input validation with NLU for correcting expense names.

- Tasks:
  - Expense Deletion:
    - Develop the command to delete expenses (remove expense [ID]).

  - Input Validation and Correction:
    - Integrate NLU for correcting user inputs.
    - Suggest corrections for misspelled expense names.

  - Math and Algorithms:
    - Levenshtein Distance: String matching.
    - CRUD Operations: SQL Delete queries.

### Cycle 4: Generating Reports
- Branch Name: cycle-4-report-generation
- Objectives:
  - Implement report generation feature using Generative AI.

- Tasks:
  - Report Generation:
    - Develop the command to generate reports (generate report).
    - Integrate with a Generative AI model to produce summaries.

  - Math and Algorithms:
    - Transformer Models: Attention mechanisms.
    - Probability Distributions: Generating coherent text.

### Cycle 5: Enhancing User Interaction
- Branch Name: cycle-5-user-interaction
- Objectives:
  - Improve the bot’s conversational abilities.
  - Enhance user experience with friendly prompts and responses.

- Tasks:
  - Conversational Interaction:
    - Refine prompts and responses to be more conversational.
    - Implement a more interactive user experience.

  - Feedback and Corrections:
    - Implement feedback loops for users to confirm or correct inputs.

  - Math and Algorithms:
    - NLP Techniques: Tokenization, POS tagging.
    - Text Similarity: Cosine similarity for corrections.

### Cycle 6: Security and Performance Enhancements
- Branch Name: cycle-6-security-performance
- Objectives:
  - Enhance security measures.
  - Optimize performance for scalability.

- Tasks:
  - Security Enhancements:
    - Implement data encryption.
    - Securely manage tokens and sensitive information.

  - Performance Optimization:
    - Optimize database queries and indexing.
    - Implement efficient data retrieval methods.

  - Math and Algorithms:
    - Cryptographic Algorithms: Encryption and decryption.
    - Query Optimization: Indexing and efficient SQL queries.

### Cycle 7: Testing and Quality Assurance
- Branch Name: cycle-7-testing-qa
- Objectives:
  - Conduct comprehensive testing.
  - Ensure quality assurance and documentation.

- Tasks:
  - Testing:
    - Develop unit and integration tests.
    - Conduct user acceptance testing.

  - Quality Assurance:
    - Review and refine documentation.
    - Perform code reviews and static analysis.

  - Math and Algorithms:
    - Test Case Generation: Validating functions and components.
    - Statistical Analysis: Analyzing feedback and test results.

## Project structure

```
passive-expenses-bot/
├── .git/                     # Git repository
├── .gitignore                # Git ignore file
├── README.md                 # Project documentation
├── requirements.txt          # Project dependencies
├── .env.example              # Example environment file
├── config/                   # Configuration files
│   ├── config.yaml           # Configuration settings
├── docs/                     # Documentation
│   ├── setup.md              # Setup guide
│   ├── usage.md              # Usage instructions
│   ├── api_reference.md      # API reference
├── src/                      # Source code
│   ├── bot.py                # Main bot script
│   ├── database.py           # Database interactions
│   ├── commands/             # Command handling modules
│   │   ├── __init__.py       # Package initialization
│   │   ├── log_expense.py    # Expense logging command
│   │   ├── list_expenses.py  # Expense listing command
│   │   ├── delete_expense.py # Expense deletion command
│   │   ├── generate_report.py# Report generation command
│   ├── utils/                # Utility modules
│   │   ├── __init__.py       # Package initialization
│   │   ├── validation.py     # Input validation functions
│   │   ├── nlu.py            # Natural Language Understanding functions
│   │   ├── ai.py             # Generative AI functions
├── tests/                    # Test cases
│   ├── __init__.py           # Package initialization
│   ├── test_bot.py           # Tests for bot.py
│   ├── test_database.py      # Tests for database.py
│   ├── test_commands/        # Tests for command modules
│   │   ├── __init__.py       # Package initialization
│   │   ├── test_log_expense.py # Tests for log_expense.py
│   │   ├── test_list_expenses.py # Tests for list_expenses.py
│   │   ├── test_delete_expense.py # Tests for delete_expense.py
│   │   ├── test_generate_report.py # Tests for generate_report.py
│   ├── test_utils/           # Tests for utility modules
│   │   ├── __init__.py       # Package initialization
│   │   ├── test_validation.py # Tests for validation.py
│   │   ├── test_nlu.py       # Tests for nlu.py
│   │   ├── test_ai.py        # Tests for ai.py


```