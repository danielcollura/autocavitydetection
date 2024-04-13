import json

# Define the paths to the source and destination JSON files
source_json_path = '/Users/danielcollura/Desktop/updateddataset/Labelled Dataset/labels/filtered_annotations.json'
destination_json_path = '/Users/danielcollura/Desktop/updateddataset/UofT Dataset/label/coco_annotations.json'

# Load the source JSON data
with open(source_json_path, 'r') as file:
    source_data = json.load(file)

# Load the destination JSON data
with open(destination_json_path, 'r') as file:
    destination_data = json.load(file)

# Extend the "images", "annotations", "categories", "info", and "licenses" lists in the destination data
destination_data['images'].extend(source_data['images'])
destination_data['annotations'].extend(source_data['annotations'])
destination_data['categories'].extend(source_data['categories'])
destination_data['info'].update(source_data['info'])
destination_data['licenses'].extend(source_data['licenses'])

# Save the merged JSON data back to the destination file
with open(destination_json_path, 'w') as file:
    json.dump(destination_data, file, indent=4)

print("The JSON files have been merged successfully.")
