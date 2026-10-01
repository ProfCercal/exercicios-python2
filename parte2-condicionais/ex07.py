# 7. Peça dois números e exiba qual é o maior. Se forem iguais, informe isso.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2: #se num1 > num2
    print("O primeiro número é o maior.")
elif num2 > num1: #senao
                    #se num2 > num1
    print("O segundo número é o maior.")
else:               #senao
    print("Os dois números são iguais.")