
divisor=2
n=600851475143
while divisor<n:
	if n%divisor==0:
		n=n/divisor
		print divisor
	if n%divisor!=0:
		divisor+=1
print divisor




#1
#n=210
#for divisor in range(2,n): 
#	if n%divisor==0:
#		n=n/divisor
#		print divisor
	
#while loops
#change the way you track the divisor from remembering 
#position to just using a single variable