import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread('lab_image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian Blur to reduce noise
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Apply Canny Edge Detection
edges = cv2.Canny(blurred_image, 100, 200)

# Show the original and Laplacian images
plt.figure(figsize=(12,6))
plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image'),plt.axis('off')

# Show the original and edge-detected images
plt.subplot(1, 2, 2), plt.imshow(edges, cmap='gray'), plt.title('Edge Detection (Canny)'),plt.axis('off')
plt.show()
