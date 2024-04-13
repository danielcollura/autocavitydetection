import json
import os

def convert_coco_bbox_to_yolo(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = box[0] + box[2] / 2.0
    y = box[1] + box[3] / 2.0
    w = box[2]
    h = box[3]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x,y,w,h)

def convert_annotations(coco_path, image_dirs, label_dir_base):
    with open(coco_path, 'r') as f:
        data = json.load(f)
    
    category_id_to_index = {category['id']: idx for idx, category in enumerate(data['categories'])}
    
    # Assuming the structure of your directories follows the naming convention you provided
    for image_dir in image_dirs:
        set_name = os.path.basename(image_dir)  # e.g., 'train', 'val', 'test'
        label_dir = os.path.join(label_dir_base, set_name)
        if not os.path.exists(label_dir):
            os.makedirs(label_dir)
        
        for image in data['images']:
            image_id = image['id']
            file_name = image['file_name']
            # Assuming your images are PNGs, if they're another format, adjust the extension as necessary
            if not os.path.exists(os.path.join(image_dir, file_name)):
                continue  # Skip images that don't exist in the current set
            width, height = image['width'], image['height']
            
            label_file = os.path.join(label_dir, file_name.replace('.png', '.txt'))
            with open(label_file, 'w') as lbl:
                for annotation in data['annotations']:
                    if annotation['image_id'] == image_id:
                        category_id = annotation['category_id']
                        bbox = annotation['bbox']
                        yolo_bbox = convert_coco_bbox_to_yolo((width, height), bbox)
                        lbl.write(f"{category_id_to_index[category_id]} {' '.join(map(str, yolo_bbox))}\n")

# Define paths
coco_path = '/Users/danielcollura/Downloads/Dental caries in bitewing radiographs/dental_rtg_test/labels/test_annotations_filtered.json'
image_dirs = [
    '/Users/danielcollura/Downloads/Dental caries in bitewing radiographs/dental_rtg_test/image/val',
    '/Users/danielcollura/Downloads/Dental caries in bitewing radiographs/dental_rtg_test/image/test',
    '/Users/danielcollura/Downloads/Dental caries in bitewing radiographs/dental_rtg_test/image/train'
]
label_dir_base = '/Users/danielcollura/Downloads/Dental caries in bitewing radiographs/dental_rtg_test/labels'

convert_annotations(coco_path, image_dirs, label_dir_base)
