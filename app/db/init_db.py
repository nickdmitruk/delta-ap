# app/db/init_db.py
import sys, os
sys.path.append(os.path.abspath("."))

from app.db.database import engine
from app.db.models import Base

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("✅ База данных и таблицы успешно созданы.")
