import Dao
#from PIL import Image #Importando biblioteca de manipulação de fotos

db_connect = Dao.Connection()
con = db_connect.cursor()

def inseriJame(dado):
     #aqui deve ser qualquer foto
    try:
        #abrirPasta(docu)
        sql = "insert into Jamegoes(codigo, dado) values('', {})".format(dado)
        con.execute(sql)
        db_connect.commit()
        #docu.save() #'foto que foi selecionada deve ser salval com o jamego'
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

def atualiJame(dado, campo, novoDado):
    try:
        sql = "update Jamegoes set {} = '{}' where codigo = '{}'".format(dado, campo, novoDado)
        con.execute(sql)
        db_connect.commit()
        print('{} Atualizado!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def excluirJame(dado):
    try:
        sql = "delete from Jamegoes where codigo = '{}'".format(dado)
        con.execute(sql)
        db_connect.commit()
        print('{} Excluido!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def abrirPasta():
    try:
        file = open('C:\Users\cristina.asubieta\Documents', 'r')
        arti = file.read()
        print(arti)
    except Exception as erro:
        print(erro)
    else:
        file.close()

def jamegarFile():
    #aqui devemos marcar esse arquivo com o nosso jamego
    if abrirPasta().open:
        docu = open('', 'r')  # deve ser qualquer documento que usuário selecionar

