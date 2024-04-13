import json

def rename_id_to_image_id(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    if 'images' in data:
        for entry in data['images']:
            if 'id' in entry:
                entry['image_id'] = entry.pop('id')

    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Provide the path to your JSON file here
json_file_path = "/Users/danielcollura/Desktop/cavity_dataset/nonaugdatasetfinal/labels/label.json"
rename_id_to_image_id(json_file_path)
