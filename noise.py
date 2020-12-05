import cv2
import numpy as np

def MeanFilter(image):
    boy= int(image.shape[0])
    en = int(image.shape[1])
    image1=np.zeros((boy,en,1),np.uint8)
    i=0  
    for x in range (1,boy-1,1):    
        j=-1        
        for y in range(1,en-1,1):
        
            j=j+1
            image1[(i,j)]=(int(image[(x,y)])/9+int(image[(x+1,y)])/9+\
                    int(image[(x-1,y)])/9+int(image[(x,y+1)])/9+\
                    int(image[(x+1,y+1)])/9+int(image[(x-1,y+1)])/9+\
                    int(image[(x-1,y-1)])/9+int(image[(x,y-1)])/9+\
                    int(image[(x+1,y-1)])/9)
        i=i+1        
    return image1  
 

image = cv2.imread("resim.jpg",0)
blur= cv2.blur(image,(5,5))
output = cv2.medianBlur(image, ksize=3)  
img_gaussian = cv2.GaussianBlur(output, (5,5), 0) #medianBlur input
mean=MeanFilter(img_gaussian) #Gaussian input
img_bilateral = cv2.bilateralFilter(image, 13, 70, 50)
#kernel = np.ones((5,5),np.float32)/25
#blur = cv2.filter2D(image,-1,kernel) 

cv2.imshow('RealImage',image)
cv2.imshow('Combined',mean) #the best result
cv2.waitKey(0)