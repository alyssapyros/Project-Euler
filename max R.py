def most_occurences(search_for):
	saved=[]
	f=open('all_words.txt','r')
	standard=2
	for word in f:
		word=word.strip()
		count=0
		for i in range(len(word)):
			letter=word[i]
			if letter==search_for:
				count=count+1
		if count==standard:
			saved.append(word)
		if count>standard:
			saved=[word]
			standard=count
	print search_for, saved
	
all_letters='abcdefghijklmnopqrstuvwxyz'
for letter in all_letters: 
	most_occurences(letter)

