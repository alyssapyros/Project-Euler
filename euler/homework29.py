total_list=[]

for i in range (2,101):
	for c in range (2,101):
		b=i**c
		if b not in total_list:
			total_list.append(b)

total_list.sort()
print len(total_list)