# Importa el módulo sqlite3 para interactuar con la base de datos SQLite.
import sqlite3

# Conéctese a la base de datos SQLite (creará el archivo si no existe)
def connect_db():
    """
    Establecer una conexión con la base de datos SQLite.

    Esta función se conecta a la base de datos 'gastos.db'. Si el archivo no existe,
    SQLite lo creará en el directorio de trabajo actual.

    Devuelve:
    --------
    sqlite3.Connection:
        Un objeto de conexión para interactuar con la base de datos SQLite.

    Ejemplo de uso:
    --------------
    conn = connect_db()
    cursor = conn.cursor()
    """
    return sqlite3.connect('expenses.db')

# Inicializar la tabla de gastos
def create_expenses_table():
    """
    Crear la tabla 'gastos' si aún no existe.

    Esta función inicializa la tabla 'gastos' con los siguientes campos:
    - id: Un entero que se autoincrementa y sirve como clave primaria.
    - amount: Un número de coma flotante que representa el importe del gasto.
    - description: Campo de texto que describe el gasto.
    - date_added: Una marca de tiempo para cuando se añadió el gasto (por defecto: marca de tiempo actual).

    Ejemplo de uso:
    --------------
    Llama a esta función al inicio del bot para asegurar que la base de datos está configurada:60
    create_expenses_table()
    """
    conn = connect_db()
    cursor = conn.cursor()

    # Crear la tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            description TEXT NOT NULL,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

# Añadir un nuevo gasto
def add_expense(amount, description):
    """
    Inserte un nuevo gasto en la tabla "gastos".

    Parametros:
    -----------
    amount : float
        El importe del gasto.
    description : str
        Breve descripción del gasto.

    Devuelve:
    --------
    int:
        El ID de la línea de gasto recién insertada.

    Ejemplo de uso:
    --------------
    expense_id = add_expense(100.0, "Groceries")
    print(f"Expense logged with ID: {expense_id}")
    """
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO expenses (amount, description)
        VALUES (?, ?)
    ''', (amount, description))

    conn.commit()
    expense_id = cursor.lastrowid  # Obtener el ID de la fila insertada
    conn.close()

    return expense_id  # Devuelve el ID de la fila insertada

# Suprimir un gasto por ID
def delete_expense(expense_id):
    """
    Eliminar un gasto de la base de datos por su ID.

    Parametros:
    -----------
    expense_id : int
        El ID único del gasto que se va a eliminar.

    Ejemplo de uso:
    --------------
    delete_expense(1)
    print("Expense with ID 1 deleted.")
    """
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))

    conn.commit()
    conn.close()

# Enumere todos los gastos
def list_expenses():
    """
    Recuperar todos los gastos de la base de datos.

    Devuelve:
    --------
    lista de tuplas:
        Una lista de tuplas, donde cada tupla representa un gasto con la siguiente estructura:
        (id, amount, description, date_added)

    EEjemplo de uso:
    --------------
    expenses = list_expenses()
    for expense in expenses:
        print(expense)
    """
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('SELECT id, amount, description, date_added FROM expenses')
    expenses = cursor.fetchall()

    conn.close()

    return expenses  # Devuelve una lista de todos los gastos

# Actualizar un gasto existente por ID
def update_expense(expense_id, new_amount, new_description):
    """
    Actualizar el importe y la descripción de un gasto existente por su ID.

    Parametros:
    -----------
    expense_id : int
        El ID único del gasto a actualizar.
    new_amount : float
        El nuevo importe del gasto.
    new_description : str
        La nueva descripción del gasto.

    Ejemplo de uso:
    --------------
    update_expense(1, 150.0, "Updated Groceries")
    print("Expense updated successfully.")
    """
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE expenses
        SET amount = ?, description = ?
        WHERE id = ?
    ''', (new_amount, new_description, expense_id))

    conn.commit()
    conn.close()

# Llama a esta función para crear la tabla cuando se inicie el bot
create_expenses_table()
