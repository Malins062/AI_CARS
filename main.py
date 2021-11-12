import cv2


if __name__ == '__main__':
    img = cv2.imgread('img/pic1.jpg')
    cv2.imshow('Result', img)
    cv2.waitkey(0)
