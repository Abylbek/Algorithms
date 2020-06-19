class Node:
	def __init__(self , value):
		self.value = value;
		self.next = None;
class CircularList:
	def __init__(self):
		self.first = None;
		self.last = None;
		self.size = 0;
	def append(self , value):
		new_node = Node(value)
		if self.first:
			self.last.next = new_node;
			self.last = new_node
		else:
			self.first = new_node
			self.last = new_node

		self.last.next = self.first;
		self.size += 1
	def delate(self , value):
		current = self.first
		prev = self.first
		while prev == current or prev != self.last:
			if current.value == value:
				if current == self.first:
					self.first = current.next
					self.last.next = self.first
				else:
					prev.next = current.next 
					self.size -= 1	
		return
		prev = current
		current = current.next
	def iter(self):
		current = self.first
		while current:
			value = current.value
			current = current.next
			yield value

names = CircularList()
names.append("Abyl")
names.append("Sanzhik")
names.append("Eldo")
names.append("Aman")
names.append("AItu")
names.append("Nurik")
count = 0
for i in names.iter():
	count +=1
	print(i)
	if count >= 6:
		break