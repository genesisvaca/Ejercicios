'''
EJERCICIO 17
CONVERSOR DE MILLAS A KILOMETROS
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros
'''
def miles_to_kilometers(miles):
  kilometers = miles * 1.60934
  return kilometers

miles = float(input('Please, enter the miles: '))
kilometers = miles_to_kilometers(miles)

print('{:.2f} miles is {:.2f} kilometers.'.format(miles, kilometers))