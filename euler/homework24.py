from itertools import permutations


numbers='0123456789'

perms = [''.join(p) for p in permutations(numbers)]


all_perms=[]

for p in perms:
	all_perms.append(int(p))

all_perms.sort()

print all_perms[999999]
