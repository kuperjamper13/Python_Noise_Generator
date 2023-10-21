import random
from PIL import Image
import math
import os


def canvas_creator(canvas_height, canvas_width):

    height = canvas_height
    width = canvas_width

    # Checks if can be devided by 2 #

    if height == 0:
        height = 10
    elif height % 2 == 0:
        height += 1
    elif height % 2 != 0:
        pass

    #--------------------------------#

    if width == 0:
        width = 10
    elif width % 2 == 0:
        width += 1
    elif width % 2 != 0:
        pass

    #________________________________#


    # __Creates the canvas (Lists)__ #
    
    canvas = []
    for h in range(height):
        row = []
        for w in range(width):
            row.append("")
        canvas.append(row)

    #________________________________#


    # Values in odd rows and colomns #

    mid_values = []

    #--------------------------------#

    old_num = random.randint(0,10)
    for n in range(int((height/2))*int((width/2))): 
        mid_values.append(old_num)
        new_number = random.randint(int(math.sqrt((old_num-2)**2)), old_num + 2)
        if new_number == 11:
            new_number = 9
        elif new_number == 12:
            new_number = 8
        old_num = new_number

    #--------------------------------#

    mid_value_time = 0
    for c in range(int((height-1)/2)):
        for r in range(int((width-1)/2)):
            canvas[2*c+1][2*r+1] = mid_values[mid_value_time]*10
            mid_value_time += 1

    #________________________________#
    

    # __________Print Rows__________ #
    os.system("cls")
    for t in range(height):
        print(canvas[t])
    

canvas_creator(10, 10)




"""     ------Create Canvas------

"""


"""     ------Image Generator------
from PIL import Image

# Create a canvas
canvas = Image.new("RGB", (20, 20), (0, 0, 0))

# Paint a red square on the canvas
canvas.putpixel((10, 10), (255, 255, 255))

# Save the canvas
canvas.save("canvas.png")
"""
