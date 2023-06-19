#carregando as funções em outros arquivos .py
import services.database as db

#função para inserir registro no banco de dados
def incluir(nome, idade, profissao):
    db.cur.execute("""
                   INSERT into public.clientes (nome, idade, profissao)
                   VALUES ('%s','%s','%s')
                   """ % (nome, idade, profissao))
    db.con.commit()
    
#função para inserir registro no banco de dados
def selecionar():
    db.cur.execute("""
                   SELECT * FROM clientes
                   """)
    data = db.cur.fetchall()
    rows = []
    for row in data:
        rows.append(row)
    return rows