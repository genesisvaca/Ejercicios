'''
EJERCICIO 13
VERIFICACION DE UN NUMERO PRIMO
Escribe un programa que determine si un numero ingresado por el usuario es primo o no.
'''
def is_prime(num):
  if num <= 1:
    return False
  
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
    return True
  
num = int(input('Please, enter the number you wish to consult: '))

if is_prime(num):
  print(num, 'is a prime number')
else:
  print(num, 'is not a prime number')