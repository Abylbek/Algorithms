def quiksort(arr):
	if len(arr) > 2:
		greater = []
		less = []
		opora = arr[0]
		greater = [i for i in arr[1:] if opora < i]
		less = [i for i in arr[1:] if opora > i]
		return quiksort(less) +[opora]+ quiksort(greater)
	else:
		return arr

print(quiksort([10,4,2,3,8, 9,1]))
