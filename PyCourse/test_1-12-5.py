a = int(input())
b = int(input())
c = int(input())

mas = [a, b, c]

max = max(mas)
min = min(mas)

avg = ( sum(mas) - ( min + max ) )

print(max)
print(min)
print(avg)