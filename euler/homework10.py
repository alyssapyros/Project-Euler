
import numpy


def get_all_primes(x):
	a = range(2,x)
	i = 0

	while i < len(a):
		# grab next prime out of list
		current_prime = a[i]
		
		multiple = 2
		while current_prime * multiple <= a[-1]:
			# find a multiple of your prime
			not_prime = multiple * current_prime
			
			# remove it if it's in the list
			if not_prime in a:
				a.remove(not_prime)
			
			# increase your multiple
			multiple += 1

		# move to the next position
		i += 1

	return a



def is_prime (x):
	y=2
	while x>=y:
		if x%y==0 and x!=y:
			return 'not prime'
		if x%y!=0:
			y+= 1
		if x==y:
			return 'prime'

#print is_prime(x)


def sieve8(n):
    """Return an array of the primes below n."""
    prime = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(3, int(n**.5) + 1, 3):
        if prime[i // 3]:
            p = (i + 1) | 1
            prime[       p*p//3     ::2*p] = False
            prime[p*(p-2*(i&1)+4)//3::2*p] = False
    result = (3 * prime.nonzero()[0] + 1) | 1
    result[0] = 3
    return numpy.r_[2,result]

x=2000000
a= sieve8(x)
print sum(a)