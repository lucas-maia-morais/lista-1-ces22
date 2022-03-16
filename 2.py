import turtle

def draw_poly(t, n, sz):
    """Draw a polygon with n sides and side size sz"""
    for i in range(n):
        t.forward(sz)
        t.left(360/n)


if __name__ == "__main__":
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    wn.title("Tess meets a function")
    tess = turtle.Turtle() # create Tess
    tess.pencolor("purple")
    tess.pensize(2)
    draw_poly(tess, 8, 50)
    wn.mainloop()