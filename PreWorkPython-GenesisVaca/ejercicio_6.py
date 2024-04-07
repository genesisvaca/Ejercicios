
'''
EJERCICIO 6
VERIFICACION DE PALINDROMO
Crea un programa que verifique si una palabra ingresada por el usuario es un palindromo (se lee igual de izquierda a derecha que de derecha a izquierda)
'''
def palindrome(word):
  word = word.lower()
  word = word.replace(' ', '')

  if word == word[::-1]:
    return True
  else:
    return False
  
userWord = palindrome(input('Please, enter a word: '))

if userWord:
  print('The word is a palindrome.')

else:
  print('The word is not a palindrome.')