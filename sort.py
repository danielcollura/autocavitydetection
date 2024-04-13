import json
import os
import shutil
from sklearn.model_selection import train_test_split

# Define paths
base_dir = '/Users/danielcollura/Desktop/cavity_dataset/nonaugdataset'
images_dir = os.path.join(base_dir, 'images')
labels_path = os.path.join(base_dir, 'labels', 'label.json')

# Define output directories for image subsets
train_dir = os.path.join(base_dir, 'train_images')
val_dir = os.path.join(base_dir, 'val_images')
test_dir = os.path.join(base_dir, 'test_images')

# Create directories if they don't exist
for directory in [train_dir, val_dir, test_dir]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Load label data
with open(labels_path, 'r') as f:
    labels_data = json.load(f)

# Get a list of all image IDs (including those without annotations)
all_images_ids = [img['id'] for img in labels_data['images'] if 'id' in img]

# Split image IDs for training, validation, and testing
train_ids, test_val_ids = train_test_split(all_images_ids, test_size=0.3, random_state=42)
val_ids, test_ids = train_test_split(test_val_ids, test_size=0.5, random_state=42)

# Function to update JSON annotations and move images
def update_json_move_images(image_ids, destination_dir):
    for img_id in image_ids:
        # Find the image entry
        img_entry = next((img for img in labels_data['images'] if img.get('id') == img_id), None)
        if img_entry:
            img_file_name = img_entry['file_name']
            src_path = os.path.join(images_dir, img_file_name)
            dst_path = os.path.join(destination_dir, img_file_name)

            # Move the image file if it exists
            if os.path.exists(src_path):
                shutil.move(src_path, dst_path)
            else:
                print(f"File {src_path} not found.")

# Manual intervention for missed images
missed_images = ['cIMG00210.png', 'cIMG00211.png']
missed_images_ids = [210, 211]  # Assuming the numeric part of the file name corresponds to the id.

# Determine the correct directory for each missed image
for img_name, img_id in zip(missed_images, missed_images_ids):
    if img_id in train_ids:
        target_dir = train_dir
    elif img_id in val_ids:
        target_dir = val_dir
    elif img_id in test_ids:
        target_dir = test_dir
    else:
        print(f"No target directory found for {img_name}.")
        continue

    src_path = os.path.join(images_dir, img_name)
    dst_path = os.path.join(target_dir, img_name)
    if os.path.exists(src_path):
        shutil.move(src_path, dst_path)
        print(f"Manually moved {img_name} to {target_dir}.")
    else:
        print(f"File {src_path} not found for manual move.")

# Proceed with the original moving logic for the rest of the images
update_json_move_images(train_ids, train_dir)
update_json_move_images(val_ids, val_dir)
update_json_move_images(test_ids, test_dir)

# Optionally update the JSON file here if needed, similar to update_json_move_images logic

print("Dataset has been split and images moved successfully.")
