class Node(object):
    def __init__(self, item, weight):
        self.left = None
        self.right = None
        self.item = item
        self.weight = weight
    
    def __repr__(self):
        return f'[ left : {self.left} right : {self.right} item : {self.item}  weight: {self.weight} ]'

    def __eq__(self, a):
        return cmp(self.weight, a.weight)
    
    def __lt__(self, a):
        return self.weight < a.weight
    
    def setChild(self, ln, rn):
        self.left = ln
        self.right = rn