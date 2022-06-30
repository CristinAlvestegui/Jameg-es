import this
import Crud

this.opcao = -1

def menu():
    print('\nEscolha umas das opções abaixo: \n\n' +
        '1. Cadastrar Jamegão\n'                   +
        '2. Consultar Jamegão\n'                   +
        '3. Atualizar Jamegão\n'                   +
        '4. Desativar Jamegão\n'                   +
        '0. Sair\n')
    this.opcao = int(input())

def operacoes():
    while(this.opcao != 0):
        menu()
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
