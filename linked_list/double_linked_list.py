
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_len(self):
        if self.head is None:
            raise Exception('List is empty')

        length = 0
        itr = self.head
        while itr:
            itr = itr.next
            length += 1
        return length

    def remove_at(self, index):
        if index < 0 or index >= self.get_len():
            raise Exception('Index out of bounds')

        elif self.head is None:
            raise Exception('List is empty')

        elif self.head.next is None and self.head.prev is None:
            self.head = None
            return

        itr = self.head
        length = 0
        while itr:
            if itr.next is None:
                itr.prev.next = None
                itr.prev = None
                break

            elif index == 0:
                self.head.next.prev = None
                self.head = self.head.next
                break

            elif length == index:
                itr.next.prev = itr.prev
                itr.prev.next = itr.next
                break

            itr = itr.next
            length += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_len():
            raise Exception('Index out of bounds')

        elif index == 0:
            self.insert_at_begining(data)
            return

        itr = self.head
        count = 0

        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next, itr)
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        if self.head is None:
            raise Exception('List is empty')

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next, self.head)
            return

        itr = self.head
        while itr:
            if itr.next is None:
                itr.next = Node(data_to_insert, itr.next, itr)
                break

            elif itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                itr.next.prev = node
                itr.next = node
                break

            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            raise Exception('Empty list')

        if self.head.data == data:
            self.head = self.head.next
            self.head.prev = None
            return

        itr = self.head
        while itr:
            if itr.next is None:
                itr.prev.next = None
                break

            elif itr.data == data:
                itr.next.prev = itr.prev
                itr.prev.next = itr.next
                break

            itr = itr.next

    def print_forward(self):
        # This method prints list in forward direction. Use node.next
        if self.head is None:
            raise Exception('List seems to be empty')

        itr = self.head
        string = ''
        while itr:
            string += str(itr.data) + '-->'
            itr = itr.next

        print(string)

    def print_backward(self):
        # Print linked list in reverse direction. Use node.prev for this.
        pass


if __name__ == '__main__':
    ll = DoubleLinkedList()
    # breakpoint()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    ll.insert_at_end('strawberry')
    ll.print_forward()
    print(ll.get_len())
    # breakpoint()

    ll.insert_after_value('strawberry', 'new')
    ll.remove_by_value('new')
    ll.print_forward()
