from matplotlib import pyplot as plt 
import cv2
# panggil dan konversi warna agar sesuai dengan Matplotlib 
ipin = cv2.imread('sawit.jpg') 
ipin =  cv2.cvtColor(ipin, cv2.COLOR_BGR2RGB) 
# panggil dan konversi warna agar sesuai dengan Matplotlib 
kumpulan_ipin = cv2.imread('zoom.jpg') 
kumpulan_ipin =  cv2.cvtColor(kumpulan_ipin, cv2.COLOR_BGR2RGB)  
plt.subplot(121),plt.imshow(ipin), plt.title('gambar') 
plt.subplot(122),plt.imshow(kumpulan_ipin), plt.title('gambarr') 
plt.show() 

import cv2
import numpy as np

img_rgb = cv2.imread('sawit.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('zoom.jpg',0)

w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

threshold = 0.15
loc = np.where(res >= threshold)
lspoint=[]
lspoint2=[]
count = 0 
for pt in zip(*loc[::-1]):
    if pt[0] not in lspoint and pt[1] not in lspoint2:
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
        for i in range(((pt[0])-9), ((pt[0])+9),1):
            lspoint.append(i)
        for k in range(((pt[1])-9), ((pt[1])+9),1):
            lspoint2.append(k)
            count+=1
    else:
        continue
print ("Jumlah objek ditemukan ", count)

cv2.imshow('Deteksi Objek', img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()