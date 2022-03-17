
import turtle
t = turtle.Turtle()


radius = 30
for i in range(4):
	t.circle(radius * i)
	t.up()
	t.sety((radius * i)*(-1))
	t.down()
