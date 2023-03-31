import sqlite3

conn = sqlite3.connect('occupancy.db')
c = conn.cursor()

c.execute("""CREATE TABLE OCCUPANCY (
    date DATE,
    time TIME,
    count INTEGER  
    )""")

conn.commit() # don't forget to commit changes

conn.close() # good practise