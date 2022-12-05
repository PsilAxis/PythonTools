# Simple Pong in Python 3 for beginners
# By @Sample
# Part 1: Getting Started


#importing the turtle module so we can use it for screen below
import turtle
from playsound import playsound # windows sound module // pip install playsound==1.2.2
# import OS # Mac and Linux sound module.

#Turtle screen Setup.
wn = turtle.Screen()
wn.title("Pong by @Sample")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # animation speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # increases the paddle size. 100 pixels tall and 20 wide. (default size without this line is 20 x 20)
paddle_a.penup()
paddle_a.goto(-350,0) # Position of paddle at start of game

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # animation speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # increases the paddle size. 100 pixels tall and 20 wide. (default size without this line is 20 x 20)
paddle_b.penup()
paddle_b.goto(350,0) # Position of paddle at start of game


# Ball

ball = turtle.Turtle()
ball.speed(0) # animation speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0) # Position of ball at start of game
ball.dx = -.25 # amount of pixels the ball will move in this coordinate when updated.  
ball.dy = -.25

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
	y = paddle_a.ycor()
	y += 20
	paddle_a.sety(y)

def paddle_a_down():
	y = paddle_a.ycor()
	y -= 20
	paddle_a.sety(y)

def paddle_b_up():
	y = paddle_b.ycor()
	y += 20
	paddle_b.sety(y)

def paddle_b_down():
	y = paddle_b.ycor()
	y -= 20
	paddle_b.sety(y)


# keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
	wn.update()

	# Move the Ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Border Checking, so ball bounces off top and bottom
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
		playsound("bounce.wav", False) # playsound Module for windows. set False to play asynchronously) 
									   # Os module - aplay is for linux, afplay is for mac

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1
		playsound("bounce.wav", False)

	# Ball Goal, Reset and update Score!
	if ball.xcor() > 390:
		ball.goto(0,0)
		ball.dx *= -1
		score_a += 1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

	if ball.xcor() < -390:
		ball.goto(0,0)
		ball.dx *= -1
		score_b += 1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

	# Paddle and Ball Collisions
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
		ball.setx(340)
		ball.dx *= -1
		playsound("bounce.wav", False)

	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
		ball.setx(-340)
		ball.dx *= -1
		playsound("bounce.wav", False)
