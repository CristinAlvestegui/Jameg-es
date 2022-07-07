import this
import Crud

this.opcao = -1

def pegArvo(arvo):
    print('Por favor informe o caminho do arquivo ou pasta')
    arvo = input()
    #Crud.jamegarFile(arvo)

def menu():
    print('\nEscolha umas das alternativas abaixo: \n\n' +
        '1. Cadastrar Jamegão\n'                         +
        '2. Consultar Jamegão\n'                         +
        '3. Editar Jamegão\n'                            +
        '4. Desativar Jamegão\n'                         +
        '0. Sair\n')
    this.opcao = int(input())


def executar():
    while(this.opcao != 0):
        menu()
        if this.opcao == 1:
            print('Imforme o nome do novo Jamego: ')
            jameg = input()
            Crud.inseriJame(jameg)
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
