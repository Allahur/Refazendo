
'''' 
a) Elaborar um programa de computador que efetue a leitura de quatro valores inteiros (variáveis A, B, C e 
D). Ao final o programa deve apresentar o resultado do produto (variável P) do primeiro com o terceiro 
valor, e o resultado do produto (variável P) do primeiro com o terceiro valor, e o resultado da soma 
(variável S) do segundo com o quarto valor. 
'''''

def armazenar_valor():
    primeiro = int(input("Digite o primeiro valor: "))
    segundo = int(input("Digite o segundo valor: "))
    terceiro = int(input("Digite o terceiro valor: "))
    quarto = int(input("Digite o quarto valor: "))
    return primeiro, segundo, terceiro, quarto

def calcular_resultados(valores):
    primeiro, segundo, terceiro, quarto = valores
    resultado1 = primeiro * terceiro
    resultado2 = segundo + quarto
    return resultado1, resultado2

def exibir_resultados(resultados):
    resultado1, resultado2 = resultados
    print("\nResultado")
    print("1°:", resultado1)
    print("2°:", resultado2)
    print("-----------------")

def excluir_valores():
    print("\nValores excluídos com sucesso!\n")

def menu():
    print("\n1 - Armazenar valores")
    print("2 - Exibir resultados")
    print("3 - Excluir valores")
    print("4 - Sair")
    option = int(input("\nSelecione: "))
    return option

def selection():
    valores = None
    resultados = None
    
    while True:
        option = menu()
        
        if option == 1:
            valores = armazenar_valor()
        elif option == 2:
            if valores is None:
                print("\nVocê precisa armazenar os valores primeiro.")
            else:
                resultados = calcular_resultados(valores)
                exibir_resultados(resultados)
        elif option == 3:
            if valores is not None:
                excluir_valores()
                valores = None
                resultados = None
            else:
                print("\nNão há valores armazenados para excluir.")
        elif option == 4:
            break
        else:
            print("\nOpção inválida.")

selection()  # Chamar a função principal de seleção do menu
