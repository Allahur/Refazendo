'''
Faça o código estruturado para controlar uma LIFO com arranjo não 
dinâmico contendo os atributos: nome, idade e salário. Você deverá 
implementar as seguintes sub rotinas obrigatórias:
''''
'''
A. push() para empilhar o registro
B. pop() para remover registros
C. int mostrar() para mostrar os registros da LIFO
D. void cheia() verificar se a LIFO está cheia
E. void vazia() verificar se a LIFO está vazia
F. int tela () exibe a tela e armazena a opção de escolha do menu 
G. void Controle() controla o menu de controle da LIFO 
''''

max_size = 3
stack = []
top = -1

def is_empty():
    return top == -1

def is_full():
    return top == max_size - 1

def push():
    if is_full():
        print("\nA pilha está cheia.")
        return
    
    nome = input("\nDigite o nome: ")
    idade = int(input("Digite a idade: "))
    salario = float(input("Digite o salário: "))
    
    registro = {
        "nome": nome,
        "idade": idade,
        "salario": salario
    }
    
    stack.append(registro)
    print("\nRegistro empilhado com sucesso.")

def pop():
    if is_empty():
        print("\nA pilha está vazia.")
        return
    
    registro = stack.pop()
    print("\nRegistro desempilhado:")
    print(f"Nome: {registro['nome']}")
    print(f"Idade: {registro['idade']}")
    print(f"Salário: {registro['salario']}")

def exibir():
    if is_empty():
        print("\nA pilha está vazia.")
        return
    
    print("\nRegistros na pilha:")
    for registro in reversed(stack):
        print(f"Nome: {registro['nome']}")
        print(f"Idade: {registro['idade']}")
        print(f"Salário: {registro['salario']}")
        print("-----------------")

def menu():
    print("\n1 - Empilhar registro")
    print("2 - Desempilhar registro")
    print("3 - Exibir registros")
    print("4 - Sair")
    option = int(input("\nSelecione a opção: "))
    return option

def controle():
    while True:
        option = menu()
        
        if option == 1:
            push()
        elif option == 2:
            pop()
        elif option == 3:
            exibir()
        elif option == 4:
            break
        else:
            print("\nOpção inválida.")

def main():
    print("Controle de LIFO com arranjo não dinâmico\n")
    controle()

main()
