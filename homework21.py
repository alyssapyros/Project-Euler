def all_divisors(number):
	divisor=1
	list_of_divisors=[]
	while divisor<number:
		if number%divisor==0:
			list_of_divisors.append(divisor)
			divisor+=1
		else:
			divisor+=1 
	return list_of_divisors


# number=20
# divisors=[x for x in range(1,number) if number%x==0]

# print divisors

amicable=[]

for i in range(10001):
	a=sum(all_divisors(i))
	if i==sum(all_divisors(a)):
		if a!=i and a not in amicable and i not in amicable:
			amicable.append(a)
			amicable.append(i)
print sum(amicable)
