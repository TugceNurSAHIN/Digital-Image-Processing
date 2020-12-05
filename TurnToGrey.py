import cv2

image=cv2.imread('pelikan.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('GreyImage', image)
cv2.waitKey()
