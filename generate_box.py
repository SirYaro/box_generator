#!/usr/bin/python

from dxfwrite import DXFEngine as dxf
execfile('config.py')
execfile('functions.py')
drawing = dxf.drawing('box.dxf')
x=0+thick
y=0+thick
side_space=3*thick

print "Generating box"

#drawing.add_layer('TEXTLAYER', color=2)
drawing.add_layer('INSERT', color=3)
drawing.add(dxf.text('Thinkness='+str(thick), insert=(0, -3)))
drawing.add(dxf.text('Thinkness='+str(insert_thick), insert=(0, -6), layer='INSERT'))


draw_rec(0,box_z/2,				insert_box_y,insert_box_z)	# scianka przednia
draw_rec(0+insert_box_y,box_z/2,		insert_box_x,insert_box_z)	# scianka lewa
#draw_rec(insert_box_y+insert_box_x,0,	insert_box_y,insert_box_z)		# scianka tylna
#draw_rec(2*insert_box_y+insert_box_x,0,	insert_box_x,insert_box_z)	# scianka prawa
draw_rec(0,-insert_box_z+box_z/2,		insert_box_y,insert_box_z)	# scianka tylna
draw_rec(insert_box_y,-insert_box_z+box_z/2,	insert_box_x,insert_box_z)	# scianka prawa
#
#draw_rec(box_y-2*thick,box_z-2*thick,	box_x,box_y)				# scianka gorna
#draw_rec(box_y-2*thick,0,		box_x,-box_y)				# scianka dolna




draw_rec2(x,y,				box_y-2*thick,box_z-2*thick, divide, inlet,1,1,1,1)	# scianka przednia
draw_rec2(box_y-thick,y,		box_x,box_z-2*thick, divide, inlet,0,1,0,1)		# scianka lewa
draw_rec2(box_y+box_x-thick,y,		box_y-2*thick,box_z-2*thick, divide, inlet,1,1,1,1)	# scianka tylna
draw_rec2(2*box_y+box_x-3*thick,y,	box_x,box_z-2*thick, divide, inlet,0,1,0,1)		# scianka prawa

draw_rec2(box_y-thick,box_z-thick,	box_x,box_y,  0, inlet,0,0,0,0)				# scianka gorna
draw_rec2(box_y-thick,-box_y+thick,	box_x,box_y, 0, inlet,0,0,0,0)				# scianka dolna



#drawing.add_layer('TEXTLAYER', color=2)
#drawing.add(dxf.text('Test', insert=(0, 0.2), layer='TEXTLAYER'))

drawing.save()