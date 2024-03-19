# EX03: Escreva um programam em Python quee recebe como entrada o valor de uma compra e apresente como saída o valor final com desconto e o desconto aplicado com base nas seguintes regras:
# Compras entre R$ 0,01 e R$ 9,99 ) - 0% de desconto
# Compras entre R$ 10,00 e R$ 99,99 - 5% de desconto
# Compras entre R$ 100,00 e R$499,99 - 10% de desconto
# Compras iguais ou superiores a R$ 500,00 - 15% de desconto

valor_compra = float(input("Entre com o valor da compra: R$ "))

if(valor_compra >= 0.01 and valor_compra <= 9.99):
    print("Valor não possui desconto: Valor se mantém em R$", valor_compra)

elif(valor_compra >= 10.00 and valor_compra <= 99.99):
    print("Valor com desconto: R$", valor_compra - valor_compra*(5/100))

elif(valor_compra >=100.00 and valor_compra <= 499.99):
    print("Valor com desconto: R$", valor_compra - valor_compra*(10/100))

elif(valor_compra >= 500.00):
    print("Valor com desconto: R$", valor_compra - valor_compra*(15/100))

else:
    print("Valor não possui desconto: R$",valor_compra)

