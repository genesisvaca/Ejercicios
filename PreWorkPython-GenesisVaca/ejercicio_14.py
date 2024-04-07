'''
EJERCICIO 14
CALCULADORA DE DESCUENTO
Crea un programa que calcule el precio final de un articulo despues de aplicar un descuento del 20%
'''
def price_calculator(price):
  return price - (20 * price / 100)

totalPrice = price_calculator(float(input('Please enter the initial price of the item: ')))

print(f'The total price after applying a 20% discount is €', totalPrice)
