import cv2;
from matplotlib import pyplot as plt
import numpy as np
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
cv2.imwrite('Template/order_dithering.jpg', template_image)

for i in range(10):
    offset_y =i* template_size*3
    sep_template = template_image[0:27,offset_y:offset_y+27]

    cv2.imwrite('Template/od'+str(i)+'.jpg', sep_template)

cv2.waitKey(0)
cv2.destroyAllWindows()
