import cv2
import numpy as np
import matplotlib.pyplot as plt

A=cv2.imread('lab_image.jpg')

h,w,_=A.shape

tl=A[0:h//2,0:w//2]
tr=A[0:h//2,w//2:w]
bl=A[h//2:h,0:w//2]
br=A[h//2:h,w//2:w]

# t=np.concatenate((tl,tr),axis=1)
# b=np.concatenate((bl,br),axis=1)
# I=np.concatenate((t,b),axis=0)

l=np.concatenate((tl,bl),axis=0)
r=np.concatenate((tr,br),axis=0)
I=np.concatenate((l,r),axis=1)

plt.figure(figsize=(12,9))

plt.subplot(2,3,1)
plt.imshow(cv2.cvtColor(tl,cv2.COLOR_BGR2RGB))
plt.title('Top Left')
plt.axis('off')

plt.subplot(2,3,2)
plt.imshow(cv2.cvtColor(tr,cv2.COLOR_BGR2RGB))
plt.title('Top Right')
plt.axis('off')

plt.subplot(2,3,3)
plt.imshow(cv2.cvtColor(I,cv2.COLOR_BGR2RGB))
plt.title('Merged')
plt.axis('off')

plt.subplot(2,3,4)
plt.imshow(cv2.cvtColor(bl,cv2.COLOR_BGR2RGB))
plt.title('Bottom Left')
plt.axis('off')

plt.subplot(2,3,5)
plt.imshow(cv2.cvtColor(br,cv2.COLOR_BGR2RGB))
plt.title('Bottom Right')
plt.axis('off')

plt.show()
