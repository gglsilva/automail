#!/usr/bin/python
##coding:utf-8

from email.mime.base import MIMEBase
#from email.MIMEImage import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import email
import email.mime.application
import smtplib

msg = MIMEMultipart()

def credenciais(de, para, subject, password ):
    msg['From'] = de
    msg['To'] = para
    msg['Subject'] = subject
    msg['password'] = password
    print('from:{}\nto:{}\nSuject:{}'.format(msg['from'],msg['to'],msg['Subject']))


def conecta(server):
    #server = smtplib.SMTP('smtp-mail.outlook.com: 587')
    server = smtplib.SMTP(server)
    server.ehlo()
    server.starttls()
    print('deu certo')

    return server

def login(server):
    server.login(msg['from'], msg['password'])


def add_inquilino():
    print('Adicionando Cliente:')
    lista_cliente = {}
    cond = True
    file = open('cliente.txt', 'a')

    while(cond):
        nome = str(input('Digite o nome do cliente:\n'))
        email = str(input('Digite o email do cliente:\n'))
        lista_cliente[nome] = email
        op = int(input('Deseja adicionar outro cliente?\n1-Sim\n2-Não'))

        if op == 1:
            file.write(nome + " - " + email)

        elif op == 2:
            for i, v in lista_cliente.items():
                file.write(i + " - " + v + "\n")
                cond=False

            file.close()


#def EnviaBoleto():



#credenciais('gabrielimobmarruas@hotmail.com','gabrielchamex@gmail.com','Teste de envio 02', 'yoda#750')
#server = conecta('smtp-mail.outlook.com: 587')
#login(server)
