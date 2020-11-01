numbers = [ int( i ) for i in input().split() ]

if len(numbers) == 1:
	print(numbers[0])
else:
	ans = [ ]
	
	for i in range( len( numbers ) ):
		if i == len( numbers ) - 1:
			ans.append( numbers[ -2 ] + numbers[ 0 ] )
		else:
			ans.append( numbers[ i + 1 ] + numbers[ i - 1 ] )
	
	print(*ans)