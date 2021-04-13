import turtle


# window
win = turtle.Screen()
win.title("--Pong--")
win.bgcolor('black')
win.setup(width = 700, height = 500)
win.tracer(0)


# Paddle A
# pa for paddle A variable

pa = turtle.Turtle()
pa.speed(0)
pa.shape('square')
pa.shapesize(stretch_wid = 5, stretch_len = 1)
pa.color('white')
pa.penup()
pa.goto(-300,0)

# Paddle B
# pb for paddle B variable

pb = turtle.Turtle()
pb.speed(0)
pb.shape('square')
pb.shapesize(stretch_wid = 5, stretch_len = 1)
pb.color('white')
pb.penup()
pb.goto(300,0)

# Ball (b for ball)
b = turtle.Turtle()
b.speed(0)
b.shape('circle')
b.color('red')
b.penup()
b.goto(0,0)
b.dx = 0.2
b.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('green')
pen.penup()
pen.hideturtle()
pen.goto(0,200)
pen.write('Player-A: 0   Player-B: 0', align = 'center', font =('ds-digital', 23, 'normal'))

# Score
# sc_a = score A and sc_b = score B
sc_a = 0
sc_b = 0

# Functions 
# For controlling paddle A
def pa_up():
    y = pa.ycor()
    y += 20
    pa.sety(y)

def pa_down():
    y = pa.ycor()
    y -= 20
    pa.sety(y)

# For controlling paddle B 
def pb_up():
    y = pb.ycor()
    y += 20
    pb.sety(y)

def pb_down():
    y = pb.ycor()
    y -= 20
    pb.sety(y)

# Keys in the Keyboard

win.listen()

# Key for moving paddle A
win.onkeypress(pa_up, "w")
win.onkeypress(pa_down, "s")

# Key for moving paddle B 
win.onkeypress(pb_up, "Up")
win.onkeypress(pb_down, "Down")


# Main game loop
while True:
    win.update()

    # Ball movement 
    b.setx(b.xcor() + b.dx)
    b.sety(b.ycor() + b.dy)

    # Border

    # For ups and downs
    if b.ycor() > 240:
        b.sety(240)
        b.dy *= -1
        

    if b.ycor() < -240:
        b.sety(-240)
        b.dy *= -1
        

    # For the right and left side. ***Note***:  if the ball collides with the right or lift side of the window...
    # ... then it goes back to the centre and starts moving like before 
    if b.xcor() > 340:
        b.goto(0,0)
        b.dx *= -1
        sc_a += 5
        pen.clear()
        pen.write(f'Player-A: {sc_a}   Player-B: {sc_b}', align = 'center', font =('ds-digital', 23, 'normal'))
        

    if b.xcor() < -340:
        b.goto(0,0)
        b.dx *= -1
        sc_b += 5
        pen.clear()
        pen.write(f'Player-A: {sc_a}   Player-B: {sc_b}', align = 'center', font =('ds-digital', 23, 'normal'))
        

    # For boncing the ball from paddle 
    if (b.xcor() > 300 and b.xcor() < 310) and (b.ycor() < pb.ycor() + 45 and b.ycor() > pb.ycor() - 45):
        b.setx(300)
        b.dx *= -1

    if (b.xcor() < -300 and b.xcor() > -310) and (b.ycor() < pa.ycor() + 45 and b.ycor() > pa.ycor() - 45):
        b.setx(-300)
        b.dx *= -1