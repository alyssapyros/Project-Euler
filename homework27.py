

# def is_prime (number):
# 	i=2
# 	while i<=number:
# 		if number%i==0 and i!=number:
# 			return 'False' 
# 		if number%i!=0:
# 			i+=1
# 		if i==number:
# 			return 'True'


# def finding_primes (a,b):
# 	full_list=range(a,b)
# 	primes=[]
	
# 	while len(full_list)>0:
# 		new_prime=full_list[0]
# 		primes.append(new_prime)
# 		multiple=1
# 		while new_prime*multiple<b:
# 			# print full_list, (new_prime*multiple)
# 			try: 
# 				full_list.remove(new_prime*multiple)
# 			except:
# 				pass

# 			multiple+=1
# 	return primes


	# multiples_list=[]

	# n=2
	# starting_point=0

	# #start loop here and then add one to starting point and add multiples to list

	# first_number=full_list[starting_point]





	# #NEED STARTING POINT TO BE INCREASED BY 1

	# if is_prime(first_number)=='True':
	# 	while n*first_number <= full_list[-1]:
	# 		multiples_list.append((n*first_number))
	# 		n+=1
	# multiples_set=set(multiples_list)

	# new_set=sorted(full_set.difference(multiples_set))
	# return new_set

# print finding_primes(2,30)


def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = list(range(np1)) # leave off `list()` in Python 2
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1): # use `xrange()` in Python 2
        if s[i]:
            # next line:  use `xrange()` in Python 2
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)


n=0
standard=0

c=sieve(100000)
c=set(c)


for a in range (-999,1000):
	# print a
	for b in range (-999,1000):
		n=0
		formula_answer = (n**2) + (a*n) + b
		while formula_answer in c:
			n+=1
			formula_answer = (n**2) + (a*n) + b
		if n > standard:
			standard=n
			print '###############', n, a, b

print a,b, standard
		

# standard=0

# for a in range (-10,10):
# 	for b in range (-10,10):
# 		formula_answer = (n**2) + (a*n) + b
# 		if is_prime(formula_answer) == 'True':
# 			n+=1
# 			print 'True', n, standard, a, b
# 			if n > standard:
# 				standard=n
				
# 		else:
# 			n=0
# 			print n, standard, a, b


#a, b is the range you want to find primes in



# def finding_primes (a,b):
# 	full_list=[]
# 	prime_list=[]
# 	n=0
# 	while n != b:
# 		for i in range (a,b):
# 			full_list.append(i)
# 		if is_prime(full_list[n])=='True':
# 			prime_list.append(full_list[n])
# 		print full_list
# 		for i in range(n,full_list[-1]):
# 			print i , 'list'
# 			c=(full_list[n])*i
# 			print c , 'eliminate'
# 			full_list.pop(c)
# 		print full_list
# 		n+=1
	# print prime_list


# def finding_primes (a,b):
# 	full_list=[]
# 	multiples_list=[]

# 	n=2
# 	starting_point=0

# 	for i in range (a,b):
# 		full_list.append(i)
# 	full_set=set(full_list)

# 	#start loop here and then add one to starting point and add multiples to list

# 	first_number=full_list[starting_point]


# 	#NEED STARTING POINT TO BE INCREASED BY 1

# 	if is_prime(first_number)=='True':
# 		while n*first_number <= full_list[-1]:
# 			multiples_list.append((n*first_number))
# 			n+=1
# 	multiples_set=set(multiples_list)

# 	new_set=sorted(full_set.difference(multiples_set))
# 	return new_set


	# for i in range (a,b):


	# print first_number

	# print full_list




# print finding_primes(2,10)





