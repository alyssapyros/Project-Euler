# with print

# s='''
# 75
# 95 64
# 17 47 82
# 18 35 87 10'''

# p=s.strip()
# rows=p.split('\n')
# numbers = []

# for row in rows:
# 	row=row.split(' ')
# 	numbers.append(row)

# print len(numbers)

# def path(depth, col_index, current_path):
# 	current_path = current_path + [ numbers[depth][col_index] ] 
# 	#takes current path and adds the depth + col number

	
# 	if depth == len(numbers) - 1:  # base case to stop recursion; counts 0,1,2,3 but len =4
# 		print current_path #this will be the 4 numbers
	


# 	else: #this is the split
# 		path(depth+1, col_index  , current_path) # left path
# 		path(depth+1, col_index+1, current_path) # right path
	
# path(0,0,[])


# with return

s='''
75
95 64
17 47 82
18 35 87 10'''

p=s.strip()
rows=p.split('\n')
numbers = []

for row in rows:
	row=row.split(' ')
	numbers.append(row)


def path(depth, col_index, current_path, full_list):
	# do stuff
	current_path = current_path + [ numbers[depth][col_index] ] 
	

	# base case
	if depth == len(numbers) - 1:  # base case to stop recursion
		full_list = full_list + [current_path]
		return full_list
	
	# recursive call
	else:
		full_list = path(depth+1, col_index, current_path, full_list) # left path
		full_list = path(depth+1, col_index+1, current_path, full_list) # right path
		return full_list
	
path_list = path(0,0,[],[])
print path_list


