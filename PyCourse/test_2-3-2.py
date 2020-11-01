a = int( input() )
b = int( input() )

if ( a % 3 ) == 0:
	pass
elif ( a % 3 ) == 1:
	a += 2
elif ( a % 3 ) == 2:
	a += 1

numbers = range( a, b + 1, 3 )

sum = 0
for num in numbers:
	sum += num
	
ans = sum / len(numbers)

print(ans)