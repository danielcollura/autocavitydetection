import json

# Load the JSON data
json_path = '/path/to/your/json/file.json'
with open(json_path, 'r') as file:
    data = json.load(file)

# Create a mapping from file names to new image IDs
file_name_to_id = {image['file_name']: image['id'] for image in data['images']}

# Update the image IDs in the annotations
for annotation in data['annotations']:
    # Find the new image ID using the file name
    file_name = f"cIMG{str(annotation['image_id']).zfill(5)}.png"
    if file_name in file_name_to_id:
        # Update the image_id in the annotation to the new image ID
        annotation['image_id'] = file_name_to_id[file_name]

# Save the updated JSON data
with open(json_path, 'w') as file:
    json.dump(data, file, indent=4)

print("The JSON file has been updated with the correct image IDs.")
