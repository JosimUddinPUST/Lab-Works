import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization(image):
    flat_image = image.flatten()
    histogram = np.zeros(256) 
    for pixel in flat_image:
        histogram[pixel] += 1
    
    cdf = np.cumsum(histogram) 
    
    #dividing CDF by the total number of pixels
    cdf_normalized = cdf * 255 / cdf[-1] 

    equalized_image = np.interp(flat_image, np.arange(0, 256), cdf_normalized)
    
    # Reshape to original shape
    equalized_image = equalized_image.reshape(image.shape).astype(np.uint8)
    
    return equalized_image

image = cv2.imread('lab_image.jpg', cv2.IMREAD_GRAYSCALE)
equalized_image = histogram_equalization(image)

plt.figure(figsize=(10, 5)),plt.subplot(1, 2, 1),plt.title("Original Image"),plt.imshow(image, cmap='gray'),plt.axis('off')

plt.subplot(1, 2, 2),plt.title("Equalized Image"),plt.imshow(equalized_image, cmap='gray'),plt.axis('off')

plt.show()