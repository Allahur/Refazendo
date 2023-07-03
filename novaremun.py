'''
b) Ler o valor correspondente ao salário mensal (variável SM) de um trabalhador e também o valor do 
percentual de reajuste (variável PR) a ser atribuído. Apresentar o valor do novo salário (variável NS).
''''
'''
Formas 

1. Salário base + 6% do salário base = nova remuneração.

2. Salário do funcionário atualizado + porcentagem de reajuste x 3 (meses de atraso) = remuneração do mês.

3. Salário base + 6% do salário base/2 = nova remuneração.
''''

import time

def salariomensal():
    sm = float(input("Digite o seu salário: "))
    return sm

def dia():
    dias = int(input("Digite os dias de atraso ou acrescentar: "))
    return dias

def month():
    mes = int(input("Digite os meses de atraso: "))
    return mes

def mostrar():
    tb['sm'] = salariomensal()
    tb['mes'] = month()
    tb['dias'] = dia()
    print("\nValores armazenados com sucesso!")
    time.sleep(3)

def calc():
    select = int(input("\nDigite a opção que deseja: "))

    if select == 1:
        tb['ns'] = tb['sm'] * pr
    elif select == 2:
        tb['ns'] = tb['sm'] + pr * tb['mes']
    elif select == 3:
        tb['ns'] = tb['sm'] + (tb['sm'] + (pr / 2))
    else:
        print("Opção inválida!")

    return select

def excluir():
    tb['sm'] = None
    tb['dias'] = None
    tb['mes'] = None
    tb['ns'] = None
    print("Valores excluídos com sucesso!")
    time.sleep(3)

def exibir():
    print("\nNovo salário reajustado: {:.2f}".format(tb['ns']))
    time.sleep(3)

def menu():
    option = int(input("\n1 - Armazenar valor\n2 - Calcular\n3 - Exibir\n4 - Excluir\n5 - Sair\n\nSelecione: "))
    return option

def selection():
    while True:
        option = menu()

        if option == 1:
            mostrar()
        elif option == 2:
            calc()
        elif option == 3:
            exibir()
        elif option == 4:
            excluir()
        elif option == 5:
            break
        else:
            print("Opção inválida!")

tb = {'ns': None, 'sm': None, 'dias': None, 'mes': None}
pr = (100.00 / 30.00) * 0.06

selection()
