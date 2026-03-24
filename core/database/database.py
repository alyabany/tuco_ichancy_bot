# db/database.py

import aiosqlite
from .models import (
    CREATE_USERS_TABLE,
    CREATE_ORDERS_TABLE
)

db = None  # الاتصال العام

async def init_db_connection():
    """فتح اتصال واحد فقط مع قاعدة البيانات"""
    global db
    if db is None:
        db = await aiosqlite.connect("core/database/database.db")
        db.row_factory = aiosqlite.Row
        await db.execute("PRAGMA foreign_keys = ON;")
        await db.execute("PRAGMA journal_mode=WAL;")
        #print("Database connected")

async def init_db():
    """إنشاء الجداول"""
    await db.execute(CREATE_USERS_TABLE)
    await db.execute(CREATE_ORDERS_TABLE)
    await db.commit()

async def close_db():
    """إغلاق الاتصال"""
    global db
    if db:
        await db.close()
        db = None
        print("Database closed")

async def execute_query(query: str, params=()):
    await db.execute(query, params)
    await db.commit()

async def fetch_query(query: str, params=()):
    async with db.execute(query, params) as cursor:
        return await cursor.fetchall()

async def fetchone_query(query: str, params=()):
    async with db.execute(query, params) as cursor:
        return await cursor.fetchone()
