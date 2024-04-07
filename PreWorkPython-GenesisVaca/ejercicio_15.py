'''
EJERCICIO 15
CONVERSOR DE TIEMPO
Escribe un programa que convierta un numero de minutos en horas y minutos. Por ejemplo, 145 minutos serian 2 horas y 25 minutos
'''
def time_converter(minutes):
  hours = minutes // 60
  remainingMinutes = minutes % 60
  return hours, remainingMinutes

minutes = int(input('Please enter the minutes: '))

hours, remainingMinutes = time_converter(minutes)

print(f'{minutes} minutes would be {hours} hours and {remainingMinutes} minutes')