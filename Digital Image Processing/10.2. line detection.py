import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image in grayscale
image = cv2.imread('line detection.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError("Image file not found. Please check the file path.")

# Use Canny to detect edges
edges = cv2.Canny(image, 50, 150, apertureSize=3)

# Use Probabilistic Hough Transform to detect line segments
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=150, minLineLength=100, maxLineGap=20)

# Convert grayscale to color for colored lines
image_with_lines = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# Draw lines on the image
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image_with_lines, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Red color

# Display images
plt.subplot(1, 2, 1),plt.imshow(image, cmap='gray'),plt.title('Original Image'),plt.axis('off')

plt.subplot(1, 2, 2),plt.imshow(cv2.cvtColor(image_with_lines, cv2.COLOR_BGR2RGB)),plt.title('Line Detection (Probabilistic Hough Transform)'),plt.axis('off')

plt.show()
