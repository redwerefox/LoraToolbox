
from PIL import Image
import os

SUFFIX = "_resized.png"

def endsOnSuffix (filename, suffix):
    return filename.endswith(suffix)

def remove_suffixes_from_dataset(folder_path):
    pngFilePaths = [entry.path for entry in os.scandir(folder_path) 
                   if entry.is_file() and entry.name.endswith(".png")]

    # (pngFilePaths, deleteFlag)
    deleteLookup = [ (pngFile, not endsOnSuffix(pngFile, SUFFIX)) for pngFile in pngFilePaths]

    for entry in deleteLookup:
        if entry[1] :
            os.remove(entry[0])
            print("deleted :" + entry[0])
        else:
            pngFilePaths.remove(entry[0])
    

    for entry in deleteLookup:
        # remove suffix from filenames
        os.rename(entry[0], entry[0][:-len(SUFFIX)] + ".png")
        print(entry[0])


def getArgumentFolderPath ():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python RemoveSuffixesFromDataset.py <folder_path>")
        sys.exit(1)
    return sys.argv[1]

def main():
    folder_path = getArgumentFolderPath()
    remove_suffixes_from_dataset(folder_path)

if __name__ == "__main__":
    main()

# The script takes a folder path as an argument and removes the suffix "_resized.png" from all PNG files in the folder.
#  Other png files without SUFFIX are deleted