class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    # umiesci nowy wezel na poczatku listy
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = self.head

    # umiesci nowy wezel na koncu listy
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
        if self.tail is None:
            self.tail = self.head

    # zwroci wezel znajdujacy sie na wskazanej pozycji
    def node(self, index):
        cur_node = self.head
        node_position = 0
        while cur_node.next is not None:
            if node_position == index - 1:
                return cur_node.value
            node_position += 1
            cur_node = cur_node.next
            if node_position == index - 1:
                return cur_node.value

    # wstawi nowy wezel za wezlem wskazanym w parametrze
    def insert(self, value, after):
        if after == 0:
            self.push(value)
            return
        node_position = 0
        cur_node = self.head
        while cur_node is not None:
            if node_position == after - 1:
                node = Node(value, cur_node.next)
                cur_node.next = node
                break
            cur_node = cur_node.next
            node_position += 1

    # usunie pierwszy element listy i go zwroci
    def pop(self):
        self.head = self.head.next
        return self.head

    # usunie ostatni element z listy i go zwroci
    def remove_last(self):
        element = self.head
        while element.next.next:
            element = element.next
        element.next = None
        self.tail = element
        return self.tail

    # usunie z listy nastepnik wezla przekazanego w parametrze
    def remove(self, after):
        if after == 0:
            self.head = self.head.next
            return

        node_position = 0
        cur_node = self.head
        while cur_node is not None:
            if node_position == after - 1:
                cur_node.next = cur_node.next.next
                break
            cur_node = cur_node.next
            node_position += 1

    def __str__(self):
        element = self.head
        list_elements = ""
        while element is not None:
            list_elements += str(element.value) + ' -> '
            element = element.next
        list_elements += "None"
        return list_elements

    def __len__(self):
        length = 0
        element = self.head
        while element is not None:
            length += 1
            element = element.next
        return length




class Stack:
    def __init__(self):
        self._storage = LinkedList()

    def push(self, value):
        self._storage.append(value)

    def pop(self):
        return self._storage.remove_last().value

    def __str__(self):
        element = self._storage.head
        stack_elements = ''
        while element.next:
            stack_elements += str(element.value) + '\n'
            element = element.next
        stack_elements += str(element.value)
        return stack_elements

    def __len__(self):
        return len(self._storage)



class Queue:
    def __init__(self):
        self._storage = LinkedList()

    def peek(self):
        return self._storage.tail.value

    def enqueue(self, value):
        self._storage.append(value)

    def dequeue(self):
        return self._storage.remove_last().value

    def __str__(self):
        element = self._storage.head
        queue_elements = ''
        while element.next is not None:
            queue_elements += str(element.value) + ', '
            element = element.next
        queue_elements += str(element.value)
        return queue_elements

    def __len__(self):
        return len(self._storage)


list_ = LinkedList()

list_.push(1)
list_.push(2)
print(list_.__str__())

list_.append(3)
print(list_.__str__())

list_.pop()
print(list_.__str__())

list_.insert(4, 1)
print(list_.__str__())

print(list_.node(1))

list_.remove(0)
print(list_.__str__())

list_.remove_last()
print(list_.__str__())

print(list_.__len__())


# stack = Stack()
# stack.push(4)
# stack.push(5)
# stack.push(6)
# print(stack.__str__())
# print('----')
# print(stack.__len__())
# stack.pop()
# print('----')
# print(stack.__str__())


# queue = Queue()
# queue.enqueue(5)
# queue.enqueue(6)
# queue.enqueue(7)
# queue.enqueue(9)
# print(queue.__str__())
# print(queue.peek())
# queue.dequeue()
# print(queue.__str__())
# print(queue.__len__())
