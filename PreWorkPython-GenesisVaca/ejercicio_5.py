'''
EJERCICIO 5
SUMA DE NUMEROS PARES
Escribe un programa que calcule la suma de todos los números pares del 1 al 100
'''
sum = 0 

for num in range(1, 101):
  if num % 2 == 0:
    sum += 1

print(f'The sum of all even numbers from 1 to 100 is:', sum)