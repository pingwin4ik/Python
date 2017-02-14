class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList(object):
    head = None
    tail = None

    def get(self):
        print "list data:"
        current_node = self.head
        while current_node is not None:
            print current_node.data, " > ",
            current_node = current_node.next
        print None

    def put(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
        self.tail = node

    def delete(self, node_value):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == node_value:

                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next

            previous_node = current_node
            current_node = current_node.next

    def size(self):
        temp = self.head
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        print count
        return count

    def indexOf(self, item):
        index = 1
        current = self.head
        found = False
        while current != None:
            if current.data == item:
                found = True
                break
            else:
                current = current.next
                index += 1
        if not found:
            index = None
        print index
        return index


s = LinkedList()
print "PUT count"
s.put(7)
s.put(8)
s.put(46)
s.put(121)
s.size()
print "Index OF"
s.indexOf(8)
s.get()
print "DEL"
s.delete(46)
s.get()
print "SIZE:"
s.size()