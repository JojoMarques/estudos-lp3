'''
AINDA EM ANDAMENTO :(
--> preciso:
- fazer com que a lista de letras tentadas
(as q n estão na palavra), seja iterada a cada
tentativa errada
- definir vitória e derrota
- ...
'''

import random

print("Jogo da forca:")

# definição das funções 
def defineSorteiaPalavra():
  palavras = ["banana", "amora", "uva", "morango", "laranja"]
  palavra = random.choice(palavras)
  return palavra

def montaTracinhos(palavra):
  palavraOculta = []
  for i in range(len(palavra)):
   palavraOculta.append("_")
  return palavraOculta

def mudaTracinhos(palavraOculta, palavra, letraTentada):
  for i in range(len(palavra)):
    if palavra[i] == letraTentada:
      palavraOculta[i] = letraTentada
  return palavraOculta


def pedeLetra (qtdTentativas):
  print("Tentativas: ", qtdTentativas)
  if(qtdTentativas > 0):
    tentativa = input (("\nDigite uma letra:"))
  else:
    print("\nAs tentativas acabaram... Você perdeu!")
  return tentativa 

def compara(tentativa, palavra):
  letrasTentadas = []
  if tentativa in palavra: #se a letra tentada estiver na palavra...
     print("\n", mudaTracinhos(palavraOculta, palavra, tentativa), letrasTentadas)
  else:
    letrasTentadas.append(tentativa)
    print("A palavra não contém essa letra.\nLetras tentadas:\n", letrasTentadas)
    return letrasTentadas
    
  
# chamada das funções 
palavra = defineSorteiaPalavra()
palavraOculta = montaTracinhos(palavra)
print(palavraOculta)

cont = len(palavra) + 1
while cont > 0:
  tentativa = pedeLetra(cont)
  if(tentativa == 0 ):
    break
  compara(tentativa, palavra)
  cont = cont - 1

      
    

