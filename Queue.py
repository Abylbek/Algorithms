class ListQueue:
	def __init__(self):
		self.items = []
		self.size = 0
	def enqueue(self,data):
		self.items.insert(0 , data);
		self.size += 1
	def dequeue(self):
		data = self.items.pop();
		self.size -= 1;
		return data;



myque = ListQueue()
myque.enqueue(1)
myque.enqueue(2)
myque.enqueue(3)
myque.enqueue(4)
myque.dequeue()
print(myque.items)