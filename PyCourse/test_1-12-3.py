a = float(input())
b = float(input())
action = input()

if action == '+':
	print( a + b )
	
if action == '-':
	print( a - b )
	
if action == '/':
	if b == 0:
		print('Деление на 0!')
	else:
		print( a / b )

if action == '*':
	print( a * b )
	
if action == 'mod':
	if b == 0:
		print('Деление на 0!')
	else:
		a = int(a)
		b = int(b)
		print( a % b )
	
if action == 'pow':
	print( a ** b )
	
if action == 'div':
	if b == 0:
		print('Деление на 0!')
	else:
		print( a // b )