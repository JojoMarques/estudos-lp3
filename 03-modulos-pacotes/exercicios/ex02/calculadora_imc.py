#imc
def imc(peso, altura):
    return  peso/altura**2

#resultado e categorização
def resultado(peso, altura, imc):

    peso_ideal = 24.9 * (altura**2) #pq o senhor especificou que o imc ideal seria 24.9

    if imc <18.5:
        resultado = f"IMC: {imc:.2f} - baixo peso.\nVocê precisaria ganhar {(peso_ideal - peso):.2f} kg para chegar ao peso normal."
    elif 18.5 <= imc <24.9:
        resultado = f"IMC: {imc:.2f} - peso normal."
    elif 25.0 <= imc <= 29.9:
        resultado = f"IMC: {imc:.2f} - excesso de peso.\n Você precisaria perder {(peso_ideal - peso):.2f} kg para chegar ao peso normal."
    elif 30.0 <= imc <= 34.9: 
        resultado = f"IMC: {imc:.2f} - obesidade de classe 1.\n Você precisaria perder {(peso_ideal - peso):.2f} kg para chegar ao peso normal."
    elif 35.0 <= imc <=39.9:
        resultado = f"IMC: {imc:.2f} - obesidade de classe 2.\n Você precisaria perder {(peso_ideal - peso):.2f} kg para chegar ao peso normal."
    elif imc >= 40.0:
        resultado = f"IMC {imc:.2f} - obesidade de classe 3.\n Você precisaria perder {(peso_ideal - peso):.2f} kg para chegar ao peso normal."
 
    return resultado
      

