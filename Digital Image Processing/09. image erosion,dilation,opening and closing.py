import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the original color image
color_image = cv2.imread('lab_image.jpg')

# Convert the color image to grayscale
image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)

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
plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.title("Original Color Image")
plt.imshow(cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(2, 3, 2)
plt.title("Grayscale Image")
plt.imshow(image, cmap='gray')
plt.axis("off")

plt.subplot(2, 3, 3)
plt.title("Eroded Image")
plt.imshow(eroded_image, cmap='gray')
plt.axis("off")

plt.subplot(2, 3, 4)
plt.title("Dilated Image")
plt.imshow(dilated_image, cmap='gray')
plt.axis("off")

plt.subplot(2, 3, 5)
plt.title("Opened Image")
plt.imshow(opened_image, cmap='gray')
plt.axis("off")

plt.subplot(2, 3, 6)
plt.title("Closed Image")
plt.imshow(closed_image, cmap='gray')
plt.axis("off")

plt.show()