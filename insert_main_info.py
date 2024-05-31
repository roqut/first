import psycopg2
import pandas as pd

class DataBase:
    def __init__(self, dbname, user, password):
        self.con = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host='192.168.8.56',
            port='5432'
        )
        self.cur = self.con.cursor()

    def execute(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()

    def commit(self):
        self.con.commit()

    def close(self):
        self.con.close()

db = DataBase('safu', 'safu_main_admin', 'sAr')

def read_xlsx(file_name, sheet_name):
    """
    Читает файл xlsx и возвращает данные из указанной таблицы в виде pandas DataFrame.
    """
    df = pd.read_excel(file_name, sheet_name)
    return df.values.tolist()

def insert_data(data, db):
    """
    Вставляет данные в БД.
    """
    query = """
        INSERT INTO users (role, fio, login, password)
        VALUES (%s, %s, %s, %s)
    """
    for row in data:
        db.cur.execute(query, row)
    db.commit()

if __name__ == "__main__":
    file_name = "tables/items_import.xlsx"
    sheet_name = "Лист1"
    db = DataBase('db_tests', 'safu_main_admin', 'sAr')
    data = read_xlsx(file_name, sheet_name)

    #insert_data(data, db)
    for i in data:
        print(i)
    db.close()

