import  turtle as t

X = t.Turtle()
S = t.Screen()

for _ in range(4):
    X.forward(100)
    X.right(90)

X.right(180)

for _ in range(15):
    X.forward(10)
    X.penup()
    X.forward(10)
    X.pendown()


for i in range(3,11):
    a = 360/i
    for _ in range(i):
        X.forward(100)
        X.right(a)




S.exitonclick()