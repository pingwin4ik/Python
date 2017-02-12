class Node:
    def __init__(self, data):
        self.data = data

        self.next = None
        self.prev = None


class LinkedList:
    def __init__( self ):
        self.head = None

    def add(self, data ):
        node = Node( data )
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    def search( self,k):
        p = self.head
        if p != None:
            while p.next != None:
                if p.data == k:
                    return p
                p = p.next
                if p.data == k:
                    return p
            return None


    def remove( self, p ):
        tmp = p.prev
        p.prev.next = p.next
        p.prev = tmp


    def __str__( self ):
        s = ""
        p = self.head
        if p != None:
            while p.next != None:
                s += p.data
                p = p.next
                s += p.data
            return s

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count


    # def get(self, pos=0):
    #     if pos == 0:
    #         return self.head.item
    #     elif pos > 0:
    #         current = self.head
    #         count = 0
    #         while count < pos - 1 and current.link != None:
    #             current = current.link
    #             count += 1
    #     return current.item
    #     else:
    #     raise IndexError()

l = LinkedList()

l.add( 'a' )
l.add( 'b' )
l.add( 'c' )

print (l)

print (size())

l.remove( l.search( 'b' ) )
print()
print (l)
