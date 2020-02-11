##############################################################
# Name: Elkana Munganga
# Submission Date: 02/09/2020
# Minnesota States University Moorhead
# CSIS 152
# Assignment 05
##############################################################



import turtle
ze = turtle.Screen()
ze.bgcolor("lightblue")


jux = turtle.Turtle()
zack = turtle.Turtle()
pal = turtle.Turtle()
niya = turtle.Turtle()
mmp = turtle.Turtle()

jux.ht()
mmp.ht()
zack.ht()
pal.ht()
niya.ht()

pal.goto(0, -300)
pal.clear()

pal.color("green")
pal.shape("square")
pal.shapesize(5, 100, 100)
pal.stamp()


#the sun

niya.clear()
niya.goto(-300, 200)
niya.clear()
niya.fillcolor("yellow")
niya.color("yellow")
niya.begin_fill()
niya.end_fill()

for l in range(0,30):
    niya.hideturtle()
    niya.pensize(2)
    niya.forward(60)
    niya.left(87)
    #niya.fillcolor("blue")


#the ground (will continue later to build the ground)


#print(list(range(5, 60, 2)))
#pal.up()                     # this is new
#for size in range(5, 60, 2):    # start with size = 5 and grow by 2
 #   pal.stamp()                # leave an impression on the canvas


###################################################
#
#
#
#pal.write("My Tesla ", True, align="right")

# fabricating a Convertible tesla car

mmp.goto(0, -200)
mmp.clear()
mmp.color("red")
mmp.pensize(5)
mmp.forward(50)
mmp.circle(20, 400, 40)                 #wheels
mmp.right(85)


zack.goto(0, -200)
zack.clear()
zack.color("red")
zack.pensize(5)
zack.backward(150)
zack.circle(20, 400, 40)                #front wheel



jux.goto(0, -200)
jux.clear()

jux.color("red")
jux.pensize(5)
jux.forward(100)
jux.circle(50, 150, 10)
jux.forward(80)
jux.left(90)
jux.forward(40)                         #front window
jux.right(60)                           #front window
jux.fd(70)
jux.right(90)                           #window seperator
jux.fd(40)                              #window seperator
jux.bk(135)                             #window/door
jux.fd(95)
jux.left(90)
jux.fd(50)
jux.right(50)
jux.fd(45)
jux.circle(30, 70, 5)
jux.fd(50)
jux.left(70)
jux.fd(75)

jux.circle(50, 75, 10)




ze.exitonclick()