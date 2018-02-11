from django.db import connection

class DBquery:

    def __init__(self, sql, *args):
        self.cursor = connection.cursor()
        self.cursor.execute(sql, args)

    def as_dicts(self):
        columns = [col[0] for col in self.cursor.description]
        listofdicts = [
            dict(zip(columns, row))
            for row in self.cursor.fetchall()
        ]
        self.cursor.close()
        return listofdicts

    def as_dict(self):
        columns = [col[0] for col in self.cursor.description]
        row = self.cursor.fetchone()
        dikt = {}
        if self.cursor.rowcount:
            dikt = dict(zip(columns, row))
        self.cursor.close()
        return dikt

    def as_list(self):
        return [row[0] for row in self.cursor.fetchall()]

    def as_value(self):
        value = None
        if self.cursor.rowcount:
            value = self.cursor.fetchone()[0]
        self.cursor.close()
        return value

def hello():
    print("hai")
