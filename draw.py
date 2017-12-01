from math import pi
from cairo import SVGSurface, Context, Matrix

WIDTH = 50*100
HEIGHT = 50*100

s = SVGSurface('example3.svg', WIDTH, HEIGHT)
c = Context(s)

# Transform to normal cartesian coordinate system
m = Matrix(yy=-1, y0=HEIGHT)
c.transform(m)

# Set a background color
c.save()
c.set_source_rgb(1,1,1)
c.paint()
c.restore()

# vertical lines
for i in range(0,50):
	c.move_to(i*100, 0*100)
	c.line_to(i*100 , 50*100)
# horizontal lines
for i in range(0,50):
	c.move_to(0*100, i*100)
	c.line_to(50*100 , i*100)
#c.close_path()

c.save()
c.set_line_width(1)
c.stroke_preserve()
c.set_source_rgb(0, 0, 0)
c.fill()
c.restore()

