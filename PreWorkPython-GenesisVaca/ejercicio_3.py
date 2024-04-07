'''
EJERCICIO 3
VERIFICADOR DE EDAD
Escribe un programa que solicite la edad de un usuario y determine si es mayor de edad(mayor o iigual a 18 a;os) o no
'''
def minor_or_adult(age):
  if age <= 17 and age >= 0:
    return'You are still a minor'
  elif age >= 18 and age <= 150:
    return'You are legally an adult'
  else:
    return"Are you sure it's your age? Try again"

age = minor_or_adult(int(input('Please, enter your age: ')))
print(age)