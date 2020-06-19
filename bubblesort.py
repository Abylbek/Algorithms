array = [1,5,3,7,3,6,10]
for i in range(len(array)):
	for j in range(len(array) -1):
		if array[j] > array[j+1]:
			array[j] , array[j+1] = array[j+1] , array[j]
print(array)