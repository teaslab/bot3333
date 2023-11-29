import sqlite3

class DatabaseMiddleware:
    def __init__(self):
        self.conn = sqlite3.connect("bot.db") # подключение к БД
    
    def close(self):
        self.conn.close()

def setup(dp):
    dp.middleware.setup(DatabaseMiddleware())