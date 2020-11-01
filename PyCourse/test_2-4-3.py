str = str( input() )

template = str[0]
temp = 0

arrInt = []
arrLet = []

for i in range( len(str) ):
	if str[i] == template:
		temp += 1
	else:
		arrInt.append(temp)
		arrLet.append(template)
		temp = 1
		template = str[ i ]

arrInt.append(temp)
arrLet.append(template)

for i in range( len(arrLet) ):
	print( arrLet[ i ], end = '' )
	print( arrInt[ i ], end = '' )