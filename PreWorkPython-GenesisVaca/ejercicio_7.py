'''
EJERCICIO 7
CALCULADORA SIMPLE
Crea un programa que realice operaciones aritmeticas simples (suma, resta, multiplicacion, division) segun la eleccion del usuario
'''
def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def divide(x, y):
  return x / y

def multiply(x, y):
  return x * y

print('Select operation: \n 1) ADDITION\n 2) SUBTRACTION\n 3) DIVISION\n 4)MULTIPLICATION')

userNum = input('Enter choice (1/2/3/4): ')

if userNum in ('1', '2', '3', '4'):
  num1 = float(input("Enter first number: "))
  num2 = float(input("Enter second number: "))

  if userNum == '1':
    print("Result:", add(num1, num2))
  elif userNum == '2':
    print("Result:", subtract(num1, num2))
  elif userNum == '3':
    print("Result:", divide(num1, num2))
  elif userNum == '4':
    print("Result:", multiply(num1, num2))
else:
  print("Invalid choice, TRY AGAIN")