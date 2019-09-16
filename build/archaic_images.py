# This file deals with the images of archaic sign forms.

import os

ideographic = os.listdir(os.path.abspath(os.path.join(__file__ ,"../..")) + '/archaic_images/prc_ideographic_jpg')
numerical = os.listdir(os.path.abspath(os.path.join(__file__ ,"../..")) + '/archaic_images/prc_numerical_jpg')

for i in ideographic:
    print(i[0:-4])
