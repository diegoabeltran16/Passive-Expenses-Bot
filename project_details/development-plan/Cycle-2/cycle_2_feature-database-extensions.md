
# Feature: Database Extensions (Cycle #2)

## Overview
In **Cycle #2**, the goal of the `feature/database-extensions` was to enhance the database schema and implement new functionalities to support **budget tracking** and **expense reporting** in the Passive Expenses Bot. We extended the existing database to accommodate features that allow users to manage their expenses and budgets more effectively.

## Accomplishments

### 1. **Budget Tracking**
We implemented the ability for users to:
- Set and manage budgets for specific **categories** (e.g., Food, Entertainment).
- Track **total expenses** in each category over a specific time period.
- Compare their total expenses against the set **budget limit**.
- Receive notifications when they exceed their budget.

### 2. **Expense Reporting**
We built a functionality that:
- Generates **expense reports** for a given time period (e.g., weekly, monthly).
- Reports show the **total expenses per category**, allowing users to review their spending habits.
  
### 3. **Database Schema Extensions**
- **Expenses Table**: We enhanced the existing `expenses` table to include:
  - `user_id`: Each expense is tied to a user, allowing multi-user functionality.
  - `category`: Expenses can be categorized (e.g., Food, Travel).

- **Budgets Table**: The `budgets` table was created to store:
  - `user_id`: The ID of the user setting the budget.
  - `category`: The category the budget is associated with.
  - `"limit"`: The spending limit for the budget (escaped due to being an SQL keyword).
  - `period`, `start_date`, and `end_date`: Defines the time frame for the budget.

## Key Functions Implemented

### 1. **get_total_expenses()**
- **Purpose**: Calculates the total expenses for a specific user, category, and time period.
- **Usage**: This function is used to track the user's total spending in relation to their budget.

### 2. **check_budget_status()**
- **Purpose**: Compares the user's total expenses for a category and time period against their set budget.
- **Result**: Returns whether the user is within their budget or has exceeded it.

### 3. **generate_expense_report()**
- **Purpose**: Generates a detailed report of expenses for a specific time period, grouped by category.
- **Result**: Returns a summary of total expenses for each category, which can be shared with the user.

## Challenges Faced

### 1. **Handling SQL Keywords**
- We encountered issues with SQL keywords, specifically `limit`. To resolve this, we had to escape the `"limit"` keyword in SQL queries.

### 2. **Data Integrity Constraints**
- When adding `user_id` as a `NOT NULL` constraint in the `expenses` table, we faced `IntegrityError` issues. This was resolved by ensuring `user_id` was properly passed during expense insertion.

### 3. **Testing with an In-Memory Database**
- We used an in-memory SQLite database for testing. This required us to properly set up and tear down the schema in each test to ensure accurate results.

## Test Cases Implemented

1. **test_insert_budget**: Ensures budgets are correctly inserted and retrieved from the database.
2. **test_update_budget**: Verifies that a budget's limit can be updated.
3. **test_update_expense_category**: Ensures expenses can be categorized and retrieved by category.
4. **test_check_budget_status**: Checks whether the user has exceeded their budget for a specific category and time period.
5. **test_generate_expense_report**: Generates and verifies expense reports for specific time periods.

## Summary
By the end of Cycle #2, the `feature/database-extensions` successfully extended the bot’s database schema and functionality. The bot is now capable of tracking user budgets, generating expense reports, and organizing expenses by category. All implemented features were thoroughly tested and validated.

The next steps in future cycles may include category management, natural language processing (NLP) for user commands, and data visualizations for expense reports.

