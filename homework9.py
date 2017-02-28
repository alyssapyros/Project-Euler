import math

for i in range (0,999):
	for x in range (0,999):
		if (i+x)<1000:
			d=1000-x-i
			if i<x and x<d:
				a=i**2
				b=x**2
				c=d**2
				if a+b==c:
					p=math.sqrt(a) * math.sqrt(b)* math.sqrt(c)
					print p
				