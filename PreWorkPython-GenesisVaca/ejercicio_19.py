'''
EJERCICIO 19
VERIFICACION DE A;O BISIESTO
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no.
'''
def leap_year_verification(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    return True
  else:
    return False

year = int(input('Enter a year: '))

if leap_year_verification(year):
  print(year, 'is a leap year')
else:
  print(year, 'is not a leap year')
