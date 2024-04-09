'''Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. 
Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.
'''
import random

numero = random.randint(1,100)

print("Jogo de adivinhação:")

tentativa = int (input("Tente adivinhar o número, digite um número entre 1 a 100:"))
'''
acertou == False

def adivinharNumero(tentativa):
    if(tentativa == numero):
        return acertou == True
    
    elif(tentativa > numero):
        return acertou == False
    
    elif(tentativa < numero):
        return acertou == False
'''    