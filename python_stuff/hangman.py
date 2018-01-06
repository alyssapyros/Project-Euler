import random
n=random.randint(1,21110)
f=open('all_words.txt','r')
for i in range(n):
	word=f.readline()
	word=word.strip()
while len(word)!=5: #new word and has to take out the space again
	word=f.readline()
	word=word.strip()
print word 


