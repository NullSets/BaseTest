



# import sqlite3
# conn = sqlite3.connect("somedatabase")
# curs = conn.cursor()
# curs.execute()
# conn.commit()
# conn.close()

import sqlite3

def convert(value):
    if value.startswith('~'):
        return value.strip("~")
    if not value:
        value = "0"
    return float(value)

s = "~07276~^~HORMEL SPAM ... PORK W/ HAM MINCED CND~^^~1 serving~^^~~^0^^^"
conn = sqlite3.connect("food.db")
curs = conn.cursor()

curs.execute("""
CREATE TABLE IF NOT EXISTS food (
id        TEXT PRIMARY KEY,
desc      TEXT,
water     FLOAT,
kcal      FLOAT,
protein   FLOAT,
fat       FLOAT,
ash       FLOAT,
carbs     FLOAT,
fiber     FLOAT,
sugar     FLOAT
)
""")

query = 'INSERT INTO food VALUES(?,?,?,?,?,?,?,?,?,?)'

fields = s.split('^')
vals = [convert(f) for f in fields[:len(fields)]]
curs.execute(query,vals)

conn.commit()
conn.close()


conn = sqlite3.connect("food.db")
curs = conn.cursor()

query = "SELECT * FROM food"
curs.execute(query)
conn.commit()
conn.close()
