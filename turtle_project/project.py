import turtle
import heroes


def draw_square():
    window = turtle.Screen()

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")

    for i in range(1, 5):
        brad.forward(100)
        brad.left(90)

    window.exitonclick()


draw_square()
