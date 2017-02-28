import turtle


t=turtle.Turtle()
t.shape('turtle')
def draw (t,distance,n):
	if n==0:
		return
	t.forward(distance)
	t.left(distance)
	draw(t,distance,n-1)


draw(t,50,8)

turtle.mainloop()