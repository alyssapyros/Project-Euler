f=open('jon_homework1.txt','r')

new_list=[]


for line in f:
	if line[0]=='-':
		d=sum(new_list)
		print 'sum of section:', d
		new_list=[]
	else:
		new_list.append(int(line))

#version 1 - count of what's below 500 and what's above
#version 2 - count many are for each group of 100
#version 3 - only consider numbers that have three different digits
#change around line 8



# new_list=[]
# new_list_two=[]
# c=0
# for line in f:
# 	t=line.split()
# 	if t[0]=='------------------------------':
# 		for i in new_list:
# 			b= int(i)
# 			new_list_two.append(b)
# 		d=sum(new_list_two)
# 		print 'sum of section:'
# 		print d
# 		new_list=[]
# 		new_list_two=[]
# 	if t[0] != '------------------------------':
# 		new_list.append(t[0])
