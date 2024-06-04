# Funções
# programa que normalmente tem uma entrada, processamento e saída (vc manda algo, ela faz alguma coisa com a entrada e te manda algo)

# declaração:
# def nomeDaFunção (parâmetros):
#   return 

# Função sem retorno e sem parâmetro:
def imprimirSaudação ():                                              
    print("Bodia princesa")
                           
# Função sem retorno com parâmetros (um ou mais):
def imprimirNome(nome):
    print(f'nome: {nome}')

# Função com retorno sem parâmetro:
def gerarSaudacao ():
    return "Bom dia, princesa" # tá só retornando 

# Função com retorno e com parâmetro(s):
def gerarSaudacao2 (nome):
    return f'Bom dia, {nome}'
        
# parâmetro vs argumento:
# parâmetro é a referência definida na assinatura da função (pq vc pode acessar nome em qualquer lugar dentro da função) --> 
# argumento é o valor (literal) ou a referência passada ou enviada para um parâmetro (pode passar um literal diretammente, ou o valor de uma variável (a referência))
# return não é obrigatório em funções, mas é "horrível" sem retorno
# em Python não tem sobrecarga

# chamada da função:
print("Olá") # uma função já declarada em algum lugar, aqui é só a chamada dela 
imprimirSaudação() # tem que ter o (), mesmo que seja vazio    
# não dá pra chamar a função antes de declarar ela
imprimirNome("Jô") # Jô é o valor, o argumento que eu tô passando pro argumento nome

print(gerarSaudacao()) # ou
saudacao = gerarSaudacao() # assim é melhor (?)
print(saudacao)

print(gerarSaudacao2("Jojozinha")) # ou
saudacaoJo = gerarSaudacao2("Jojo")
print(saudacaoJo)

# Funções:
# return     parâmetro
#   0            0
#   0            1
#   1            0
#   1            1     (melhor caso, porque )

# caso: imprimir saudação com o nome do usuário
# 1° caso não dá
# 2° caso dá
def imprimir_saudacao(nome):
    print(f'Bom dia, {nome}')
# 3° caso não dá
# 4° caso dá e é melhor:
# pq as vezes vc não quer imprimir
def geral_saudacao2(nome):
    return f'Bom dia, {nome}'
# posso usar ela pra fazer todas as coisas que eu quero
# função pura: não tem efeito colateral e sem acesso a estado global
# efeito colateral dá 2: vai jogar um i.o, efeito colateral da 4: nenhum, pq só retorna

# EXEMPLO: calcule a média das notas de vários alunos:
# entrada = [[10,6], [10,10], [6,6]] (lista onde dentro dela vc tem outras listas (as notas de um aluno))
# calcularmedia = lista de notas --> return media
# calcularMedias (de td mundo) = lista de lista de notas --> return lista de média (pq cada lista de notas retorna um valor só (a média))
# imprimir lista de média


notas_alunos = [
    [10,6],
    [10,10],
    [6,6]
]

def calcularMedia(notas):
    return sum(notas)/len(notas)

def calcularMedias(notas_alunos): #essa recebe o conjunto todo de
    #medias = []

    '''
    for notas in notas_alunos:
        medias.append(calcularMedia)

    return medias'''
    
    return [calcularMedia(notas) for notas in notas_alunos] # retornando um alista, nela é retornado todos os elementos que estão em notas ... (?)

print(calcularMedias(notas_alunos))

# Argumentos nomeados: quando se tem muitos parâmetrps, e você nomeia o0 argumneto na hora de chamar (esse valor vai pra esse param, esse pra outro...)
def nova_saudacao (nome, saudacao):
    return f'{saudacao}, {nome}'

print(nova_saudacao("Jojo", "Bom dia"))
print(nova_saudacao("Latorre", "Boa tarde"))
print(nova_saudacao("Igor", "Boa noite"))
# ou
print(nova_saudacao(nome = "Jô Tavares", saudacao ="Bodia")) #nomeou um , tem que nomear todos (no caso os prineiros não precisam ser nomeados obrigatoriamente se o 
# último tiver sido) --> se tirar a definição do nome, roda normal, se tirar a do último, não vai

print("Olá", "mundo!", sep=" qqr coisaaaa")
# sep eh acessado via argumento nomeado --> sep eh a separação

# Valores padrão para parâmetros:
def obter_saudacao(nome, saudacao = "Bom dia"):
    return f'{saudacao}, {nome}'

obtemSaudacao = obter_saudacao("Jojozita")
print(obtemSaudacao)

#sobrecarga:
obtemSaudacao2 = obter_saudacao("Cabron!", "Buenos días") # --> substituiu a saudação padrão pelo que eu coloquei
print(obtemSaudacao2)
# simula com parâmetros default

# *args (Non-Keywords Arguments)
''''
def calcular_media (notas):
    return sum(notas)/len(notas)
# nessa função, eu espero que entrem com uma lista ou uma tupla de notas
'''
# calcular_media(10.0, 3.0) --> ele entende que são 2 valores
# calcular_media(7.0, 3.0, 2.0, 5.50) # --> ele entende que são 4 valores --> poderia colocar 4 param, mas:
# usa o Non-Keywords Arguments
def calcular_media (*notas):
    print(type(notas))
    return sum(notas)/len(notas)
# --> * fala que pode passar qqr número de valores nos args, e o python transforma isso em uma TUPLA (o type ali foi só pra comprovar)
# sempre que ver o *, vc sabe que vai receber uma TUPLA
print(calcular_media(10.0, 10.0, 10.0, 10.0))


'''
ex03:
def contarVogaisEConsoantes ():
    return (2 valores...)
    '''