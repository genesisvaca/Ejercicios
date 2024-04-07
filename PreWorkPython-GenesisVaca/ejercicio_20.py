'''
EJERCICIO 20
SUMA DE NUMEROS EN UNA LISTA
Crea un programa que sume todos los números en una lista ingresada por el
usuario
'''
numbersList = input('Please, enter the list of numbers separated by spaces: ').split()

numbersList = [int(num) for num in numbersList]

sumNumbers = sum(numbersList)

print('Total numbers in the list is', sumNumbers)