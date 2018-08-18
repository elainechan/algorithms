class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, x):
        current = self.head # initialize current to head
        while current != None: # loop until current not equal to None
            if current.data == x:
                return True # data found
            current = current.next
        return False # data not found
    
    def print_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
            
    def print_nodes(self):
        node = self.head
        while node:
            print(node)
            node = node.next
            
    def delete_position(self, position):
        node = self.head
        counter = 0
        while node is not None:
            if (counter == position - 1) and node.next is not None:
                print(f'Data to be deleted: {node.next.data}')
                node.next = node.next.next
                print('Data has been deleted.')
                return
            counter += 1
            node = node.next
        return

    def __iter__(self): # generator
        node = self.head
        while node:
            yield(node.data)
            node = node.next

class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
        
    def insert_after(self, new_node):
        new_node.next = self.next # set current `next` as new node's `next
        self.next = new_node # set new node as current's `next`
        
    # delete node after current, assuming node is not a tail.
    def delete_after(self):
        self.next = self.next.next
        
if __name__ == "__main__":
    main()