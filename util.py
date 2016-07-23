# -*- coding: cp936 -*-
import cv2
import pywt
import numpy as np
import sys


def edge_detect_paper(coeff,show=True):
    #提取  multistage coeff
    multi_ll=[ i[0]  for i in coeff]
    LH=[ i[1][0] for i in coeff]
    HL=[ i[1][1] for i in coeff]
    HH=[ i[1][2] for i in coeff]

    x,y=multistage_merge_paper(LH ,HL)

    x[np.where(x<0)]=0
    y[np.where(y<0)]=0

    x[np.where(x<np.mean(x))]=0
    y[np.where(y<np.mean(y))]=0

    h=np.sqrt(x+y)
    h=h/np.max(h)
    if show==True:
        cv2.imshow('edge_map', h)
        cv2.waitKey(0)
    return h
   
        

def multistage_merge_paper(HL,LH):
    '''
        mat:存放各stage 除LL外的系数，按照尺寸降序排列
    '''
    
    #翻转为升序排列
    HL=HL[::-1]
    LH=LH[::-1]
    
    
    p_current_x=HL[0]
    p_current_y=LH[0]
    for i in xrange(1,len(LH)):
        
        p_next_x=HL[i]
        p_next_y=LH[i]
        
        # 确保小尺寸的系数排列在前
        if p_current_x.shape[0]>p_next_x.shape[0]:
            print 'multistage should rand in ascending order'
            sys.exit()
            
        size=p_next_x.shape

        # resize 将小尺寸resize到大尺寸
        p_current_x=cv2.resize(p_current_x,(size[1],size[0]))
        p_current_y=cv2.resize(p_current_y,(size[1],size[0]))
        
        # cross stage multiply
        p_current_x=p_current_x*p_next_x
        p_current_y=p_current_y*p_next_y

    return p_current_x,p_current_y

def img_initial(img_path,gray=True,size=(512,512)):
    img=cv2.imread(img_path)
    gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    gray=cv2.resize(gray,size)
    return gray

def add_noise(img,noise_type='gauss',mean=20,var=0.1,percent=0.001):
    '''
        var:控制高斯噪声的方差
        percent:控制pluse噪声占整张图的比例（像素比例）
    '''
    row,col= img.shape
    if noise_type == "gauss":
        mean = mean
        var =var
        sigma = var**0.5
        gauss = np.random.normal(mean,var,(row,col))
        gauss = gauss.reshape(row,col)
        noisy = img + gauss
        return noisy
    
    elif noise_type == "pluse":

        num_salt=np.ceil(percent * img.size)
        out = img
        # Salt mode
        coords = [np.random.randint(0, i - 1, int(num_salt)) for i in img.shape]
        out[coords] = 255
        return out
    else:
        print 'no noise effect '
    



def wave_trans(img,wave_type='haar',level=4):
    
    '''
        逐层提取LL，并利用LL再次进行小波分解
    '''
    
    coeff=[]
    TIME=0
    while TIME<level:
        
        if TIME==0:
            LL=img
        else :
            LL=temp_coeff[0]

        # temp_coeff=[LL,(LH,HL,HH)]
        temp_coeff=pywt.dwt2(LL, wavelet ='haar')
        coeff.append(temp_coeff)
        TIME+=1
    return coeff




def visualize_stage(stage,level=4):
    stage=stage[level-1]
    ll=stage[0]
    lh,hl,hh=stage[1]
    
    ll=ll/np.max(ll)
    lh=lh/np.max(lh)
    hl=hl/np.max(hl)
    hh=hh/np.max(hh)
    cv2.imshow('stage %d' % level ,np.vstack((np.hstack((ll,lh)),\
                                              np.hstack((hl,hh)))))
    
    cv2.waitKey(0)
    
def show_noise_img(img,noise_img):

    noise_img
    noise_img=noise_img/np.max(noise_img)
    img=img*1.0/np.max(img)
    cv2.imshow('noise', np.hstack((img,noise_img)))
    cv2.waitKey(0)

    
