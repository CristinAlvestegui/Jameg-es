import Dao
#from PIL import Image #Importando biblioteca de manipulação de fotos continuara....em outra.
db_connect = Dao.connectar()
con = db_connect.cursor()

def inserirJame(dado):
    docu = open(r"C:\Users\cristina.asubieta\Documents\Fotos\foto7.jpg")  #aqui deve ser qualquer foto
    #imag.show() #se não conseguimos...então faremos com arquivos de txt  ;( ou arquivos....sla :(
    if docu.open:
        try:
            sql = "insert into Jamegoes(codigo, dado) values('', {})".format(dado)
            con.execute(sql)
            db_connect.commit()
            docu.save() #Agora salvamo o arquivo com o jamego                                                   ******             'foto que foi selecionada deve ser salval com o jamego'
            print("{} Inserido".format(con.rowcount))
        except Exception as erro:
            print(erro)
        else:
            docu.close()

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

#def criarPasta():
    #aqui temos que criar a condição de: quando 3 fotos foram salvas com o msm jamego, o sistema deve criar uma pasta.
    #os.makedirs comando para criar pasta
    #tbm devemos lembrar que cada jamegão vai ter seu própio caminho o sistema deve reconhecer cada um deles.
