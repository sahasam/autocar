'''
converts the input image to a 2D array that is fed into the A*
algorithm in astar.py

'''
from PIL import Image
import numpy as np
import astar

im = Image.open("path.png")
pix = im.load()

im_width = im.size[0]
im_height = im.size[1]

picture = ''
start = (-1,-1)
end = (-1,-1)


for i in range(0, im_width):
	for j in range(0,im_height):
		if(pix[i,j] == (0,0,0,255) or pix[i,j] == (127,127,127,255)):
			picture+="1 "
		else:
			picture+="0 "
		if(pix[i,j] == (0,0,255,255)):
			start = (i,j)
		if(pix[i,j] == (0,255,0,255)):
			end = (i,j)
		
	if(not(i==im_width - 1)):
		picture+="; "

picArray = np.array(np.mat(picture))
data = astar.astar(picArray,start,end)

for i in range(0,len(data)):
    pix[data[i][0], data[i][1]] = (255,0,0)


#save the data to path.txt
with open("path.txt", "w") as f:
    for i in range(0,len(data)):
        f.write(str(data[i][0]) + " " +str(data[i][1]) + "\n")

        
    	 
	
			
		
