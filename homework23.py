
# highest_abundant = 28123



# def all_divisors(number):
# 	divisor=1
# 	list_of_divisors=[]
# 	while divisor<number:
# 		if number%divisor==0:
# 			list_of_divisors.append(divisor)
# 			divisor+=1
# 		else:
# 			divisor+=1 
# 	return list_of_divisors



# abundant = number if sum(divisors) > number

# def find_abundant (number):
# 	sum_divisors=sum(all_divisors(number))
# 	if sum_divisors > number:
# 		return 'abundant'


# list_of_abundants=[12]
# not_sum_abundants=[]
# i=0





# for number in range (0,highest_abundant):
# 	if find_abundant(number) == 'abundant':
		

# list_of_abundants=[]

# def find_abundant (number):
	
# 	if sum(divisors) > number:
# 		return 'True'

# highest_abundant = 28123

# for number in range (1,highest_abundant):
# 	divisors=[i for i in range (1,number) if number%i==0]

# 	if sum(divisors)>number:
# 		list_of_abundants.append(number)



# total_sums={i+g for i in list_of_abundants for g in list_of_abundants}

# positive_ints=[i for i in range(0,highest_abundant)]

# uniques=set(positive_ints).difference(total_sums)

# print sum(uniques)
		




def find_abundant (number):
	divisors=[]
	for i in range (1,number):
		if number%i==0:
			divisors.append(i)
	if sum(divisors) > number:
		return True

highest_abundant = 28123

list_of_abundants=[n for n in range(1,highest_abundant) if find_abundant(n)==True]

total_sums={i+g for i in list_of_abundants for g in list_of_abundants}

positive_ints=[i for i in range(0,highest_abundant)]

uniques=set(positive_ints).difference(total_sums)

print sum(uniques)

