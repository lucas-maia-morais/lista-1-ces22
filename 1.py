import turtle

def draw_square( t, sz ):
    """Make turtle t draw a square of side sz"""
    t.penup()
    t.goto(-sz/2, -sz/2)
    t.pendown()
    for i in range(4):
        t.forward(sz)
        t.left(90)


if __name__ == "__main__":

    wn = turtle.Screen() # Set up the window and its attributes
    wn.bgcolor("lightgreen")
    wn.title("Alex meets a function")
    alex = turtle.Turtle() # Create alex
    alex.pencolor("purple")
    alex.pensize(2)
    for i in range(1, 5):
        draw_square(alex, 20*i) # Call the function to draw the square
    wn.mainloop()