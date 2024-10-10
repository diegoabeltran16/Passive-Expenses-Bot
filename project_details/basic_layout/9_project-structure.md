# Passive Expenses Bot Project Structure

This is the organized structure of the Passive Expenses Bot project, reflecting all current directories and files.

### Root Directory
- **project_details/**: Contains project-related documents and information.
- **src/**: Main source code directory.
- **tests/**: Contains all test scripts for the project.
- **.editorconfig**: Configuration for consistent coding styles.
- **.env**: Environment variables.
- **.flake8**: Linting configuration for code quality.
- **.gitignore**: Specifies files and directories ignored by git.
- **.gitlab-ci.yml**: CI/CD pipeline configuration for GitLab.
- **.pre-commit-config.yaml**: Configuration for pre-commit hooks.
- **environment.yml**: Environment configuration for package dependencies.
- **expenses.db**: SQLite database for managing expenses.
- **LICENSE**: Project license information.
- **README.md**: Overview and documentation of the project.
- **requirements.txt**: List of dependencies for the project.
- **sync_branch.sh**, **sync_feature.sh**, **sync_repos.sh**: Shell scripts for syncing branches and repositories.

### Source Directory (src)
- **src/\_\_pycache\_\_/**: Directory for compiled Python files.
- **src/commands/**: Contains all bot commands.
  - **\_\_pycache\_\_/**: Directory for compiled Python command files.
  - **delete_expense.py**: Command to delete an expense.
  - **generate_report.py**: Command to generate a report.
  - **list_expenses.py**: Command to list all expenses.
  - **log_expense.py**: Command to log a new expense.
  - **set_language.py**: Command to set user language.
  - **update_expense.py**: Command to update an expense.
- **src/config/**
  - **config.yaml**: Configuration file for bot settings.
- **src/database/**
  - **expenses.db**: Database file for storing expenses data.
- **src/migrations/**
  - **migrate_database.py**: Script for managing database migrations.
- **src/utils/**: Utility files for shared functionalities.
  - **\_\_pycache\_\_/**: Directory for compiled Python utility files.
  - **ai.py**: AI-related utilities.
  - **database.py**: Database connection utility.
  - **db.py**: Database utility functions.
  - **lang.py**: Language translations utility.
  - **logging_config.py**: Logging configuration utility.
  - **nlu.py**: Natural Language Understanding-related utility.
  - **scheduler.py**: Scheduling utility.
  - **shared.py**: Shared variables and utilities.
  - **validation.py**: Input validation utilities.
  - **\_\_init\_\_.py**: Initializes the utility module.
  - **bot.py**: Main bot logic.
  - **expenses.db**: SQLite database for utility purposes.

### Tests Directory
- **tests/\_\_pycache\_\_/**: Directory for compiled Python test files.
- **tests/test_commands/**: Contains all tests for bot commands.
  - **\_\_pycache\_\_/**: Directory for compiled Python test files.
  - **test_delete_expense.py**: Test for deleting an expense.
  - **test_generate_report.py**: Test for generating a report.
  - **test_list_expenses.py**: Test for listing expenses.
  - **test_log_expense.py**: Test for logging a new expense.
  - **test_set_language.py**: Test for setting user language.
  - **test_update_expense.py**: Test for updating an expense.
- **tests/test_utils/**: Contains all tests for utility functions.
  - **\_\_pycache\_\_/**: Directory for compiled Python test files.
  - **test_ai.py**: Test for AI-related utilities.
  - **test_budget.py**: Test for budget management utilities.
  - **test_database.py**: Test for database connection utilities.
  - **test_lang.py**: Test for language translation utilities.
  - **test_logging.py**: Test for logging configuration utilities.
  - **test_nlu.py**: Test for Natural Language Understanding utilities.
  - **test_scheduler.py**: Test for scheduling utilities.
  - **test_validation.py**: Test for input validation utilities.
  - **\_\_init\_\_.py**: Initializes the test utility module.
- **tests/test_bot.py**: Test for the main bot functionality.
- **tests/test_budget.py**: Test for budget management functions.
- **tests/test_database.py**: Test for database-related functions.
- **tests/test_lang.py**: Test for language-related functions.



```
passive-expenses-bot/
├── .editorconfig                    # Editor configuration file for consistent coding style
├── .env                             # Environment variables configuration file
├── .flake8                          # Configuration file for the Flake8 linter
├── .gitignore                       # Specifies files and directories to be ignored by Git
├── .gitlab-ci.yml                   # Configuration file for GitLab CI/CD pipeline
├── .pre-commit-config.yaml          # Configuration for pre-commit hooks to enforce coding standards
├── environment.yml                  # Conda environment configuration file
├── expenses.db                      # SQLite database storing expense information
├── LICENSE                          # License information for the project
├── README.md                        # Project overview, setup instructions, and usage details
├── requirements.txt                 # Python dependencies (deprecated in favor of environment.yml)
├── sync_branch.sh                   # Script for synchronizing branches
├── sync_feature.sh                  # Script for synchronizing features
├── sync_hotfix.sh                   # Script for synchronizing hotfixes
├── sync_merge_features.sh           # Script for merging feature branches
├── sync_repos.sh                    # Script for synchronizing repositories
├── docs/                            # Documentation related to the project
│   ├── api_reference.md             # API reference for the bot's functions
│   ├── setup.md                     # Instructions for setting up the project
│   └── usage.md                     # Usage guidelines for the bot
├── project_details/                 # Detailed information about the project's design and development plan
│   ├── basic_layout/                # Contains basic structural documents
│   ├── development-plan/            # Documents outlining the project development phases
│   └── md-files/                    # Markdown files with additional project details
├── src/                             # Source code for the bot
│   ├── commands/                    # Command scripts for the bot's functionality
│   │   ├── __pycache__/             # Compiled Python files for optimization
│   │   ├── __init__.py              # Initializes the commands package
│   │   ├── delete_expense.py        # Command for deleting an expense entry
│   │   ├── generate_report.py       # Command for generating an expense report
│   │   ├── list_expenses.py         # Command for listing all expenses
│   │   ├── log_expense.py           # Command for logging a new expense
│   │   ├── set_language.py          # Command for setting the bot language
│   │   └── update_expense.py        # Command for updating an expense
│   ├── config/                      # Configuration files
│   │   └── config.yaml              # Main configuration settings for the bot
│   ├── migrations/                  # Database migration scripts
│   │   └── migrate_database.py      # Script for migrating or updating the database schema
│   ├── utils/                       # Utility scripts used across the bot
│   │   ├── __pycache__/             # Compiled Python files for optimization
│   │   ├── __init__.py              # Initializes the utils package
│   │   ├── ai.py                    # AI-related functions and models
│   │   ├── database.py              # Database interaction functions
│   │   ├── db.py                    # Database connection management
│   │   ├── lang.py                  # Language settings and translation utilities
│   │   ├── logging_config.py        # Logging configuration for debugging
│   │   ├── nlu.py                   # Natural Language Understanding functions
│   │   ├── scheduler.py             # Task scheduling functions
│   │   ├── shared.py                # Shared utilities used by various modules
│   │   └── validation.py            # Input validation functions
│   ├── bot.py                       # Main script for running the bot
│   └── expenses.db                  # SQLite database containing the expense records
├── tests/                           # Unit and integration tests for the bot
│   ├── __pycache__/                 # Compiled Python files for optimization
│   ├── test_commands/               # Tests related to command functionalities
│   ├── test_utils/                  # Tests related to utility functions
│   ├── __init__.py                  # Initializes the tests package
│   ├── test_bot.py                  # Tests for the main bot functionality
│   ├── test_budget.py               # Tests for budget calculations
│   └── test_database.py             # Tests for database interactions

```