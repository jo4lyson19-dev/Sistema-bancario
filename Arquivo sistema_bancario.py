
# Desenvolvimento de sistema bancário simples

print("="*60)
print("Bem vindo ao Banco BB")
print("="*60)
while True:
        print("D - Deposito")
        print("S - Sacar")
        print("E - Extrato")
        print("Q - Sair")

        escolha = input("Qual sua escolha? ").upper()

        saldo = 0 
        resultado=0
        if escolha== "D":

                valor = float(input("Qual valor será depositado?"))

        if valor <= 0:
                        print("Valor inválido")
        else:
                        saldo = saldo + valor
                        print("Valor aceito!")
                        print(f"Seu saldo agora é: R$ {saldo:.2f}")
        if escolha == "S":

                valor1= float(input("Informe o valor do saque: "))
                resultado =("resultado-valor1")
                print(f"Saque de $ {valor1:.2f} reais feito com sucesso!\n")
                
        elif escolha =='E':
                print(f"Seu Saldo atual é de ${resultado:.2f}reais!\n")

        if escolha == "Q" :
                print("Obrigado por utilizar nosso Banco!")
                break
        else:
                print("Operação inválida,por favor informe a operação correta.")

                
        
        



    




    
    




 