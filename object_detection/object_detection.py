import matplotlib.pyplot as plt
from torchvision.io import read_image

# Loading images
image = read_image('data/PennFudanPed/PNGImages/FudanPed00046.png')
mask = read_image('data/PennFudanPed/PedMasks/FudanPed00046_mask.png')

# Drawing the plot
plt.figure(figsize=(16, 8))

# Drawing the image into first plot
plt.subplot(121)
plt.title('Image')
plt.imshow(image.permute(1, 2, 0))

# Drawing the mask into second plot
plt.subplot(122)
plt.title('Image')
plt.imshow(mask.permute(1, 2, 0))

plt.show()