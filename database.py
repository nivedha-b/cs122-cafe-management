import sqlite3

# Connect to the database (it will be created if it doesn't exist)
connection = sqlite3.connect("cafe_database.db")
connection.execute("PRAGMA foreign_keys = 1")

# Create a cursor object to execute SQL commands
c = connection.cursor()

# Create tables
SQL_create_menuitem = """CREATE TABLE IF NOT EXISTS MenuItem (
    item_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    description TEXT,
    category TEXT,
    hot_available INTEGER NOT NULL DEFAULT 1
        CHECK (hot_available IN (0, 1)),
    iced_available INTEGER NOT NULL DEFAULT 1
        CHECK (iced_available IN (0, 1)),
    availability INTEGER NOT NULL DEFAULT 1
        CHECK (availability IN (0, 1))
)"""

SQL_create_employee = """CREATE TABLE IF NOT EXISTS Employee (
    employee_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)"""

SQL_create_orders = """CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY,
    total REAL NOT NULL DEFAULT 0,
    status TEXT NOT NULL,
    order_date TEXT
)"""

SQL_create_orderitem = """CREATE TABLE IF NOT EXISTS OrderItem (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (item_id) REFERENCES MenuItem(item_id)
)"""

SQL_create_transactions = """CREATE TABLE IF NOT EXISTS Transactions (
    transaction_id INTEGER PRIMARY KEY,
    order_id INTEGER NOT NULL UNIQUE,
    date_time TEXT,
    amount REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
)"""

c.execute(SQL_create_menuitem)
c.execute(SQL_create_employee)
c.execute(SQL_create_orders)
c.execute(SQL_create_orderitem)
c.execute(SQL_create_transactions)

# Add menu items

c.execute("""INSERT INTO MenuItem (name, price, description, category, hot_available, iced_available, availability)
            VALUES ('Americano', 4.50, NULL, 'Drink', 1, 1, 1),
            ('Latte', 5.50, NULL, 'Drink', 1, 1, 1),
            ('Cappuccino', 5, NULL, 'Drink', 1, 1, 1),
            ('Matcha Latte', 6, NULL, 'Drink', 1, 1, 1),
            ('Tiramisu Latte', 6, NULL, 'Drink', 0, 1, 1),
            ('Mocha', 5.50, NULL, 'Drink', 1, 1, 1),
            ('Affogato', 6, NULL, 'Drink', 0, 0, 1),
            ('Cold Brew', 5.50, NULL, 'Drink', 0, 1, 1),
            ('Chai', 5.50, NULL, 'Drink', 0, 1, 1),
            ('Pistachio Latte', 6, NULL, 'Drink', 0, 1, 1),
            ('Croissant', 4, NULL, 'Food', 0, 0, 1),
            ('Muffin', 3.50, NULL, 'Food', 0, 0, 1),
            ('Cinnamon Roll', 4.50, NULL, 'Food', 0, 0, 1),
            ('Breakfast Sandwich', 7.50, NULL, 'Food', 0, 0, 1),
            ('Avocado Toast', 7, NULL, 'Food', 0, 0, 1),
            ('Bagel', 4, NULL, 'Food', 0, 0, 1),
            ('Yogurt Parfait', 5.50, NULL, 'Food', 0, 0, 1)""")


# Save (commit) the changes and close the connection
connection.commit()
connection.close()

print("Database and table created successfully!")