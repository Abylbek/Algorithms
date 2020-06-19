def quiksort(arr):
	if len(arr) < 2:
		return arr;
	else:
		less = []
		greater = []
		opora = arr[0]
		for i in arr[1:]:
			if i <= opora:
				less.append(i)
			else:
				greater.append(i)
		print(str(less) + "---" + str(opora) + "---" + str(greater))
		print(arr)
		return quiksort(less) + [opora] + quiksort(greater)

print(quiksort([1,5,4,2,3]))