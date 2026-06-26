menu1=int(input("Digite o número da operação desejada: \n1 para Adição \n2 para Subtração \n3 para Multiplicação \n4 para Divisão "))
if menu1==1:
    num1=float(input("Digite o primeiro número: "))
    num2=float(input("Digite o segundo número: "))
    resultado=num1+num2
    print()
    print(f"O resultado da adição é: {resultado:.2f}")
    print()
    
elif menu1==2:
    print()
    num1=float(input("Digite o primeiro número: "))
    num2=float(input("Digite o segundo número: "))
    resultado=num1-num2
    print()
    print(f"O resultado da subtração é: {resultado:.2f}")
    print()
    
elif menu1==3:
    print()
    num1=float(input("Digite o primeiro número: "))
    num2=float(input("Digite o segundo número: "))
    resultado=num1*num2
    print()
    print(f"O resultado da multiplicação é: {resultado:.2f}")
    print()
    
elif menu1==4:
    print()
    num1=float(input("Digite o primeiro número: "))
    num2=float(input("Digite o segundo número: "))
    resultado=num1/num2
    print()
    print(f"O resultado da divisão é: {resultado:.2f}")
    print()
    
else:
    print()
    print("Operação inválida. Escolha um número entre 1 e 4.")
    print()
    
    print("FIM")