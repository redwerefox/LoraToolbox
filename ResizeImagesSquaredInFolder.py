
from PIL import Image
import os

RESOLUTION = 1024
GENERATED_FILE_SUFFIX = "_resized.png"

def clip_image_center_square(image_path):
    image = Image.open(image_path)
    width, height = image.size

    if width == height:
        return image
    elif width > height:
        left = (width - height) / 2
        top = 0
        right = left + height
        bottom = height
    else:
        left = 0
        top = (height - width) / 2
        right = width
        bottom = top + width

    return image.crop((left, top, right, bottom))
        

def resize_image(image_path, RESOLUTION):
    
    imageCropped = clip_image_center_square(image_path)

    image = imageCropped.resize((RESOLUTION, RESOLUTION))
    
    image_path = os.path.splitext(image_path)[0] + "_resized.png"

    image.save(image_path, "PNG")


def runOperationOnImagesInFolder (folder_path):
    
    with os.scandir(folder_path) as entries:
        return [resize_image(entry, RESOLUTION) for entry in entries
                          if entry.is_file()
                            and (entry.name.endswith(".png")
                                  or entry.name.endswith(".jpg")) 
                                  and not entry.name.endswith(GENERATED_FILE_SUFFIX)]

def getArgumentFolderPath ():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python ResizeImage.py <folder_path>")
        sys.exit(1)
    return sys.argv[1]

def main():
    folder_path = getArgumentFolderPath()
    runOperationOnImagesInFolder(folder_path)

if __name__ == "__main__":
    main()

# Usage: python ResizeImage.py <folder_path>
