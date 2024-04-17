# EX06: Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), 
#converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.
#fonte do padrão de  notas adotado:

'''
link: 
https://pt.wikihow.com/Calcular-Notas
(me baseei na tabela apresentada no 5° método apresentado)

"[...] a divisão mais comum é a seguinte:
A = 93-100%.
A- = 90-92%.
B+ = 87-89%.
B = 83-86%.
B- = 80-82%.
C+ = 77-79%.
C = 73-76%.
C- = 70-72%.
D+ = 67-69%.
D = 63-66%.
D- = 60-62%.
F = 0-59%. "
'''

print("• Conversor de notas escolares numéricas (0 - 100) para notas letradas (A, B, C, D ou F): •\n")
nota = float(input("Digite a nota/pontuação: "))

# definição da função 
def conversor(nota):
    if nota >= 0 and nota <=100:
        print("Nota/pontuação convertida para:")
        if(nota >= 93):
            print("A")
        elif (nota >= 90 and nota <=92):
            print("A-")
        elif (nota >= 87 and nota <= 89):
            print("B+")
        elif (nota >= 83 and nota <= 86):
            print("B")
        elif (nota >= 80 and nota <= 82):
            print("B-")
        elif (nota >= 77 and nota <= 79):
            print("C+")
        elif (nota >= 73 and nota <= 76):
            print("C")
        elif (nota >= 70 and nota <= 72):
            print("C-")
        elif (nota >= 67 and nota <= 69):
            print("D+")
        elif (nota >= 63 and nota <= 66):
            print("D")
        elif (nota >= 60 and nota <= 62):
            print("D-")
        elif (nota >= 0 and nota <= 59):
            print("F")
    else:
        print("A nota/pontuação digitada é inválida.")

# chamada da função 
conversor(nota)


