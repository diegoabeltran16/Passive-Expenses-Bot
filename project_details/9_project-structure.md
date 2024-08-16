## Project structure

```
passive-expenses-bot/
├── .editorconfig                    # Editor configuration file for consistent coding style
├── .env                             # Environment variables configuration file
├── .flake8                          # Configuration file for the Flake8 linter
├── .gitignore                       # Specifies files and directories that Git should ignore
├── .gitlab-ci.yml                   # GitLab CI/CD configuration file
├── .pre-commit-config.yaml          # Pre-commit hooks configuration
├── environment.yml                  # Conda environment configuration file
├── LICENSE                          # License file for the project
├── README.md                        # Project overview and instructions
├── requirements.txt                 # Required Python packages
├── sync_branch.sh                   # Shell script to sync branches
├── sync_feature.sh                  # Shell script to sync features
├── sync_hotfix.sh                   # Shell script to sync hotfixes
├── sync_merge_features.sh           # Shell script to merge feature branches
├── sync_repos.sh                    # Shell script to sync repositories
├── config/                          # Configuration files
│   ├── config.yaml                  # Configuration settings
├── docs/                            # Documentation
│   ├── setup.md                     # Setup guide
│   ├── usage.md                     # Usage instructions
│   ├── api_reference.md             # API reference
├── src/                             # Source code
│   ├── commands/                    # Command handling modules
│   │   ├── __init__.py              # Package initialization
│   │   ├── log_expense.py           # Expense logging command
│   │   ├── list_expenses.py         # Expense listing command
│   │   ├── delete_expense.py        # Expense deletion command
│   │   ├── generate_report.py       # Report generation command
│   ├── utils/                       # Utility modules
│   │   ├── __init__.py              # Package initialization
│   │   ├── validation.py            # Input validation functions
│   │   ├── nlu.py                   # Natural Language Understanding (NLP) functions for English and Spanish
│   ├── interaction/                 # User interaction and flow control
│   │   ├── __init__.py              # Package initialization
│   │   ├── onboarding.py            # Onboarding process module
│   │   ├── flow_controller.py       # Interaction flow control module
│   ├── data/                        # Data management modules
│   │   ├── __init__.py              # Package initialization
│   │   ├── database.py              # Database connection and operations
│   │   ├── backup.py                # Data backup and export functions
├── tests/                           # Testing suite
│   ├── __init__.py                  # Package initialization
│   ├── test_commands.py             # Unit tests for command handling
│   ├── test_nlu.py                  # Unit tests for NLP functions
│   ├── test_interaction.py          # Unit tests for interaction flow
│   ├── test_data.py                 # Unit tests for data management

```