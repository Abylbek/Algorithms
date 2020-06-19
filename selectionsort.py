def findsmalles(arr):
	smallest = arr[0]
	smallest_index = 0;
	for i in range(1 , len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index;

def selectionsort(arr):
	new_arr = []
	for i in range(len(arr)):
		smallest = findsmalles(arr)
		new_arr.append(arr.pop(smallest))
	return new_arr


print(selectionsort([3,1,2,5,12,9,2]))