import cv2
import numpy as np
 
image = cv2.imread("pelikan.jpg",0)
def mean(im,im1,x,y,i,j):

    im[(i,j)]=(int(im1[(x,y)])+int(im1[(x+1,y)])+int(im1[(x,y+1)])+int(im1[(x+1,y+1)]))/4
    
    return im[(i,j)]


def resizeToQuarter(image):
    
    
    boy= int(image.shape[0])
    en = int(image.shape[1])
    #print(en,boy)
    boy1=int(boy/2)
    en1=int(en/2)
    image1=np.zeros((boy1,en1,1),np.uint8)
    i=0
  
    for x in range (0,boy-1,2):
    
        j=0
        
        for y in range(0,en-1,2):
            
             
            image1[(i,j)]=mean(image1,image,x,y,i,j)
            j=j+1

        i=i+1        
    #print(j,i)
    return image1         
      
       
cv2.imshow("FirstImage", image)
cv2.imshow("Resized image", resizeToQuarter(image))
cv2.waitKey(0)
cv2.destroyAllWindows()
