class Node:
	def __init__(self , data = None ):
		self.data = data;
		self.next = None;
		self.prev = None;
class DoublyLinkedList:
	def __init__(self):
		self.first  = None;
		self.last = None;
		self.size = 0;
	def append(self , data):
		new_node = Node(data)
		if self.first is None:
			self.first = new_node;
			self.last = self.first;
		else:
			self.last.next = new_node;
			self.last = new_node;
		self.size  +=  1
	def iter(self):
		current = self.first;
		while current:
			value = current.data;
			current = current.next;
			yield value;
	def deleteNode(self, data):
		current = self.first
		node_deleted = False
		if current is None:
			node_deleted = False
		elif current.data == data:
			self.first = current.next 
			self.first.prev = None 
			node_deleted = True
		elif self.last.data == data: 
			self.last = self.tail.prev
			self.last.next = None;
			node_deleted = True
		else:
			while current: 
				if current.data == data:
					current.prev.next = current.next 
					current.next.prev = current.prev 
					node_deleted = True
				current = current.next
		if node_deleted:
			self.size -= 1
	def search(self , data):
		for value in self.iter():
			if value == data:
				return True
		return False
cars = DoublyLinkedList()
cars.append("Audi A8")
cars.append("Tesla S")
cars.append("Lexus LS")
cars.append("Lexus GS")
#cars.deleteNode("Tesla S")
for car in cars.iter():
	print(car)
print(cars.size)
print(cars.search("Audi A8"))