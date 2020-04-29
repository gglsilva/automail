#!/usr/bin/python
##coding:utf-8

import mail as ml


def main():
    opcao = int(input('''
		Escolha uma opção
\n1 - Adicionar Inquilino
2 - Enviar Boletos
3 - Mudar Servidor SMTP
4 - Confirmaçao de Recebido
		'''))
    if opcao == 1:
        ml.add_inquilino()
    elif opcao == 2:
        ml.EnviaBoleto()
    #elif opcao == 3:

    #elif opcao == 4:


if __name__ == '__main__':
    main()