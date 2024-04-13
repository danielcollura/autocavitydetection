import json

def load_json(filename):
    """Load and return the JSON content from a file."""
    with open(filename, 'r') as file:
        return json.load(file)

def save_json(data, filename):
    """Save JSON data to a file, overwriting any existing content."""
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

json_path = '/Users/danielcollura/Desktop/updateddataset/Labelled Dataset/labels/filtered_annotations.json'
data = load_json(json_path)

# Generate a mapping from old 'image_id' (assumed based on file_name without extension) to new 'id'
image_id_mapping = {}
for img in data.get('images', []):
    if 'file_name' in img:
        file_name_without_extension = img['file_name'].replace('.png', '')
        if file_name_without_extension.isdigit():  # Ensure the file name contains digits
            image_id_mapping[file_name_without_extension] = img['id']

# Update 'image_id' in annotations using the mapping
for ann in data.get('annotations', []):
    original_image_id_str = str(ann['image_id'])
    if original_image_id_str in image_id_mapping:
        ann['image_id'] = image_id_mapping[original_image_id_str]

# Update 'id' for each annotation, starting at 5105
for i, ann in enumerate(data.get('annotations', []), start=5105):
    ann['id'] = i

save_json(data, json_path)
print("Updated JSON successfully with corrected image_ids and sequential annotation ids starting at 5105.")
