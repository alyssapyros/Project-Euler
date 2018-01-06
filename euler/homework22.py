import string 


f=open('names.txt','r')


alphabet={}

all_letters=string.ascii_uppercase
for i,c in zip(all_letters,range (1,27)):
	alphabet[i]=c


sum_letters=[]
list_of_sums=[]
for names in f:
	names=names.split(',')
	names.sort()
	# print len(names)
	for letter in range(0,len(names)):
		one_name=names[letter]
		for letter in one_name:			
			if letter =='"':
				if len(sum_letters)>0:
					x=sum(sum_letters)
					list_of_sums.append(x)
				sum_letters=[]
			else:
				sum_letters.append(alphabet[letter])


grand_total=[]
for count, sums in zip(range(1,5164),list_of_sums):
	new_value=count*sums
	grand_total.append(new_value)


print sum(grand_total)