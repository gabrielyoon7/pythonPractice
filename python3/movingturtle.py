import turtle
t=turtle.Turtle()
t.width(3)
t.shape("turtle")
t.shapesize(3,3)
while True:
    command=input("명령어를 입력하시오: ")
    if command =="l":
        t.lt(90)
        t.fd(100)
    if command =="r":
        t.rt(90)
        t.fd(100)
    if command =="q":
        break;
    
