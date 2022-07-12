from turtle import Turtle, Screen
import random


def random_color():
    colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
              "SeaGreen"]
    return random.choice(colors)


def random_direction():
    directions = [0, 90, 180, 270]
    return random.choice(directions)


def main():
    tim = Turtle()
    tim.speed(5)
    tim.pensize(15)

    for _ in range(200):
        tim.color(random_color())
        tim.setheading(random_direction())
        tim.forward(30)

    screen = Screen()
    screen.exitonclick()


if __name__ == "__main__":
    main()
