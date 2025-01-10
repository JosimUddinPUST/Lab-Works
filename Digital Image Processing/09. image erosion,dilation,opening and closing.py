import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load a binary image
image = cv2.imread('lab_image.jpg', 0)  # 0 to load as grayscale

# Define a 5x5 structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Apply dilation
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Apply opening (erosion followed by dilation)
opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Apply closing (dilation followed by erosion)
closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Display the results
plt.figure(figsize=(12, 8))
plt.subplot(2, 3, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image'),plt.axis('off')
plt.subplot(2, 3, 2), plt.imshow(eroded_image, cmap='gray'), plt.title('Eroded Image'),plt.axis('off')
plt.subplot(2, 3, 3), plt.imshow(dilated_image, cmap='gray'), plt.title('Dilated Image'),plt.axis('off')
plt.subplot(2, 3, 5), plt.imshow(opened_image, cmap='gray'), plt.title('Opened Image'),plt.axis('off')
plt.subplot(2, 3, 6), plt.imshow(closed_image, cmap='gray'), plt.title('Closed Image'),plt.axis('off')
plt.show()
