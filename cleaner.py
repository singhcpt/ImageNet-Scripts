import os
from PIL import Image
    
#Function to check whether image is corrupted
def imgCheck(fp):
    try:
        Image.open(fp)
        return True
    except:
        return False

for filename in os.listdir("/path/to/file"):
    filepath = "/path/to/file/" + filename
    # Removing images that are corrupted
    if not imgCheck(filepath):
        try: 
            os.remove(filepath)
            print("Removed " + filename)
        except OSError:
            print("Could not delete " + filename)
    # Removing images with X and white background - removes based on the size of the file (all of these files have less than 3000 bytes)
    if os.stat(filepath).st_size < 3000:
        try: 
            os.remove(filepath)
            print("Removed " + filename)
        except OSError:
            print("Could not delete " + filename)


    