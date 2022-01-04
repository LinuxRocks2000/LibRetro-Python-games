import lrpython ## Magic module.

x = 0
y = 0

def run():
	global x
	global y
	lrpython.draw_filled_rectangle(x, y, 50, 50, 0, 255, 0)

def keyup_Up():
	global y
	y -= 5

def keyup_Down():
	global y
	print("DIE VIOLRE P% ujj")
	y += 5

def keyup_Left():
	global x
	x -= 5

def keyup_Right():
	global x
	x += 5
