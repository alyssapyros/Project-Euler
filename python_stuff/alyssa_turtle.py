import turtle

# right forward
def rf(t):
	t.right(90)
	t.forward(100)

# left forward
def lf(t):
	t.left(90)
	t.forward(100)

# forward
def f(t):
	t.forward(100)


def letter_O(t):
	for i in range(360):
		t.right(1)
		t.forward(1)

def letter_J(t):
	rf(t)
	f(t)
	rf(t)
	rf(t)


def letter_L(t):
	lf(t)
	t.backward(100)
	t.right(90)
	t.forward(50)

def letter_Y(t):
	t.left(90)
	t.forward(75)
	t.left(90)
	t.forward(25)
	t.right(90)
	t.forward(25)
	t.backward(25)
	t.right(90)
	t.forward(50)
	t.left(90)
	t.forward(25)

def letter_S(t):
	f(t)
	t.left(90)
	t.forward(50)
	t.left(90)
	t.forward(100)
	t.right(90)
	t.forward(50)
	t.right(90)
	t.forward(100)

#rewrite with 4 turtles and have them write at once and dance


# def dance(t):
# 	import random
# 	color = ['red', 'orange', 'green', 'purple' ] 	
# 	t.color(color[random.randint(0,3)])
# 	t.lt(random.random()*180 - random.random()*180)


def move_to (t,a,b):
	t.setheading(0)
	t.penup()
	t.setposition(a,b)
	t.pendown()


alyssa = turtle.Turtle()
alyssa.shape('turtle')
alyssa_2= turtle.Turtle()
alyssa_2.shape('turtle')
alyssa_3= turtle.Turtle()
alyssa_3.shape('turtle')
alyssa_4= turtle.Turtle()
alyssa_4.shape('turtle')




move_to(alyssa,-200,1)
letter_L(alyssa)
move_to(alyssa_2,-100,1)
letter_Y(alyssa_2)
move_to(alyssa_3,-50,1)
letter_S(alyssa_3)
move_to(alyssa_4,60,1)
letter_S(alyssa_4)



# jon = turtle.Turtle()
# jon.shape('turtle')
# jon.penup()
# jon.fd(100)

# while True:
# 	dance(alyssa)
# 	dance(jon)


# alyssa = turtle.Turtle()
# alyssa.shape('turtle')

# letter_J(alyssa)

# dance(alyssa)



turtle.mainloop()