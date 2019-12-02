import turtle 
def drawSquare(x,y,n):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(n)
        turtle.right(90)
        
for i in range(20,141,40):
    drawSquare(i,20,40)
for j in range(20,141,40):
    drawSquare(20,j,40)
for i in range(4):
    drawSquare(20+40*i,140,40)
for i in range(4):
    drawSquare(20+40*i,100,40)
for i in range(4):
    drawSquare(20+40*i,60,40)