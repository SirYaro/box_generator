#!/bin/bash -e

source config.py

python ./generate_box.py

file_side_out='img/side.jpg'
file_front_out='img/front.jpg'
file_top_out='img/top.jpg'

rm -f img/*jpg

dpi=300

crop_x=$(echo "${box_x}*${dpi}/25.4"|bc)	# mm to px
crop_y=$(echo "${box_y}*${dpi}/25.4"|bc)
crop_z=$(echo "${box_z}*${dpi}/25.4"|bc)



##### SIDE IMG

echo "Croping left/right image: ${crop_x}x${crop_z}px @${dpi} dpi."

IMGW=$(identify -format '%w' ${file_side_in})
IMGH=$(identify -format '%h' ${file_side_in})

if [[ ${crop_x} -gt ${IMGW} || ${crop_z} -gt ${IMGH} ]]; then
    echo "Image too small (${IMGW}x${IMGH}). Exiting."
    exit 1
fi

IMGWC=$((${IMGW}/2-${crop_x}/2))	#dl
IMGHC=$((${IMGH}/2-${crop_z}/2))	#wys

convert ${file_side_in}[${crop_x}x${crop_z}+${IMGWC}+${IMGHC}] ${file_side_out}

##### FRONT IMG

echo "Croping front/back image: ${crop_y}x${crop_z}px @${dpi} dpi."

IMGW=$(identify -format '%w' ${file_front_in})
IMGH=$(identify -format '%h' ${file_front_in})

if [[ ${crop_y} -gt ${IMGW} || ${crop_z} -gt ${IMGH} ]]; then
    echo "Image too small (${IMGW}x${IMGH}). Exiting."
    exit 1
fi

IMGWC=$((${IMGW}/2-${crop_y}/2))	#dl
IMGHC=$((${IMGH}/2-${crop_z}/2))	#wys

convert ${file_front_in}[${crop_y}x${crop_z}+${IMGWC}+${IMGHC}] ${file_front_out}


##### TOP IMG

echo "Croping top/bottom image: ${crop_y}x${crop_x}px @${dpi} dpi."

IMGW=$(identify -format '%w' ${file_top_in})
IMGH=$(identify -format '%h' ${file_top_in})

if [[ ${crop_y} -gt ${IMGW} || ${crop_x} -gt ${IMGH} ]]; then
    echo "Image too small (${IMGW}x${IMGH}). Exiting."
    exit 1
fi

IMGWC=$((${IMGW}/2-${crop_y}/2))	#dl
IMGHC=$((${IMGH}/2-${crop_x}/2))	#wys

convert ${file_top_in}[${crop_y}x${crop_x}+${IMGWC}+${IMGHC}] ${file_top_out}


##### TOP STICKER

echo "Creating top image"
convert ${file_side_out} -rotate 90 img/sideL.jpg								# side L
    IMGW=$(identify -format '%w' img/sideL.jpg)
    crop=`echo "(${IMGW}*(1-${divide}+0.1))/1"|bc`
    convert img/sideL.jpg -gravity East -crop ${crop}x+0+0 +repage img/sideL.jpg

convert ${file_side_out} -rotate -90 img/sideP.jpg								# side P
    IMGW=$(identify -format '%w' img/sideP.jpg)
    crop=`echo "(${IMGW}*(1-${divide}+0.1))/1"|bc`
    convert img/sideP.jpg -gravity West -crop ${crop}x+0+0 +repage img/sideP.jpg

montage img/sideL.jpg ${file_top_out} img/sideP.jpg -tile 3x1 -geometry +0+0 img/LTP.jpg			# left+top+right
convert ${file_front_out} -background white -gravity center -extent $(identify -format '%w' img/LTP.jpg)x img/frontF.jpg	# front
    IMGH=$(identify -format '%h' img/frontF.jpg)
    crop=`echo "(${IMGH}*(1-${divide}+0.1))/1"|bc`
    convert img/frontF.jpg -gravity North -crop x${crop}+0+0 +repage img/frontF.jpg

convert img/frontF.jpg -rotate 180 img/frontB.jpg								# back
montage img/frontB.jpg img/LTP.jpg img/frontF.jpg -tile 1x3 -geometry +0+0 img/top_image.jpg			# all

convert A4.jpg img/top_image.jpg -gravity center -composite img/top_image_A4.jpg				# set up on A4 page

##### BOTTOM STICKER

echo "Creating bottom image"
convert ${file_side_out} -rotate 90 img/sideL.jpg								# side L
    IMGW=$(identify -format '%w' img/sideL.jpg)
    crop=`echo "(${IMGW}*(${divide}+0.1))/1"|bc`
    convert img/sideL.jpg -gravity West -crop ${crop}x+0+0 +repage img/sideL.jpg

convert ${file_side_out} -rotate -90 img/sideP.jpg								# side P
    IMGW=$(identify -format '%w' img/sideP.jpg)
    crop=`echo "(${IMGW}*(${divide}+0.1))/1"|bc`
    convert img/sideP.jpg -gravity East -crop ${crop}x+0+0 +repage img/sideP.jpg

montage img/sideP.jpg ${file_top_out} img/sideL.jpg -tile 3x1 -geometry +0+0 img/LTP.jpg			# +top
convert ${file_front_out} -background white -gravity center -extent $(identify -format '%w' img/LTP.jpg)x img/frontF.jpg			# front
    IMGH=$(identify -format '%h' img/frontF.jpg)
    crop=`echo "(${IMGH}*(${divide}+0.1))/1"|bc`
    convert img/frontF.jpg -gravity South -crop x${crop}+0+0 +repage img/frontF.jpg

convert img/frontF.jpg -rotate 180 img/frontB.jpg								# back
montage img/frontF.jpg img/LTP.jpg img/frontB.jpg -tile 1x3 -geometry +0+0 img/bottom_image.jpg			# all

convert A4.jpg img/bottom_image.jpg -gravity center -composite img/bottom_image_A4.jpg				# set up on A4 page

##### GENERATE PDF

convert -units PixelsPerInch -density 300 -define pdf:fit-page=A4 img/top_image_A4.jpg top_image_A4.pdf
convert -units PixelsPerInch -density 300 -define pdf:fit-page=A4 img/bottom_image_A4.jpg bottom_image_A4.pdf

