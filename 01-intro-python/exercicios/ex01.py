# EX01: Escreva um programa em Python que solicite ao usuário um número inteiro e apresenta seu antecessor e sucessor

# numero = input("Digite um núemero:")
# print(type(numero))
# numero = int (numero)
# print(type(numero))

numero = int (input("Digite um número:")) # vai converter a entrada do usuario pra int
print(type(numero))

print("Antecessor do número digitado:", numero-1)
print("Sucessor do número digitado:", numero+1)