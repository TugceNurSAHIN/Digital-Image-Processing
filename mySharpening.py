import cv2
import numpy as np

img = cv2.imread('pelikan.jpg', 0)

cv2.imshow('ilk resim', img)
#img = cv2.medianBlur(img, ksize=3)
#img = cv2.GaussianBlur(img, (5,5), 0)
#cv2.imshow('filtre', img)

def mySharpening(img):
    laplacian = np.array((
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]), dtype="int")

    boy = int(img.shape[0])
    en = int(img.shape[1])
    #print(img.shape)
    new = np.zeros((boy, en, 1), np.uint8)
    sum1 = np.zeros(((boy) * (en), 1), 'int32')
    a = 0
    max1 = 0
    min1 = 0
    for i in range(0,boy - 2,1):

        for j in range(0,en - 2,1):


            if (j == en - 2 and i < 0):
                a1 = img[i + 1][j] * laplacian[0][0]
                b = img[i + 1][j] * laplacian[1][0]
                c = img[i + 2][j] * laplacian[2][0]
                d = img[i + 1][j + 1] * laplacian[0][1]
                e = img[i + 1][j + 1] * laplacian[1][1]
                f = img[i + 2][j + 1] * laplacian[2][1]
                g = img[i + 1][j + 1] * laplacian[0][2]
                h = img[i + 1][j + 1] * laplacian[1][2]
                z = img[i + 2][j + 1] * laplacian[2][2]
                sum1[a] = int(a1 + b + c + d + e + f + g + h + z)
                #sum1[a]=sum1[a]+90
                #sum1[a]=int(sum1[a]/(2.37))
                new[i + 1][j + 1] = sum1[a]
            elif (j < 0 and i < 0):
                a1 = img[i + 1][j + 1] * laplacian[0][0]
                b = img[i + 1][j + 1] * laplacian[1][0]
                c = img[i + 2][j + 1] * laplacian[2][0]
                d = img[i + 1][j + 1] * laplacian[0][1]
                e = img[i + 1][j + 1] * laplacian[1][1]
                f = img[i + 2][j + 1] * laplacian[2][1]
                g = img[i + 1][j + 2] * laplacian[0][2]
                h = img[i + 1][j + 2] * laplacian[1][2]
                z = img[i + 2][j + 2] * laplacian[2][2]
                sum1[a] = int(a1 + b + c + d + e + f + g + h + z)
                #sum1[a]=sum1[a]+90
                #sum1[a]=int(sum1[a]/(2.37))
                new[i + 1][j + 1] = sum1[a]
            elif (i == boy - 2 and j < 0):
                a1 = img[i][j + 1] * laplacian[0][0]
                b = img[i + 1][j + 1] * laplacian[1][0]
                c = img[i + 1][j + 1] * laplacian[2][0]
                d = img[i][j + 1] * laplacian[0][1]
                e = img[i + 1][j + 1] * laplacian[1][1]
                f = img[i + 1][j + 1] * laplacian[2][1]
                g = img[i][j + 2] * laplacian[0][2]
                h = img[i + 1][j + 2] * laplacian[1][2]
                z = img[i + 1][j + 2] * laplacian[2][2]
                sum1[a] = int(a1 + b + c + d + e + f + g + h + z)
                #sum1[a]=sum1[a]+90
                #sum1[a]=int(sum1[a]/(2.37))
                new[i + 1][j + 1] = sum1[a]

            elif (j == en - 2 and i == en - 2):
                a1 = img[i][j] * laplacian[0][0]
                b = img[i + 1][j] * laplacian[1][0]
                c = img[i + 1][j] * laplacian[2][0]
                d = img[i][j + 1] * laplacian[0][1]
                e = img[i + 1][j + 1] * laplacian[1][1]
                f = img[i + 1][j + 1] * laplacian[2][1]
                g = img[i][j + 1] * laplacian[0][2]
                h = img[i + 1][j + 1] * laplacian[1][2]
                z = img[i + 1][j + 1] * laplacian[2][2]
                sum1[a] = int(a1 + b + c + d + e + f + g + h + z)
                #sum1[a]=sum1[a]+90
                #sum1[a]=int(sum1[a]/(2.37))
                new[i + 1][j + 1] = sum1[a]
            elif (j < 0 and i > 0 and i < boy + 1):
                a1 = img[i][j + 1] * laplacian[0][0]
                b = img[i + 1][j + 1] * laplacian[1][0]
                c = img[i + 2][j + 1] * laplacian[2][0]
                d = img[i][j + 1] * laplacian[0][1]
                e = img[i + 1][j + 1] * laplacian[1][1]
                f = img[i + 2][j + 1] * laplacian[2][1]
                g = img[i][j + 2] * laplacian[0][2]
                h = img[i + 1][j + 2] * laplacian[1][2]
                z = img[i + 2][j + 2] * laplacian[2][2]
                sum1[a] = int(a1 + b + c + d + e + f + g + h + z)
                #sum1[a]=sum1[a]+90
                #sum1[a]=int(sum1[a]/(2.37))
                new[i + 1][j + 1] = sum1[a]
            elif (i < 0 and j < en - 2 and j > 0):
                a1 = img[i + 1][j] * laplacian[0][0]
                b = img[i + 1][j] * laplacian[1][0]
                c = img[i + 2][j] * laplacian[2][0]
                d = img[i + 1][j + 1] * laplacian[0][1]
                e = img[i + 1][j + 1] * laplacian[1][1]
                f = img[i + 2][j + 1] * laplacian[2][1]
                g = img[i + 1][j + 2] * laplacian[0][2]
                h = img[i + 1][j + 2] * laplacian[1][2]
                z = img[i + 2][j + 2] * laplacian[2][2]
                sum1[a] = int(a1 + b + c + d + e + f + g + h + z)
                #sum1[a]=sum1[a]+90
                #sum1[a]=int(sum1[a]/(2.37))
                new[i + 1][j + 1] = sum1[a]
            elif (j == en - 2 and i > 0 and i < boy - 2):
                a1 = img[i][j] * laplacian[0][0]
                b = img[i + 1][j] * laplacian[1][0]
                c = img[i + 2][j] * laplacian[2][0]
                d = img[i][j + 1] * laplacian[0][1]
                e = img[i + 1][j + 1] * laplacian[1][1]
                f = img[i + 2][j + 1] * laplacian[2][1]
                g = img[i][j + 1] * laplacian[0][2]
                h = img[i + 1][j + 1] * laplacian[1][2]
                z = img[i + 2][j + 1] * laplacian[2][2]
                sum1[a] = int(a1 + b + c + d + e + f + g + h + z)
                #sum1[a]=sum1[a]+90
                #sum1[a]=int(sum1[a]/(2.37))
                new[i + 1][j + 1] = sum1[a]
            elif (i == en - 2 and j > 0 and j < en - 2):
                a1 = img[i][j] * laplacian[0][0]
                b = img[i + 1][j] * laplacian[1][0]
                c = img[i + 1][j] * laplacian[2][0]
                d = img[i][j + 1] * laplacian[0][1]
                e = img[i + 1][j + 1] * laplacian[1][1]
                f = img[i + 1][j + 1] * laplacian[2][1]
                g = img[i][j + 2] * laplacian[0][2]
                h = img[i + 1][j + 2] * laplacian[1][2]
                z = img[i + 1][j + 2] * laplacian[2][2]
                sum1[a] = int(a1 + b + c + d + e + f + g + h + z)
                #sum1[a]=sum1[a]+90
                #sum1[a]=int(sum1[a]/(2.37))
                new[i + 1][j + 1] = sum1[a]
            else:
                a1 = img[i][j] * laplacian[0][0]
                b = img[i + 1][j] * laplacian[1][0]
                c = img[i + 2][j] * laplacian[2][0]
                d = img[i][j + 1] * laplacian[0][1]
                e = img[i + 1][j + 1] * laplacian[1][1]
                f = img[i + 2][j + 1] * laplacian[2][1]
                g = img[i][j + 2] * laplacian[0][2]
                h = img[i + 1][j + 2] * laplacian[1][2]
                z = img[i + 2][j + 2] * laplacian[2][2]
                sum1[a] = (a1 + b + c + d + e + f + g + h + z)
                #sum1[a]=sum1[a]+90
                #sum1[a]=int(sum1[a]/(2.37))
                if(sum1[a] < 0):
                    sum1[a] = 0
                elif(sum1[a] > 255):
                    sum1[a] = 255
                new[i + 1][j + 1] = sum1[a]


            if (sum1[a] > max1):
                max1 = sum1[a]
            if (sum1[a] < min1):
                min1 = sum1[a]
            a = a + 1
    return new
    #print(max1, min1)

    
shape=mySharpening(img)
cv2.imwrite("greylap.png",shape)
cv2.imshow('foto',shape)
cv2.waitKey()