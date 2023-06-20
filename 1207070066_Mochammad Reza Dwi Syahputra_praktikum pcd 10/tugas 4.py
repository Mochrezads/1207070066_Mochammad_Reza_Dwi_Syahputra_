# Menggunakan Shi-Tomasi GFTT untuk deteksi ujung (corner detection) 
 
import numpy as np  
import cv2 
from matplotlib import pyplot as plt 
 
# gunakan gambar  
img = cv2.imread('jkt.jpg') 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
 
# deteksi pojok dengan GFTT 
corners = cv2.goodFeaturesToTrack(gray,1000,0.01,10) 
corners = np.int0(corners) 
 
# menampilkan jumlah titik terdeteksi dengan fungsi numpy (np.ndarray.shape) 
print("jumlah titik terdeteksi = ", corners.shape[0]) 
 
# untuk ditampilkan di Matplotlib, urutan band dibalik 
rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) 
 
# perbesar ukuran hasil plotting  
plt.rcParams["figure.figsize"] = (10,10) 
 
# untuk tiap pojok yang terdeteksi, munculkan pada gambar 
for i in corners: 
    x,y = i.ravel() 
    cv2.circle(rgb,(x,y),3,255,-1) 
plt.imshow(rgb),plt.show()


#harris corner detector

import numpy as np
import cv2 as cv
filename = 'jkt.jpg'
img = cv.imread(filename)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
#result is dilated for marking the corners, not important
dst = cv.dilate(dst,None)
# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]
cv.imshow('dst',img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()