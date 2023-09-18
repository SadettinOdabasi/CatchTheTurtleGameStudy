import random
import turtle
import time

board = turtle.Screen()
board.bgcolor("#14c0f1")
board.title("Catch The Turtle")
board.screensize(600, 600)

turtle_instance = turtle.Turtle()
turtle_first_line = turtle.Turtle()
turtle_second_line = turtle.Turtle()

turtle_instance.ht()
turtle_first_line.ht()
turtle_second_line.ht()


turtle_first_line.penup()
turtle_first_line.setposition(0, 370)

turtle_second_line.penup()
turtle_second_line.setposition(0, 350)

font = ("Arial", 14, "normal")

score = 0


def turtle_move():
    xPos = random.randint(-300, 300)
    yPos = random.randint(-300, 300)
    turtle_instance.shape("turtle")
    turtle_instance.shapesize(1, 1, 8)
    turtle_instance.color("#9e0101")
    turtle_instance.penup()
    turtle_instance.setposition(xPos, yPos)
    turtle_instance.st()
    turtle_instance.speed(9)
    time.sleep(0.5)
    turtle_first_line.onclick(detect_score)


def detect_score(x, y):
    global score
    score += 1
    score_text = "Score: {}".format(score)
    turtle_first_line.write(score_text, align="center", font=font)
    turtle_first_line.clear()
    print(x, y)


def countdown(t):
    while t:
        timer = "{:02d}".format(t)
        timer_text = "Time: {}".format(timer)
        turtle_first_line.write("Score: 0", align="center", font=font)
        turtle_second_line.write(timer_text, align="center", font=font)
        turtle_move()
        turtle_move()
        turtle_second_line.clear()

        t -= 1

        if t <= 0:
            turtle_second_line.write("Game Over", align="center", font=font)


countdown(15)

turtle.mainloop()
