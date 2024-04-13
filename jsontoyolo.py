import json
import os

def convert_to_yolo(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    yolo_annotations = []
    for annotation in data['annotations']:
        image_id = annotation['image_id']
        image_data = next((img for img in data['images'] if img['id'] == image_id), None)
        if image_data:
            image_path = image_data['file_path']
            image_width = image_data['width']
            image_height = image_data['height']
            
            bbox = annotation['bbox']
            x_center = bbox[0] + bbox[2] / 2
            y_center = bbox[1] + bbox[3] / 2
            normalized_width = bbox[2] / image_width
            normalized_height = bbox[3] / image_height
            
            yolo_annotation = {
                'image_path': image_path,
                'annotations': [{
                    'class_id': 0,  # Class ID for "cavity"
                    'x_center': x_center / image_width,
                    'y_center': y_center / image_height,
                    'width': normalized_width,
                    'height': normalized_height
                }]
            }
            
            yolo_annotations.append(yolo_annotation)
    
    return yolo_annotations

# Convert JSON to YOLO format
json_file = '/Users/danielcollura/Desktop/updateddataset/dataset/labels/label.json'
yolo_annotations = convert_to_yolo(json_file)

# Save YOLO annotations to a file in the same directory as the input JSON file
output_file = os.path.join(os.path.dirname(json_file), 'yolo_annotations.json')
with open(output_file, 'w') as f:
    json.dump(yolo_annotations, f, indent=4)
