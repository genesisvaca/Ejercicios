'''
EJERCICIO 12
CALCULADORA DE AREA DE UN RECTANGULO
Crea un programa que calcule el area de un rectangulo. El usuario debe ingresar la longitud y el anchodel rectangulo
'''
def rectangle_area(length, width):
  area = length * width
  return area

length = float(input('Enter the length of the rectangle: '))
width = float(input('Enter the width of the rectangle: '))

area = rectangle_area(length, width)
print(f'The total area of the triangle is:', area)
