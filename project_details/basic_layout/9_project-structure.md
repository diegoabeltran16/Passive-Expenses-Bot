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
├── .editorconfig                    # Configuration for consistent coding styles
├── .env                             # Environment variables
├── .flake8                          # Linting configuration for code quality
├── .gitignore                       # Specifies files and directories ignored by git
├── .gitlab-ci.yml                   # CI/CD pipeline configuration for GitLab
├── .pre-commit-config.yaml          # Configuration for pre-commit hooks
├── environment.yml                  # Environment configuration for package dependencies
├── LICENSE                          # Project license information
├── README.md                        # Overview and documentation of the project
├── requirements.txt                 # List of dependencies for the project
├── sync_branch.sh                   # Shell script for syncing branches
├── sync_feature.sh                  # Shell script for syncing features
├── sync_repos.sh                    # Shell script for syncing repositories
├── project_details/                 # Contains project-related documents and information
├── src/                             # Main source code directory
│   ├── __pycache__/                 # Directory for compiled Python files
│   ├── commands/                    # Contains all bot commands
│   │   ├── __pycache__/             # Directory for compiled Python command files
│   │   ├── delete_expense.py        # Command to delete an expense
│   │   ├── generate_report.py       # Command to generate a report
│   │   ├── list_expenses.py         # Command to list all expenses
│   │   ├── log_expense.py           # Command to log a new expense
│   │   ├── set_language.py          # Command to set user language
│   │   └── update_expense.py        # Command to update an expense
│   ├── config/                      # Configuration files
│   │   └── config.yaml              # Configuration file for bot settings
│   ├── database/                    # Database directory
│   │   └── expenses.db              # Database file for storing expenses data
│   ├── migrations/                  # Database migration scripts
│   │   └── migrate_database.py      # Script for managing database migrations
│   ├── utils/                       # Utility files for shared functionalities
│   │   ├── __pycache__/             # Directory for compiled Python utility files
│   │   ├── ai.py                    # AI-related utilities
│   │   ├── database.py              # Database connection utility
│   │   ├── db.py                    # Database utility functions
│   │   ├── lang.py                  # Language translations utility
│   │   ├── logging_config.py        # Logging configuration utility
│   │   ├── nlu.py                   # Natural Language Understanding-related utility
│   │   ├── scheduler.py             # Scheduling utility
│   │   ├── shared.py                # Shared variables and utilities
│   │   ├── validation.py            # Input validation utilities
│   │   └── __init__.py              # Initializes the utility module
│   └── bot.py                       # Main bot logic
├── tests/                           # Contains all test scripts for the project
│   ├── __pycache__/                 # Directory for compiled Python test files
│   ├── test_commands/               # Contains all tests for bot commands
│   │   ├── __pycache__/             # Directory for compiled Python test files
│   │   ├── test_delete_expense.py   # Test for deleting an expense
│   │   ├── test_generate_report.py  # Test for generating a report
│   │   ├── test_list_expenses.py    # Test for listing expenses
│   │   ├── test_log_expense.py      # Test for logging a new expense
│   │   ├── test_set_language.py     # Test for setting user language
│   │   └── test_update_expense.py   # Test for updating an expense
│   ├── test_utils/                  # Contains all tests for utility functions
│   │   ├── __pycache__/             # Directory for compiled Python test files
│   │   ├── test_ai.py               # Test for AI-related utilities
│   │   ├── test_budget.py           # Test for budget management utilities
│   │   ├── test_database.py         # Test for database connection utilities
│   │   ├── test_lang.py             # Test for language translation utilities
│   │   ├── test_logging.py          # Test for logging configuration utilities
│   │   ├── test_nlu.py              # Test for Natural Language Understanding utilities
│   │   ├── test_scheduler.py        # Test for scheduling utilities
│   │   ├── test_validation.py       # Test for input validation utilities
│   │   └── __init__.py              # Initializes the test utility module
│   ├── test_bot.py                  # Test for the main bot functionality
│   ├── test_budget.py               # Test for budget management functions
│   ├── test_database.py             # Test for database-related functions
│   └── test_lang.py                 # Test for language-related functions


```