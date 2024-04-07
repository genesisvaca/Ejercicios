'''
EJERCICIO 10
DETERMINAR EL DIA DE LA SEMANA
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.)
'''
def day_of_week(number):
  weekDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  
  if number < 1 or number > 7:
    return 'Incorrect number. Please enter a number between 1 and 7'
  
  return weekDays[number - 1]

number = int(input('Enter a number between 1 - 7 too know the day of the week: '))

weekDays = day_of_week(number)

print(f'The day of the week is:', weekDays)