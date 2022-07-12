from turtle import Turtle, Screen


def main():
    tim = Turtle()
    for _ in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

    screen = Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
