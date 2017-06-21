#!/usr/bin/python


def draw_rec(x_start,y_start, x_move,y_move, divide=0):
    drawing.add(dxf.line((x_start,y_start), (x_start,y_start+y_move), layer='INSERT'))					# Y |
    drawing.add(dxf.line((x_start,y_start+y_move), (x_start+x_move,y_start+y_move), layer='INSERT'))			# X -
    drawing.add(dxf.line((x_start+x_move,y_start+y_move), (x_start+x_move,y_start), layer='INSERT'))			# Y |
    drawing.add(dxf.line((x_start+x_move,y_start), (x_start,y_start), layer='INSERT'))					# X _
#    drawing.add(dxf.line((x_start,y_start+y_move*divide), (x_start+x_move,y_start+y_move*divide), color=7))	# podzial na pol

def draw_rec2(x_start,y_start, x_move,y_move, divide=0, inlet=0,in_l=0,in_t=0,in_r=0,in_b=0,layer_name='s0'):
    global x
    global y
    global top_or_bottom
    x=x_start
    y=y_start
    top_or_bottom=0

    if in_l==0 and in_t==0 and in_r==0 and in_b==0:
	top_or_bottom=1

    if in_l==1:
	draw_left_out(x,y, x_move,y_move, divide, inlet, layer_name)
    else:
	draw_left_in(x,y, x_move,y_move, divide, inlet, layer_name)

    if in_t==1:
	draw_top_out(x,y, x_move,y_move, divide, inlet, layer_name)
    else:
	draw_top_in(x,y, x_move,y_move, divide, inlet, layer_name)

    if in_r==1:
	draw_right_out(x,y, x_move,y_move, divide, inlet, layer_name)
    else:
	draw_right_in(x,y, x_move,y_move, divide, inlet, layer_name)

    if in_b==1:
	draw_bottom_out(x,y, x_move,y_move, divide, inlet, layer_name)
    else:
	draw_bottom_in(x,y, x_move,y_move, divide, inlet, layer_name)

    if divide>0:
	drawing.add(dxf.line((x_start,y_start+y_move*divide), (x_start+x_move-0.001,y_start+y_move*divide), layer='s0'))	# podzial na pol

def draw_top_out(x_start,y_start, x_move,y_move, divide, inlet, layer_name):
    global x
    global y
    distance=x_move-side_space-inlet-inlet-side_space
    x=x_start
    y=y_start
    drawing.add(dxf.line((x,y), (x+side_space,y),  layer=layer_name))
    x=x+side_space
    draw_outlet_top(x,y,layer_name)
    drawing.add(dxf.line((x,y), (x+distance,y),  layer=layer_name))
    x=x+distance
    draw_outlet_top(x,y,layer_name)
    drawing.add(dxf.line((x,y), (x+side_space,y),  layer=layer_name))
    x=x+side_space

def draw_top_in(x_start,y_start, x_move,y_move, divide, inlet, layer_name):
    global x
    global y
    distance=x_move-side_space-inlet-inlet-side_space
    x=x_start
    y=y_start
    drawing.add(dxf.line((x,y), (x+side_space,y),  layer=layer_name))
    x=x+side_space
    draw_inlet_top(x,y,layer_name)
    drawing.add(dxf.line((x,y), (x+distance,y),  layer=layer_name))
    x=x+distance
    draw_inlet_top(x,y,layer_name)
    drawing.add(dxf.line((x,y), (x+side_space,y),  layer=layer_name))
    x=x+side_space

def draw_left_out(x_start,y_start, x_move,y_move, divide, inlet, layer_name):
    global x
    global y
    distance=y_move-side_space-inlet-inlet-side_space
    x=x_start
    y=y_start
    drawing.add(dxf.line((x,y), (x,y+side_space),  layer=layer_name))
    y=y+side_space
    draw_outlet_left(x,y,layer_name)
    drawing.add(dxf.line((x,y), (x,y+distance),  layer=layer_name))
    y=y+distance
    draw_outlet_left(x,y,layer_name)
    drawing.add(dxf.line((x,y), (x,y+side_space), layer=layer_name))
    y=y+side_space

def draw_left_in(x_start,y_start, x_move,y_move, divide, inlet, layer_name):
    global x
    global y
    global top_or_bottom
    if top_or_bottom==0:
	distance=y_move-side_space-inlet-inlet-side_space
    else:
	distance=y_move-side_space-inlet-inlet-side_space-2*thick

    x=x_start
    y=y_start

    if top_or_bottom==0:
	drawing.add(dxf.line((x,y), (x,y+side_space),  layer=layer_name))
	y=y+side_space
    else:
	drawing.add(dxf.line((x,y), (x,y+side_space+thick),  layer=layer_name))
	y=y+side_space+thick

    draw_inlet_left(x,y,layer_name)
    drawing.add(dxf.line((x,y), (x,y+distance),  layer=layer_name))
    y=y+distance
    draw_inlet_left(x,y,layer_name)

    if top_or_bottom==0:
	drawing.add(dxf.line((x,y), (x,y+side_space),  layer=layer_name))
	y=y+side_space
    else:
	drawing.add(dxf.line((x,y), (x,y+side_space+thick),  layer=layer_name))
	y=y+side_space+thick


def draw_right_out(x_start,y_start, x_move,y_move, divide, inlet, layer_name):
    global x
    global y
    distance=y_move-side_space-inlet-inlet-side_space
    x=x_start
    y=y_start
    drawing.add(dxf.line((x,y), (x,y-side_space),  layer=layer_name))
    y=y-side_space
    draw_outlet_right(x,y,layer_name)
    drawing.add(dxf.line((x,y), (x,y-distance),  layer=layer_name))
    y=y-distance
    draw_outlet_right(x,y,layer_name)
    drawing.add(dxf.line((x,y), (x,y-side_space),  layer=layer_name))
    y=y-side_space

def draw_right_in(x_start,y_start, x_move,y_move, divide, inlet, layer_name):
    global x
    global y
    global top_or_bottom
    if top_or_bottom==0:
	distance=y_move-side_space-inlet-inlet-side_space
    else:
	distance=y_move-side_space-inlet-inlet-side_space-2*thick

    x=x_start
    y=y_start

    if top_or_bottom==0:
	drawing.add(dxf.line((x,y), (x,y-side_space),  layer=layer_name))
	y=y-side_space
    else:
	drawing.add(dxf.line((x,y), (x,y-side_space-thick),  layer=layer_name))
	y=y-side_space-thick

    draw_inlet_right(x,y,layer_name)
    drawing.add(dxf.line((x,y), (x,y-distance), layer=layer_name))
    y=y-distance
    draw_inlet_right(x,y,layer_name)

    if top_or_bottom==0:
	drawing.add(dxf.line((x,y), (x,y-side_space),  layer=layer_name))
	y=y-side_space
    else:
	drawing.add(dxf.line((x,y), (x,y-side_space-thick),  layer=layer_name))
	y=y-side_space-thick


def draw_bottom_out(x_start,y_start, x_move,y_move, divide, inlet, layer_name):
    global x
    global y
    distance=x_move-side_space-inlet-inlet-side_space
    x=x_start
    y=y_start
    drawing.add(dxf.line((x,y), (x-side_space,y), layer=layer_name))
    x=x-side_space
    draw_outlet_bottom(x,y,layer_name)
    drawing.add(dxf.line((x,y), (x-distance,y),  layer=layer_name))
    x=x-distance
    draw_outlet_bottom(x,y,layer_name)
    drawing.add(dxf.line((x,y), (x-side_space,y), layer=layer_name))
    x=x-side_space

def draw_bottom_in(x_start,y_start, x_move,y_move, divide, inlet, layer_name):
    global x
    global y
    distance=x_move-side_space-inlet-inlet-side_space
    x=x_start
    y=y_start
    drawing.add(dxf.line((x,y), (x-side_space,y),layer=layer_name))
    x=x-side_space
    draw_inlet_bottom(x,y,layer_name)
    drawing.add(dxf.line((x,y), (x-distance,y),  layer=layer_name))
    x=x-distance
    draw_inlet_bottom(x,y,layer_name)
    drawing.add(dxf.line((x,y), (x-side_space,y), layer=layer_name))
    x=x-side_space

def draw_outlet_left(x_,y_,layer_name):
    global x
    global y
    drawing.add(dxf.line((x,y), (x-thick,y), layer=layer_name))
    x=x_-thick
    drawing.add(dxf.line((x,y), (x,y+inlet), layer=layer_name))
    y=y_+inlet
    drawing.add(dxf.line((x,y), (x+thick,y), layer=layer_name))
    x=x+thick

def draw_inlet_left(x_,y_,layer_name):
    global x
    global y
    drawing.add(dxf.line((x,y), (x+thick,y), layer=layer_name))
    x=x_+thick
    drawing.add(dxf.line((x,y), (x,y+inlet), layer=layer_name))
    y=y_+inlet
    drawing.add(dxf.line((x,y), (x-thick,y), layer=layer_name))
    x=x-thick

def draw_outlet_top(x_,y_,layer_name):
    global x
    global y
    drawing.add(dxf.line((x,y), (x,y+thick), layer=layer_name))
    y=y_+thick
    drawing.add(dxf.line((x,y), (x+inlet,y), layer=layer_name))
    x=x_+inlet
    drawing.add(dxf.line((x,y), (x,y-thick), layer=layer_name))
    y=y-thick

def draw_inlet_top(x_,y_,layer_name):
    global x
    global y
    drawing.add(dxf.line((x,y), (x,y-thick), layer=layer_name))
    y=y_-thick
    drawing.add(dxf.line((x,y), (x+inlet,y), layer=layer_name))
    x=x_+inlet
    drawing.add(dxf.line((x,y), (x,y+thick), layer=layer_name))
    y=y+thick

def draw_outlet_right(x_,y_,layer_name):
    global x
    global y
    drawing.add(dxf.line((x,y), (x+thick,y), layer=layer_name))
    x=x_+thick
    drawing.add(dxf.line((x,y), (x,y-inlet), layer=layer_name))
    y=y_-inlet
    drawing.add(dxf.line((x,y), (x-thick,y), layer=layer_name))
    x=x-thick

def draw_inlet_right(x_,y_,layer_name):
    global x
    global y
    drawing.add(dxf.line((x,y), (x-thick,y), layer=layer_name))
    x=x_-thick
    drawing.add(dxf.line((x,y), (x,y-inlet), layer=layer_name))
    y=y_-inlet
    drawing.add(dxf.line((x,y), (x+thick,y), layer=layer_name))
    x=x+thick

def draw_outlet_bottom(x_,y_,layer_name):
    global x
    global y
    drawing.add(dxf.line((x,y), (x,y-thick), layer=layer_name))
    y=y_-thick
    drawing.add(dxf.line((x,y), (x-inlet,y), layer=layer_name))
    x=x_-inlet
    drawing.add(dxf.line((x,y), (x,y+thick), layer=layer_name))
    y=y+thick

def draw_inlet_bottom(x_,y_,layer_name):
    global x
    global y
    drawing.add(dxf.line((x,y), (x,y+thick), layer=layer_name))
    y=y_+thick
    drawing.add(dxf.line((x,y), (x-inlet,y), layer=layer_name))
    x=x_-inlet
    drawing.add(dxf.line((x,y), (x,y-thick), layer=layer_name))
    y=y-thick

