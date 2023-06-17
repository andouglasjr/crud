import psycopg2

#Fazendo a conexão com o banco de dados
con = psycopg2.connect(
    host='localhost',
    database='crud',
    user='postgres',
    password='ifrn123'
)

#Curso da conexão
cur = con.cursor()