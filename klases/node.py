class Node:
  def __init__(self,n,s,b,m):
    self.number=n
    self.score=s
    self.bank=b
    self.max=m
    self.heur=0
    self.next=[]
  def append(self, node1):
    self.next.append(node1)

  def heiristika(self):
    if self.score % 2 != self.bank % 2:
      self.heur += 1
      if self.number % 5 == 0:
        self.heur += 10
    else:
      self.heur -= 1
      if self.number % 5 == 0:
        self.heur -= 10
  
  def new_banka(self, nm):
      return 1 if nm % 5 == 0 else 0

  def new_punkti(self, nm):
      return 1 if nm % 2 == 0 else -1

  def __lt__(self, other):
    return self.heur < other.heur