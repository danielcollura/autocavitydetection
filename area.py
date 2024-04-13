import json

def fix_bounding_box_areas(json_file_path):
    # Load the JSON annotations
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    # Iterate over all annotations
    for annotation in data['annotations']:
        # The bbox is in the form [x_min, y_min, width, height]
        bbox = annotation['bbox']
        width = bbox[2]
        height = bbox[3]
        
        # Calculate the area as width * height
        area = width * height
        
        # Update the area in the annotation
        annotation['area'] = area
    
    # Save the fixed JSON annotations
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Path to your JSON file
json_file_path = '/Users/danielcollura/Desktop/Dental Neural Net/UofT Dataset/coco_annotations.json'

# Fix the bounding box areas
fix_bounding_box_areas(json_file_path)
