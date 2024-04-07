'''
EJERCICIO 11
CALCULADORA DE EDAD
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual
'''
def age_calculator(currentYear, birthYear):
  age = currentYear - birthYear
  return age

currentYear = float(input('Enter current year: '))
birthYear = float(input('Enter year of birth: '))

age = age_calculator(currentYear, birthYear)

print(f'The age is:', age, 'years old')