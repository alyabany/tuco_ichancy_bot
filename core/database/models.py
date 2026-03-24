# db/models.py

CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tg_id INTEGER UNIQUE,
    tg_username TEXT,
    tg_full_name TEXT,
    balance REAL DEFAULT 0,
    ichancy_balance REAL DEFAULT 0,
    ichancy_id TEXT,
    ichancy_username TEXT,
    ichancy_password TEXT,
    created_at TEXT,
    join_date TEXT,
    last_active TEXT,
    is_banned BOOLEAN DEFAULT FALSE,
    role TEXT DEFAULT 'user'
);
"""

CREATE_ORDERS_TABLE = """
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    service TEXT,
    amount REAL,
    status TEXT DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""