#983

from __future__ import division
from decimal import *

repeating_decimals_list=[]

#takes number and returns 1/number; ie i=2, returns 0.5
def denominator_decimal (i):
	i=i*1.0
	n=1/i
	variable_length=3000
	# n= "%.100f" % n
	getcontext().prec=variable_length
	n=Decimal(1)/Decimal(i)
	n=str(n)
	if len(n) > variable_length:
		n=n[0:-1]
	return n[2::]


#takes decimal base and returns length of repeat
def get_repeat_length(decimal):
	decimal=str(decimal)
	doubled=decimal*2
	doubled=str(doubled)
	doubled=doubled[1:-1]
	length=doubled.find(decimal)
	return length

standard=0
for x in range (2,1001):
	c=x
	x=denominator_decimal(x)
	while len(x)>0:
		repeat_length=get_repeat_length(x)
		if repeat_length==-1:
			x=x[1:]
		elif repeat_length>standard:
			standard=repeat_length
			print standard, x, c
		else:
			break

# find the base value with the longest length 




# #i is a decimal; returns len of repeat
# def repeating_decimals(i):
# 	#count irrelevant 
# 	count=0

# 	starting_point=2
# 	i=str(i)
# 	#split into its own function
# 	number=i[starting_point::]
# 	# print number
# 	repeat_number=number*2
# 	repeat_number=str(repeat_number)
# 	repeat_number=repeat_number[1:-1]
# 	length=repeat_number.find(number)
# 	final_length=length




# #to check that it doesn't repeat later on by removing one number 
# 	while length == -1 and starting_point!=len(repeat_number):
# 		starting_point+=1
# 		#count irrelevant 
# 		count+=1

# 		number=i[starting_point:]
# 		repeat_number=number*2
# 		repeat_number=str(repeat_number)
# 		repeat_number=repeat_number[1:-1]
# 		length=repeat_number.find(number)
# 		final_start_point=count+length
# 	# if length > -1: 
# 	# 	print i[starting_point:(starting_point+length)], i

# 	return length


# # print repeating_decimals(0.12345671234567)

# for i in range (2,1001):

# 	if len(denominator_decimal(i)) > 10:
# 		repeating_decimals_list.append(denominator_decimal(i))

# standard=0

# for number in repeating_decimals_list:
# 	#returns the len of the repeat
# 	base_length = repeating_decimals(number)

# 	if base_length > standard:
# 		standard=base_length
# 		# print number, base_length

# # find the base value with the longest length 
# 	for i in range (2,1001):
# 		if denominator_decimal(i)==number:
# 			print i
