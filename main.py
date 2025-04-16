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
        self.color('red')
        self.hideturtle()
        self.setpos(-1000, -1000)
        screen.bye()

    def out_of_bounds(self):
        if self.ycor() > 300 or self.ycor() < -300:
            self.die()

    def collision(self, pipe, pipe_type):
        #bird
        b_right = self.xcor() + 10
        b_top = self.ycor() + 10
        b_bottom = self.ycor() - 10
        #pipe
        p_left = pipe.xcor() - 20
        p_top = pipe.ycor() + 200
        p_bottom = pipe.ycor() - 200

        if pipe_type == 'upper':
            if b_right > p_left and b_bottom > p_bottom:
                self.die()

        elif pipe_type == 'lower':
            if b_right > p_left and b_top < p_top:
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
        self.forward(12)
    
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

class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.penup()
        self.speed(0)
        self.setpos(x, y)
        self.hideturtle()
        self.write('Score: 0', False, 'center', ("Courier", 16, "bold"))
    
    def update_score(self, pipe, num):
        if pipe.xcor() < - 230:
            num += 1
            str_num = str(num)
            self.clear()
            self.write(f'Score: {str_num}', False, 'center', ("Courier", 16, "bold"))
        return num

def number_maker():
    num = randint(-170, 170)
    return num

screen = Screen()
screen.title('Flappy Cube')
screen.listen()

bird = Player()
score_num = 0
player_score = Score(-280, 250)
#upper add 260
#lower remove 260
upper = Pipe(260, 300)
lower = Pipe(-260, 300)

while True:
    num = number_maker()
    bird.out_of_bounds()
    bird.gravity()
    upper.move()
    lower.move()
    score_num = player_score.update_score(lower, score_num)
    upper.kill('upper', num)
    lower.kill('lower', num)
    bird.collision(upper, 'upper')
    bird.collision(lower, 'lower')

screen.mainloop()