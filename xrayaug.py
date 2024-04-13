import albumentations as A
import cv2
import json
import os
import random
from tqdm import tqdm

# Load the original JSON data
def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

data = load_json('/Users/danielcollura/Desktop/cavity_dataset/nonaugdatasetfinal/labels/normalized_label.json')

# Define your augmentation pipeline
augmentation = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
    A.Rotate(limit=20, p=0.5, border_mode=cv2.BORDER_CONSTANT),
    A.GaussNoise(p=0.2)
], bbox_params=A.BboxParams(format='coco', label_fields=['category_ids']))

# Function to apply augmentations and update JSON
def augment_images_and_update_json(data, augmentation, images_dir, target_total):
    image_files = [f for f in os.listdir(images_dir) if f.endswith('.png')]
    current_count = len(image_files)
    next_image_id = max([img['image_id'] for img in data['images']]) + 1
    next_annotation_id = max([ann['image_id'] for ann in data['annotations']]) + 1

    while current_count < target_total:
        random_file_name = random.choice(image_files)  # Randomly select an image to augment
        img_path = os.path.join(images_dir, random_file_name)
        image = cv2.imread(img_path)
        if image is None:
            continue  # If the image can't be loaded, skip it
        
        original_image_id = [img for img in data['images'] if img['file_name'] == random_file_name][0]['image_id']
        
        annotations = [ann for ann in data['annotations'] if ann['image_id'] == original_image_id]
        bboxes = [ann['bbox'] for ann in annotations]
        category_ids = [ann['category_id'] for ann in annotations]

        augmented = augmentation(image=image, bboxes=bboxes, category_ids=category_ids)
        aug_image = augmented['image']
        aug_bboxes = augmented['bboxes']
        aug_category_ids = augmented['category_ids']

        # Verify if augmented bboxes are valid
        aug_bboxes = [bbox for bbox in aug_bboxes if all(0 <= b <= 1 for b in bbox[:4])]  # Ensure all bbox values are between 0 and 1

        if not aug_bboxes:
            continue  # Skip saving this augmentation if no valid bboxes

        new_file_name = f"cIMG{next_image_id:05d}.png"
        cv2.imwrite(os.path.join(images_dir, new_file_name), aug_image)

        # Update JSON data for the new image
        data['images'].append({
            "image_id": next_image_id,
            "file_name": new_file_name,
            "width": aug_image.shape[1],
            "height": aug_image.shape[0]
            # Add other fields if necessary
        })

        # Update JSON data for new annotations
        for bbox, category_id in zip(aug_bboxes, aug_category_ids):
            data['annotations'].append({
                "image_id": next_image_id,
                "category_id": category_id,
                "bbox": bbox,
                "area": bbox[2] * bbox[3],  # Update this calculation if your bbox format is different
                "iscrowd": 0,
                "segmentation": []
            })
            next_annotation_id += 1

        next_image_id += 1
        current_count += 1

    return data

# Path to your images and target total count
images_dir = '/Users/danielcollura/Desktop/cavity_dataset/nonaugdatasetfinal/images/train_images'
target_total = 1000  # Update with your target

# Update the data and save it to a new JSON file
updated_data = augment_images_and_update_json(data, augmentation, images_dir, target_total)
output_json_path = '/Users/danielcollura/Desktop/cavity_dataset/nonaugdatasetfinal/labels/augmented_label.json'
with open(output_json_path, 'w') as file:
    json.dump(updated_data, file, indent=4)

print("Augmentation complete. New JSON file created.")
