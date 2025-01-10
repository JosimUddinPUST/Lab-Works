from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

image = Image.open('lab_image.jpg').convert('RGB')

image_array=np.array(image)

negative_image_array= 255-image_array


negative_image=Image.fromarray(negative_image_array)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title("Original Image")
plt.imshow(image)
plt.axis("off")

plt.subplot(1,2,2)
plt.title("Negative Image")
plt.imshow(negative_image)
plt.axis("off")

plt.show()
