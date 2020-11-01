ticket = int(input())

a = ticket // 1000
b = ticket % 1000

s1 = 0
s2 = 0

for i in range(3):
	s1 += a % 10
	a = a // 10
	
for i in range(3):
	s2 += b % 10
	b = b // 10
	
if s1 == s2:
	print('Счастливый')
else:
	print('Обычный')