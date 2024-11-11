
import turtle


def drawSquare(speed, size, angle, color):
    turtle.speed(speed)
    turtle.color(color)
    turtle.begin_fill()
    
    def move(len, angl):
        turtle.forward(len)
        turtle.left(angl)
        
    for _ in range(4):
        move(size, angle)
        
    turtle.end_fill()
        
drawSquare(1, 100, 90, 'red')
turtle.goto(200, 200)
drawSquare(1, 200, 90, 'blue')




