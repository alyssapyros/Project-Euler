# dictionary with the known counters
# while loop that doesnt equal 1
# counter for the numbers and add that to the dictionary ones you already have. once you have that number add it to the dictionary



# loop through all numbers
import operator
dictionary={1:1}
starting_n=1
while starting_n <1000000:
	starting_n+=1
	counter=0
	n=starting_n
	new_list=[starting_n]
	if n%10000==0:
		print n
	while n !=1 and n not in dictionary:

		if n%2==0:
			n=n/2
			counter+=1
			new_list.append(n)
		else:
			n=(3*n)+1
			counter+=1
			new_list.append(n)

	if n==1:
		counter=counter+0
	else:
		counter=counter+dictionary[n]
	

	# 	dictionary[starting_n]=new_counter

	b=len(new_list)
	a=new_list[-1]

	for n in new_list[:-1]:
		b-=1

		dictionary[n]= dictionary[a] + b

print max(dictionary.iteritems(), key=operator.itemgetter(1))[0]

# standard=10
# for value in dictionary.values():
# 	if value>standard:
# 		standard=value
# print standard


