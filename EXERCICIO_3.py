# EXERCICIO 03

import random

nome_dos_doadores = []


def doadores():
    sair = False
    while sair != True:
        nome = input("Digite um nome ou '0' para sair: ")
        if nome == "0":
            sair = True
        else:
            valor = float(input("Digite um valor maior do que R$ 10 para doar: R$ "))
            if (valor >= 10):
                nome_dos_doadores.append(nome)
            else:
                print("ERRO - Digite um valor maior ou igual a R$ 10")
        print(nome_dos_doadores)


def sorteio():
    random.shuffle(nome_dos_doadores)
    print("Lista embaralhada dos participantes: ", nome_dos_doadores)
    sorteado = random.choice(nome_dos_doadores)
    print("Parabens, o vencedor do sorteio foi: ", sorteado)


doadores()

if len(nome_dos_doadores) > 0:
    sorteio()
else:
    print("Não existe nada na lista!")