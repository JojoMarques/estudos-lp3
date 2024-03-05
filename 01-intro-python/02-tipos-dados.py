# Tipos de dados:

# 1. Numérico: int, float, complex
idade = 17 # int (identificador = valor int)
saldo = -1

altura = 1.54 # float
# complex (pesquisar)

# 2. Booleano 
verdade = True # tem que ser maiúsculo
mentira = False

# 3. String: sequência de caracteres
nome = "Jô"
nome = 'Jô'
# pode definir das duas formas (com aspas duplas e apóstrofo)

# multilinha: manter a formatação da string
frase = """ Olá mundo, 
Como você está?
Teste
123
"""

# interpolação:
# f-strings: coloca no início da string um f minúsculo
nome = "Jô"
idade = 17
frase = f"Olá {nome}. Você tem {idade} anos"
print (frase)

# char: string de um caracter só
letra = 'a'
letra = "b"

# Acesso de um caracter da string:Docstring
nome = "Jô Tavares"
nome[0] #acessa igual array
print(nome[0])
print(nome[-1]) # põe - pra pegar ao contrário
print(nome[0:3]) # pega a sequência de um intervalo
# espaço conta 

# Strings no python são objetos:

# a variável nome é uma variável do tipo string que aponta pra um objeto string
# Strings tem métodos em python, porque são objetos
print(nome.upper()) # retorna uma nova string em maiúsculo, ele não transforma, so retorna
# nome = nome.upper() aqui transforma em maiúsculo
print(nome.capitalize())

# 4. List: também é objeto em python
# lista de valores: é indexada, consegue acessar os valores a partir da posição
habilidades = [] # representa uma lista vazia
# colocar valores: 
habilidades = ['java', 'python', 'php']
# como acessar:
print(habilidades[0])
# como adicionar um elemento na lista:
habilidades.append('c#')
print(habilidades[-1])
# como mostrar a lista inteira:
print(habilidades)
# como inserir em uma posição específica:
habilidades.insert(2, "css")
print(habilidades)
# habilidades.clear()

for habilidade in habilidades:
    print(habilidade, end = ", ")
# habilidade é uma variável dinâmica que vai ter o valor da lista a cada rodada --> costuma sempre colocar no singular

# 5. Tuple (tupla): é uma lista de valores, que não pode ser alterada--> não pode adicionar e nem remover valores
# só trocar [] da lista por ()
opcoes = ('sim', 'não', 'talvez')
# como acessar o primeiro índice da tupla: igual em lista
opcoes[0]

for opcao in opcoes:
    print(opcao)

# Set (conjunto): é um conjunto de valores
# não permite elementos duplicados
# não é indexado    
# só trocar [] da lista por {}
habilidades = {'java', 'python','c#'}
print(habilidades)
# habilidades[i] não vai funcionar

# 6. Dict (dicionário):
# palavras -> definição 
# chave -> valor associado
# key -> value
# conjunto chave valor
nome = "Pedro Alves"
idade = 17
habilidades = ["java", "c#"]
empregado = True

candidato = {
    'nome': "Pedro Alves", 
    'idade': 17, 
    'habilidades': ['java', 'c#'],
    'empregado': True
}

print(candidato) #pega inteiro
print(candidato ['nome']) #pega só o nome
print(candidato.keys()) # pega todas as chaves
print(candidato.values()) # pega todos os valores

# quando tem uma classe só com get e set, dicionário é a melhor opção

# 7. None: é o nulo
# nulo é um tipo em python
nome = None # só aceita none
# quando que definir a variável sem valor, usa ele, já que python não deixa definir sem tipo









