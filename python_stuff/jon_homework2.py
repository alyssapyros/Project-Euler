# version 1 - count of what's below 500 and what's above

# f=open('jon_homework1.txt','r')

# new_list=[]
# count_below=0
# count_above=0

# for line in f:
# 	if line[0]=='-':
# 		d=sum(new_list)
# 		if d<500:
# 			count_below+=1
# 		else:
# 			count_above+=1
# 		new_list=[]
# 	else:
# 		new_list.append(int(line))
# print count_above, count_below

# version 2 - count many are for each group of 100

# f=open('jon_homework1.txt','r')

# new_list=[]
# dictionary=dict()

# for line in f:
# 	if line[0]=='-':
# 		d=sum(new_list)
# 		c=d/100*100
# 		b=str(c)
# 		if b not in dictionary:
# 			dictionary[b]=1
# 		else:
# 			dictionary[b]+=1
		
# 		new_list=[]
# 	else:
# 		new_list.append(int(line))
# print dictionary

#version 3 - only consider numbers that have three different digits
f=open('jon_homework1.txt','r')

new_list=[]


for line in f:
	if line[0]=='-':
		d=sum(new_list)
		c=str(d)
		if c[0] !=c[1] and c[1] != c[2] and c[0]!=c[2]:
			print c[0]+c[1]+c[2]
		new_list=[]
	else:
		new_list.append(int(line))

