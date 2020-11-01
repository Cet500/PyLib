data = [] # данные
ans  = []
list = []

while True:
	list = input()
	
	if list == "end":
		break
	else:
		list = [ int( i ) for i in list.split() ]
		data.append(list)

x = 0
y = 0

for	y in range( len( data ) ):
	ans.append([])
	
	for x in range( len( data[ 0 ] ) ):
		ans[ y ].append( 0 )
		
		ans[ y ][ x ] += data[ y ][ x - 1 ]
		ans[ y ][ x ] += data[ y - 1 ][ x ]
		
		if y == ( len( data ) - 1 ):
			ans[ y ][ x ] += data[ 0 ][ x ]
		else:
			ans[ y ][ x ] += data[ y + 1 ][ x ]
		
		if x == ( len( data[ 0 ] ) - 1 ):
			ans[ y ][ x ] += data[ y ][ 0 ]
		else:
			ans[ y ][ x ] += data[ y ][ x + 1 ]
		
		print( ans[ y ][ x ], end = " " )
	
	print()