import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import cv2


img = cv2.imread('un.jpeg') # Load the image
img=cv2.resize(img,(600,600)) #resizing the image
img_mod = img.copy() # create a copy to modify

points = [] #initializing the co-ordinates

def select_points(event, x, y, flags, param):
    global points, img_mod,cr

    if event == cv2.EVENT_LBUTTONUP:
        points.append((x, y))
        if len(points) == 4: # If we have four points, draw the quadrilateral and crop the image
            
            # Crop the image
            width, height = 500, 500 
            pts1 = np.float32(points)
            pts2 = np.float32([[0,0], [width,0], [width,height], [0,height]])
            matrix = cv2.getPerspectiveTransform(pts1, pts2) #to convert it into rectangular shape
            cropped = cv2.warpPerspective(img_mod, matrix, (width, height)) #cropping image
            cr=cropped

            
            cv2.imshow("Cropped Image", cropped) # Show the cropped image


cv2.namedWindow("Image")
cv2.setMouseCallback("Image", select_points)

cv2.imshow("Image", img)


cv2.waitKey(0)
cv2.destroyAllWindows()


