import string 

f=open('names.txt','r')

alphabet={}

all_letters=string.ascii_uppercase
alphabet= {i:c for (i,c) in zip(all_letters,range (1,27))}


sum_letters=[]
list_of_sums=[]

line = f.readline()
names = line.split(',')
names.sort()

# list_of_sums=[ sum([alphabet[letter] for letter in n[1:-1]]) for n in names]
# print list_of_sums


def letters_to_num(s):
	numbers = [alphabet[letter] for letter in s[1:-1]]
	return sum(numbers) 

list_of_sums = [ letters_to_num(n) for n in names ]




# for n in names:
# 	a = []
# 	for letter in n[1:-1]:
# 		a.append(alphabet[letter])
# print names

# names=names.sort()
# print names

# for names in f:
# 	names=names.split(',')
# 	names.sort()
# print names

	# print len(names)

# for name in range(0,len(names)):
# 	one_name=names[name]

# 	for letter in one_name:			
# 		if letter =='"':
# 			if len(sum_letters)>0:
# 				x=sum(sum_letters)
# 				list_of_sums.append(x)
# 			sum_letters=[]
# 		else:
# 			sum_letters.append(alphabet[letter])


new_value=[count*sums for count, sums in zip (range(1,5164), list_of_sums)]
print sum(new_value)

# # for count, sums in zip(range(1,5164),list_of_sums):
# # 	new_value=count*sums
# # 	grand_total.append(new_value)

