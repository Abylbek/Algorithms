def mincostroad(n , price : list):
	c = [0]*n
	c[1] = 1
	c[2] = 2
	for i in range(3 , n+1):
		c[i] = price[i] + min(c[i-1],c[i-2])
	return c[n]

print(mincostroad(5 , [3,2,3]))