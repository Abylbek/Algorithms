def fib(n):
	fib = [0 , 1]  + [0]*(n-1)
	for i in range(2 , n + 1):
		fib[i] = fib[i-2] + fib[i-1]
	return fib[n]
print(fib(4))
