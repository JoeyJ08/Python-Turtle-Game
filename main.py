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
        self.setpos(-1000, -1000)
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
    
    def kill(self, pipe_type, num):
        if self.xcor() < -230:
            self.hideturtle()
            self.setpos(-1000, -1000)
            self.make_new(pipe_type, num)

    def make_new(self, pipe_type, num):
        self.showturtle()
        if pipe_type == 'upper':
            num = num + 260
            self.setpos(300, num)
        elif pipe_type == 'lower':
            num = num - 260
            self.setpos(300, num)

def number_maker():
    num = randint(-150, 150)
    return num

screen = Screen()
screen.title('Game')
screen.listen()

bird = Player()
#upper add 260
#lower remove 260
upper = Pipe(260, 300)
lower = Pipe(-260, 300)

while True:
    num = number_maker()
    bird.out_of_bounds()
    bird.gravity()
    upper.move()
    upper.kill('upper', num)
    lower.move()
    lower.kill('lower', num)


screen.mainloop()