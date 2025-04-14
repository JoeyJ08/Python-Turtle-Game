from turtle import *
from random import *

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.setpos(-200,0)
        self.shape('square')
        self.left(90)
        self.showturtle()
        screen.onkey(self.jump, 'Up')
    
    def jump(self):
        self.sety(self.ycor() + 80)

    def gravity(self):
        self.sety(self.ycor() - 10)

    def die(self):
        self.hideturtle()
        self.setpos(-5000, -5000)
        screen.bye()

    def out_of_bounds(self):
        if self.ycor() > 300 or self.ycor() < -300:
            self.die()

class Pipe(Turtle):
    def __init__(self, y, x):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.color('green')
        self.shape('square')
        self.shapesize(20, 2)
        self.setpos(x, y)
        self.setheading(180)
        self.showturtle()

    def move(self):
        self.forward(7)
    
    def kill(self):
        if self.xcor() < -230:
            self.hideturtle()
            self.setpos(-1000, -1000)

def make_new(upper, lower):
    pass

screen = Screen()
screen.title('Game')
screen.listen()

bird = Player()
#upper add 270
#lower remove 270
upper = Pipe(270, 300)
lower = Pipe(-270, 300)

while True:
    bird.out_of_bounds()
    bird.gravity()
    upper.move()
    upper.kill()
    lower.move()
    lower.kill()

screen.mainloop()