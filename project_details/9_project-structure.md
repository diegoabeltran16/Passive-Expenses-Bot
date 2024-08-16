## Project structure

```
passive-expenses-bot/
├── config/                         # Configuration files
│   ├── config.yaml                 # Configuration settings
├── docs/                           # Documentation
│   ├── setup.md                    # Setup guide
│   ├── usage.md                    # Usage instructions
│   ├── api_reference.md            # API reference
├── src/                            # Source code
│   ├── commands/                   # Command handling modules
│   │   ├── __init__.py             # Package initialization
│   │   ├── log_expense.py          # Expense logging command
│   │   ├── list_expenses.py        # Expense listing command
│   │   ├── delete_expense.py       # Expense deletion command
│   │   ├── generate_report.py      # Report generation command
│   ├── utils/                      # Utility modules
│   │   ├── __init__.py             # Package initialization
│   │   ├── validation.py           # Input validation functions
│   │   ├── nlu.py                  # Natural Language Understanding functions
│   │   ├── ai.py                   # Generative AI functions
│   │   ├── logging_config.py       # Logging configuration file
│   │   ├── scheduler.py            # Module for scheduling tasks
│   ├── bot.py                      # Main bot script
│   ├── database.py                 # Database interactions
├── tests/                          # Test cases
│   ├── test_commands/              # Tests for command modules
│   │   ├── __init__.py             # Package initialization
│   │   ├── test_log_expense.py     # Tests for log_expense.py
│   │   ├── test_list_expenses.py   # Tests for list_expenses.py
│   │   ├── test_delete_expense.py  # Tests for delete_expense.py
│   │   ├── test_generate_report.py # Tests for generate_report.py
│   ├── test_utils/                 # Tests for utility modules
│   │   ├── __init__.py             # Package initialization
│   │   ├── test_validation.py      # Tests for validation.py
│   │   ├── test_nlu.py             # Tests for nlu.py
│   │   ├── test_ai.py              # Tests for ai.py
│   │   ├── test_logging.py         # Unit tests for logging configurations
│   │   ├── test_scheduler.py       # Unit tests for scheduler module
│   ├── __init__.py                 # Package initialization
│   ├── test_bot.py                 # Tests for bot.py
│   ├── test_database.py            # Tests for database.py
├── .editorconfig                   # Editor configuration
├── .env                            # Environment file
├── .flake8                         # Linting configuration
├── .gitignore                      # Git ignore file
├── .gitlab-ci.yml                  # GitLab CI configuration
├── .pre-commit-config.yaml         # Pre-commit hooks configuration
├── environment.yml                 # Conda environment dependencies
├── LICENSE                         # License file
├── project.details.md              # Project details
├── README.md                       # Project documentation
├── requirements.txt                # Project dependencies
└── sync_branch.sh                  # Script to sync branches
└── sync_feature.sh                 # Script to sync features
└── sync_hotfix.sh                  # Script to sync hotfixes
└── sync_merge_features.sh          # Script to merge features
└── sync_repos.sh                   # Script to sync repositories


```