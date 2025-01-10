import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread('image for lab.jpg', cv2.IMREAD_GRAYSCALE)

# Apply the Laplacian filter for point detection
laplacian = cv2.Laplacian(image, cv2.CV_64F)


# Show the original and Laplacian images
plt.figure(figsize=(12,7))
plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image'),plt.axis('off')
# Show the Point Detection
plt.subplot(1, 2, 2), plt.imshow(np.abs(laplacian), cmap='gray'), plt.title('Point Detection (Laplacian)'),plt.axis('off')
plt.show()
