# -*- coding: utf-8 -*-

from PIL import Image
import random

class Canvas:
    
    def __init__(self, width=92, height=96, step_size=2):
        
        self.width = float(width)
        self.height = float(height)
        self.step = float(step_size)
    
    def rand_canvas(self):
        w = int(self.width*10)
        h = int(self.height*10)
        s = int(self.step*10)
        
        q_ = Image.new("RGB", (w,h),(255,255,255))
        pixel = q_.load()
        for x in range(0,w,s):
            for y in range(0,h,s):
                red = random.randrange(0,255)
                blue = random.randrange(0,255)
                green = random.randrange(0,255)
                
                for i in range(x, x+s):
                    for j in range(y, y+s):
                        pixel[i,j]=(red,blue,green)
        return q_
    
    def __str__(self):
        return "I'm a quilt"
    