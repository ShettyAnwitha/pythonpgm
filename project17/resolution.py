from PIL import Image
image = "E:/nature.jpg"
img = Image.open(image)
width, height = img.size
print("The image resolution  is", width, "x", height)
