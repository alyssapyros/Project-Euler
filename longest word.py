f=open('all_words.txt','r')
standard=10
for word in f:
	length=len(word)
	if len(word)>standard:
		standard=len(word)
		longest=word
print standard
f=open('all_words.txt','r')
for word in f:
	if len(word)==standard:
		print word