import MySQLdb
SQL_IP ="192.168.20.230"
SQL_USERNAME="remote"
SQL_PASSWORD="Fr0nt!er"
SQL_DB="radius"
sql_connection = MySQLdb.connect(SQL_IP,SQL_USERNAME,SQL_PASSWORD,SQL_DB)
print(sql_connection)