def find_factorial(n):
    number = 1
    while n >= 1:
        number = number * n
        n = n - 1
    return number

factorial=str(find_factorial(100))

total=[]
for i in factorial:
	total.append(int(i))
print sum(total)