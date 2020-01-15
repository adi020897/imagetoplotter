import cv2
import scipy.ndimage
import PIL
from PIL import Image

def dodge(front,back):
    result=front*255/(255-back)
    for res in result:
        if((sum(res)/len(res))>=1):
            result[back>=150]=175
            result[back>175]=200
            result[back>200]=255
            result[back<=150]=50
            result[back<50]=30
            result[back<30]=15
            return result.astype('uint8')
        elif((sum(res)/len(res))<=1):
            result[back>=100]=115
            result[back>115]=130
            result[back>130]=160
            result[back>160]=255
            result[back<=100]=66
            result[back<66]=33
            result[back<33]=12
            return result.astype('uint8')

img = cv2.imread('C:/Users/ADi GooNeR/Desktop/image1.jpg')
basewidth = 900
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original image',img)
#cv2.imshow('Gray image', grayimg)
invertedimg = 255-grayimg
#cv2.imshow('Inverted image', invertedimg)
blurimg = scipy.ndimage.filters.gaussian_filter(invertedimg,sigma=-10000)
#cv2.imshow('Blur image', blurimg)
finalimg=dodge(grayimg,blurimg)
finalimg=255-finalimg
cv2.imshow('Final image', finalimg)

'''finalimg2=dodge(grayimg,invertedimg)
finalimg2=255-finalimg2
cv2.imshow('Final image inv', finalimg2)
'''

cv2.waitKey(0)
cv2.destroyAllWindows()
