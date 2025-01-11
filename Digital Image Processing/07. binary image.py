import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image using OpenCV and convert it to grayscale
image = cv2.imread('lab_image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply a binary threshold manually to convert the image to binary
threshold = 128
binary_image = np.where(image > threshold, 255, 0).astype(np.uint8)

# Plot the original grayscale image and the binary image
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Grayscale Image")
plt.imshow(image, cmap='gray')
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Binary Image")
plt.imshow(binary_image, cmap='gray')
plt.axis("off")

plt.show()