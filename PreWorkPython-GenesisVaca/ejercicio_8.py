'''
EJERCICIO 8
CALCULO DE INDICE DE MASA CORPORAL (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona
'''
def user_bmi(weight, height):
  bmi = weight / (height * height)
  return bmi

def result_bmi(bmi):
  if bmi < 18.5:
    return 'Underweight'
  elif bmi <25:
    return 'Normal weight'
  elif bmi <30:
    return 'Overweight'
  else:
    return 'Obese'
  
weight = float(input('Enter your weight in Kg: '))
height = float(input('Enter your height in meters: '))

bmi = user_bmi(weight, height)

result = result_bmi(bmi)

print(f'Your BMI is:', bmi)
print(f'Result:', result)