#((2n)+(-1)^n)/n+1

#   import math
#   import matplotlib.pyplot as plt
#   import numpy as np
#   
#   
#   x_array = []
#   y_array = []
#   
#   #for n in range(1000):
#   #    print(((2*n)+pow(-1,n))/(n+1))
#   #    x_array.append(n)
#   #    y_array.append(((0.2*n)+pow(-1,n))/(n+1))
#   
#   for x in range(360):
#       x_array.append(pow(x,2)+ pow(x,2))
#       y_array.append(pow(x,2)+ pow(x,2))
#   
#   
#       
#   plt.plot(x_array, y_array)
#   plt.show()

#n = 1000000000
#print(((2*n)+pow(-1,n))/(n+1))

#import numpy as np
#import matplotlib.pyplot as plt
#
#theta = np.linspace(0, 2*np.pi, 100)
#
#radius = 0.3
#
#a = radius*np.cos(theta)
#b = radius*np.sin(theta)
#
#figure, axes = plt.subplots(1)
#
#axes.plot(a, b)
#axes.set_aspect(1)
#
#plt.title('Circle using Parametric Equation')
#plt.show()


import math
import turtle
import matplotlib.pyplot as plt
import numpy as np
import random
from turtle import *
import subprocess
import os
from PIL import Image

turtle.speed(0)

def make_shit():
    for shit in range(1):

        turtle.setpos(0,0)

        for x in range(50):
            #number_x = random.randrange(-550,550)
            #number_y = random.randrange(-350,350)
            #turtle.goto(number_x,number_y)
            forward(200)
            left(170)

        turtle.goto(0,0)

        turtle.hideturtle()
        file = f'outputname{shit}.eps'
        turtle.getscreen().getcanvas().postscript(file=file)
        screenshot(file)
        turtle.clear()

def screenshot(name):
        filename  = name
        directory  = 'C:/Users/alexp/Desktop/pspng' 
        fullpath  = os .path .join( directory,  filename )
        eps, png  = f'{fullpath}',  f'{fullpath}.png'
        #canvas .postscript( file=eps,  pagewidth=Width -1,  pageheight=Height -1 )
        #print( 'saved', eps )
        img  = Image .open( eps )  ##  use PIL to convert to PNG
        img .save( png, 'png', optimize = True, compress_level = 9 )
        img.close()
        os .remove( eps )
        #print( f'converted to', png )

#screenshot()



make_shit()
