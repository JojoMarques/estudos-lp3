#EX03: Contador de Vogais e Consoantes: Peça ao usuário para 
#digitar uma frase e retorne o número de vogais e consoantes na frase.

print("Contador de vogais e consoantes:")
frase = input("Digite uma frase:")

# definição da função 
def contagem(frase):
    qtdVogais = 0
    qtdConsoantes = 0
    vogais = ["A", "E", "I", "O", "U", 
              "À", "Á", " ", "Ã", "Ê", "É", "Í", 
              "Ó", "Ô", "Õ"]
    for letra in frase: # percorrendo cada letra da frase
      if letra.isalpha():
        if letra.upper() in vogais:
            qtdVogais += 1
        elif letra.isalpha():
            qtdConsoantes += 1
          
    quantidades = [qtdVogais, qtdConsoantes]
    return quantidades

# chamada da função 
resultado = contagem(frase)

print("Quantidade de vogais: ", resultado[0])
print("Quantidade de consoantes:", resultado[1])
