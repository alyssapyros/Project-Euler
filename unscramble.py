# this is the word it will attempt to unscramble
word = "bdri"
# use short words, because long ones will take forever to complete
# I'll show you how to speed it up another time


# this opens a file and stores the file object in variable "f"
f = open('all_words.txt', 'r')

# you can read the file line by line, like so
for line in f:
	print line

# import a python module with cool functionality
from itertools import permutations

# use the imported module to generate permutations of "word"
perms = [''.join(p) for p in permutations( word )]

# perms contains a list of strings, each string is a reordering of letters
# you can see that by using the code below
for p in perms:
 	print p



# TO DO : write code that unscrables "word"
word="brid"
f=open('all_words.txt','r')
from itertools import permutations
perms = [''.join(p) for p in permutations( word )]
for line in f:
	w=line.strip()
	for p in perms:
		if p==w:
			print p 
