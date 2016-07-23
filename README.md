# image-edge-detection
This project is mainly to detect the edge of image using Wavelet Transform

first, use add noise.py to input noise, in add noise file, we input the image with function cv2.imread, fill the name of image in it. it will generate 2 image with impluse noise and gaussian noise. 
with the function imwrite, it will generate 2 new image for next step.
second, use wavelet edge file, with name in imread, just fill in the name, guass.jpg and impluse.jpg, it will generate different results for differnet levels.
for results, in all gauss results,use # to  delete the threshold in (wavelet edge.py), edge2 is the results, in all impluse results, edge3 is the results

failed filter.py is just the failed code for filter.
