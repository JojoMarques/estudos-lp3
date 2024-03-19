# if, if/else, elif (else if) --> sempre que cair em um, tenta ver se match case não dá conta/
# operador ternário
idade = 20

if idade>=18:
    status = "Maior de idade"
else:
    status = "Menor de idade"       

status = "Maiior de idade" if idade>=18 else "Menor de idade"

#match case (é o switch do python)
#está no python desde a versão 3.10
#mais poderoso que o switch case

dia = 3
match dia:
    case 1:
        print("Segunda-feira")
    case 2:
        print("Terça-feira")
    case 3:
        print("Quarta-feira")
    case _:
        print("Inválido")

#identação: segue os blocos (onde cada um está dentro)

#imprimir
#1 e 7 - fim de semana
#2,3,4,5 e 6 - dia útil
#agrupar cases

match dia:
    case 1 | 7:
        print("Fim de semana")
    case 2 | 3 | 4 | 5 | 6:
        print("Dia útil")
    case _:
        print("Dia inválido")





