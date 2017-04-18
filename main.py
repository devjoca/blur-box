import cv2
import numpy as np

BOX_LENGTH = 500.0
img = cv2.imread('pikachu.png')
dims = img.shape[:2]

#resized img to fit the whole image inside the box
factor = BOX_LENGTH / max(dims)
res_ori = cv2.resize(img, (int(dims[1]*factor), int(dims[0]*factor)), interpolation = cv2.INTER_AREA)

#reize the image to complete the blur backgorund
factor = BOX_LENGTH / min(dims)
res_back= cv2.resize(img, (int(dims[1]*factor), int(dims[0]*factor)), interpolation = cv2.INTER_AREA)
blur = cv2.GaussianBlur(res_back,(65,65), 0)

#merge imgs
offset_x = res_back.shape[0]/2 - res_ori.shape[0]/2
offset_y = res_back.shape[1]/2 - res_ori.shape[1]/2
blur[offset_x:offset_x+res_ori.shape[0], offset_y:offset_y+res_ori.shape[1]] = res_ori

#crop image
blur = blur[0:res_back.shape[0], offset_y:offset_y+res_ori.shape[1]]
cv2.imwrite('pikachu-blur.png', blur)




