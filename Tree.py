class Node:
	def __init__(self , data = None):
		self.data = data;
		self.right_child = None;
		self.left_child = None;
	def inorder(self , root_node):
		current = root_node;
		if current is None:
			return
		self.inorder(current.left_child)
		print(current.data)
		self.inorder(current.right_child)
	def preorder(self , root_node):
		current = root_node;
		if current is None:
			return
		print(current.data)
		self.preorder(current.left_child)
		self.preorder(current.right_child)
	def postorder(self , root_node):
		current = root_node;
		if current is None:
			return
		self.postorder(current.left_child)
		self.postorder(current.right_child)
		print(current.data)
	def find_min(root_node):
		current = root_node;
		while current.left_child:
			current = current.left_child
		return current.data;
	def fing_max(root_node):
		current = root_node;
		while current.right_child:
			current = current.right_child;
		return current.data;

	def insert(self , data):
		node = Node(data);
		if self.root_node is None:
			self.root_node =node;
		else:
			current = self.root_node;
			parent = None;
			while True:
				parent = current;
				if node.data < current.data:
					current = current.left_child;
				
n1 = Node(6)
n2 = Node(4)
n3 = Node(3)
n4 = Node(5)
n5 = Node(7)

n1.left_child = n2
n1.right_child = n5
n2.left_child = n3
n2.right_child = n4


print("Max value is :  "  + str(n1.fing_max()))
print("Min value is :  "  + str(n1.find_min()))