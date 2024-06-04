# import matematica

# main space
from matematica import PI as PI_MATH, somar, subtrair
# PI as PI_MATH renomeia pra cá (passa pra cá com esse nome)

PI = 3

print('PI:',PI_MATH)
print('meu PI:', PI)
print('soma:', somar(2, 3))

# from matematica import *

from estatistica.descritiva import media, maximo, minimo
from estatistica.inferencial import VALOR

print(media(range(0,11)))
print(maximo(range(0,11)))
print(minimo(range(0,11)))



