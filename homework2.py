fib=[1,2]

# loop until the last value of the list is larger than 4000000
while fib[-1]<4000000:
	# calculate next_fib by adding the last two valuse of the list together
	next_fib=fib[-1]+fib[-2]
	# add next_fib into my list
	fib.append(next_fib)
print fib


fib_sum=0
# iterate through all values in my fib list
for i in fib:
	# check if they are divisble by 2
	if i%2==0:
		# add the even ones together
		fib_sum+=i
		print i, fib_sum
