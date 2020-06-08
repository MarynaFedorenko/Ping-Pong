import turtle
from random import choice, randint

window = turtle.Screen()
window.title("Ping-Pong")
window.setup(width=1.0, height=1.0)  # the whole screen
window.bgcolor("black")
window.tracer(2)

border = turtle.Turtle()
border.speed(0)
border.color("dark green")
border.begin_fill()
border.goto(-500, 300)
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()

border.goto(0, 300)
border.setheading(270)
border.color("white")
for i in range(25):
    if i % 2 == 0:  # сли чётный отрезок
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.goto(0, -300)
border.hideturtle()

rocket_left = turtle.Turtle()
rocket_left.color("white")
rocket_left.shape("square")
rocket_left.shapesize(stretch_len=1, stretch_wid=5)  # 1 = 10px
rocket_left.penup()  # не будет оставлять след
rocket_left.goto(-450, 0)

rocket_right = turtle.Turtle()
rocket_right.color("white")
rocket_right.shape("square")
rocket_right.shapesize(stretch_len=1, stretch_wid=5)  # 1 = 10px
rocket_right.penup()  # не будет оставлять след
rocket_right.goto(450, 0)

FONT = ("Arial", 44)#big letters = const

score_left = 0
sl = turtle.Turtle(visible=False)
sl.color("white")
sl.penup()
sl.setposition(-200, 300)
sl.write(score_left, font=FONT)

score_right = 0
sr = turtle.Turtle(visible=False)
sr.color("white")
sr.penup()
sr.setposition(200, 300)
sr.write(score_left, font=FONT)

def move_up_left():
    y = rocket_left.ycor() + 10
    if y > 250:
        y = 250
    rocket_left.sety(y)

def move_down_left():
    y = rocket_left.ycor() - 10
    if y < -250:
        y = -250
    rocket_left.sety(y)

def move_up_right():
    y = rocket_right.ycor() + 10
    if y > 250:
        y = 250
    rocket_right.sety(y)

def move_down_right():
    y = rocket_right.ycor() - 10
    if y < -250:
        y = -250
    rocket_right.sety(y)

ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.color("red")
ball.dx = 1
ball.dy = -1
ball.penup()

window.listen()
window.onkeypress(move_up_left, "w")
window.onkeypress(move_down_left, "s")
window.onkeypress(move_up_right, "Up")
window.onkeypress(move_down_right, "Down")

while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.dy = -ball.dy

    if ball.xcor() <= -490:
        score_right+=1
        sr.clear()
        sr.write(score_right, font=FONT)
        ball.goto(0, 0)
        ball.dx = choice([-1.5, -1, 1, 1.5])
        ball.dy = choice([-1.5, -1, 1, 1.5])

    if ball.xcor() >= 490:
        score_left+=1
        sl.clear()
        sl.write(score_left, font=FONT)
        ball.goto(0, 0)
        ball.dx = choice([-1.5, -1, 1, 1.5])
        ball.dy = choice([-1.5, -1, 1, 1.5])

    if ball.ycor() >= rocket_right.ycor() - 50 \
            and ball.ycor() <= rocket_right.ycor() + 50 \
            and ball.xcor() >= rocket_right.xcor() - 10 \
            and ball.xcor() <= rocket_right.xcor() + 10:
        ball.dx = -ball.dx
    if ball.ycor() >= rocket_left.ycor() - 50 \
            and ball.ycor() <= rocket_left.ycor() + 50 \
            and ball.xcor() >= rocket_left.xcor() - 10 \
            and ball.xcor() <= rocket_left.xcor() + 10:
        ball.dx = -ball.dx

window.mainloop()
