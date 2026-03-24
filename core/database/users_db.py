from .database import execute_query, fetchone_query
from core.utils.hepler import now, now_str
async def add_user(user_id, user_name, full_name, join_date, balance):
    if balance is None:
        balance = 0
    join_date = now_str()
    await execute_query("""
                  INSERT OR IGNORE INTO users (tg_id, tg_username, tg_full_name, join_date, balance)
                 VALUES (?, ?, ?, ?, ?)
                 """,(user_id, user_name,full_name, join_date, balance))
    row = await fetchone_query("SELECT changes()")
    return row[0] > 0   # True = مستخدم جديد


async def create_ichancy_account(user_id, ichancy_id, ichancy_username, ichancy_password):
    await execute_query("""
                  UPDATE users SET ichancy_id=?, ichancy_username=?, ichancy_password=? WHERE tg_id=?
                  """, (ichancy_id, ichancy_username, ichancy_password, user_id))

async def delete_ichancy_account(user_id):
    await execute_query("""
        UPDATE users
        SET ichancy_id = NULL,
            ichancy_username = NULL,
            ichancy_password = NULL
        WHERE tg_id = ?
    """, (user_id,))


    
async def get_ichancy_id(user_id):
    row = await fetchone_query(
        "SELECT ichancy_id FROM users WHERE tg_id=?", (user_id,)
    )
    return row["ichancy_id"] if row else None