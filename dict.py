from collections import deque
graph = dict()
graph["Abyl"] = ["Aitu" , "Khan"]
graph["Aitu"] = ["aAza" , "Ernar"]
graph["Khan"] = ["Biba" , "Ulusia"]
graph["Aza"] = []
graph["Ernar"] = []
graph["Biba"] = []
graph["Ulusia"] = []
search_queue = deque()
search_queue += graph["Abyl"]
serached = []
while search_queue:
	person = search_queue.popleft();
	if person not in serached:
		if person[0] == "a":
			print(person +  " apple seller")
		else:
			search_queue += graph[person]
			serached.append(person)



