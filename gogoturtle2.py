import turtle as t
t.shape('turtle')
t.color('plum')
rotate=0
while (rotate < 10):
    if (rotate%2 == 0):
        t.up()
        t.circle(75)
        t.right(36)
        rotate = rotate + 1
    else:
        t.down()
        t.circle(75)
        t.right(36)
        rotate = rotate + 1
#penup&pendown이 추가되었습니다. 