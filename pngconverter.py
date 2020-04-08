'''
PNG Converter
Convert any image type to a .PNG file type by providing the folder where the images are already stored
and a new folder name to where the converted files should be saved/outputed to.
'''

import os
import sys
from PIL import Image

image_folder = sys.argv[1]
output_folder = sys.argv[2]

# This will create a new folder depending on the name of the second argument given in the command line.
# If one already exists it will skip over this if statement.
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    # Opens every image inside the folder that was given as an agrument in the command line
    img = Image.open(f'{image_folder}{filename}')
    # This will remove the .jpg from the image so it can then save it as a .png.
    clean_name = os.path.splitext(filename)[0]
    # Saves the file in the output folder that was provided with the new clean_name of the file
    # followed by .png and also converts the file to an actual PNG file.
    img.save(f'{output_folder}{clean_name}.png', 'PNG')
    # Will print 'all done' for each and every single image that is then changed to a PNG file.
    print('all done')
