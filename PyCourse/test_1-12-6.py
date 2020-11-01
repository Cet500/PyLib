# вариант 1 ( свёрнутый )

num = int(input())

end10 = num % 10
end100 = num % 100

if ( ( end10 == 1 ) and not ( ( end100 == 11 ) ) ) :
	end = ''
elif ( ( end10 == 2 ) or ( end10 == 3 ) or ( end10 == 4 ) ) and not ( ( end100 == 12 ) or ( end100 == 13 ) or ( end100 == 14 ) ):
	end = 'а'
else:
	end = 'ов'

ans = str(num) + ' программист' + end

print(ans)

# вариант 2 ( развёрнутый )

num = int(input())

end10 = num % 10
end100 = num % 100

if ((num % 5) == 0) or (end10 == 6) or (end10 == 7) or (end10 == 8) or (end10 == 9):
	end = 'ов'

if ((end10 == 1) and not ((end100 == 11))):
	end = ''

if (end100 == 11):
	end = 'ов'

if ((end10 == 2) or (end10 == 3) or (end10 == 4)) and not ((end100 == 12) or (end100 == 13) or (end100 == 14)):
	end = 'а'

if ((end100 == 12) or (end100 == 13) or (end100 == 14)):
	end = 'ов'

ans = str(num) + ' программист' + end

print(ans)