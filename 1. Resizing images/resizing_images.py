from PIL import Image
import os

i = 0
data_dir = "0. Data samples"

# Resizing all our images from the dataset to (256x256) pixels

for filename in os.listdir(data_dir):
    image = Image.open(f"./{data_dir}/{filename}")
    resized_image = image.resize((256,256))
    resized_image.save(f"1. Resizing images/resized/test{i}.jpg")
    i += 1