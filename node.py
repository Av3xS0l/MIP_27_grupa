class Node:
  def __init__(self,n,s,b,m):
    self.number=n
    self.score=s
    self.bank=b
    self.max=m
    self.heur=None
    self.next=[]
  def append(self, node1):
    self.next.append(node1)
