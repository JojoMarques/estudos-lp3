'''Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. 
Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.
'''
import random

print("Jogo de adivinhação\nAdivinhe o número")
numero = random.randint(1, 100)

# definindo a função
def jogoAdivinhacao(numero):
    tentativa = int(input("Entre com o seu palpite de número: "))
    acertou = False
  
    if (tentativa == numero):
        print("Parabéns!! Você acertou :)")
        acertou = True
    elif (tentativa > numero):
        print("Palpite muito alto.")
    elif (tentativa < numero):
        print("Palpite muito baixo.")
    
    return acertou

# chamando a função
resultado = jogoAdivinhacao(numero)
while resultado == False: # vai chamar ate o jogador acertar
    acertou = jogoAdivinhacao(numero)
