import turtle as t
import random
import colorgram

'''Extracting colors from the picture hirst'''

colors = colorgram.extract('hirst.jpg', 30)

# it will take time depending on the image size

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
