from PIL import Image

from PIL import Image

def convertImage():
	img = Image.open("./generated_image.png")
	img = img.convert("RGBA")

	datas = img.getdata()

	newData = []

	for item in datas:
		if item[0] == 0 and item[1] == 0 and item[2] == 0:
			newData.append((255, 255, 255, 0))
		else:
			newData.append(item)

	img.putdata(newData)
	img.save("./768-200x300.png", "PNG")
	print("Successful")

convertImage()
