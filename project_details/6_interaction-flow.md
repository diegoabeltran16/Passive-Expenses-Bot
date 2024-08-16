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