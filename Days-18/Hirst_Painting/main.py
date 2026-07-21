import random
import turtle as turtle_module
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('images.jpg',30)
# for color in colors:
#     rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.shape("turtle")
tim.penup()
tim.hideturtle()
colors_list = [[0,0,0],[33,37,41],[44,62,80],[30,64,175],[37,99,235],[124,58,237],[255,0,0],[0,128,0],[255,165,0]]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1,number_of_dots + 1):
    tim.dot(20,random.choice(colors_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)





screen = turtle_module.Screen()
screen.exitonclick()