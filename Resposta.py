from textblob import TextBlob
from googletrans import Translator
from funcoes import detects_feeling

""" 
A biblioteca que eu estou utilizando, a textblob, só faz testes de polaridade em inglês, logo tive de utilizar outra
biblioteca para fazer a tradução.
"""

tradutor = Translator()

print('Digite a frase a ser analisada: ')
texto = input().lower()

textoTraduzido = tradutor.translate(texto, src='pt', dest="en")
textoSentimento = TextBlob(textoTraduzido.text)

# Sentimentos dentro de um dicionario
dados = {
       'tristeza':['triste', 'chorar', 'chorei', 'choro', 'melancolia', 'melancólico', 'deprimido', 'mal'],
       'alegria':['alegria', 'feliz', 'felicidade', 'amor', 'boa', 'contente', 'próspero', 'abençoado', 'amar', 'bem'],
       'raiva':['raiva', 'irritação', 'cólera', 'ira', 'fúria', 'zangado', 'desprazer', 'ódio', 'odeia']
}

feelings = list()


for feeling in dados:
  current_feeling = detects_feeling(feeling, texto, dados)

  if len(current_feeling) > 0:
    feelings.append(current_feeling)

if textoSentimento.sentiment.polarity > 0 and len(feelings) > 0:
  print("Os sentimentos detectados foram positivos! Detectou-se {}".format(feelings))
elif textoSentimento.sentiment.polarity < 0 and len(feelings) > 0:
  print("Os sentimentos detectados foram negativos! Detectou-se {}".format(feelings))
else:
  print('Nenhum sentimento foi detectado')

