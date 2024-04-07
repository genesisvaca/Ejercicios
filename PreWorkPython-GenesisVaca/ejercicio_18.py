'''
EJERCICIO 18
CONTADOR DE PALABRAS
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario
'''
def word_counter(sentece):
  words = sentence.split()
  wordCount = len (words)
  return wordCount

sentence = input("Enter a sentece: ")

numWords = word_counter(sentence)

print("Number of word:", numWords)