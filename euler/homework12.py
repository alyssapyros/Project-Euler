


def get_divisors (number):
	i=1
	divisors=[]
	while i<=number:
		if number%i==0 and i!=number:
			divisors.append(i)
			i+=1
		if number%i!=0:
			i+=1
		if i==number:
			divisors.append(i)
			i+=1
			return divisors

def triangle (number):
	return sum(range(1,number+1))

def prod(numbers):
	p=1
	for n in numbers:
		p*=n
	return p




# exponent to get divisors


def exponent_to_divisors (n):
	divisor=2
	d=dict()
	while divisor<n:
		if n%divisor==0:
			n=n/divisor
			if divisor not in d:
				d[divisor]=1
			else:
				d[divisor]+=1
		if n%divisor!=0:
			divisor+=1
	if divisor==n:
		if divisor not in d:
			d[divisor]=1
		else:
			d[divisor]+=1
	new_list=[]
	for i in d.values():
		c= i+1
		new_list.append(c)
	return prod(new_list)

# print get_divisors(36)
# print exponent_to_divisors(n)



counter=1
number=1
num_divisor=1
while num_divisor < 500:
	counter+= 1
	number=triangle(counter)
	num_divisor=exponent_to_divisors(number)
	print number,num_divisor


