from PIL import Image,ImageDraw,ImageFont

img = Image.open(r'project12:/python.jpg')
width, height = img.size

draw = ImageDraw.Draw(img)
text = "www.FunWithPython"

font = ImageFont.truetype('project12:/B20Sans.ttf',80)
textwidth, textheight = draw.textsize(text,font)

margin = 10
x = width - textwidth - margin
y = height - textheight - margin

draw.text((x,y), text, font=font)
img.show()
img.save(r'project12:/watermark.jpg')
