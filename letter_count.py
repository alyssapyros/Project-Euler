word="bdir"
f=open('all_words.txt','r')
for line in f:
	word=line.strip()
	c=15
	if len(word)==c:
		print word