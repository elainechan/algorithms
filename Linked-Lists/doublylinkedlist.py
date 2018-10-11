class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def push(self, new_data): # insert in front of list
        new_node = DNode(new_data)
        new_node.next = self.head # set head as new node's `next`
        if self.head is not None:
            self.head.prev = new_node # set new node as head's `prev`
        self.head = new_node
    
    def insert_after(self, target_node, new_data):
        if target_node is None:
            print('The given target node does not exist')
            return
        new_node = DNode(new_data)
        new_node.next = target_node.next # set target `next` as new node's `next`
        target_node.next = new_node # set new node as target's `next`
        new_node.prev = target_node # set target as now node's `prev`
        if new_node.next is not None: # if a node exists after target
            new_node.next.prev = new_node # set new node as that node's `prev`
        
    def append(self, new_data):
        new_node = DNode(new_data)
        new_node.next = None # set new node as last node, set `next` as None
        if self.head is None: # if list is empty
            new_node.prev = None
            self.head = new_node # set new node as `head`
            return
        # traverse list
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node # set new node as last's `next`
        new_node.prev = last # set last as `prev` of new node
        return

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next
            
    def print_from_node(self, node):
        print('\nTraversal in forward direction:')
        while node is not None:
            print('%d'%(node.data))
            last = node
            node = node.next
            
        print('\nTraversal in reverse direction:')
        while node is not None:
            print('%d'%(last.data))
            last = last.prev
        
class DNode:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
if __name__ == "__main__":
    main()