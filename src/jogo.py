import csv
import random

def getPerguntas(lista):
  with open('perguntas.csv', mode='r',encoding='utf-8') as arquivo:
    leitor_csv = csv.reader(arquivo)
    next(leitor_csv)
    for linha in leitor_csv:
      if linha[7] == 'Ciência de Dados':
        pergunta = {'id':linha[0], 'pergunta':linha[1],'opcoes':linha[2:6],'resposta':linha[6]}
        lista.append(pergunta)

def sortearPergunta(lista):
  num = random.randint(0,len(lista))
  pergunta = lista[num]
  return pergunta

def getResposta (pergunta,op,placar):
 resposta = int(pergunta['resposta'])
 return getCorrecao(resposta == op, placar)
def getCorrecao(booleano,placar):
  if booleano == True:
    print("Resposta correta!")
  else:
    print("Resposta incorreta!")
  return atualizaPlacar(booleano,placar)
def atualizaPlacar(booleano,placar):
  if booleano == True:
    placar[0] += 1
    return placar
  else:
    placar[1] += 1
    return placar

perguntas = []
placar = [0,0]
a = 0
while a <= 2:
  getPerguntas(perguntas)
  pergunta = sortearPergunta(perguntas)
  print(pergunta['pergunta'])
  opcoes = pergunta['opcoes']
  for i in range(len(opcoes)):
    print(f'\t {i+1}. {opcoes[i]}')
  op = int(input())
  resposta = getResposta(pergunta,op,placar)
  placar = resposta
  print(f"Placar: {placar[0]} X {placar[1]}")
  a += 1