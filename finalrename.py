import json
import os

# Define the paths to your image directory and JSON file
images_dir = '/Users/danielcollura/Desktop/updateddataset/Labelled Dataset/images'
json_path = '/Users/danielcollura/Desktop/updateddataset/Labelled Dataset/labels/filtered_annotations.json'

# Load the JSON data
with open(json_path, 'r') as file:
    data = json.load(file)

# Assume images are renamed and sorted; now match the JSON data to the new names
# Starting IDs
start_image_id = 146  # Starting point for image IDs
current_annotation_id = 5105  # Starting point for annotation IDs

# Update the image IDs in the JSON data
for img in data['images']:
    img_id_int = int(img['file_name'].rstrip('.png'))  # Assuming file_name is like "1.png"
    new_img_id = start_image_id + img_id_int - 1  # Adjust to start from 146
    img['id'] = new_img_id
    # Update file_name to match the new naming convention
    img['file_name'] = f"cIMG{new_img_id:05d}.png"

# Update the annotation IDs and their corresponding image_id references
for ann in data['annotations']:
    # Find the matching image to get its new ID
    matching_img = next((img for img in data['images'] if img['id'] == ann['image_id']), None)
    if matching_img:
        ann['image_id'] = matching_img['id']  # Update to the new image ID
    ann['id'] = current_annotation_id  # Assign new annotation ID
    current_annotation_id += 1  # Increment for the next annotation

# Save the updated JSON data back to the file
with open(json_path, 'w') as file:
    json.dump(data, file, indent=4)

print("The JSON file has been updated to reflect the new image naming and ID conventions.")
