import json
import os

# Updated path to your JSON file containing annotations
json_file_path = "/Users/danielcollura/Desktop/trainval/coco_annotations.json"

# Path to the directory containing your images (assuming it hasn't changed)
image_dir_path = "/Users/danielcollura/Desktop/trainval"

# Load JSON file
with open(json_file_path, 'r') as f:
    data = json.load(f)

# Add image paths to JSON data
for item in data['images']:
    file_name = item['file_name']
    item['file_path'] = os.path.join(image_dir_path, file_name)

# Save updated JSON file
with open(json_file_path, 'w') as f:
    json.dump(data, f, indent=4)

print("Image paths added to JSON file successfully.")
