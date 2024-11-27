import sqlite3

class FB_szotar_kezelese:
    def __init__(self):
        self.kapcsolat=sqlite3.connect("projekt.db")
        self.FB_tabla()

    def FB_tabla(self):
        ab=self.kapcsolat.cursor()
        ab.execute('''CREATE TABLE IF NOT EXISTS szavak(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    angol TEXT NOT NULL,
                    magyar TEXT NOT NULL)''')
        self.kapcsolat.commit()

    def FB_hozzaadas(self,angol,magyar):
        ab=self.kapcsolat.cursor()
        ab.execute('INSERT INTO szavak (angol,magyar) VALUES (?,?)',(angol,magyar))
        self.kapcsolat.commit()

    def FB_valasztas(self):
        ab=self.kapcsolat.cursor()
        ab.execute('SELECT angol,magyar FROM szavak ORDER BY RANDOM() LIMIT 1')
        return ab.fetchone()

    def FB_bezar(self):
        self.kapcsolat.close()