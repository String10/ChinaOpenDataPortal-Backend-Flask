import atexit
import pymysql

from .config import DB_HOST, DB_PORT, DB_USER, DB_PSWD, DB_NAME


_database = pymysql.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PSWD,
    database=DB_NAME,
    charset="utf8",
)


def get_cursor():
    return _database.cursor()

def fetch_as_dict(query: str):
    with get_cursor() as cursor:
        cursor.execute(query)
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

def commit():
    _database.commit()


# close db connection when the program exits
atexit.register(_database.close)
