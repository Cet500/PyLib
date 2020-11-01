y1 = int( input() )
y2 = int( input() )
x1 = int( input() )
x2 = int( input() )

y = range( y1, y2 + 1 )
x = range( x1, x2 + 1 )

print(end= '\t')
for ix in x:
	print(ix, end = '\t')

print()

for iy in y:
	print(iy, end = '\t')

	for ix in x:
		print(ix * iy, end = '\t')
		
	print()