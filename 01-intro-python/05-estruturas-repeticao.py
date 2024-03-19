# for, while, break, continue 
# operador in é usado no contexto de verificar se existe e retornar um boolean, mas no for ele serve pra fazer for each

# for
for letra in "Python":
    print(letra)
# aqui tá priintando cada uma das letras da palavra

itens = ["Banana", "Arroz", "Limão"]
alunos = ["Maria", "Pedro"]

for item in itens:
    print(item)

for i in range(5):
    print(i)

print("Range com os três parâmetros:")
for i in range(0,11,2):
    print(i)

lista = list(range(100))
# range convertido em lista

print("exemplo combinação de list + range")
for item in lista:
    print(item)

# type (passa qualquer coisa, e ele devolve o tipo da variável, do valor)
print(type(10))
print(type(range(10)))
print(type(list(range(10))))

# len --> se passar uma sequência, ela retorna o tamanho
print(len(itens))
print(len("Python"))

numeros = [1, 5, 6, 9]

# vai do zero até o final (printando os números)
for numero in numeros:
    print(numero)

print("não precisa, porque vai do zero até o final")
for numero in range(len(numeros)):
    print(numero)

# usa range quando quiser algo especifico

# while
contador = 0
print("While:")
while contador <=5:
    print(contador)
    contador += 1

# break: para parar uma execução totalmente
# encontre o 1º número par:

numeros =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("For usando break")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
        break #aí imprime só o primeiro par que achar

# continue
numeros = [-3, -1, 3, 0, -2]    

print("For usando continue")
for numero in numeros:
    if numero <= 0:
        continue # ele não para a execução, ele só para a interação (ele continua no for, não executa o que está embaixo)
    print(numero)


# compreensão de lista (forma concisa de criar listas em python)
numeros = [2, 3, 4, 5, 6]
quadrados = [4, 9, 16, 25, 36] # mas você não quer fazer isso manualmente -->

print("Jeito não compressivo:")
for numero in numeros:
    quadrados.append(numero ** 2)

quadrados = [numero ** 2 for numero in numeros]
# faz um ao quadrad pra cada numero dentro da lista números

print("Printando a lista ao quadrado feita com compressão de lista")
for quadrado in quadrados:
    print(quadrado)

palavra = "Olá mundo"
letras = [letra for letra in palavra]
print(letras)
letras = [letra.upper () for letra in palavra]
print(letras)

print("Compressão de lista com filtro")
numeros = [1, 2, 3, 4, 6]
pares = [numero for numero in numeros if numero %2 == 0]
print(pares)

