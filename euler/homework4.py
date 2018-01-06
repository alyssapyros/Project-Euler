standard=24
for i in range(111, 999):
	for n in range (111,999):
		c=i*n
		c=str(c)
		if c[0::]==c[::-1]:
			c=int(c)
			if c>standard:
				standard=c
				print c
			



# n=1
# for i in range (1,5):
# 	for p in range (1,5):
# 		print i,p