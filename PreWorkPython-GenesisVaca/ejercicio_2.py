'''
EJERCICIO 2
CALCULADORA DE PROPINA
Crea un programa que calcule el monto total a pagar en un restaurante, inlcuyendo una propina del 15% sobre el total de la cuenta
'''
def bill_plus_tip(baseBill):
  return ((baseBill * 15) /100 + baseBill)

totalAmount = bill_plus_tip(float(input('Please, enter the base amount: ')))
print(f'The total amount, including tip, is', totalAmount) 