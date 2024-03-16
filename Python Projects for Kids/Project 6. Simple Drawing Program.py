import turtle

def drawing_program():
    window = turtle.Screen()
    pen = turtle.Turtle()

    pen.speed(1)

    pen.color("blue")
    pen.shape("turtle")

    for _ in range(4):
        pen.forward(100)
        pen.right(90)

    window.mainloop()

drawing_program()
