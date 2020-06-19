class Node:
	def __init__(self ,data):
		self.data = data;
		self.next = None;
class Stack:
	def __init__(self):
		self.top = None;
		self.size = 0
	def push(self,data):
		new_node = Node(data)
		if self.top is None:
			self.top = new_node
		else:
			new_node.next = self.top
			self.top = new_node 
		self.size += 1;
	def pop(self):
		if self.top:
			result = self.top.data
			if self.top.next:
				self.top = self.top.next
			else:
				self.top = None;
			return result;
		else:
			return None;
	def peek(self):
		if self.top:
			return self.top.data;
		else:
			return None;

	def iter(self):
		if self.top:
			current = self.top;
			while current:
				value = current.data;
				current = current.next;
				yield value
		else:
			return None;

def check_brackets(sentence):
	mysentenses = Stack()
	openbarckets = ["{" , "[" , "("]
	closebrackets  = ["}" , "]" , ")"]
	for char in sentence:
		if char in openbarckets:
			mysentenses.push(char)
		if char in closebrackets:
			last = mysentenses.pop()
			if last is "{" and char is "}":
				continue
			elif last is "[" and char is "]":
				continue
			elif last is "(" and char is ")":
				continue
			else:
				return False;
	if mysentenses.size>0:
		return False
	else:
		return True



sentences = {
	"{[()]}",
	"{}{",
	"{(ass)}",
}

for s in sentences:
	m = check_brackets(s)
	print("{}-----:-----{}".format(s , m))