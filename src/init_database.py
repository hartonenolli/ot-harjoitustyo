import sqlite3

for_ristinolla = sqlite3.connect("src/tilastot.db")
cursor = for_ristinolla.cursor()

cursor.execute("CREATE TABLE Pelit (id INTEGER PRIMARY KEY, maara INTEGER);")
cursor.execute("INSERT INTO Pelit (maara) VALUES (0);")
for_ristinolla.commit()
