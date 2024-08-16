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
