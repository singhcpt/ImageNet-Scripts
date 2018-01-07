import urllib
import os

# Read URLs from file line by line from text file
txt = open("/path/to/file")
lines = txt.readlines()

# Incrememnt counter to generate unique file paths for each image
urlCount = 0
invalids = []                                                           

for line in lines:
    urlCount += 1
    try:
        path = "/path/to/file/imagename" + str(urlCount) + ".jpg"
        urllib.urlretrieve(line, path)
        print("Downloaded image " + str(urlCount) + "@" + path)
    except IOError:
        urlCount += 1
        print("Error at line " + str(urlCount))


