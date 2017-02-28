
# recursive

# def fib(n):
#     if n == 0: 
#     	return 0
#     elif n == 1: 
#     	return 1
#     else: 
#     	return fib(n-1)+fib(n-2)


# n=12
# while len(str(fib(n)))<1000:
# 	n+=1
# print n

#list


# fibs=[1,1]
# fib_number=5

# while len(str(fibs[-1]))<1000:
# 	c=fibs[-1]+fibs[-2]
# 	fibs.append(c)

# print len(fibs)



#variables
counter=2
a=1
b=1

while len(str(b)) < 1000:
	c=a+b
	a=b
	b=c
	counter+=1

print counter
