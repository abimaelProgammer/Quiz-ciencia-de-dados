import csv
import random
from classes import Pergunta, Placar

def getPerguntas(lista):
  with open(r'src\perguntas.csv', mode='r',encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
      if linha[7] == 'Ciência de Dados':
        pergunta = Pergunta(linha[0], linha[1], linha[2:6], int(linha[6]))
        lista.append(pergunta)

def sortearPergunta(lista):
  num = random.randint(0,len(lista)-1)
  pergunta = lista[num]
  lista.pop(num)
  return pergunta

perguntas = []
placar = Placar()
getPerguntas(perguntas)
while len(perguntas) > 0:
  pergunta = sortearPergunta(perguntas)
  pergunta.getPergunta(placar)
print("Acabaram as Perguntas!")