from turtle import *
import turtle
t=turtle.Turtle()
t.shape()
turtle.title("해해해")
color('red', 'black')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
turtle.exitonclick()
