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