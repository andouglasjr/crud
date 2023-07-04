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

# função para selecionar apenas um registros no banco de dados
def selecionar_id (id):
  db.cur.execute("""
           SELECT * FROM clientes WHERE id = '%s'
   """ % (id))
  recset = db.cur.fetchall()
  rows = []
  for rec in recset:
    rows.append(rec)
  return rows

# função para excluir registros no banco de dados
def excluir (id):
  db.cur.execute("""
           DELETE FROM clientes WHERE id = '%s'
   """ % (id))
  data = db.con.commit()
  return data

def alterar(nome, idade, profissao, id):
  data = db.cur.execute("""
           UPDATE clientes SET nome='%s', idade='%s', profissao='%s'  WHERE id = '%s'
           """ % (nome, idade, profissao, id))
  db.con.commit()
  return data