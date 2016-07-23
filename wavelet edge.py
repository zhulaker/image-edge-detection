import pywt
import numpy as np
import cv2
import scipy
from scipy import signal
img=cv2.imread('guass.jpg',0) #read image
cv2.imshow('org.jpg',img)
wave18='sym2' #wavelet type
w1=pywt.dwt2(img, wavelet =wave18)
img1=np.zeros((2*(w1[0].shape[0]),2*(w1[0].shape[0])),np.uint8)
img122=np.zeros((w1[0].shape),np.uint8)
img112=np.zeros((w1[0].shape),np.uint8)
img121=np.zeros((w1[0].shape),np.uint8)
img111=np.zeros((w1[0].shape),np.uint8)
img111=np.zeros((w1[0].shape),np.uint8)
img112=w1[1][0]
img121=w1[1][1]
img122=w1[1][2]
img112=img112/np.max(img112)
img121=img121/np.max(img121)
img111[:,:]=w1[0]*255/w1[0].max()
img122=img122/np.max(img122)

img112=img112*255/img112.max()
img121=img121*255/img121.max()
img122=w1[1][2]*255/w1[1][2].max()
#img111=LL, img112=LH, img121=HL, img122=HH
for i in xrange(0,w1[0].shape[0]):
    for j in xrange(0,w1[0].shape[0]):
        img1[i][j]=img111[i][j]
        img1[i+w1[0].shape[0]][j]=img121[i][j]
        img1[i][j+w1[0].shape[0]]=img112[i][j]
        img1[i+w1[0].shape[0]][j+w1[0].shape[0]]=img122[i][j]

#img1=LL,LH,HL,HH    
cv2.imshow('zhu111',img111)

cv2.imwrite('zhu1.jpg',img111)

imgg=cv2.imread('zhu1.jpg',0)
#same as w1
w2=pywt.dwt2(imgg, wavelet =wave18)
img2=np.zeros((2*(w2[0].shape[0]),2*(w2[0].shape[0])),np.uint8)
img222=np.zeros((w2[0].shape),np.uint8)
img212=np.zeros((w2[0].shape),np.uint8)
img221=np.zeros((w2[0].shape),np.uint8)
img211=np.zeros((w2[0].shape),np.uint8)
img211=np.zeros((w2[0].shape),np.uint8)
img212=w2[1][0]
img221=w2[1][1]
img212=img212/np.max(img212)
img221=img221/np.max(img221)
img211[:,:]=w2[0]*255/w2[0].max()
img212=img212*255/img212.max()
img221=img221*255/img221.max()
img222=w2[1][2]*255/w2[1][2].max()
for i in xrange(0,w2[0].shape[0]):
    for j in xrange(0,w2[0].shape[0]):
        img2[i][j]=img211[i][j]
        img2[i+w2[0].shape[0]][j]=img221[i][j]
        img2[i][j+w2[0].shape[0]]=img212[i][j]
        img2[i+w2[0].shape[0]][j+w2[0].shape[0]]=img222[i][j]

    
cv2.imshow('zhu211',img211)

cv2.imwrite('zhu2.jpg',img211)

imggg=cv2.imread('zhu2.jpg',0)
#same as w1
w3=pywt.dwt2(imggg, wavelet =wave18)
img3=np.zeros((2*(w3[0].shape[0]),2*(w3[0].shape[0])),np.uint8)
img322=np.zeros((w3[0].shape),np.uint8)
img312=np.zeros((w3[0].shape),np.uint8)
img321=np.zeros((w3[0].shape),np.uint8)
img311=np.zeros((w3[0].shape),np.uint8)
img311=np.zeros((w3[0].shape),np.uint8)
img312=w3[1][0]
img321=w3[1][1]
img312=img312/np.max(img312)
img321=img321/np.max(img321)
img311[:,:]=w3[0]*255/w3[0].max()
img312=img312*255/img312.max()
img321=img321*255/img321.max()
img322=w3[1][2]*255/w3[1][2].max()
for i in xrange(0,w3[0].shape[0]):
    for j in xrange(0,w3[0].shape[0]):
        img3[i][j]=img311[i][j]
        img3[i+w3[0].shape[0]][j]=img321[i][j]
        img3[i][j+w3[0].shape[0]]=img312[i][j]
        img3[i+w3[0].shape[0]][j+w3[0].shape[0]]=img322[i][j]

    
cv2.imshow('zhu311',img311)

cv2.imwrite('zhu3.jpg',img311)

imgggg=cv2.imread('zhu3.jpg',0)
#same as w1
w4=pywt.dwt2(imgggg, wavelet =wave18)
img4=np.zeros((2*(w4[0].shape[0]),2*(w4[0].shape[0])),np.uint8)
img422=np.zeros((w4[0].shape),np.uint8)
img412=np.zeros((w4[0].shape),np.uint8)
img421=np.zeros((w4[0].shape),np.uint8)
img411=np.zeros((w4[0].shape),np.uint8)
img411=np.zeros((w4[0].shape),np.uint8)
img412=w4[1][0]
img421=w4[1][1]
img412=img412/np.max(img412)
img421=img421/np.max(img421)
img411[:,:]=w4[0]*255/w4[0].max()
img412=img412*255/img412.max()
img421=img421*255/img421.max()
img422=w4[1][2]*255/w4[1][2].max()
for i in xrange(0,w4[0].shape[0]):
    for j in xrange(0,w4[0].shape[0]):
        img4[i][j]=img411[i][j]
        img4[i+w4[0].shape[0]][j]=img421[i][j]
        img4[i][j+w4[0].shape[0]]=img412[i][j]
        img4[i+w4[0].shape[0]][j+w4[0].shape[0]]=img422[i][j]

    
cv2.imshow('zhu411',img411)

cv2.imwrite('zhu4.jpg',img411)
#COMBINE LEVEL1
g1=np.zeros(img421.shape)
for i in xrange(0,img421.shape[0]):
    for j in xrange(0,img421.shape[0]):
        g1[i][j]=np.sqrt(img421[i][j]**2+img412[i][j]**2)
g1=g1*255/g1.max()
g1=np.array(g1,dtype='uint8')
cv2.imshow('im1',g1)

img42=cv2.resize(g1,(64,64))
img42=np.array(img42,dtype='f')
img321=np.array(img321,dtype='f')
img312=np.array(img312,dtype='f')
#COMBINE IMAGE LL(2)
g2=np.zeros(img321.shape)
for i in xrange(0,img321.shape[0]):
    for j in xrange(0,img321.shape[0]):
        g2[i][j]=np.sqrt(img321[i][j]**2+img312[i][j]**2)
g2=g2*255/g2.max()
g2=np.array(g2,dtype='uint8')
cv2.imshow('im2',g2)
#COMBINE IMAGE LL(3)
g3=np.zeros(img221.shape)
for i in xrange(0,img221.shape[0]):
    for j in xrange(0,img221.shape[0]):
        g3[i][j]=np.sqrt(img221[i][j]**2+img212[i][j]**2)

g3=np.array(g3,dtype='uint8')
cv2.imshow('im3',g3)
#COMBINE IMAGE LL(4)
g4=np.zeros(img121.shape)
for i in xrange(0,img121.shape[0]):
    for j in xrange(0,img121.shape[0]):
        g4[i][j]=np.sqrt(img121[i][j]**2+img112[i][j]**2)

g4=np.array(g4,dtype='uint8')
cv2.imshow('im4',g4)
g1=np.array(g1,dtype='f')
g2=np.array(g2,dtype='f')
g3=np.array(g3,dtype='f')
g4=np.array(g4,dtype='f')
g40=g4
g41=(cv2.resize(g3,(g4.shape)))*g4
g31=(cv2.resize(g2,(g3.shape)))*g3
g42=(cv2.resize(g31,(g4.shape)))*g4
g21=(cv2.resize(g1,(g2.shape)))*g2
g32=(cv2.resize(g21,(g3.shape)))*g3
g43=(cv2.resize(g32,(g4.shape)))*g4
g90=g40/np.max(g40)
g91=g41/np.max(g41)
g92=g42/np.max(g42)
g93=g43/np.max(g43)
#g90=level1,g91=level2,g92=level3,g93=level4,

for i in xrange(0,g41.shape[0]-1):
    for j in xrange(0,g41.shape[0]-1):
        if g92[i][j]<0.038:
            g92[i][j]=0
        if g92[i][j]>0.038:
            g92[i][j]=255


g41=g41*255/g41.max()
g18=cv2.resize(g3,(g4.shape))
 
edge=g4.copy()
edge[:,:]=g41

cv2.imshow('edge2',g91)
cv2.imshow('edge4',g93)
cv2.imshow('edge3',g92)
cv2.imshow('edge1',g90)
cv2.waitKey(0)
cv2.destroyAllWindows()
