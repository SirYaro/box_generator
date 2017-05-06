#!/usr/bin/python


def draw_rec(x_start,y_start, x_move,y_move, divide=0):
    drawing.add(dxf.line((x_start,y_start), (x_start,y_start+y_move), layer='INSERT'))					# Y |
    drawing.add(dxf.line((x_start,y_start+y_move), (x_start+x_move,y_start+y_move), layer='INSERT'))			# X -
    drawing.add(dxf.line((x_start+x_move,y_start+y_move), (x_start+x_move,y_start), layer='INSERT'))			# Y |
    drawing.add(dxf.line((x_start+x_move,y_start), (x_start,y_start), layer='INSERT'))					# X _
#    drawing.add(dxf.line((x_start,y_start+y_move*divide), (x_start+x_move,y_start+y_move*divide), color=7))	# podzial na pol

def draw_rec2(x_start,y_start, x_move,y_move, divide=0, inlet=0,in_l=0,in_t=0,in_r=0,in_b=0):
    global x
    global y
    x=x_start
    y=y_start
    if in_l==1:
	draw_left_out(x,y, x_move,y_move, divide, inlet)
    else:
	draw_left_in(x,y, x_move,y_move, divide, inlet)
    if in_t==1:
	draw_top_out(x,y, x_move,y_move, divide, inlet)
    else:
	draw_top_in(x,y, x_move,y_move, divide, inlet)
    if in_r==1:
	draw_right_out(x,y, x_move,y_move, divide, inlet)
    else:
	draw_right_in(x,y, x_move,y_move, divide, inlet)
    if in_b==1:
	draw_bottom_out(x,y, x_move,y_move, divide, inlet)
    else:
	draw_bottom_in(x,y, x_move,y_move, divide, inlet)
    if divide>0:
	drawing.add(dxf.line((x_start,y_start+y_move*divide), (x_start+x_move,y_start+y_move*divide), color=7))	# podzial na pol

def draw_top_out(x_start,y_start, x_move,y_move, divide, inlet):
    global x
    global y
    distance=x_move-side_space-inlet-inlet-side_space
    x=x_start
    y=y_start
    drawing.add(dxf.line((x,y), (x+side_space,y), color=7))
    x=x+side_space
    draw_outlet_top(x,y)
    drawing.add(dxf.line((x,y), (x+distance,y), color=7))
    x=x+distance
    draw_outlet_top(x,y)
    drawing.add(dxf.line((x,y), (x+side_space,y), color=7))
    x=x+side_space

def draw_top_in(x_start,y_start, x_move,y_move, divide, inlet):
    global x
    global y
    distance=x_move-side_space-inlet-inlet-side_space
    x=x_start
    y=y_start
    drawing.add(dxf.line((x,y), (x+side_space,y), color=7))
    x=x+side_space
    draw_inlet_top(x,y)
    drawing.add(dxf.line((x,y), (x+distance,y), color=7))
    x=x+distance
    draw_inlet_top(x,y)
    drawing.add(dxf.line((x,y), (x+side_space,y), color=7))
    x=x+side_space

def draw_left_out(x_start,y_start, x_move,y_move, divide, inlet):
    global x
    global y
    distance=y_move-side_space-inlet-inlet-side_space
    x=x_start
    y=y_start
    drawing.add(dxf.line((x,y), (x,y+side_space), color=7))
    y=y+side_space
    draw_outlet_left(x,y)
    drawing.add(dxf.line((x,y), (x,y+distance), color=7))
    y=y+distance
    draw_outlet_left(x,y)
    drawing.add(dxf.line((x,y), (x,y+side_space), color=7))
    y=y+side_space

def draw_left_in(x_start,y_start, x_move,y_move, divide, inlet):
    global x
    global y
    distance=y_move-side_space-inlet-inlet-side_space
    x=x_start
    y=y_start
    drawing.add(dxf.line((x,y), (x,y+side_space), color=7))
    y=y+side_space
    draw_inlet_left(x,y)
    drawing.add(dxf.line((x,y), (x,y+distance), color=7))
    y=y+distance
    draw_inlet_left(x,y)
    drawing.add(dxf.line((x,y), (x,y+side_space), color=7))
    y=y+side_space

def draw_right_out(x_start,y_start, x_move,y_move, divide, inlet):
    global x
    global y
    distance=y_move-side_space-inlet-inlet-side_space
    x=x_start
    y=y_start
    drawing.add(dxf.line((x,y), (x,y-side_space), color=7))
    y=y-side_space
    draw_outlet_right(x,y)
    drawing.add(dxf.line((x,y), (x,y-distance), color=7))
    y=y-distance
    draw_outlet_right(x,y)
    drawing.add(dxf.line((x,y), (x,y-side_space), color=7))
    y=y-side_space

def draw_right_in(x_start,y_start, x_move,y_move, divide, inlet):
    global x
    global y
    distance=y_move-side_space-inlet-inlet-side_space
    x=x_start
    y=y_start
    drawing.add(dxf.line((x,y), (x,y-side_space), color=7))
    y=y-side_space
    draw_inlet_right(x,y)
    drawing.add(dxf.line((x,y), (x,y-distance), color=7))
    y=y-distance
    draw_inlet_right(x,y)
    drawing.add(dxf.line((x,y), (x,y-side_space), color=7))
    y=y-side_space

def draw_bottom_out(x_start,y_start, x_move,y_move, divide, inlet):
    global x
    global y
    distance=x_move-side_space-inlet-inlet-side_space
    x=x_start
    y=y_start
    drawing.add(dxf.line((x,y), (x-side_space,y), color=7))
    x=x-side_space
    draw_outlet_bottom(x,y)
    drawing.add(dxf.line((x,y), (x-distance,y), color=7))
    x=x-distance
    draw_outlet_bottom(x,y)
    drawing.add(dxf.line((x,y), (x-side_space,y), color=7))
    x=x-side_space

def draw_bottom_in(x_start,y_start, x_move,y_move, divide, inlet):
    global x
    global y
    distance=x_move-side_space-inlet-inlet-side_space
    x=x_start
    y=y_start
    drawing.add(dxf.line((x,y), (x-side_space,y), color=7))
    x=x-side_space
    draw_inlet_bottom(x,y)
    drawing.add(dxf.line((x,y), (x-distance,y), color=7))
    x=x-distance
    draw_inlet_bottom(x,y)
    drawing.add(dxf.line((x,y), (x-side_space,y), color=7))
    x=x-side_space

def draw_outlet_left(x_,y_):
    global x
    global y
    drawing.add(dxf.line((x,y), (x-thick,y), color=7))
    x=x_-thick
    drawing.add(dxf.line((x,y), (x,y+inlet), color=7))
    y=y_+inlet
    drawing.add(dxf.line((x,y), (x+thick,y), color=7))
    x=x+thick

def draw_inlet_left(x_,y_):
    global x
    global y
    drawing.add(dxf.line((x,y), (x+thick,y), color=7))
    x=x_+thick
    drawing.add(dxf.line((x,y), (x,y+inlet), color=7))
    y=y_+inlet
    drawing.add(dxf.line((x,y), (x-thick,y), color=7))
    x=x-thick

def draw_outlet_top(x_,y_):
    global x
    global y
    drawing.add(dxf.line((x,y), (x,y+thick), color=7))
    y=y_+thick
    drawing.add(dxf.line((x,y), (x+inlet,y), color=7))
    x=x_+inlet
    drawing.add(dxf.line((x,y), (x,y-thick), color=7))
    y=y-thick

def draw_inlet_top(x_,y_):
    global x
    global y
    drawing.add(dxf.line((x,y), (x,y-thick), color=7))
    y=y_-thick
    drawing.add(dxf.line((x,y), (x+inlet,y), color=7))
    x=x_+inlet
    drawing.add(dxf.line((x,y), (x,y+thick), color=7))
    y=y+thick

def draw_outlet_right(x_,y_):
    global x
    global y
    drawing.add(dxf.line((x,y), (x+thick,y), color=7))
    x=x_+thick
    drawing.add(dxf.line((x,y), (x,y-inlet), color=7))
    y=y_-inlet
    drawing.add(dxf.line((x,y), (x-thick,y), color=7))
    x=x-thick

def draw_inlet_right(x_,y_):
    global x
    global y
    drawing.add(dxf.line((x,y), (x-thick,y), color=7))
    x=x_-thick
    drawing.add(dxf.line((x,y), (x,y-inlet), color=7))
    y=y_-inlet
    drawing.add(dxf.line((x,y), (x+thick,y), color=7))
    x=x+thick

def draw_outlet_bottom(x_,y_):
    global x
    global y
    drawing.add(dxf.line((x,y), (x,y-thick), color=7))
    y=y_-thick
    drawing.add(dxf.line((x,y), (x-inlet,y), color=7))
    x=x_-inlet
    drawing.add(dxf.line((x,y), (x,y+thick), color=7))
    y=y+thick

def draw_inlet_bottom(x_,y_):
    global x
    global y
    drawing.add(dxf.line((x,y), (x,y+thick), color=7))
    y=y_+thick
    drawing.add(dxf.line((x,y), (x-inlet,y), color=7))
    x=x_-inlet
    drawing.add(dxf.line((x,y), (x,y-thick), color=7))
    y=y-thick

