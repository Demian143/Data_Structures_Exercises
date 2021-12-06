
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Linked list is empty')

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_len(self):
        length = 0
        itr = self.head

        while itr:
            itr = itr.next
            length += 1
        return length

    def remove_at(self, index):
        if index < 0 or index > self.get_len():
            raise Exception('Invalid index')

        if index == 0:
            self.head = self.head.next
            return

        lenght = 0
        itr = self.head
        while itr:
            if lenght == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            lenght += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_len():
            raise Exception('Index out of bounds')

        if index == 0:
            self.insert_at_begining(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        # Now insert data_to_insert after data_after node
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return

        itr = self.head

        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)

            itr = itr.next

    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next

        itr = self.head

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break

            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("grapes", "apple")
    ll.print()  # insert apple after mango

    for item in ["orange", "banana", "mango", "grapes"]:
        ll.remove_by_value(item)
        ll.print()
