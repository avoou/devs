import psycopg2

con = psycopg2.connect(
    host='localhost',
    database='devs',
    user='postgres',
    password='123'
)

con.close()