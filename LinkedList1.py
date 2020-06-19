class Node:
	def __init__(self , data):
		self.data = data;
		self.next = None;		
class SinglyLinkedList:
	def __init__(self):
		self.head = None;
		self.size = 0;
	def appenditem(self,data):
		new_node = Node(data);
		if self.head is None:
			self.head = new_node;
		else:
			current = self.head;
			while current.next:
				current = current.next;
			current.next = new_node
		self.size += 1;
	def iter(self):
		current = self.head;
		while current:
			val = current.data
			current = current.next
			yield val
	def searchitem(self , data):
		for val in self.iter():
			if val == data:
				return True;
		return False;
	def clearlist(self):
		self.head = None;


names = SinglyLinkedList()
names.appenditem("Nurik")
names.appenditem("Beka")
names.appenditem("Anelya")
names.appenditem("Nazeka")

for name in names.iter():
	print(name)
print(names.size)
print(names.searchitem("Nurik"))