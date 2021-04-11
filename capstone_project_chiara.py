import turtle
import random
import os

#setting up window
wn = turtle.Screen()
wn.title("Crossy Island")
wn.bgcolor("white")
wn.setup(800, 600)
wn.tracer(0)

#score
score = 0

#lives
life = 1

#creating player
player = turtle.Turtle()
player.color("black")
player.shape("circle")
player.speed(0)
player.penup()
player.goto(0, -270)
#player facing up
player.setheading(90)
player.dx = 0

#creating the good guys
good_guys = []

for _ in range(1):
    good_guy = turtle.Turtle()
    good_guy.color("green")
    good_guy.shape("triangle")
    good_guy.speed(0)
    good_guy.penup()
    good_guy.goto(0, 270)
    good_guy.setheading(270)
    x = random.randint(-400, 400)
    y = random.randint(250, 350)
    good_guy.goto(x, y)
    good_guy.dx = 0
    good_guy.dy = random.randint(-6, -2)
    good_guys.append(good_guy)

#creating the bad guys
bad_guys = []

for _ in range(1):
    bad_guy = turtle.Turtle()
    bad_guy.color("red")
    bad_guy.shape("square")
    bad_guy.speed(0)
    bad_guy.penup()
    bad_guy.goto(0, 270)
    bad_guy.setheading(270)
    x = random.randint(-400, 400)
    y = random.randint(250, 350)
    bad_guy.goto(x, y)
    bad_guy.dx = 0
    bad_guy.dy = random.randint(-6, -2)
    bad_guys.append(bad_guy)

#move the player

#keyboard binding
#wn.listen()
#wn.onkeypress(go_right, "Right")
#wn.onkeypress(go_left, "Left")

#main game loop



wn.mainloop()


