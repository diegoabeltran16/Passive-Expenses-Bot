# Project Details

## Project structure

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