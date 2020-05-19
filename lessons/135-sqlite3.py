import sqlite3

conn = sqlite3.connect("test_sqlite.db")
# conn = sqlite3.connect(":memory:")



curs = conn.cursor()

# curs.execute(
#     'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
# conn.commit()

# curs.execute(
#     'INSERT INTO persons(name) values("Meow")')
# conn.commit()

# curs.execute(
#     'INSERT INTO persons(name) values("Banana")')
# curs.execute(
#     'INSERT INTO persons(name) values("Monkey")')
# conn.commit()

# curs.execute("UPDATE persons set name = 'Two Bananas' WHERE name = 'Banana'")
# conn.commit()

# curs.execute("DELETE FROM persons WHERE name = 'Two Bananas'")
# conn.commit()

curs.execute("SELECT * FROM persons")
print(curs.fetchall())

curs.close()
conn.close()