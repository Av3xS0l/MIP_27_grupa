from .node import Node

def _minimax(sakums: Node, dzilums):
    MAX_DZILUMS = 3
    
    if dzilums == MAX_DZILUMS:
        sakums.heiristika()
        return 
    
    for i in range(3, 6):
        sakums.next.append(Node(sakums.number*i, sakums.score + sakums.new_punkti(sakums.number*i),sakums.bank + sakums.new_banka(sakums.number*i), not sakums.max))
        _minimax(sakums.next[-1], dzilums+1)
    
    if sakums.max:
        sakums.heur = max(sakums.next).heur
    else:
        sakums.heur = min(sakums.next).heur

def Minimax(sakums: Node):
    MAX_DZILUMS = 3
    _minimax(sakums, 0)
    next_node = sakums
    cels = []
    for i in range(MAX_DZILUMS):
        for n in next_node.next:
            if n.heur == next_node.heur:
                cels.append(n.number // next_node.number)
                next_node = n
                break
    return cels