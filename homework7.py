def is_prime (number):
	i=2
	while i<=number:
		if number%i==0 and i!=number:
			return 'False' 
		if number%i!=0:
			i+=1
		if i==number:
			return 'True'

number=1
count=0
while count<10001:
	number+=1
	if is_prime(number)=='True':
		count+=1
print number

# add counter and when counter gets to 1000 then print
# check counter to see if it started at 0 or if it's greater than or equal to; do you count 1 or 0
