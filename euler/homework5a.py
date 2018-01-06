#define vowels as string
vowels='aeiou'
#open/read the file
f=open('all_words.txt','r')
#define passed_all_tests
passed_all_tests=False
#start the loop
#while passed_all_tests==False:
#change passed_all_tests so if it goes through it will break the loop
#loop through words in file and strip the space
for word in f:
	word=word.strip()
	passed_all_tests=True
#loop through letters in the vowels string
	for letter in vowels:
#if the letter is not in the word then passed_all_tests is false
		if letter not in word:
			#print letter, word
			passed_all_tests=False
#print words that have all vowels
	if passed_all_tests==True:
		print word
	




