list = [ int( i ) for i in input().split() ]
x = int( input() )

if list.count( x ) == 0:
	print( "Отсутствует" )
elif list.count( x ) == 1:
	print( list.index( x ) )
else:
	i = 0
	count = 1
	while count <= list.count( x ):
		i = list.index( x, i )
		print( i, end = " " )
		i += 1
		count += 1