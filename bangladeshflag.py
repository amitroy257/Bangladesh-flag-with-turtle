import turtle as t
def ractangle(color):
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.forward(300)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()
def circle(color):
    t.begin_fill()
    t.fillcolor(color)
    t.circle(-50)
    t.end_fill()

t.up()
t.goto(0, -200)
t.down()
t.goto(0, 250)
ractangle('green')

t.goto(0,170)
t.color('green')
t.forward(85)
circle('red')
