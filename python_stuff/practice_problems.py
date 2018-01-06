word="confomr"
f=open('all_words.txt','r')
from itertools import permutations
perms = [''.join(p) for p in permutations( word )]
d={}
for line in f:
	word=line.strip()
	d[word]=1
for p in perms:
	if d.get(p,0)==1:
		print p
	
		
			