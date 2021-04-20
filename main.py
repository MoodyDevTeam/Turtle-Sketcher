from turtle import *
import turtle

print("Turtle Sketcher version 1.0 by C-Developer-Studios")
print("Press the s key to start the program. Use the arrow keys to draw. ")
print("Press the 1 key to change the canvas color to white")
print("Press the 2 key to change the canvas color to grey")
print("Press the 3 key to change the canvas color to black")
print("Press the Space bar to change color to black")
print("Press the b key to change color to blue")
print("Press the g key to change color to green")
print("Press the w key to change color to white")
print("Press the i key to change color to pink")
print("Press the r key to change color to red")
print("Press the y key to change color to yellow")
print("Press the p key to take the pen up from the canvas")
print("Press the d key to put the pen back on the canvas and continue drawing")
print("Press the c key to clear the canvas")
print("More updates coming soon!")

t = turtle.Turtle()
my_window = turtle.Screen()
my_window.setup(900, 540)
my_window.bgcolor("grey")
speed(0) 
penup()
goto(-100, 205)
turtle.hideturtle = hideturtle()
color("white")
write("Turtle Sketcher", font=("Arial", 20, "bold"))


move_speed = 10
turn_speed = 10

def up():
    t.forward(move_speed)

def down():
    t.backward(move_speed)

def left():
    t.left(turn_speed)

def right():
    t.right(turn_speed)

colors = ["red", "blue", "green", "yellow", "black", "grey", "pink", ""]

def start():
    t.color("black")

def black():
    t.color("black")
    
def red():
    t.color("red")
    
def green():
    t.color("green")
    
def blue():
    t.color("blue")
    
def yellow():
    t.color("yellow")

def pink():
    t.color("pink")

def penup():
    t.penup()

def pendown():
    t.pendown()

def clear():
    t.clear()
        
def white():
    t.color("white")

def bgwhite():
    my_window.bgcolor("white")
    goto(-100, 205)
    turtle.hideturtle = hideturtle()
    color("grey")
    write("Turtle Sketcher", font=("Arial", 20, "bold"))
    t.color("black")

def bggrey():
    my_window.bgcolor("grey")
    goto(-100, 205)
    turtle.hideturtle = hideturtle()
    color("white")
    write("Turtle Sketcher", font=("Arial", 20, "bold"))
    t.color("black")

def bgblack():
    my_window.bgcolor("black")
    goto(-100, 205)
    turtle.hideturtle = hideturtle()
    color("white")
    write("Turtle Sketcher", font=("Arial", 20, "bold"))
    t.color("white")

screen = turtle.Screen()
screen.listen()

screen.onkey(black, "space")
screen.onkey(red, "r")
screen.onkey(green, "g")
screen.onkey(blue, "b")
screen.onkey(yellow, "y")
screen.onkey(pink, "i")
screen.onkey(penup, "p")
screen.onkey(pendown, "d")
screen.onkey(start, "s")
screen.onkey(clear, "c")
screen.onkey(white, "w")
screen.onkey(bgwhite, "1")
screen.onkey(bggrey, "2")
screen.onkey(bgblack, "3")


screen.onkey(up, "Up")  
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

screen.mainloop()
