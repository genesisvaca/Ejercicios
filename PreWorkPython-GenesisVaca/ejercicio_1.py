'''
EJERCICIO 1
CONVERSOR DE TEMPERATURA
Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit
'''
def celsius_to_fahrenheit(degreesCelsius):
  return (degreesCelsius * 9/5) + 32

degreesFahrenheit = celsius_to_fahrenheit(float(input('Please, enter degrees Celsius: ')))
print(f'It is {degreesFahrenheit} degrees Fahrenheit')