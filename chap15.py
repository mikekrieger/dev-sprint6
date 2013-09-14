# This is where chapter 15 exercises go.

#ex 15.3

from tkinter import *

class rectangle():
	def __init__(self, coords, color):   
		self.coords = coords
		self.color = color   
	def __del__(self):
		print("InDELETE")
		del self
		print("Goodbye")
	def draw(self, canvas):
		print("In draw")
		print("Canvas  = ",canvas)
		print("self = ",self)
		print("build canvas = ", rectangle_id = Canvas.create_rectangle(*(0, 0, 30, 30), fill="yellow")

root = Tk()
root.title('Basic Tkinter straight line')
width = 500
height = 500
w = Canvas(root, width=width, height=height)

f = []
f=Rectangle((0+30*10, 0+30*10, 100+30*10, 100+30*10),"blue")
print("Draw object",f.draw(w),f)
f.__del__()
del f
w.pack()
mainloop()