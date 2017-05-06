page_size="A4"		# page size (A5/A4/A3 available)

box_x=150		# outside X dimension
box_y=50		# outside Y dimension
box_z=100		# outside Z dimension (height)
inlet=10		# inlet width
thick=3			# material thickness
divide=0.6		# divide box at. 0-1 range, 0.2=20%, 0.7=70% etc

insert_thick=1		# material thickness
insert_top_overlap=20	# enclosing depth 
insert_free_space=1	# space between box and insert
insert_x_length_ratio=1	# shorter insert on x axis, 0-1 range, 0.2=20%, 0.7=70% etc
insert_y_length_ratio=1	# shorter insert on y axis, 0-1 range, 0.2=20%, 0.7=70% etc

insert_box_x=(box_x*insert_x_length_ratio)-2*thick-insert_free_space			# insert X dimension
insert_box_y=(box_y*insert_y_length_ratio)-2*thick-2*insert_thick-insert_free_space	# insert Y dimension
insert_box_z=box_z/2+insert_top_overlap							# insert height

file_side_in='img.jpg'
file_front_in='img2.jpg'
file_top_in='img3.jpg'

DEPS="python convert montage identify"
