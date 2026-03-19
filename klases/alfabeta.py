from .node import Node

def _alfabeta(sakums: Node, ieprieks: Node | None, dzilums):
    MAX_DZILUMS = 3

    if sakums.heur != 0:
        return
    if dzilums == MAX_DZILUMS:
        sakums.heiristika()
        return

    for i in range(3, 6):
        sakums.next.append(Node(sakums.number*i, sakums.score + sakums.new_punkti(sakums.number*i),sakums.bank + sakums.new_banka(sakums.number*i), not sakums.max))
        _alfabeta(sakums.next[-1], sakums, dzilums+1)

        if sakums.max:
            if sakums.next[-1].heur > sakums.ab:
                sakums.ab = sakums.next[-1].heur
            elif sakums.ab == 0:
                sakums.ab = sakums.next[-1].heur
            
            if ieprieks != None:
                if ieprieks.ab <= sakums.ab:
                    sakums.heur = sakums.ab
                    return
        
        else:
            if sakums.next[-1].heur < sakums.ab:
                sakums.ab = sakums.next[-1].heur
            elif sakums.ab == 0:
                sakums.ab = sakums.next[-1].heur
            
            if ieprieks != None:
                if ieprieks.ab >= sakums.ab:
                    sakums.heur = sakums.ab
                    return

    sakums.heur = sakums.ab

    


def AlfaBeta(sakums: Node):
    MAX_DZILUMS = 3
    _alfabeta(sakums, None, 0)
    next_node = sakums
    cels = []

    for i in range(MAX_DZILUMS):
        for n in next_node.next:
            if n.heur == next_node.heur:
                cels.append(n.number // next_node.number)
                next_node = n
                break
    return cels