limit = int( input() )
data = []
ans = []

for y in range( limit ):
	data.append( [] )
	ans.append( [] )
	
	for x in range( limit ):
		data[ y ].append( [] )
		data[ y ][ x ] = 0
		ans[ y ].append( [] )
		ans[ y ][ x ] = 0

print( "data =", data )
print( "ans  =", ans )

i = 0

for y in range( limit ):
	for x in range( limit ):
		i += 1
		data[ y ][ x ] = i
		
print( "data =", data )

i = 0
t = 0
n = limit
y = 0
x = 0
yd = 0
xd = 0

while i < limit ** 2:
	if n % 4 == 1:
		xd = 1
		
	if n % 4 == 2:
		yd = 1
	
	if n % 4 == 3:
		xd = -1
	
	if n % 4 == 0:
		yd = -1
	
	while t <= ( n // 1 ):
		print( "y", y + ((limit - int( n // 1 )) * yd), "| x", x + ((limit - int( n // 1 )) * xd) )
		ans[ y + ( ( limit - int( n // 1 ) ) * yd ) ][ x + ( ( limit - int( n // 1 ) ) * xd ) ] = i
		print( "i", i, "| t", t, "| n", n )
		print( "ans =", ans )
		x += xd
		y += yd
		t += 1
		i += 1
		print()
	
	t = 0
	yd = 0
	xd = 0
	n -= 0.5