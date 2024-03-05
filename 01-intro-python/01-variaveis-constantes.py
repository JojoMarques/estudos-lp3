# 1. Identificadores: um nome que se dá para variáveis, funções e classes
# letras, números e _
# case sensitive (diferencia maiúsculo de minúsculo)
# palavras reservadas: if, for, class...


# 2. Variável: define o identificador e atribui um valor, não pode não atribuir um valor
# inferência do tipo
# python é linguagem dinâmica
Idade = 20

# 3. Constante
# no python não existe constante, tem convenção: algo definido pelos programadores, que todo mundo segue
# tem que ser com letras maiúsculas
PI = 3.14
PI = 99 # alteraria o valor 

# Comentário de uma linha

'''
comentário de múltiplas linhas (3 apóstrofos)
'''

# 4. Docstring
# Documentar código de funções, classes...
# usa def <identificadores> (parâmetros): --> dois pontos serve pra indicar que terminei de escrever a assinatura da função

def somar (numero1, numero2):
    '''
    Função que soma dois números

    :param numero1: primeiro numero
    :param numero2: segundo numero
    :return: soma dos números
    '''
    return numero1 + numero2

somar (10.0, 2.0)




