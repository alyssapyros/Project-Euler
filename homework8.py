s = '''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''


def load_data(s):
	s= s.split()
	data={}
	for c in range(len(s[0])):
		for r in range (len(s)):
			value=s[r][c]
			data[ (r,c) ]=int(value)
	return data

print load_data(s)

def get_positions_right (r,c,l):
	if c>49-l:
		return []
	else:
		count=0
		test_list=[]
		while count<=l:
			test_list.append((r,c))
			c+=1
			count+=1
		return test_list


def get_positions_down (r,c,l):
	if r>19-l:
		return []
	else:
		count=0
		test_list_down=[]
		while count<=l:
			test_list_down.append((r,c))
			r+=1
			count+=1
		return test_list_down


# print get_positions_down(x_value,y_value,l)



def get_positions_diagonal (r,c,l):
	if r>19-l or c>49-l:
		return []
	else:
		counter=0
		test_list_diagonal=[]
		while counter<=l: 
			test_list_diagonal.append((r,c))
			r+=1
			counter+=1
			c+=1
		return test_list_diagonal

# x_position=15
# y_position=15
# l=5
# print get_positions_diagonal(x_position,y_position,l)


def get_positions_diagonal_left(r,c,l):
	if c<l or r>19-l:
		return []
	else:
		counter=0
		test_list_diagonal_left=[]
		while counter<=l: 
			test_list_diagonal_left.append((r,c))
			r+=1
			counter+=1
			c-=1
		return test_list_diagonal_left


def get_neighbors (x,y,length):
	neighbor_list=[]
	right=get_positions_right(x,y,length)
	down=get_positions_down(x,y,length)
	diagonal=get_positions_diagonal (x,y,length)
	diagonal_left=get_positions_diagonal_left(x,y,length)
	return [right,down,diagonal,diagonal_left]

def all_starting_positions(data):
	print len(data.keys())
	return data.keys()


def product_function(check,d):
	product=long(1)
	for i in check:
		number=d[i]
		product*=number
	return product

dictionary=load_data(s)


starting_positions=all_starting_positions(dictionary)


all_neighbors=[]

length=12

for sp in starting_positions:
	r=sp[0]
	c=sp[1]
	print r,c
	gn=get_neighbors(r,c,length)
	all_neighbors+=gn





standard=1

for an in all_neighbors:
	pf=product_function(an,dictionary)
	# print len(an)
	if pf>standard:
		standard=pf
		print standard, an


# print len(dictionary.keys())




# x=1
# y=47
# length=2



# sp=get_positions_right(x,y,length)
# print sp

# pf=product_function(sp,dictionary)

# print pf




