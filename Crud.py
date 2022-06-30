import Dao
from PIL import Image #Importando biblioteca de manipulação de fotos

db_connect = Dao.Connection()
con = db_connect.cursor()

def inseriJame(dado):
    imag = Image.open() #aqui deve ser qualquer foto
    if imag.open:
        try:
            sql = "insert into Jamegoes(codigo, dado) values('', {})".format(dado)
            con.execute(sql)                  
            db_connect.commit()
            imag.save() #'foto que foi selecionada deve ser salval com o jamego'
            print("{} Inserido".format(con.rowcount))
        except Exception as erro:
            print(erro)

def consuJame():
    try:
        sql = 'select * from Jamegoes'
        con.execute(sql)
        for(codigo, dado) in con:
            print("Código: {}, Jamegão: {}".formar(codigo, dado))
    except Exception as erro:
        print(erro)

def atualiJame(cod, campo, novoDado):
    try:
        sql = "update Jamegoes set {} = '{}' where codigo = '{}'".format(cod, campo, novoDado)
        con.execute(sql)
        db_connect.commit()
        print('{} Atualizado!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def excluirJame(cod):
    try:
        sql = "delete from Jamegoes where codigo = '{}'".format(cod)
        con.execute(sql)
        db_connect.commit()
        print('{} Excluido!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def criarPasta():
