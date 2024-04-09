# Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.

numero = int(input("Digite um número:"))

# definição da função
def tabuada (numero):
    for cont in range(0,11):
         resultado = numero * cont
         print(f'{numero} x {cont} = {resultado}')

# chamada da função
tabuada(numero)