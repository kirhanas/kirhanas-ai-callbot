import pandas as pd
from datetime import datetime
import os

FILE = "calls.xlsx"

def log_call(phone, result):
    row = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "phone": phone,
        "result": result
    }

    if os.path.exists(FILE):
        df = pd.read_excel(FILE)
        df = pd.concat([df, pd.DataFrame([row])])
    else:
        df = pd.DataFrame([row])

    df.to_excel(FILE, index=False)
