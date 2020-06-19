class Node:
    def __init__(self , data = None):
        self.data = data;
        self.right_child = None;
        self.left_child = None;

class Tree:
    def __init__(self):
        self.root_node = None;
    def find_max(self,root_node):
        if root_node is None:
            return False;
        else:
            return self.right_child.find_max()



n1 = Node(6)
n2 = Node(4)
n3 = Node(3)
n4 = Node(5)
n5 = Node(7)

n1.left_child = n2
n1.right_child = n5
n2.left_child = n3
n2.right_child = n4

print(n1.find_max())

