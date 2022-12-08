from PIL import Image
import requests
import io

s = str(input("please input filename and extension.(file.txt)"))

images = []
img = []

with open(s, 'r') as f:
    # Loop through the list of image URLs and request each one
    for line in f:
        images.append(line.strip())
f.close()

for url in images:
    response = requests.get(url)
    image_data = response.content
    # Create an image from the binary data
    dataBytesIO = io.BytesIO(image_data)
    image = Image.open(dataBytesIO)
    # Append the image to the list
    img.append(image)

# Save the images as a GIF
img[0].save('my_gif.gif',
               save_all=True,
               append_images=img[1:],
               optimize=False,
               duration=600,
               loop=0)