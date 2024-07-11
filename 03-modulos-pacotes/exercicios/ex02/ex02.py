import calculadora_imc as calcula

print("Vamos calcular seu IMC (índice de massa corporal)")
peso = float(input("Entre com seu peso em kg:"))
altura = float(input("Entre com sua altura em metros:"))

imc = calcula.imc(peso, altura)
print("________________________________________________")
resultado = calcula.resultado(peso,altura, imc)
print("Resultado: \n",resultado)
