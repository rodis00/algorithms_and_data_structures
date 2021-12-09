from collections import deque


class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self):
        if self.right_child is None and self.left_child is None:
            return True
        return False

    def add_left_child(self, value):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value):
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit):
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
            visit(self)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit):
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit):
        visit(self)
        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)

    def show(self, level):
        if self.left_child is not None:
            self.left_child.show(level + 1)
        if level == 0:
            print(self.value, '--')
        else:
            print(' ' * 5 * level + '|-->', self.value)
        if self.right_child is not None:
            self.right_child.show(level + 1)


class BinaryTree:
    def __init__(self, root):
        self.root = BinaryNode(root)

    def traverse_in_order(self, visit):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit):
        self.root.traverse_pre_order(visit)

    def show(self):
        self.root.show(0)


def horizontal_sum(tree):
    queue = deque()
    queue.append(tree.root)
    l_elem = len(queue)

    li = []
    while l_elem > 0:
        count = 0
        while l_elem > 0:
            element = queue.popleft()
            count += element.value

            if element.left_child is not None:
                queue.append(element.left_child)

            if element.right_child is not None:
                queue.append(element.right_child)

            l_elem -= 1

        li.append(count)
        l_elem = len(queue)

    return li


tree = BinaryTree(1)
tree.root.add_left_child(2)
tree.root.add_right_child(5)

tree.root.left_child.add_left_child(3)
tree.root.left_child.add_right_child(4)

tree.root.right_child.add_left_child(6)
tree.root.right_child.add_right_child(7)

tree.show()
print()

print(horizontal_sum(tree))



