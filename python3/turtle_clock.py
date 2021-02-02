import turtle
t=turtle.Turtle()
t.shape("turtle")
t.color("green")
t.stamp()
move=30
for i in range(12):
    t.penup()
    t.fd(50)
    t.pendown()
    t.fd(25)
    t.penup()
    t.fd(15)
    t.stamp()
    t.home()
    t.right(move)
    move+=30
    
