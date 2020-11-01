min = int(input())
max = int(input())
time = int(input())

if (time > max):
	print('Пересып')

if (time < min):
	print('Недосып')

if (min <= time <= max):
	print('Это нормально')