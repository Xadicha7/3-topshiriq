# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X5ANYkgh-MsKa9rxv3mdClg4NwqLyl58
"""

from google.colab.patches import cv2_imshow
import cv2
rasm1=cv2.imread("rasm1.jpg")
rasm2=cv2.imread("rasm2.jpg")
rasm3=cv2.imread("rasm3.jpg")
cv2_imshow(rasm1)
cv2_imshow(rasm2)
cv2_imshow(rasm3)

oqqora=cv2.cvtColor(rasm1,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora)
oqqora1=cv2.cvtColor(rasm2,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora1)
oqqora2=cv2.cvtColor(rasm3,cv2.COLOR_BGR2GRAY)
cv2_imshow(oqqora2)