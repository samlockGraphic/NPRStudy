import numpy as np;
import cv2;
def Floyd_Steinberg_approx(oldColor):
    return round(oldColor/50)*50

#Floyd-Steinberg algorithm
#error diffusion
def Floyd_Steinberg_dither():

    orgin_img = cv2.imread('../image/cat1.jpg', 0)

    approx_img = orgin_img[:,:]

    for i in range(orgin_img.shape[0]):
        for j in range(orgin_img.shape[1]):
            approx_img[i,j] = Floyd_Steinberg_approx(orgin_img[i,j])
    new_img = approx_img[:,:]

    err_p1 = 7.0/16
    err_p2 = 3.0/16
    err_p3 = 5.0/16
    err_p4 =1.0/16
    for i in range(1, orgin_img.shape[0]-1):
        for j in range(1,orgin_img.shape[1]):
            err = orgin_img[i,j]-approx_img[i,j]
            new_img[i+1, j] += err_p1*err
            new_img[i-1, j] += err_p2*err
            new_img[i, j-1] += err_p3 * err
            new_img[i+1, j-1] += err_p4*err
    cv2.imshow('fs', new_img)
Floyd_Steinberg_dither()
