# вариант 1

numbers = [ int( i ) for i in input().split() ]
numbers.sort()

template = numbers[0]
temp = 0

arrCount = []
arrInt = []

for i in range( len(numbers) ):
	if numbers[i] == template:
		temp += 1
	else:
		arrCount.append(temp)
		arrInt.append(template)
		temp = 1
		template = numbers[ i ]

arrCount.append(temp)
arrInt.append(template)

for i in range( len(arrCount) ):
	if arrCount[i] > 1:
		print(arrInt[i], end = " ")
		
# вариант 2

numbers = [ int( i ) for i in input().split() ]
numbers.sort()

ans = []

for i in range( min( numbers ) - 1, max( numbers ) + 1 ):
	if numbers.count(i) > 1:
		ans.append(i)

print(*ans)
