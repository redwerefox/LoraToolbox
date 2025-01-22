
from PIL import Image
import os


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
        

def resize_image(image_path, X_RESOLUTION, Y_RESOLUTION):
    
    imageCropped = clip_image_center_square(image_path)

    image = imageCropped.resize((X_RESOLUTION, Y_RESOLUTION))

    # Save as png
    # ensure format
    
    image_path = os.path.splitext(image_path)[0] + "_resized.png"

    image.save(image_path, "PNG")


def runOperationOnImagesInFolder (folder_path):
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            resize_image(folder_path + filename, 256, 256)
        else:
            continue

    print("All images in folder resized")

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
