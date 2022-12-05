#Snake variant
import turtle
import random
import time
import tkinter

wn = turtle.Screen()
wn.title("Echos by @Psilaxis")
wn.bgcolor("black")
wn.setup(width = 500, height = 500)
wn.tracer(0)

root = turtle.Screen()._root
root.iconbitmap("G:\DevProjects\web\Python\games\Images\icon.ico")
img = tkinter.Image("photo", file="G:\DevProjects\web\Python\games\Images\icon.png")
turtle._Screen._root.iconphoto(True, img)

Coins = 0
Lives = 3
delay = 0.1

# Coin 
coin = turtle.Turtle()
coin.speed(2)
coin.shape("circle")
coin.color("yellow")
coin.shapesize(stretch_wid=.1, stretch_len=.1)
coin.penup()

x = random.randint(-250, 250)
y = random.randint(-100, 250)
coin.goto(x,y) # Position of coin at start of game


# Character
char = turtle.Turtle()
char.speed(0) # animation speed
char.shape("square")
char.color("white")
char.shapesize(stretch_wid=.5, stretch_len=.5)  # increases the character size. 20 pixels tall and 20 wide. (default size without this line is 20 x 20)
char.penup() # penup to move without drawing, pendown to draw when moving 
# char.pensize(20)# Change the Pen Size
char.goto(-50,0) # Position of character at start of game
char.direction = 'stop'

segments = []

# Pen - Coins / Lives
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle() # hides the turtle arrow from displaying.
pen.goto(0,200) # Location of the Score Board
pen.write("Coins: 0 Lives: 3", align="center", font=("Courier", 24, "normal"))


# Character Movement Function
def go_up():
    if char.direction != 'down':
        char.direction = 'up'
def go_down():
    if char.direction != 'up':
        char.direction = 'down'
def go_left():
    if char.direction != 'right':
        char.direction = 'left'
def go_right():
    if char.direction != 'left':
        char.direction = 'right'



def move():
    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
    # Move segment 0 to the char
    if len(segments) > 0:
        x = char.xcor()
        y = char.ycor()
        segments[0].goto(x,y)
    # Keep the snake moving in the same direction
    if char.direction == 'up':
        char.sety(char.ycor() + 10)
    if char.direction == 'down':
        char.sety(char.ycor() - 10)
    if char.direction == 'left':
        char.setx(char.xcor() - 10)
    if char.direction == 'right':
        char.setx(char.xcor() + 10)

def collision(): 
    global Lives
    Lives -= 1
    pen.clear()
    pen.write("Coins: {} Lives: {}".format(Coins,Lives), align="center", font=("Courier", 24, "normal"))
    time.sleep(0.5)
    char.goto(0,0)
    char.direction = 'stop'
    # Hide the segments
    for segment in segments:
        segment.hideturtle()
    # Clear the segments list
    segments.clear()
    # Reset the delay
    delay = 0.1
   

# keyboard Binding
wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')

while True:
	wn.update()

	# Player Border Creation
	if char.ycor() < -242:
		char.sety(242)

	if char.ycor() > 242:
		char.sety(-242)

	if char.xcor() < -242:
		char.setx(242)

	if char.xcor() > 242:
		char.setx(-242)
	

	#Game Over Screen
	if Lives == 0:
		pen.clear()
		pen.goto(0,0)
		pen.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

	#coin collision
	if char.distance(coin) < 10:
		Coins += 1
		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape('square')
		new_segment.color("white")
		new_segment.shapesize(stretch_wid=.1, stretch_len=.1)
		new_segment.penup()
		segments.append(new_segment)
		delay -= 0.001

		pen.clear()
		pen.write("Coins: {} Lives: {}".format(Coins,Lives), align="center", font=("Courier", 24, "normal"))
		
		x = random.randint(-235, 235)
		y = random.randint(-235, 235)
		coin.goto(x,y)
	move()

		# Check for char collision with the body segments
	for segment in segments:
		if segment.distance(char) < 5:
			collision()
	time.sleep(delay)

wn.mainloop()
