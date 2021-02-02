import turtle

def tree(length):
    if length >5:
        t.fd(length)
        t.rt(20)
        tree(length-15)
        t.lt(40)
        tree(length-15)
        t.rt(20)
        t.backward(length)
t=turtle.Turtle()
t.lt(90)
t.color("green")
t.speed(1)
tree(90)
