# Architecture

The Passive Expenses Discord Bot is designed using a multi-layered architecture to ensure modularity, maintainability, and scalability. The architecture consists of the following layers: Client Layer, Application Layer, Data Layer, and Integration Layer.

## Client Layer
- **Description:** This layer represents the user interface where users interact with the bot through Discord. It handles user commands and responses.
- **Components:** 
  - **Discord Client:** The interface through which users interact with the bot using Discord commands.
- **Responsibilities:**
  - Receive and interpret user commands.
  - Display responses and information to users.
  - Provide user feedback and error messages.
- **Breakdown:**
  - **Discord Client:**
    - Utilizes `discord.py` to connect to Discord.
    - Handles events such as receiving messages and commands.
    - Sends responses back to the Discord server.

## Application Layer
- **Description:** This layer contains the core logic and functionality of the bot, including command handling, business logic, and interactions with other layers.
- **Components:**
  - **Command Handler:** Manages the various commands issued by the users and routes them to the appropriate functions. Now includes support for natural language processing (NLP).
  - **Business Logic:** Implements the core functionalities such as logging expenses, generating reports, validating inputs, and managing user preferences.
  - **Error Handler:** Provides detailed and actionable error messages to users.
  - **Onboarding Module:** Guides new users through initial setup and familiarizes them with the bot's commands.
- **Responsibilities:**
  - Process user commands and execute corresponding actions.
  - Handle business logic for expense management.
  - Ensure proper flow of data between the client layer and the data layer.
- **Breakdown:**
  - **Command Handler:**
    - Maps user commands to functions, including alias resolution and NLP.
    - Validates user input and handles errors.
    - Coordinates with business logic for processing commands.
  - **Business Logic:**
    - Implements expense logging by interacting with the data layer.
    - Generates reports by fetching data from the database and using generative AI (if needed).
    - Manages user preferences and ensures they are stored correctly.
  - **Error Handler:**
    - Extends error handling to provide detailed messages and suggestions for resolving common mistakes.
  - **Onboarding Module:**
    - Implements an interactive setup process, helping users configure key settings and become familiar with the bot.

## Data Layer
- **Description:** This layer is responsible for data storage, retrieval, and management. It interacts with the database to perform CRUD operations.
- **Components:**
  - **Database (SQLite):** Stores expense data and other relevant information.
  - **Data Access Objects (DAO):** Interfaces for interacting with the database.
  - **Data Management Module:** Handles data backup, export, and integrity.
- **Responsibilities:**
  - Store and retrieve expense data.
  - Ensure data integrity and security.
  - Manage database schema and perform necessary migrations.
- **Breakdown:**
  - **Database (SQLite):**
    - Stores user expenses, categories, and other metadata.
    - Uses tables with fields such as `id`, `amount`, `description`, `payment_method`, and `date`.
  - **Data Access Objects (DAO):**
    - Provides methods for CRUD operations.
    - Ensures data is stored and retrieved efficiently.
    - Handles database connections and queries.
  - **Data Management Module:**
    - Manages regular data backups and supports CSV export functionality.
    - Ensures data integrity through regular checks and automated cleaning processes.

## Integration Layer
- **Description:** This layer handles integration with external services such as generative AI for report generation and NLU for understanding user input.
- **Components:**
  - **Generative AI (OpenAI GPT):** Generates summary reports and insights from expense data.
  - **NLU Model (SpaCy or NLTK):** Processes and understands user inputs for better interaction.
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

## Updated Architecture Overview

### Command Aliases
- **Component:** Command Handler
- **Update:** Implement an alias resolution system within the command handler. This system maps alias commands (e.g., `!log`) to their respective full commands (e.g., `!log_expense`), ensuring consistent processing.

### Expense Categorization
- **Component:** Database Schema, Expense Logger
- **Update:** Update the database schema to include a `category` field. Modify the Expense Logger to accept and store categories when logging expenses.

### Monthly Summary Command
- **Component:** Reporting Module
- **Update:** Add a new reporting function that aggregates expenses by category for the current month and generates a summary report. The command handler triggers this function via the `!monthly_summary` command.

### Data Backup/Export Feature
- **Component:** Data Management Module
- **Update:** Implement a backup and export system to handle exporting the SQLite database to a CSV file, ensuring data integrity during export.

### Basic Budgeting Feature
- **Component:** Budget Manager
- **Update:** Introduce a Budget Manager component that allows users to set and track budgets for different categories. This component monitors expenses and triggers notifications when users approach or exceed their budget limits.

### Customization of Responses
- **Component:** User Preferences, Command Handler
- **Update:** Add a User Preferences component to store settings like preferred response style (e.g., formal, casual, humorous) and language preference (English or Spanish). The Command Handler adjusts responses based on user preferences.

### Automated Data Cleaning
- **Component:** Data Validation Module
- **Update:** Enhance the Data Validation Module to regularly check for duplicates or anomalies in the data. Notify users to review and correct any flagged entries.

### Improved Error Handling
- **Component:** Error Handler
- **Update:** Extend the Error Handler to provide more detailed and actionable error messages. Include suggestions for correcting common mistakes, with messages available in both English and Spanish.

### Interactive Setup Process
- **Component:** Onboarding Module
- **Update:** Develop an Onboarding Module that guides new users through the initial setup process, helping them configure key settings and familiarize themselves with the bot's commands. The onboarding process will be available in both English and Spanish.

### More Robust Testing Framework
- **Component:** Testing Suite
- **Update:** Expand the Testing Suite to cover new features, especially edge cases and varied user inputs, in both English and Spanish. Regular updates to the test cases will ensure continued stability as the bot evolves.

### NLP Integration
- **Component:** Command Handler
- **Update:** The Command Handler includes an NLP module that processes natural language inputs, mapping phrases to corresponding commands, allowing conversational interaction in both English and Spanish.

### Contextual Response System
- **Component:** Response Generator
- **Update:** Produce context-aware responses that align with the user's input style, adjusting tone and content based on whether the input is formal, casual, or humorous, and in the preferred language.

### User Interaction Flow
- **Component:** Interaction Flow Controller
- **Update:** Support a dynamic flow that adapts to user inputs in natural language, ensuring smooth interactions with suggestions and feedback in the user's preferred language.

### Testing and Validation Framework
- **Component:** Testing Suite
- **Update:** Expand the Testing Suite to include tests for NLP and natural language input processing, ensuring accurate and reliable bot responses in both English and Spanish.
