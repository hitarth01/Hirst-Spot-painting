# from email.mime import image
# import colorgram

# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
import random
import turtle as t

t.colormode(255)
color_list = [(246, 243, 237), (200, 167, 110), (144, 74, 52), (169, 152, 45), (58, 92, 119), (224, 203, 131), (136, 162, 180), (131, 34, 26), (51, 117, 89), (143, 25, 30), (18, 97, 74), (69, 47, 40), (173, 146, 153), (150, 177, 152), (131, 70, 74), (56, 43, 46), (237, 174, 163), (184, 88, 94), (38, 58, 71), (28, 82, 89), (182, 204, 178), (242, 156, 160), (93, 144, 124), (20, 66, 57), (36, 65, 96), (108, 125, 154)]
jim = t.Turtle()
jim.hideturtle()
print(jim.position())
jim.penup()
jim.setposition(-200, -200)
for row in range(10):
    for col in range(10):
        jim.color(random.choice(color_list))
        jim.dot(20)
        jim.forward(50)
    jim.setposition(-200, -200 + 50*(row + 1))
    
    
# 
# print(jim.position())


screen = t.Screen()
screen.exitonclick()