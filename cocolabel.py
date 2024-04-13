import cv2
import numpy as np
import json
import os

# Directory containing the images and mask images
image_directory = '/Users/danielcollura/Desktop/Dental Neural Net/Neural Net/UofT Dataset'
# The path where you want to save the COCO JSON file
coco_json_path = '/Users/danielcollura/Desktop/Dental Neural Net/Neural Net/UofT Dataset/coco_annotations.json'

# Initialize the COCO dataset structure
coco_dataset = {
    "info": {
        "description": "Dental Cavities Dataset",
        "version": "1.0",
        "year": 2024,
    },
    "licenses": [{"id": 0, "url": "", "name": ""}],
    "images": [],
    "annotations": [],
    "categories": [{"id": 1, "name": "cavity", "supercategory": ""}]
}

# Unique ID for each annotation
annotation_id = 1

# Iterate over each reordered image and its associated mask images
for image_filename in sorted(os.listdir(image_directory)):
    if not image_filename.startswith('cIMG') or '_' in image_filename:
        continue  # Skip non-bitewing images or mask images

    image_id = int(image_filename[4:].split('.')[0])
    image_path = os.path.join(image_directory, image_filename)
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # Add image information to COCO dataset
    coco_dataset["images"].append({
        "file_name": image_filename,
        "width": width,
        "height": height,
        "id": image_id,
        "coco_url": "",
        "flickr_url": "",
        "date_captured": 0,
        "license": 0
    })

    # Now, find and process corresponding mask images
    for mask_filename in sorted(os.listdir(image_directory)):
        if mask_filename.startswith(f'cIMG{str(image_id).zfill(5)}') and mask_filename.endswith('.png'):
            mask_path = os.path.join(image_directory, mask_filename)
            mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

            # Find contours in the mask image
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Calculate bounding boxes for each contour and add annotations
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                area = cv2.contourArea(contour)
                coco_dataset["annotations"].append({
                    "id": annotation_id,
                    "image_id": image_id,
                    "category_id": 1,
                    "segmentation": [],
                    "area": float(area),
                    "bbox": [float(x), float(y), float(w), float(h)],
                    "iscrowd": 0
                })
                annotation_id += 1

# Save the COCO dataset to a JSON file
with open(coco_json_path, 'w') as json_file:
    json.dump(coco_dataset, json_file, indent=4)
