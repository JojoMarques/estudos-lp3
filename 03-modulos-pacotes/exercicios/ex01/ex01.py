
import calculadora_aquario as calcula

#volume
print("Vamos calcular o volume do seu aquário:")
print("Entre com as seguintes informações sobre o aquário:")
comprimento = float(input("comprimento em cm:"))
altura = float(input("altura em cm:"))
largura = float(input("largura em cm:"))
2
volume = calcula.volume(comprimento, altura, largura)
print(f"O volume do aquário é: {volume} litros")

#potência termostato
print("__________________________________________________________________________")
print("Agora vamos calcular a potência ideal do termostato:")
temp_desejada = float(input("Em qual temperatura você deseja manter seu aquário?"))

potencia = calcula.potencia_termostato(volume,temp_desejada)
print(f"A potência ideal do termostato para alcançar a temperatura de {temp_desejada} ºC é a de {potencia}.")

#quantidade de filtragem
print("__________________________________________________________________________")
filtragem = calcula.qtd_filtragem(volume)
print("A quantidade de água que deve ser filtrada por hora é a de no mínimo", filtragem)
