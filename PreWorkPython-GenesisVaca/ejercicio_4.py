'''
EJERCICIO 4
CONTADOR DE VOCALES
Crea un programa que cuente el numero de vocales en una palabra ingresada por el usuario.
'''
def vowel_counter(word):
  counter = 0
  vowels = ['a', 'e', 'i', 'o', 'u']
  word = word.lower()

  for letter in word:
    if letter in vowels:
      counter += 1
  return counter

userWord = vowel_counter(input('Please, Enter yout word: '))
print(f'The number of vowels in the entered word is:', userWord)