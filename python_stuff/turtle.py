import turtle
import random

def create_turtle(color='blue',size=2):
	t=turtle.Turtle()
	t.shape('turtle')
	t.speed(6)
	t.color(color)
	t.shapesize(1*size,1*size,1*size)
	return t  

def check_boundary(turtle):
	if turtle.xcor()<300 and turtle.xcor()>-300 and turtle.ycor()<300 and turtle.ycor()>-300:
		pass
	else:
		turtle.undo ()

def wander(turtle):
	import random
	turtle.left(random.randint(-90,90))
	turtle.forward(10)
	check_boundary(turtle)

def face_point(t, target):
	x= t.towards(target.position())
	target.setheading(x)


def chase(chaser_turtle, target_turtle):
	x= chaser_turtle.towards(target_turtle.position())
	chaser_turtle.setheading(x)
	chaser_turtle.forward(5)


def celebrate(t):
	import random
	color = ['red', 'orange', 'green', 'purple' ] 	
	t.color(color[random.randint(0,3)])
	t.lt(random.random()*180 - random.random()*180)



def check_if_caught(chaser_turtle,target_turtle):
	d= chaser_turtle.distance(target_turtle)
	# print d
	if d < 10:
		celebrate(chaser_turtle)
		
		# c=create_turtle(color='black',size=1)
		# c.penup()
		# c.setpos(chaser_turtle.pos())
		# babies.append(c)


boy = create_turtle()
girl = create_turtle('pink')

babies=[]

while True:
	wander(girl)
	chase(boy,girl)
	check_if_caught(boy,girl)





turtle.mainloop()