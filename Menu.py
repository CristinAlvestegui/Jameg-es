import this
import Crud

this.opcao = -1

def menu1():
    print('\nEscolha umas das opções abaixo: \n\n' +
        '1. Abrir Fotos\n'                         +
        '2. Abrir Documentos\n'                    +
        '3. Abrir Aplicativos\n'                   +
        '0. Sair\n')
    this.opcao = int(input())

def menu2():
    print('\nEscolha umas das alternativas abaixo: \n\n' +
        '1. Cadastrar Jamegão\n'                         +
        '2. Consultar Jamegão\n'                         +
        '3. Editar Jamegão\n'                            +
        '4. Desativar Jamegão\n'                         +
        '0. Sair\n')
    this.opcao = int(input())

def executarop1():
    while(this.opcao !=0):
        menu1()
        if this.opcao == 1:
            print('Elemento ainda em desenvolvimento...agradecemos a sua compreensão')
        elif this.opcao == 2:
            print('Por favor selecione um dos arquivos de teste disponives na pasta a seguir:')
            Crud.abrirPasta()

            docu = input()

            executarop2()
        elif this.opcao == 3:
            print('Componente ainda em desenvolvimento...agradecemos a sua compreensão')

def executarop2():
    while(this.opcao != 0):
        menu2()
        if this.opcao == 1:
            print('Imforme o nome do novo Jamego: ')
            dado = input()
            Crud.inseriJame(dado)
        elif this.opcao == 2:
            print('Informe o nome ou código do Jamego que deseja consultar: ')
            dado = input()
            Crud.consuJame(dado)
        elif this.opcao == 3:
            print('Informe o nome que deseja atualizar: ')
            dado = input()
            Crud.atualiJame(dado)
        elif this.opcao == 4:
            print('Simplesmente não :(')
            dado = input()
            Crud.excluirJame(dado)
