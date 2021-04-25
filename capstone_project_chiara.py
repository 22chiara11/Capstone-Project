import turtle
import random
import os

#setting up window
wn = turtle.Screen()
wn.title("Crossy Island")
wn.bgcolor("white")
wn.setup(1000, 600)
wn.tracer(0)

lines = ["gggggcgggggg", "ggbbgggbbg", "ggcggggggg", "bgbgggggcg"]

#creating the good guys
good_guys = []

for _ in range(0):
    good_guy = turtle.Turtle()
    good_guy.color("green")
    good_guy.shape("square")
    good_guy.shapesize(5.0, 5.0, 0.0)
    good_guy.speed(0)
    good_guy.penup()
    good_guy.goto(0, 270)
    good_guy.setheading(270)
    good_guy.goto(10000,10000)
    good_guy.dx = 0
    good_guy.dy = -5
    good_guys.append(good_guy)
    
# creating the coins
coins = []

for _ in range(0):
    coin = turtle.Turtle()
    coin.color("yellow")
    coin.shape("square")
    coin.shapesize(5.0, 5.0, 0.0)
    coin.speed(0)
    coin.penup()
    coin.goto(0, 270)
    coin.setheading(270)
    coin.goto(10000,10000)
    coin.dx = 0
    coin.dy = -5
    coins.append(coin)

#creating the bad guys
bad_guys = []

for _ in range(0):
    bad_guy = turtle.Turtle()
    bad_guy.color("red")
    bad_guy.shape("square")
    bad_guy.shapesize(5.0, 5.0, 0.0)
    bad_guy.speed(0)
    bad_guy.penup()
    bad_guy.goto(0, 270)
    bad_guy.setheading(270)
    bad_guy.goto(10000,100000)
    bad_guy.dx = 0
    bad_guy.dy = -5
    bad_guys.append(bad_guy)


#move the player
def go_right():
    x = player.xcor()
    x += 100
    if x >= 450:
        x = 450
    player.setx(x) 

def go_left():
    x = player.xcor()
    x += -100
    if x <= -450:
        x = -450
    player.setx(x) 
    
def go_up():
    y = player.ycor()
    y += 100
    if y >= 250:
        y = 250
    player.sety(y) 
    
def go_down():
    y = player.ycor()
    y += -100
    if y <= -250:
        y = -250
    player.sety(y) 

#keyboard binding
wn.listen()
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")

# Create start level


for row in range(7):
    for col in range(10):
        x = -450 + col * 100
        y = 350 - row * 100
        
        line = random.choice(lines)
        
        if line[col] == "g":
            good_guy = turtle.Turtle()
            good_guy.color("green")
            good_guy.shape("square")
            good_guy.shapesize(5.0, 5.0, 0.0)
            good_guy.speed(0)
            good_guy.penup()
            good_guy.goto(0, 270)
            good_guy.setheading(270)
            good_guy.goto(x,y)
            good_guy.dx = 0
            good_guy.dy = -4
            good_guys.append(good_guy)
        elif line[col] == "b":
            bad_guy = turtle.Turtle()
            bad_guy.color("red")
            bad_guy.shape("square")
            bad_guy.shapesize(5.0, 5.0, 0.0)
            bad_guy.speed(0)
            bad_guy.penup()
            bad_guy.goto(0, 270)
            bad_guy.setheading(270)
            bad_guy.goto(x,y)
            bad_guy.dx = 0
            bad_guy.dy = -4
            bad_guys.append(bad_guy)
        elif line[col] == "c":
            coin = turtle.Turtle()
            coin.color("yellow")
            coin.shape("square")
            coin.shapesize(5.0, 5.0, 0.0)
            coin.speed(0)
            coin.penup()
            coin.goto(0, 270)
            coin.setheading(270)
            coin.goto(x,y)
            coin.dx = 0
            coin.dy = -4
            coins.append(coin)
            

#creating player
player = turtle.Turtle()
player.color("black")
player.shape("circle")
player.speed(0)
player.penup()
player.goto(50, -270)

#player facing up
player.setheading(90)
player.dx = 0
player.dy = 0
player.score = 0
player.life = 1


pen = turtle.Turtle()
pen.color("black")
pen.speed(0)
pen.penup()
pen.goto(0, 250)
pen.hideturtle()
pen.write("Score: 0", move=False, align="center", font=("Courier New", 32, "normal"))



#main game loop
while True:
    wn.update()
    

     #iterate through good_guys
    for good_guy in good_guys:
        
        #move good guy
        good_guy.sety(good_guy.ycor()+good_guy.dy)

        #bottom border
        if good_guy.ycor() <= -350:
            good_guy.sety(350)

        #check for collision
        if player.distance(good_guy) < 20:
            pass
            #player.score += 1
            
        #iterate through coins
    for coin in coins:
        
        #move good guy
        coin.sety(coin.ycor()+coin.dy)

        #bottom border
        if coin.ycor() <= -350:
            coin.sety(350)


        #check for collision
        if player.distance(coin) < 20:  
            player.score += 1
            pen.clear()
            pen.write(f"Score: {player.score}", move=False, align="center", font=("Courier New", 32, "normal"))
            
     #iterate through bad_guys
    for bad_guy in bad_guys:
        #move good guy
        bad_guy.sety(bad_guy.ycor()+bad_guy.dy)

        #bottom border
        if bad_guy.ycor() <= -350:
            bad_guy.sety(350)

        #check for collision
        if player.distance(bad_guy) < 20:
            player.life -= 1
            
        #check for no life
    if player.life == 0:
        pen.clear()
        pen.write(f"GAME OVER", move=False, align="center", font=("Courier New", 32, "normal"))
        wn.update()
        break



wn.mainloop()


