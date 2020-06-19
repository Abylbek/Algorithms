class Node:
	def __init__(self , data = None , next = None, prev = None):
		self.data = data
		self.next = next
		self.prev = prev
class Queue:
	def __init__(self):
		self.first = None;
		self.last = None;
		self.size = 0
	def enqueue(self , data):
		new_node = Node(data)
		if self.first is None:
			self.first = new_node
			self.last = self.first
		else:
			new_node.prev = self.last
			self.last.next = new_node
			self.last = new_node
		self.size += 1;
	def dequeue(self):
		currrent = self.first;
		result = self.first.data
		if self.size == 1:
			self.size -=1
			self.first = None;
			self.last = None;
		else:
			currrent = currrent.next
			currrent.prev = None;
			self.size -= 1;
		return result



names = Queue()
names.enqueue("Nurik")
names.enqueue("Beka")
names.enqueue("Anelya")
print(names.dequeue())