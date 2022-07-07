import Dao
import os
#from PIL import Image #Importando biblioteca de manipulação de fotos

db_connect = Dao.connection()
con = db_connect.cursor()

def inseriJame(codigo, jameg):
     #aqui deve ser qualquer foto
    try:
        #abrirPasta(docu)
        sql = "alter table Jamegoes(codigo, jameg) add('', {})".format(codigo, jameg)
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
        for(codigo, jameg) in con:
            print("Código: {}, jameg: {}".format(codigo, jameg))
    except Exception as erro:
        print(erro)

def atualiJame(jameg, campo, novoJameg):
    try:
        sql = "update Jamegoes set {} = '{}' where codigo = '{}'".format(jameg, campo, novoJameg)
        con.execute(sql)
        db_connect.commit()
        print('{} Atualizado!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def excluirJame(jameg):
    try:
        sql = "delete from Jamegoes where codigo = '{}'".format(jameg)
        con.execute(sql)
        db_connect.commit()
        print('{} Excluido!'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def abrirPasta():
    return ('\nBem-vindo ao seu diretorio!\n' +
            '\nEscolha um arquivo: ')
    arvo = 'C:\\Users\\calve\\Documents'  # 'C:\\Users\\cristina.asubieta\\Documents\\'
    for (root, dirs, files) in os.walk(arvo):
        print(root)
        print(dirs)
        print(files)
        print('\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n')


#def jamegarFile(jameg=docu):
    #aqui devemos marcar esse arquivo com o nosso jamego
    #if abrirPasta().open:
        #docu = open('', 'r')  # deve ser qualquer documento que usuário selecionar

