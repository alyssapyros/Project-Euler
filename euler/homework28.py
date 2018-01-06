# 00 00 00 00 00 00 00
# 00 21 22 23 24 25 26
# 00 20 07 08 09 10 00
# 00 19 06 01 02 11 00
# 00 18 05 04 03 12 00
# 00 17 16 15 14 13 00
# 00 00 00 00 00 00 00

# edge cases (how to handle boundaries)

# if # lt,
#    0 dn, 		move down

# if 0 up,
#    0 rt, 		move right

# if 0 up,		move up

# if # up, 
#    0 lt 		move left

# if 0 dn me		move down



# list of list = [ [00,00,], [] ]
# dictionary d[x,y] = '1'

# def format(x):
# 	if x <10:
# 		return ' '+str(x)
# 	else return
# 		str(x)



def create_grid (h,w):
	