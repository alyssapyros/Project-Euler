import turtle
import random

alyssa = turtle.Turtle()
alyssa.shape('turtle')
alyssa.speed(10)
alyssa.color('purple')


# def grid (t):
# 	t.penup()
# 	t.setposition(0,20)
# 	t.pendown()
# 	path=[]
# 	new_path=[]
# 	count=0
# 	while t.ycor()>0:
# 		t.setheading(0)
# 		a=[0,90]
# 		t.right(random.choice(a))
# 		t.forward(1)
# 		d=t.position()
# 		new_path.append(d)
# 	if new_path not in path:
# 		count+=1
# 		path.append(new_path)
# 	print count, path

# grid(alyssa)



def homework_grid(t):
	t.setposition(0,20)
	position_count=0
	while t.ycor()>0 and t.xcor()<20:
		for i in range(0,20):			
			t.penup()
			t.setposition(0,20)
			t.setheading(0)
			t.pendown()
			t.forward(i)
			t.right(90)
			t.forward(20)
			position_count+=1
			# for i in range (0,20):
			# 	t.penup()
			# 	t.setposition(0,20)
			# 	t.setheading(90)
			# 	t.forward(i)
			# 	t.left(90)
			# 	t.forward(20)
			# 	t.pendown()


		# for i in range (0,20):
		# 	t.color('blue')
		# 	t.penup()
		# 	t.setposition(0,20)

	print position_count

homework_grid(alyssa)






turtle.mainloop()