#while counter < 100:
#	word=f.readline()
#	counter+=1
#	print counter, word


#counter = 0
#while counter < 100:
	#f.readline()
	#counter+=1


# word=f.readline()
# while word[0]=='a':
# 	print word
# 	word=f.readline()


f=open('all_words.txt','r')
vowels='aeiou'
passed_all_tests=False
while passed_all_tests==False:
	word=f.readline()
	print 'outerloop', word
	while word[0]=='a':
		word=f.readline()
		print 'innerloop', word
	passed_all_tests=True
	for letter in vowels:
		if letter not in word:
			passed_all_tests=False
	if passed_all_tests==True:
		print word


# vowels='aeiou'
# f=open('all_words.txt','r')
# d={}
# word_list=[]
# passed_all_tests=False
# for word in f:
# 	word=word.strip()
# 	passed_all_tests=True
# 	for letter in vowels:
# 		if letter not in word:
# 			passed_all_tests=False
# 	if passed_all_tests==True:
# 		word_list.append(word)
# print word_list