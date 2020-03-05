import os
from PIL import Image

def compress():
    for image in os.listdir(r"input"):
        path = r"input" + os.sep + image
        Openedimage = Image.open(path)
        print(Openedimage.size, end=" ")

        out_path = r"output" + os.sep + "image_" + image.replace("-", "_")
        Openedimage.save(out_path, optimize=True, quality=1)
        Openedimage = Image.open(out_path)
        print(Openedimage.size)


if __name__ == '__main__':
    compress()
