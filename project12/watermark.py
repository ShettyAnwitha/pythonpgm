from PIL import Image,ImageDraw,ImageFont

img = Image.open(r'E:/python.jpg')
width, height = img.size

draw = ImageDraw.Draw(img)
text = "www.FunWithPython"

font = ImageFont.truetype('E:/B20Sans.ttf',80)
textwidth, textheight = draw.textsize(text,font)

margin = 10
x = width - textwidth - margin
y = height - textheight - margin

draw.text((x,y), text, font=font)
img.show()
img.save(r'E:/watermark.jpg')
