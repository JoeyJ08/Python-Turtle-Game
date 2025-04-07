import turtle

def jump():
    player.forward(20)

screen = turtle.Screen()
screen.title('Game')

player = turtle.Turtle()
player.shape('square')
player.penup()
player.left(90)

x_num = player.xcor()
y_num = player.ycor()

print(f'x = {x_num} \ny = {y_num}')

screen.onkeypress(jump, 'Up')
screen.listen() 

screen.mainloop()