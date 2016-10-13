import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

#Class for Creating Images out of the font file specified
class CreateImages(object):

    def __init__(self):
        self.fontName = "Arial.ttf"
    #Function Image from the String Font
    def imageFromFont(self, fontName):
        font = ImageFont.truetype("Arial.ttf", 14)
        img = Image.new("RGBA", (500, 250), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), "This is a test", (0, 0, 0), font=font)
        draw = ImageDraw.Draw(img)
        img.save("a_test.png")

