import turtle

wn = turtle.Screen()
wn.title("Window")
wn.bgcolor("green")
wn.setup(height=600,width=600)
tur = turtle.Turtle()
tur.color("white")
tur.pendown()
tur.pensize(2)
tur.speed(0)
tur.fillcolor("yellow")
tur.begin_fill()
for i in range(20):
    tur.circle(40)
    tur.left(140)
tur.end_fill()
wn.mainloop()