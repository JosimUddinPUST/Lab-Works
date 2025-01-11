import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_array = cv2.imread('lab_image.jpg', cv2.IMREAD_GRAYSCALE)

height, width = image_array.shape[:2]  # Assuming it's a grayscale image

# Initialize histogram for 256 intensity levels
hist_manual = [0] * 256

# Manually compute the histogram
for i in range(height):
    for j in range(width):
        pixel_value = image_array[i, j]
        hist_manual[pixel_value] += 1

# Total number of pixels in the image
total_pixels = height * width

prob_hist = [0] * 256
for i in range(256):
    prob_hist[i] = hist_manual[i] / total_pixels

# Plot the original image and the manually computed probability histogram
plt.figure(figsize=(15, 5))

# Subplot for the original image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image_array, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

# Subplot for the probability histogram
plt.subplot(1, 2, 2)
plt.bar(range(256), prob_hist)
plt.xlim(0, 255)
plt.title('Manually Computed Probability Histogram of Pixel Intensities')

plt.show()