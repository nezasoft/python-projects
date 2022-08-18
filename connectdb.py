import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='maindb_rel')

cur = conn.cursor()
cur.execute("SELECT id AS user_id, user_name, firstname,surname,email, active FROM users ORDER BY firstname ASC")

print(cur.description)
print()

for row in cur:
    print(row)

cur.close()
conn.close()