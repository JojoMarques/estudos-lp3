
#EX04: Simulador 'de Eleições': Crie um programa que simule uma votação com 
#três candidatos. O programa deve pedir ao usuário para votar várias vezes e,
#no final, mostrar o número de votos de cada candidato e quem foi o vencedor.

print("Simulador de eleições entre 3 candidatos:")

listaVotos = [0, 0, 0]

# definição das funções 
def defineCandidatos():

    candidato1 = input("Entre com o nome do primeiro candidato:")
    candidato2 = input("Entre com o nome do segundo candidato:")
    candidato3 = input("Entre com o nome do terceiro candidato:")
    candidatos = [candidato1, candidato2, candidato3]

    return candidatos


def votacao(candidatos, listaVotos):

    print("\n---VOTAÇÃO---\n")
    print("Opção: | Candidato:")
    print(f'  1    | {candidatos[0]}')
    print(f'  2    | {candidatos[1]}')
    print(f'  3    | {candidatos[2]}')
    voto = int(input("\nEntre com a opção referente ao candidato que você deseja votar:\n"))


    match voto:
        case 1:
            listaVotos[0] += 1
        case 2:
            listaVotos[1] += 1
        case 3:
            listaVotos[2] += 1
        case _:
            print("Opção inválida!!")

    return listaVotos

def verificaParada():

    print("\n\nDeseja continuar a votação?")
    continuar = int(input("\n1 | SIM \n2 | NÃO\n--> "))

    pararVotacao = False

    match continuar:
        case 1:
            pararVotacao = False
        case 2:
            pararVotacao = True
        case 3:
            print("Opção inválida!!")

    return pararVotacao

def exibeQtdVotos(votos, candidatos):

    print("\nQUANTIDADE DE VOTOS DE CADA CANDIDATO:\n")
    print(f'Candidato 1: {candidatos[0]} --> {votos[0]} votos.')
    print(f'Candidato 2: {candidatos[1]} --> {votos[1]} votos. ')
    print(f'Candidato 3: {candidatos[2]} --> {votos[2]} votos.')

def verificaVencedor(votos, candidatos):
  
    if votos[0] > 0 and votos[0] == votos[1] and votos[1] == votos[2]:
        print("Empate entre os três candidatos.")
    elif votos[0] > votos[1] and votos[0] > votos[2]:
        print(f'O candidato {candidatos[0]} ganhou a votação, com {votos[0]} votos.')
    elif votos[1] > votos[0] and votos[1] > votos[2]:
        print(f'O candidato {candidatos[1]} ganhou a votação, com {votos[1]} votos.')
    elif votos[2] > votos[0] and votos[2] > votos[1]:
        print(f'O candidato {candidatos[2]} ganhou a votação, com {votos[2]} votos.')
    elif votos[0] > 0 and votos[0] == votos[1]:
        print(f'Empate entre os candidatos {candidatos[0]} e {candidatos[1]}.')
    elif votos[0] > 0 and votos[0] == votos[2]:
        print(f'Empate entre os candidatos {candidatos[0]} e {candidatos[2]}.')
    elif votos[1] > 0 and votos[1] == votos[2]:
        print(f'Empate entre os candidatos {candidatos[1]} e {candidatos[2]}.')

# chamada das funções   
listaCandidatos = defineCandidatos()

# pra fazer com que a votacao ocorra 3x (p dar chance de cada cand receber um voto)
votos = votacao(listaCandidatos, listaVotos)
votos = votacao(listaCandidatos, votos)
votos = votacao(listaCandidatos, votos)
    
resposta = verificaParada()

while resposta is False:
    votos = votacao(listaCandidatos, votos)
    resposta = verificaParada()

exibeQtdVotos(votos,listaCandidatos)   
verificaVencedor(votos,listaCandidatos)
          
