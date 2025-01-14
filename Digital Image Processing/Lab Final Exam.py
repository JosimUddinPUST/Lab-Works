import numpy as np
import matplotlib.pyplot as plt
import cv2 


A=cv2.imread('lab_image.jpg',cv2.IMREAD_GRAYSCALE)
image=cv2.imread('lab_image.jpg')
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
def histogram_calculation(A):
    h,w=A.shape[:2]
    total_pixels=h*w

    histogram=[0]*256
    prob_hist=[0]*256

    for i in range (h):
        for j in range (w):
            pixels=A[i,j]
            histogram[pixels]+=1
    
    for i in range(256):
        prob_hist[i]=(histogram[i]/total_pixels)

    return prob_hist


def histogram_equalization(A):
    flat_image = A.flatten()
    histogram = np.zeros(256) 
    for pixel in flat_image:
        histogram[pixel] += 1
    
    cdf = np.cumsum(histogram) 
    
    cdf_normalized = cdf * 255 / cdf[-1] 

    equalized_image = np.interp(flat_image, np.arange(0, 256), cdf_normalized)
    
    equalized_image = equalized_image.reshape(A.shape).astype(np.uint8)
    
    return equalized_image

histogram_of_A=histogram_calculation(A)
equalized_image=histogram_equalization(A)
histogram_of_equalized_image=histogram_calculation(equalized_image)

def low_pass_filter(A,kernel_size=5,sigma=1.0):
    return cv2.GaussianBlur(A,(kernel_size,kernel_size),sigma)

def high_pass_filter(A,kernel_size=5,sigma=1.0):
    low_pass_filter_image=low_pass_filter(A)
    high_pass_filter_image=A-low_pass_filter_image
    return high_pass_filter_image

low_pass_filtered_image=low_pass_filter(equalized_image,kernel_size=5,sigma=1.9)
high_pass_filtered_image=high_pass_filter(equalized_image,kernel_size=5,sigma=1.9)

hist_after_low_pass=histogram_calculation(low_pass_filtered_image)
hist_after_high_pass=histogram_calculation(high_pass_filtered_image)

boundary_extracted_image=cv2.dilate(A,kernel=np.ones((5,5)),iterations=1)

plt.figure(figsize=(12,10))

plt.subplot(2,4,1),plt.imshow(image,cmap='gray'),plt.title('Original Image'),plt.axis('off')
plt.subplot(2,4,2),plt.bar(range(256),histogram_of_A),plt.title('Histogram of A'),plt.xlim(0,255)
plt.subplot(2,4,3),plt.imshow(equalized_image,cmap='gray'),plt.title('Equalized Image'),plt.axis('off')
plt.subplot(2,4,4),plt.bar(range(256),histogram_of_equalized_image),plt.title('Histogram of Equalized A'),plt.xlim(0,255)
plt.subplot(2,4,5),plt.bar(range(256),hist_after_low_pass),plt.title('Histogram After Low Pass'),plt.xlim(0,255)
plt.subplot(2,4,6),plt.bar(range(256),hist_after_low_pass),plt.title('Histogram After High Pass'),plt.xlim(0,255)

plt.subplot(2,4,7),plt.imshow(boundary_extracted_image,cmap='gray'),plt.title('Boundary Extracted Image'),plt.axis('off')

plt.subplots_adjust(hspace=0.5,wspace=.5)
plt.show()  



