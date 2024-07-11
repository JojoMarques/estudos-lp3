#volume
def volume(comprimento, altura, largura):
    return (comprimento*altura*largura)/1000

#potencia termostato
# "De acordo com a OMS, a temperatura ambiente ideal para locais fechados varia de 23°C a 26°C."
# fonte: https://blog.frigelar.com.br/qual-temperatura-ideal-ambiente/
TEMP_AMBIENTE = 26.00
def potencia_termostato(volume, temp_desejada):
    return (volume*0.05*(temp_desejada - TEMP_AMBIENTE))

#filtragem
def qtd_filtragem (volume):
    return f"{volume*2} a {volume*3} litros"
