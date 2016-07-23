# -*- coding: cp936 -*-
from util import *

img=img_initial("lena_gray.png",size=(512,512))
noise_img=add_noise(img,noise_type='gauss',mean=5,var=5,percent=0.00001)


# 多层小波变换  bior1.1     haar
coeff=wave_trans(img,wave_type='haar',level=4)


# 显示原图 VS 噪声图
show_noise_img(img,noise_img)
# 显示各层 4通道图
visualize_stage(coeff,level=1)

# multi stage multiply
h=edge_detect_paper(coeff,show=True)

