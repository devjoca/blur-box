import cv2

def blurImage(src, dst):
    img = cv2.imread(src)
    blur = cv2.GaussianBlur(img,(65,65), 0)
    cv2.imwrite(dst, blur)