limit = int( input() )
i = 0
num = 1
count = 0

while i < limit:
	if count < num:
		print( num, end = " " )
		count += 1
		i += 1
	else:
		num += 1
		count = 0