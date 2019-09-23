# -*- coding: utf-8 -*-

from canvas import Canvas
import matplotlib.pyplot as plt

x = Canvas(step_size=2)


l = x.rand_canvas()

print(type(l))

plt.figure(figsize=(8,8))
plt.imshow(l)
plt.show()
