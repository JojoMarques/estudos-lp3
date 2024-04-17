
# Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite uma
#palavra ou frase e verifique se é um palíndromo (ou seja, pode ser lida 
#de frente para trás e de trás para frente da mesma forma).
# ex: ana

print ("Verificador de palíndromos:")
entrada = input(("Digite uma palavra ou frase:"))

# definicao da função:
def verificador(entrada):
  entrada = entrada.replace(" ", "").lower() # remove espaços e 
  # deixa tudo minúsculo pra comparação 
  
  if entrada == entrada[::-1]:
    print("É um palíndromo.")
  else:
    print("Não é um palíndromo.")

# chamada da função:
verificador(entrada)
