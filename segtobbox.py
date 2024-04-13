import os
import re

# Define the directory containing the images and masks
image_directory = '/Users/danielcollura/Desktop/DENTAL NEURAL NET/UoftTBBOX/Images'

# Get all the files in the directory
files = os.listdir(image_directory)

# Separate image and mask files
image_files = sorted([f for f in files if re.match(r'cIMG\d+\.png', f)], 
                     key=lambda x: int(re.findall(r'(\d+)', x)[0]))
mask_files = sorted([f for f in files if re.match(r'cIMG\d+_.*\.png', f)], 
                    key=lambda x: int(re.findall(r'(\d+)', x)[0]))

# Start renaming from 101 for the image files
new_index = 101

# Dictionary to keep track of new mask indices
mask_indices = {}

# Rename image files and create a mapping for their new names
for image_file in image_files:
    new_image_name = f"{new_index}.png"
    old_image_number = re.findall(r'(\d+)', image_file)[0]
    mask_indices[old_image_number] = {'image': new_index, 'mask_count': 0}
    
    # Rename the image file
    os.rename(
        os.path.join(image_directory, image_file),
        os.path.join(image_directory, new_image_name)
    )
    new_index += 1

# Rename mask files based on the new image indices
for mask_file in mask_files:
    old_image_number = re.findall(r'(\d+)', mask_file)[0]
    if old_image_number in mask_indices:
        mask_count = mask_indices[old_image_number]['mask_count'] + 1
        mask_indices[old_image_number]['mask_count'] = mask_count
        new_mask_name = f"{mask_indices[old_image_number]['image']}_{mask_count}.png"
        
        # Rename the mask file
        os.rename(
            os.path.join(image_directory, mask_file),
            os.path.join(image_directory, new_mask_name)
        )

print("Renaming complete.")
