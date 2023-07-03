'''
2 - Crie um algoritmo que tenha um vetor explícito para armazenar 5 
idades e um vetor não explícito para armazenar 5 nomes. Ao final Exiba o 
nome da pessoa de maior idade, menor idade, a média das idades é o saldo 
das idades. 
''''

def obter_info_pessoas():
    idades = [19, 20, 18, 17, 16]
    nomes = []
    
    for i in range(len(idades)):
        nome = input("\nDigite o nome: ")
        nomes.append(nome)
        
        media = sum(idades) / len(idades)
        
        print(f"\nNome: {nome}\nIdade: {idades[i]}\nMédia: {media:.2f}")
    
    return idades, nomes

def exibir_resultados(idades, nomes):
    maior_idade = max(idades)
    menor_idade = min(idades)
    saldo_idades = sum(idades)
    
    index_maior = idades.index(maior_idade)
    index_menor = idades.index(menor_idade)
    
    nome_maior = nomes[index_maior]
    nome_menor = nomes[index_menor]
    
    print("\nResultados:")
    print(f"Maior idade: {nome_maior} ({maior_idade} anos)")
    print(f"Menor idade: {nome_menor} ({menor_idade} anos)")
    print(f"Média das idades: {saldo_idades / len(idades):.2f}")
    print(f"Saldo das idades: {saldo_idades}")

def main():
    while True:
        print("\n------- Menu -------")
        print("1 - Inicializar")
        print("2 - Sair")
        option = int(input("\nSelecione: "))
        
        if option == 1:
            idades, nomes = obter_info_pessoas()
            exibir_resultados(idades, nomes)
        elif option == 2:
            break
        else:
            print("Opção inválida.")

main()
