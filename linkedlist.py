#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(1) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each

        #return len(self.items())  #This function is 0(n) because it calls the items() function.
        return self.size

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) It does the same thing no matter what, no for/while loops and if statements are 0(1)"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        node = Node(item)
        if self.tail is not None:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) It does the same thing no matter what, no for/while loops and if statements are 0(1)"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        node = Node(item)
        if not self.is_empty():
            node.next = self.head
        else:
           self.tail = node
        self.head = node
        self.size += 1

    def find(self, quality, case=1):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(n) I think because its just 1 while loop no matter what its 0(n)
        TODO: Worst case running time: O(n) I think because its just 1 while loop no matter what its 0(n)"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        node = self.head
        while node is not None:
            if quality(node.data):
                if case == 1:
                    return node.data
                elif case == 2:
                    return node
            else:
                node = node.next
        return None
            
    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) If it deletes at head or has no head.
        TODO: Worst case running time: O(n) Worst case the item is not in head the linked list is greater than 1 and it is the last item."""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        #Checks if head exists and if not it raises value error
        if self.head is None:
            raise ValueError(f'Item not found: {item}')
        # If linkedlist is size of 1
        if self.head == self.tail:  #Checks if linked list is only 1 big
            if self.head.data == item: #Checks if head data matches the item
                self.head = None
                self.tail = None 
                self.size -= 1
                return
            else:
                raise ValueError(f'Item not found: {item}')
        # If linked list item is in the head and size is not 1
        if self.head.data == item: #Checks if head data matches the item
            self.head = self.head.next # Changes the head to next node
            self.size -= 1
            return
        # If linked list item is not in head
        curr_node = self.head.next  #Defines current node in relation to head
        prev_node = self.head   #Defines previous node in relation to head

        while curr_node is not None: #While current Node exists so while current node is still itterating through the linked list
            if curr_node.data == item: #If its a match
                if curr_node == self.tail: #If item is at tail
                    self.tail = prev_node #makes the previous the new tail
                    prev_node.next = None #Sets the node before the tail to point to None because its new tail
                else:
                    prev_node.next = curr_node.next #Says the previous node points to what the current node points to because current node is deleted.
                self.size -= 1 #Deletes one from size to correctly remember length
                return #Exits loop it found and deleted the item
            #Iterates to next node
            prev_node = curr_node
            curr_node = curr_node.next
        #If these statements still have not found item, its not in linked list so we raise value error
        raise ValueError(f"Item not found: {item}")

    def replace(self, data, replacewith):
        """ This replaces target data with new data (replacewith).
            Best case running time: O(1) If its empty it raises value error
            Worse case running time: 0(n) It runs the find method.
        """
        if self.head is None:
            raise ValueError('Linked list is empty')
        #Runs find on data and case2 then because it returns a Node it calls .data on it and it is set equal to replacewith
        self.find(lambda item: item == data, case=2).data = replacewith



def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    ll.replace(ll.head.data, 'Beck')
    print('head replaced: {}'.format(ll.head))

    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
    #ll = LinkedList()
    #ll.length()
