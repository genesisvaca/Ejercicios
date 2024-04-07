'''
EJERCICIO 9
CONVERSOR DE DIVISAS
Crea un programa que convierta una cantidad de dolares a euros. Suponiendo que 1 dolar es igual a 0.85 euros
'''
def currency_converter(dollars):
  euros = dollars * 0.85
  return euros

dollars = float(input('Enter how many dollars you want exchange: '))

euros = currency_converter(dollars)
print('with ${} you will get €{:.2f}'.format(dollars,  euros))