# import pynum2word

# # from num2words import num2words
# num2word(36)

total_numbers=[]

ones=['one','two','three','four','five','six','seven','eight','nine']
tens =['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
twenty_plus=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
hundred=['hundred']
thousand=['one thousand']

space=0
counter=0
#1-9
for i in ones:
	total_numbers.append(i)
#10-19
for i in tens:
	total_numbers.append(i)
#20,30,40,50,60,70,80,90
for i in twenty_plus:
	total_numbers.append(i)
#21-99 (not counting 20,30,40,50,60,70,80,90)
for i in twenty_plus:
	for c in ones:
		d=i+' '+c
		total_numbers.append(d)
#100,200,300,400,500,600,700,800,900
for i in ones:
	for c in hundred:
		hundreds=i+' '+c
		total_numbers.append(hundreds)
		#hundreds + 1-9
		for digit in ones:
			b= hundreds +' '+'and'+ ' '+ digit
			total_numbers.append(b)
		#hundreds + 11-19
		for numbers in tens:
			f=hundreds+' '+'and'+' '+numbers
			total_numbers.append(f)
		#hundreds + 20,30,40,50,60,70,80,90
		for number in twenty_plus:
			m=hundreds+' '+'and'+' '+number
			total_numbers.append(m)
		#hundred interval + 21-99 (not counting 20,30,40,50,60,70,80,90)
		for r in twenty_plus:
			for q in ones:
				g=hundreds+' '+'and'+' '+r+' '+q
				total_numbers.append(g)
for i in thousand:
	total_numbers.append(i)


print (total_numbers)

for i in total_numbers:
	for letter in i:
		if letter ==' ':
			space+=1
		else:
			counter+=1
print counter



# unique = list(set(total_numbers))
# print len(unique), len(total_numbers)

		

