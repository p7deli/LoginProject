from sqlite3 import connect


def create_table():
    my_db = connect("db_user.db")

    my_cursor = my_db.cursor()
    my_cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            family TEXT,
            username TEXT,
            password TEXT
        )
    ''')


class Database:
    def __init__(self, database_name):
        self.database_name = database_name
        self.db = None

    def is_connect(self):
        self.db = connect(self.database_name)

    def close_db(self):
        self.db.close()

    def creat_user(self, name, family, username, password):
        my_cursor = self.db.cursor()
        if not self.check_user(username, password):
            my_cursor.execute('''
                INSERT INTO users(name, family, username, password) VALUES(?, ?, ?, ?)
            ''', (name, family, username, password))
            self.db.commit()
            return True
        else:
            return False

    def check_user(self, username, password):
        my_cursor = self.db.cursor()
        my_cursor.execute('''
            SELECT * FROM users WHERE username=? AND password=?
        ''', (username, password))
        user = my_cursor.fetchone()
        if user:
            return True
        else:
            return False
