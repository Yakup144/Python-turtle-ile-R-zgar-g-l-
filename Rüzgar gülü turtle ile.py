import turtle
t = turtle.Turtle()
t.shape("turtle")

t.speed(2)
t.begin_fill()
t.fillcolor("Blue")
for i in range(4):
    t.circle(50, 180)
    t.forward(100)
    t.left(90)
t.end_fill()
t.right(90)
t.pensize(4)
t.forward(150)
