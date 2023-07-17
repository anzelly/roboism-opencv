import cv2
import numpy as np
import math

# creating a numpy array filled with zeros to use as a blank image 
img=np.zeros((512,512,3), np.uint8) #cv2.imread('file address')

points=[] #stores co-ordinates of the points you click on image

# creating function to mark points on image
def drawcircle(event,x,y,flags,parameter):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),6,(128, 0, 128),-1)

        # drawing lines from the point at index 0 
        if (len(points)!=0):
            cv2.arrowedLine(img, tuple(points[0]), (x,y), (128, 0, 128), 3)

        points.append([x,y])
        cv2.imshow('image',img)
        print(points)

        # uses findangle() function on your first 3 clicks 
        if len(points)==3:
            degrees=findangle()
            print(degrees) # will have to add 180 for OBTUSE angles

# slope function (y2-y1)/(x2-x1) for two points on the list
def slope(p1,p2):
    return (p2[1]-p1[1])/(p2[0]-p1[0])

# creating function to find angle (tan inverse formula w slopes)
def findangle():
    a=points[-2]
    b=points[-3]
    c=points[-1]
    m1=slope(b,a)
    m2=slope(b,c)
    angle=math.atan((m2-m1)/(1+m1*m2))
    angle=round(math.degrees((angle)))
    if angle<0:
        angle=angle+180
    cv2.putText(img, str(angle), (b[0]+40, b[1]+40), cv2.FONT_ITALIC,2,(0, 128, 0),2, cv2.LINE_AA)
    cv2.imshow('image',img)
    return angle

while True:

    cv2.imshow('image',img)
    cv2.setMouseCallback('image',drawcircle)
    if cv2.waitKey(1)&0xff==ord('r'): # if you click 'r', it RESETS
        img=np.zeros((512,512,3), np.uint8)
        points=[] # updates list to empty again
        cv2.imshow('image',img)
        cv2.setMouseCallback('image',drawcircle) # runs the func again

    if cv2.waitKey(1)&0xff==ord('q'): # if you click 'q', it BREAKS
        break

    # cv2.destroyAllWindows()




