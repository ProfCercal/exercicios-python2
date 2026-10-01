# 12. Peça números ao usuário e vá somando. Quando ele digitar 0, pare e exiba a soma.

soma = 0
numero = float(input("Digite um número (0 para sair): "))
# escreval("Digite um número (0 para sair): ")
# leia(numero)

while numero != 0:
    soma = soma + numero
    numero = float(input("Digite um número (0 para sair): "))

print(f"A soma total é: {soma}")