import cv2
import json
import os
from tqdm import tqdm

# Define paths
json_path = '/Users/danielcollura/Desktop/cavity_dataset/nonaugdataset/label/unaugmentedlabels.json'
images_base_dir = '/Users/danielcollura/Desktop/cavity_dataset/nonaugdataset/images'

# Load the JSON data
with open(json_path, 'r') as file:
    data = json.load(file)

def resize_image_and_bbox(image_path, annotations):
    target_size = 640
    image = cv2.imread(image_path)
    if image is None:
        print(f"Warning: Could not load image at {image_path}. Check if the file exists.")
        return None, None

    h, w = image.shape[:2]
    scale = target_size / max(h, w)
    nh, nw = int(h * scale), int(w * scale)

    image_resized = cv2.resize(image, (nw, nh))
    top_pad = (target_size - nh) // 2
    bottom_pad = target_size - nh - top_pad
    left_pad = (target_size - nw) // 2
    right_pad = target_size - nw - left_pad

    image_padded = cv2.copyMakeBorder(image_resized, top_pad, bottom_pad, left_pad, right_pad, cv2.BORDER_CONSTANT, value=[0, 0, 0])

    cv2.imwrite(image_path, image_padded)

    # Update bounding box coordinates
    for annotation in annotations:
        x_min, y_min, width, height = annotation['bbox']
        x_min = int(x_min * scale) + left_pad
        y_min = int(y_min * scale) + top_pad
        width = int(width * scale)
        height = int(height * scale)
        annotation['bbox'] = [x_min, y_min, width, height]

    return nh, nw

# Process images and update JSON
for root, _, files in tqdm(os.walk(images_base_dir), desc="Resizing images"):
    for file in files:
        if file.endswith(('.jpg', '.jpeg', '.png', '.bmp')):  # Add more formats if needed
            img_path = os.path.join(root, file)
            image_annotations = [ann for ann in data['annotations'] if ann['image_id'] == os.path.splitext(file)[0]]
            new_height, new_width = resize_image_and_bbox(img_path, image_annotations)
            if new_height is not None and new_width is not None:
                for img in data.get('images', []):
                    if 'file_name' in img and img['file_name'] == file:
                        img['width'] = new_width
                        img['height'] = new_height
                        break

# Save updated JSON data
with open(json_path, 'w') as outfile:
    json.dump(data, outfile, indent=4)

print("All images have been resized, and the JSON file updated.")
