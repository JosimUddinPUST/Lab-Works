import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = Image.open('lab_image.jpg').convert('RGB')

image_array=np.array(image)

# Define the gamma value
gamma = 1.9

# Apply power-law (gamma) transformation
c = 255 / (np.max(image_array) ** gamma)  # Calculate scaling constant
power_image = c * (image_array ** gamma)   # Apply the transformation

# Convert to uint8 for display
power_image = np.array(power_image, dtype=np.uint8)

log_c=255/(np.log(1+np.max(image_array)))

log_image= log_c* (np.log(1+ image_array))

log_image=np.array(log_image,dtype=np.uint8)

plt.figure(figsize=(12,6))
plt.subplot(1,3,1)
plt.imshow(image,cmap="gray")
plt.title("original Image")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(power_image,cmap="gray")
plt.title(f"Power Image Gamma= ({gamma})")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(log_image,cmap="gray")
plt.title("Log Image ")
plt.axis("off")

plt.show()
