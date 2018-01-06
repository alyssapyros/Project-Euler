s='''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

p=s.strip()
rows=p.split('\n')

# numbers=[]
numbers=[]
values=[]

for i in rows:
	i=i.split(' ')
	numbers.append(i)


length=len(numbers)


def build_path(starting_point,length_of_triangle):
	new_list=[]
	full_path=[]
	p1 = starting_point + [starting_point[-1]]
	p2 = starting_point + [starting_point[-1]+1]
	new_list.append(p1)
	new_list.append(p2)
	# print new_list
	for i in new_list:
		# print type(i)
		#3 is the len of the triangle
		if len(i) <length_of_triangle:
			p1 = i + [i[-1]]
			p2 = i + [i[-1]+1]
			new_list.append(p1)
			new_list.append(p2)
		if len(i)==length_of_triangle:
			full_path.append(i)
	return (full_path)



x=build_path([0],length)


value_path=[]

for i in range(len(x)):
	path_chain = x[i]
	# print path_chain
	single_path=[]
	for c in range(len(numbers)):
		path_pos = path_chain[c]
		tri_row = numbers[c]
		value = tri_row[path_pos]
		single_path.append(int(value))
	value_path.append(single_path)

highest_number=0
for i in value_path:
	total=sum(i)
	if total>highest_number:
		highest_number=total
print highest_number







	