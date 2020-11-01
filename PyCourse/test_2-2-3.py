numbers = []

while True:
	num = int(input())
	
	if num < 10:
		continue
	elif num > 100:
		break
	else:
		numbers.append(num)

for i in numbers:
	print(i)