class Node():
    def __init__(self,item):
        self.item = item
        self.next = None
class Link():
    head = None
    def a(self,item):
        if not self.head :
            self.head = Node(item)
        else:
            n = self.head
            while n.next != None:
                n = n.next
            n.next =  Node(item)
    def string(self):
        if self.head :
            a= self.head
            s = []
            while  a.next != None:
                s.append( str(a.item))
                a = a.next
            return ','.join(s)

l = Link()
l.a(1)
l.a(2)
l.a("3")    
l.a("4")
l.a("5")
print(l.string()) 