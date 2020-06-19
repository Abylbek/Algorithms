array = [-1,2,4,-3,5,2,-5,2]
total = 0
best = 0
for i in range(len(array)):
	total = max(array[i] , total + array[i])
	best = max(best , total)
print(best)
