import numpy as np
import cv2
import matplotlib.pyplot as plt

def low_pass_filter(img, kernel_size=5, sigma=1.0):
    """
    Apply Gaussian Low-pass filter to the image using cv2.GaussianBlur.
    
    Args:
    - img: Input image.
    - kernel_size: Size of the Gaussian kernel.
    - sigma: Standard deviation for Gaussian kernel.
    
    Returns:
    - Low-pass filtered image.
    """

    # Apply Gaussian Blur to smooth the image
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), sigma)

def high_pass_filter(img, kernel_size=5, sigma=1.0):
    """
    Apply High-pass filter by subtracting the Low-pass filtered image from the original image.
    
    Args:
    - img: Input image.
    - kernel_size: Size of the Gaussian kernel.
    - sigma: Standard deviation for Gaussian kernel.
    
    Returns:
    - High-pass filtered image.
    """
    low_pass = low_pass_filter(img, kernel_size, sigma)
    high_pass = img - low_pass  # High-pass filter by subtracting low-pass from original
    return high_pass

# Load image
img = cv2.imread('lab_image.jpg', cv2.IMREAD_GRAYSCALE)  # Load as grayscale
# Apply low-pass filter
low_pass_img = low_pass_filter(img, kernel_size=7, sigma=1.5)

# Apply high-pass filter
high_pass_img = high_pass_filter(img, kernel_size=7, sigma=1.5)

# Display images
plt.figure(figsize=(12, 6))

# Original Image
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

# Low-pass Filtered Image
plt.subplot(1, 3, 2)
plt.imshow(low_pass_img, cmap='gray')
plt.title("Low-pass Filtered Image")
plt.axis('off')

# High-pass Filtered Image
plt.subplot(1, 3, 3)
plt.imshow(high_pass_img, cmap='gray')
plt.title("High-pass Filtered Image")
plt.axis('off')

plt.show()
