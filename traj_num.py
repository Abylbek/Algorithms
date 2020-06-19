def traj_num(n , allowed:list):
	k = [0 , 1 , int(allowed[2])] + [0]*(n-3)
	for i in range(3 , n + 1):
		if allowed[i]:
			k[i] = k[i -1] + k[i-2] + k[i -3]
	return k[n]

print(traj_num(7 ,[4]))