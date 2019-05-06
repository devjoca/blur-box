import cv2, base64, sys, math
import numpy as np

def generate_blurred(img):
    BOX_LENGTH = 500.0

    dims = img.shape[:2]

    #resized img to fit the whole image inside the box
    factor = BOX_LENGTH / max(dims)
    res_ori = cv2.resize(img, (int(dims[1]*factor), int(dims[0]*factor)), interpolation = cv2.INTER_AREA)

    #resize the image to complete the blur backgorund
    factor = BOX_LENGTH / min(dims)
    res_back= cv2.resize(img, (int(dims[1]*factor), int(dims[0]*factor)), interpolation = cv2.INTER_AREA)
    blur = cv2.GaussianBlur(res_back,(65,65), 0)

    #merge imgs
    offset_x = res_back.shape[0]/2 - res_ori.shape[0]/2
    offset_y = res_back.shape[1]/2 - res_ori.shape[1]/2
    offset_x, offset_y = math.trunc(offset_x), math.trunc(offset_y)
    blur[offset_x:offset_x+res_ori.shape[0], offset_y:offset_y+res_ori.shape[1]] = res_ori

    #crop image
    if res_back.shape[0] < res_back.shape[1]:
        blur = blur[0:res_back.shape[0], offset_y:offset_y+res_ori.shape[1]]
    else:
        blur = blur[offset_x:offset_x+res_ori.shape[0], 0:res_back.shape[1]]

    return blur

if __name__ == "__main__":
    input, splitted_input = sys.argv[1], sys.argv[1].split("/")
    output = "/".join(splitted_input[:-1]) + "/blur-" + splitted_input[-1]
    blurred_img = generate_blurred(cv2.imread(input))
    cv2.imwrite(output, blurred_img)
