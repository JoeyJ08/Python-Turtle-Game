from turtle import *

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

class Pipe(Turtle):
    def __init__(self, y, x):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.color('green')
        self.shape('square')
        self.shapesize(15, 2)
        self.setpos(x, y)
        self.setheading(180)
        self.showturtle()

    def move(self):
        self.forward(7)

screen = Screen()
screen.title('Game')
screen.listen()

bird = Player()
upper = Pipe(230, 300)
lower = Pipe(-230, 300)

while True:
    bird.gravity()
    upper.move()
    lower.move()

screen.mainloop()