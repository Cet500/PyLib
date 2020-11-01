str = str( input() )

str = str.upper()

x = str.count('C')
x += str.count('G')

ans = ( x / len(str) ) * 100

print(ans)