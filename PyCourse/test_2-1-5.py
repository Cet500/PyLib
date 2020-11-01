a = int(input())
b = int(input())
lcm = 0 # least common multiple / наименьшее общее кратное

if a == b:
	lcm = a
else:
	lcm = a * b
	i = lcm
	while i > 0:
		if ( i % a == 0 ) and ( i % b == 0 ):
			lcm = i
		i -= 1
	
print(lcm)