array = [-1,2,4,-3,5,2,-5,2]
best = 0
for i in range(len(array)):
	tot =0
	for j in range(i , len(array)):
		tot += array[j]
		best = max(best , tot)
print(best)
