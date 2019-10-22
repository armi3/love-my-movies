from application import db

db = db.create_db()


class item:

    def __init__(self):
        self._count = ""
        self._title = ""
        self._year = ""
        self._synopsis = ""
        self._score = ""

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, val):
        self._count = val
