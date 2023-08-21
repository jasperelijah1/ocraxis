# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 18:39:38 2018

@author: HP
"""

from PIL import Image
import pytesseract 
import argparse
import cv2
import os


ap= argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,
                help="path to input image to be ")
ap.add_argument("-p","--preprocess",type=str,default="thresh",
                help="type of preprocessing to be done")
args =vars(ap.parse_args())


image = cv2.imread(args["image"])
gray= cv2.imread(image,0)

if args["preprocess"]== "thresh":
        gray =cv2.threshold(gray,0, 255,
                            cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        
elif args["preprocess"]=="blur":
    gray = cv2.medianBlur(gray,3)
    
filename="{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

cv2.imshow("Image",image)
cv2.imshow("Output",gray)
cv2.waitkey(0)