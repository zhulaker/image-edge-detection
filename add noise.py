import pywt
import numpy as np
import cv2

img=cv2.imread('lena_gray.png',0)

inoise=img.copy()
per=0.002
implusenum=int(per*512*512)
for i in xrange(implusenum):
    
    X= np.random.random_integers(0,511)
    Y= np.random.random_integers(0,511)
    if  np.random.random_integers(0,1)==0:
        inoise[X,Y]=0
    else:
        inoise[X,Y]=255

impluse=img.copy()
impluse[:,:]=inoise

cv2.imshow('zhu',img)
cv2.imshow('zhu.impluse',impluse)
cv2.imwrite('impluse.jpg', impluse)

#use Box-Muller gussian algorithm
gnoise=np.zeros((512,512),np.uint8)
for x in xrange(0,512):
    for y in xrange(0,512,2):
        a1=np.random.random_sample()
        a2=np.random.random_sample()
        z1=18*np.cos(2*np.pi*a2)*np.sqrt((-2)*np.log(a1))
        z2=18*np.sin(2*np.pi*a2)*np.sqrt((-2)*np.log(a1))
        f1=int(img[x,y]+z1)
        f2=int(img[x,y+1]+z2)       
        if f1<0:
            f1_val=0
        elif f1>255:
            f1_val=255
        else:
            f1_val=f1
        if f2<0:
            f2_val=0
        elif f2>255:
            f2_val=255
        else:
            f2_val=f2
        gnoise[x,y]=f1_val
        gnoise[x,y+1]=f2_val
gauss=img.copy()
gauss[:,:]=gnoise

cv2.imshow('zhu.gauss',gauss)
cv2.imwrite('guass.jpg', gauss)




cv2.waitKey (0)
