import turtle as t

t.shape("turtle")

n = 50
t.bgcolor("black")
t.color("green")
t.speed(0)

for x in range(n+1):
    t.circle(80)
    t.left(360.0/n)

t.done()
