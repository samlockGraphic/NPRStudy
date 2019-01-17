import cv2;
from matplotlib import pyplot as plt
import numpy as np

def ConstantConstruct():
    #6 8 4
    #1 0 3
    #5 2 7
    d = np.array([[6,8,4],[1,0,3],[5,2,7]])
    template_size = 15;
    template_image = np.ones((3 * template_size , 3 * template_size * 10, 1), np.uint8) * 255

    for threshold in range(10):

        offset_y = threshold* template_size*3
        for i in range(template_size):
            for j in range(template_size):
                base_i = 3*i ;
                base_j = 3*j+ offset_y;
                for m in range(3):
                    for n in range(3):
                        if d[m,n] >threshold-1:
                            template_image[base_i+m][base_j+n] =255
                        else:
                            template_image[base_i + m][ base_j+n] =0
    cv2.imwrite('../Template/order_dithering.jpg', template_image)

    for i in range(10):
        offset_y =i* template_size*3
        sep_template = template_image[0:27,offset_y:offset_y+27]

        cv2.imwrite('../Template/od'+str(i)+'.jpg', sep_template)


def OrderDither(img):
    cv2.imshow('o',img)

    d = np.array([[3, 6, 8],
                  [1, 4, 7],
                  [0, 2, 5]])
    new_image = img[:,:]
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            a = i%3
            b = j%3

            if img[i,j]/25 > d[a,b]:
                new_image[i,j] = 255
            else:
                new_image[i,j] = 0
    cv2.imshow('od', new_image)

OrderDither(cv2.imread('image/cat1.jpg',0))
cv2.waitKey(0)
