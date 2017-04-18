import cv2, base64
import numpy as np

def readBase64(base64image):
    img = base64.b64decode(base64image)
    npimg = np.fromstring(img, dtype=np.uint8);
    return cv2.imdecode(npimg, 1)

def toBase64(npImage):
    cnt = cv2.imencode('.png',npImage)[1]
    return base64.encodestring(cnt)

def generate_blur(image):
    BOX_LENGTH = 500.0

    img = readBase64(image)
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
    blur[offset_x:offset_x+res_ori.shape[0], offset_y:offset_y+res_ori.shape[1]] = res_ori

    #crop image
    if res_back.shape[0] < res_back.shape[1]:
        blur = blur[0:res_back.shape[0], offset_y:offset_y+res_ori.shape[1]]
    else:
        blur = blur[offset_x:offset_x+res_ori.shape[0], 0:res_back.shape[1]]

    return toBase64(blur)