class Placar:
  def __init__(self):
    self.pont = [0,0]
  
  def mostraPlacar(self):
      print(f"Placar: {self.pont[0]} X {self.pont[1]}")
  
  def getCorrecao(self,Boll):
    if Boll == True:
      self.pont[0] += 1
    else:
      self.pont[1] += 1
    self.mostraPlacar()

class Pergunta:
  def __init__(self, id:int, questao:str, op:list, RC:int):
    self.id = id
    self.questao = questao
    self.op = op
    self.RC = RC
  
  def getPergunta(self,placar:Placar):
    print(f"{self.id}. {self.questao}")
    for i in range(4):
      print(f"\t {i+1}. {self.op[i]}")
    op = int(input("Digite uma das Alternativas acima: "))
    return self.getResposta(op,placar)
    
  
  def getResposta (self,op:int, placar:Placar):
    if op not in [1,2,3,4]:
      print("Resposta Inválida")
      self.getPergunta(placar)
    elif self.RC == op:
      print("Resposta Correta!")
      return placar.getCorrecao(True)
    else:
      print("Resposta Incorreta!")
      return placar.getCorrecao(False)