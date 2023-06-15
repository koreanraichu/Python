import turtle as t
t.shape('turtle')
t.color('purple')
circle=100
while (circle >= 10):
    t.pendown()
    t.circle(circle)
    t.penup()
    t.goto(0,t.ycor()+10)
    circle=circle-10
    #동심원
