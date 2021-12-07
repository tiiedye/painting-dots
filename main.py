# Painting Dots
import colorgram
import turtle
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
turtle.colormode(255)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

cursor = turtle.Turtle()
cursor.penup()

x_coord = -250
y_coord = -225

cursor.goto(x_coord, y_coord)


def draw_row():
    for dot in range(10):
        cursor.dot(10, random.choice(rgb_colors))
        cursor.fd(50)


for i in range(10):
    draw_row()
    y_coord += 50
    cursor.goto(x_coord, y_coord)

cursor.hideturtle()

# Exit canvas
screen = turtle.Screen()
screen.exitonclick()
