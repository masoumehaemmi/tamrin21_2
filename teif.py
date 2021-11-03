import cv2
import numpy as np

img= np.arange(0, 65025 , 1, np.uint8)

new_img=np.reshape(img , (255 , 255))

h , w =new_img.shape

for i in range ( h ):

    for j in range(w):

        new_img[i,0:6500]= 255 - i
    

cv2.imwrite('grad.jpg',new_img)

cv2.imshow("gradiant" , new_img)

cv2.waitKey()