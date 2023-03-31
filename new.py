import sqlite3
from main import Occupants, event

conn = sqlite3.connect('occupancy.db')
c = conn.cursor()
#
# c.execute("""CREATE TABLE OCCUPANCY (
#     date DATE,
#     time TIME,
#     count INTEGER
#     )""")
def add_new(event):
    c.execute("INSERT INTO OCCUPANCY VALUES (:date, :time, :count)", {'date': event.date, 'time': event.time, 'count': event.count})

#add_new(event)
c.execute("SELECT * FROM OCCUPANCY ORDER BY date DESC, time DESC")
print(c.fetchmany(3))

conn.commit()  # don't forget to commit changes
conn.close()  # good practise
