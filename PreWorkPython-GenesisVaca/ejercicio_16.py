'''
EJERCICIO 16
CONTADOR DE NUMEROS PARES E IMPARES
Crea un programa que cuente y muestre la cantidad de numeros pares e impares en una lista ingresada por el usuario
'''
def number_counter(numbers):
  evenNumber = 0
  oddNumber = 0
  for num in numbers:
    if num % 2 == 0:
      evenNumber += 1
    else:
      oddNumber += 1
  return evenNumber, oddNumber

userList = input('Enter the list of numbers separated by spaces: ').split()
userList = [int(num) for num in userList]

evenNumber, oddNumber = number_counter(userList)

print(f'Number of even numbers:', evenNumber, '\nNumber of odd numbers:', oddNumber)
