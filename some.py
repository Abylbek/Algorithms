n = int(input())
for i in range(n):
	total = 0
	numbers = map(int , input().split())
	for i in numbers:
		total += i
	if total == 0:
		print("YES")
	else:
		print("NO")