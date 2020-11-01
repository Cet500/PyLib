sum = 0
ans = 0

while True:
	num = int( input() )
	
	ans += num * num
	sum += num

	if sum == 0:
		break

print(ans)