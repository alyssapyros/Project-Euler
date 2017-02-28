#set to number
number=90
#loop through numbers 1-10
passed_all_tests=False
while passed_all_tests==False:
	passed_all_tests=True
	number+=1
	for divisor in range (1,21):
	#check if i is divisible by number
		#if number is divisible by divisor, increase divisor by 1
		if number%divisor!=0:
			passed_all_tests=False
			break
		#if number is not divisible by 1, increase number by 1
print number





# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


