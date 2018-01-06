l=[]
for i in range (1,101):
	c=i**2
	l.append(c)
print sum(l)

d=[]
for i in range (1,101):
	d.append(i)
print sum(d)**2


print (sum(d)**2)-(sum(l))