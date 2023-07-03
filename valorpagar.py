'''
1 - Faça o algoritmo para calcular o valor de uma prestação em atraso com base na multa de 2% e também do juros mensal de 1% sobre o valor principal. 
Declare vetores explícitos para entrada do valor da prestação, valorprincipal [ ] e da quantidade de dias em atraso: dias [ ].
Armazene os resultados no vetor ValorPagar [ 5 ].
Ao final imprima a tabela com os vetores valorPrincipal [], dias [] e valorpagar[] . 
Faça um menu de controle.
''''

def calcular_valor_prestacao(valor_pagar, dias):
    const_juros = (100.00 / 30.00) * 0.01
    const_multa = 0.02
    valor_principal = []
    
    for i in range(len(valor_pagar)):
        juros = const_juros * dias[i] * valor_pagar[i]
        multa = const_multa * valor_pagar[i]
        valor_total = valor_pagar[i] + juros + multa
        valor_principal.append(valor_total)
        
        print(f"\nJuros: {juros:.2f}%\nMulta: R${multa:.2f}\nValor total: R${valor_total:.2f}")

    return valor_principal

def main():
    valor_pagar = []
    dias = []
    
    while True:
        print("\n-------- Menu --------")
        print("\n1 - Executar")
        print("2 - Sair")
        opcao = int(input("\nEscolha: "))
        
        if opcao == 1:
            for i in range(5):
                valor = float(input(f"\nDigite o valor a pagar {i + 1}: "))
                valor_pagar.append(valor)
                dia = int(input(f"Dias após vencimento {i + 1}: "))
                dias.append(dia)
            
            valor_principal = calcular_valor_prestacao(valor_pagar, dias)
            valor_pagar.clear()
            dias.clear()
        elif opcao == 2:
            break
        else:
            print("Opção inválida.")
        
main()
