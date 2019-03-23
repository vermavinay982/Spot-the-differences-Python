

# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 10:45:07 2019

@author: CodersMine
"""

import cv2

import numpy as np



image1 = cv2.imread("image1.png")

image2 = cv2.imread("image2.png")

print(len(image1))

print(len(image2))

image2=image2[1:,:,:]
print(len(image2))

difference = cv2.subtract(image2, image1)



result = not np.any(difference) #if difference is all zeros it will return False



if result is True:

    print ("The images are the same")

else:

    cv2.imwrite("result.jpg", difference)

    print("the images are different")














