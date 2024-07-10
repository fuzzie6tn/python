"""Extracting colors. A tuple with R value G value and B value"""
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
color_list = [(1, 9, 29), (121, 96, 42), (238, 211, 72), (77, 34, 23), (221, 80, 59), (225, 117, 100), (92, 1, 21), (178, 140, 171), (151, 92, 116), (35, 90, 26), (8, 154, 73), (204, 64, 92), (220, 178, 219), (167, 129, 76), (1, 63, 146), (4, 220, 218), (3, 80, 30), (80, 135, 178), (78, 115, 146), (131, 156, 178), (122, 186, 167), (122, 11, 32), (10, 216, 222), (137, 221, 208), (245, 202, 7), (229, 174, 166)]