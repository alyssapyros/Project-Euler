f= open('all_words.txt','r')




class word ():
	def __init__(self, line):
		self.raw=line
		self.clean=line.strip()

	def has_a(self):
		return 'a' in self.clean


	def is_palindrome(self):
		l=list(self.clean)
		l.reverse()
		s="".join(l)
		return s==self.clean


for line in f:
	w=word(line)
	if w.is_palindrome():
		print w.clean, type(w.clean), w.has_a()

