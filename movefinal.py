import json
import shutil
import os

# Define paths
base_dir = '/Users/danielcollura/Desktop/cavity_dataset/nonaugdataset'
source_dir = os.path.join(base_dir, 'images')
train_dir = os.path.join(base_dir, 'train_images')
test_dir = os.path.join(base_dir, 'test_images')
labels_path = os.path.join(base_dir, 'labels', 'label.json')

# Define image information and destination directories
image_info = {
    'cIMG00210.png': {'id': 210, 'target_dir': test_dir},
    'cIMG00211.png': {'id': 211, 'target_dir': train_dir}
}

# Load the existing JSON data
with open(labels_path, 'r') as file:
    labels_data = json.load(file)

# Find the insertion index based on existing IDs
insertion_index = next((i for i, img in enumerate(labels_data['images']) if img.get('id') == 212), None)

if insertion_index is not None:
    for img_name, info in image_info.items():
        src_path = os.path.join(source_dir, img_name)
        dst_path = os.path.join(info['target_dir'], img_name)

        # Move the image
        if os.path.exists(src_path):
            shutil.move(src_path, dst_path)
            print(f"Moved {img_name} to {dst_path}")
        else:
            print(f"File {src_path} not found.")

        # Prepare the new image entry
        new_img_entry = {
            "file_name": img_name,
            "width": 1068,
            "height": 847,
            "id": info['id'],
            "date_captured": 0,
            "license": 0,
            "file_path": dst_path  # Optional: Only include if you track file paths in JSON
        }

        # Insert the new image entry into the JSON structure
        labels_data['images'].insert(insertion_index, new_img_entry)
        insertion_index += 1  # Increment the insertion index for the next insertion

    # Save the updated JSON data
    with open(labels_path, 'w') as file:
        json.dump(labels_data, file, indent=4)

    print("JSON file has been updated with new entries.")
else:
    print("Error: Could not find the position to insert new images.")
