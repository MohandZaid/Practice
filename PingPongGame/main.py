####initialization

# import turtle module which is responsible of GUI drawing
from tkinter.tix import Tree
import turtle

WIN=turtle.Screen() #initialize screen
WIN.title("Ping Pong") #set the title of the window
WIN.bgcolor("black") #set the background to a color
# WIN.bgpic("background.png") #set the background to a picture
WIN.setup(width=800,height=600) #set width and hight of window
WIN.tracer(0) #stop automatic updating of window screen

racket_width=4
racket_len=0.5
# racket1 object
racket1=turtle.Turtle() #initialize turtle object (racket1)
racket1.speed(0) #set the refresh speed of the object
racket1.shape("square") #set the shape of the object
racket1.color("orange") #set the color of the object
racket1.shapesize(stretch_wid=racket_width,stretch_len=racket_len) #stretch the shape size (default: wid=20pi*1 , len=20pi*1)
racket1.penup() #stop object of drawing lines
racket1.goto(-380,0) #set the position of the object

# racket2 object
racket2=turtle.Turtle()
racket2.speed(0)
racket2.shape("square")
racket2.color("orange")
racket2.shapesize(stretch_wid=racket_width,stretch_len=0.5)
racket2.penup()
racket2.goto(380,0)

# ball object
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_wid=1,stretch_len=1)
ball.penup()
ball.goto(0,0)

ball.dx=0.1
ball.dy=0.1

# score system

score_racket1=0
score_racket2=0

def score_system():
    score=turtle.Turtle()
    score.speed(0)
    score.color("white")
    score.penup()
    score.hideturtle()
    score.goto(0,-280)
    score.write(f"player1 : {score_racket1} -- {score_racket2} : player2" ,align="center", font=("Courier",24,"bold"))

score_system()

#### functions

RACKETS_STEPS=20 #set y coordinate movement steps >> 20pi

#1# racket1 movement input initialization

def racket1_up():
    y=racket1.ycor() #get the y coordinate of racket1
    y+=RACKETS_STEPS #set the new y after click by adding step
    racket1.sety(y) #set the new y coordinate position 

def racket1_down():
    y=racket1.ycor()
    y-=RACKETS_STEPS
    racket1.sety(y)

#2# racket2 movement input initialization

def racket2_up():
    y=racket2.ycor()
    y+=RACKETS_STEPS
    racket2.sety(y)

def racket2_down():
    y=racket2.ycor()
    y-=RACKETS_STEPS
    racket2.sety(y)


#3# keyboard binding
WIN.listen() #tell the window to listen keyboard input

def close(): #function to close loop
    WIN.bye() #set status to false to exit the loop
WIN.onkeypress(close,"c") #when pressing c do close function

#4# listening functions
def movement_action():
        WIN.onkeypress(racket1_up,"w") #when pressing w do racket1_up function
        WIN.onkeypress(racket1_down,"s")
        WIN.onkeypress(racket2_up,"Up")
        WIN.onkeypress(racket2_down,"Down")    
    
#5# game loop
def game_loop():

    movement_action()

    while True: #while status of window is true , window still update
        WIN.update() #update screen everytime the loop run

        #move the ball 
        ball.setx(ball.xcor()+ball.dx)
        ball.sety(ball.ycor()+ball.dy)

        #border check
        if ball.ycor()>290:
            ball.dy *= -1
        if ball.ycor()<-290:
            ball.dy *= -1
        
        if ball.xcor() > 380-0.5*racket_len*20 and ball.xcor() < 380 and ball.ycor()<(racket2.ycor()+20*racket_width) and ball.ycor()>(racket2.ycor()-20*racket_width):
            ball.setx(380-0.5*racket_len*20)
            ball.dx *= -1
        if ball.xcor() < -380+0.5*racket_len*20 and ball.xcor() > -380 and ball.ycor()<(racket1.ycor()+20*racket_width) and ball.ycor()>(racket1.ycor()-20*racket_width):
            ball.setx(-380+0.5*racket_len*20)
            ball.dx *= -1

        if ball.xcor()>390:
            ball.setx(390)
            print("you lose !")
            racket1.goto(-380,0)
            racket2.goto(380,0)
            ball.goto(0,0)
            ball.dx *= -1
            break
        if ball.xcor()<-390:
            ball.setx(390)
            print("you lose !")
            racket1.goto(-380,0)
            racket2.goto(380,0)
            ball.goto(0,0)
            ball.dx *= -1
            break

        if racket1.ycor()>(300-11*racket_width):
            racket1.sety((300-11*racket_width))
        if racket1.ycor()<(-300+11*racket_width):
            racket1.sety((-300+11*racket_width))

        if racket2.ycor()>(300-11*racket_width):
            racket2.sety((300-11*racket_width))
        if racket2.ycor()<(-300+11*racket_width):
            racket2.sety((-300+11*racket_width))

#### main
start_round=False

if WIN.onkeypress(game_loop,"v"):
    start_round=True
elif start_round==False:

    while True: 
            WIN.update()

        