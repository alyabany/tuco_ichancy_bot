from datetime import datetime
import pytz
import random
import string
#from config import BOT_USERNAME
#لتوحيد الوقت بتوقيت دمشق
def now():
    tz = pytz.timezone("Asia/Damascus")
    return datetime.now(tz)  # ← يرجع datetime object

def now_str():
    return now().strftime("%Y-%m-%d %H:%M:%S")  # ← يرجع نص

def generate_tx_id(prefix="ORD"):
    time_now = now().strftime("%Y%m%d-%H%M%S")
    rand = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    return f"{prefix}-{time_now}-{rand}"

'''def get_referral_link(user_id):
    return f"https://t.me/{BOT_USERNAME}?start=ref_{user_id}"'''