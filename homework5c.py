f=open('all_words.txt','r')
vowels='aeiou'
d={}
passed_all_tests=False
while passed_all_tests==False:
	word=f.readline()
	passed_all_tests=True
	for letter in vowels:
		if letter not in word:
			passed_all_tests=False
	if passed_all_tests==True:
		d[word[0]]=word
print d


# # vowels='aeiou'
# # f=open('all_words.txt','r')
# # d={}
# # passed_all_tests=False
# # for word in f:
# # 	word=word.strip()
# # 	passed_all_tests=True
# # 	for letter in vowels:
# # 		if letter not in word:
# # 			passed_all_tests=False
# # 	if passed_all_tests==True:
# # 		key=word[0]
# # 		value=word
# # 		current_list=
# # 		new_list=current_list.append(word)
# # 		d[key]=new_list
# # print d


# vowels='aeiou'
# f=open('all_words.txt','r')
# d={}
# passed_all_tests=False
# for word in f:
# 	word=word.strip()
# 	passed_all_tests=True
# 	for letter in vowels:
# 		if letter not in word:
# 			passed_all_tests=False
# 	if passed_all_tests==True:
# 		key=word[0]
# 		value=word
# 		d[key]=[value]
# 		d[key]=d.get(key,[])+[value]
# print d



