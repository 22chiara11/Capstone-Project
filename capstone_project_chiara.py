import turtle
import random
import os

#setting up window
wn = turtle.Screen()
wn.title("Crossy Island")
wn.bgcolor("white")
wn.setup(800, 600)
wn.tracer(0)

pen = turtle.Turtle()
pen.color("black")
pen.speed(0)
pen.penup()
pen.goto(0, 250)
pen.hideturtle()
pen.write("Score: 0", move=False, align="center", font=("Courier New", 32, "normal"))

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
player.score = 0
player.life = 1

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
    
# creating the coins
coin = []

for _ in range(1):
    coin = turtle.Turtle()
    coin.color("yellow")
    coin.shape("arrow")
    coin.speed(0)
    coin.penup()
    coin.goto(0, 270)
    coin.setheading(270)
    x = random.randint(-400, 400)
    y = random.randint(250, 350)
    coin.goto(x, y)
    coin.dx = 0
    coin.dy = random.randint(-6, -2)
    coin.append(coin)

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
def go_right():
    x = player.xcor()
    x += 100
    player.setx(x) 

def go_left():
    y = player.ycor()
    y += 100
    player.sety(y) 

#keyboard binding
wn.listen()
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")

#main game loop
while True:
    wn.update()
    #move player
    #player.setx(player.xcor()+player.dx)
    
        #right border
    if player.xcor() > 400:
        player.setx(400)
        player.dx *= -1
    #left border
    if player.xcor() < -400:
        player.setx(-400)
        player.dx *= -1
        
     #iterate through good_guys
    for good_guy in good_guys:
        
        #move good guy
        good_guy.sety(good_guy.ycor()+good_guy.dy)

        #bottom border
        if good_guy.ycor() < -300:
            x = random.randint(-400, 400)
            y = random.randint(250, 350)
            good_guy.goto(x, y)

        #check for collision
        if player.distance(good_guy) < 20:
            x = random.randint(-400, 400)
            y = random.randint(250, 350)
            good_guy.goto(x, y)   
            #player.score += 1
            
        #iterate through coins
    for coin in coins:
        
        #move good guy
        coin.sety(coin.ycor()+coin.dy)

        #bottom border
        if coin.ycor() < -300:
            x = random.randint(-400, 400)
            y = random.randint(250, 350)
            coin.goto(x, y)

        #check for collision
        if player.distance(coin) < 20:
            x = random.randint(-400, 400)
            y = random.randint(250, 350)
            coin.goto(x, y)   
            player.score += 1
            pen.clear()
            pen.write(f"Score: {score}", move=False, align="center", font=("Courier New", 32, "normal"))
            
     #iterate through bad_guys
    for bad_guy in bad_guys:
        #move good guy
        bad_guy.sety(bad_guy.ycor()+bad_guy.dy)

        #bottom border
        if bad_guy.ycor() < -300:
            x = random.randint(-400, 400)
            y = random.randint(250, 350)
            bad_guy.goto(x, y)

        #check for collision
        if player.distance(bad_guy) < 20:
            x = random.randint(-400, 400)
            y = random.randint(250, 350)
            bad_guy.goto(x, y)   
            player.lives -= 1 
    




wn.mainloop()


