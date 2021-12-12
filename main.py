from cv2 import cv2 as cv


if __name__ == '__main__':
    # print(dir(numpy))
    print(cv.__version__)

    img = cv.imgread('img/pic1.jpg')
    cv.imshow('Result',
               img)
    cv.waitkey(0)
    cv.destroyallwindows()
