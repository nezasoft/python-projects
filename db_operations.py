import mysql.connector as mysql
db = mysql.connect(host="localhost",user="root",passwd="fr0nt!er",database="maindb_rel")
cursor = db.cursor()
query = "SELECT * FROM users"
cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)
