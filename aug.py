import os
import cv2

# Define directories for train and validation masks and labels
train_masks_dir = '/Users/danielcollura/Desktop/DENTAL NEURAL NET/Dataset/Misc/UoftTSeg/masks/train'
val_masks_dir = '/Users/danielcollura/Desktop/DENTAL NEURAL NET/Dataset/Misc/UoftTSeg/masks/val'
train_labels_dir = '/Users/danielcollura/Desktop/DENTAL NEURAL NET/Dataset/Misc/UoftTSeg/labels/train'
val_labels_dir = '/Users/danielcollura/Desktop/DENTAL NEURAL NET/Dataset/Misc/UoftTSeg/labels/val'

# Ensure the output directories exist
os.makedirs(train_labels_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# Process masks and generate labels
def process_masks(input_dir, output_dir):
    for j in os.listdir(input_dir):
        image_path = os.path.join(input_dir, j)
        # Only process files that are images
        if j.lower().endswith(('.png', '.jpg', '.jpeg')):
            mask = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            _, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)
            H, W = mask.shape
            contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # convert the contours to polygons
            polygons = []
            for cnt in contours:
                if cv2.contourArea(cnt) > 200:
                    polygon = [p[0][0] / W for p in cnt] + [p[0][1] / H for p in cnt]
                    polygons.append(polygon)

            # Write the polygons to a .txt file in the output directory
            with open(os.path.join(output_dir, os.path.splitext(j)[0] + '.txt'), 'w') as f:
                for polygon in polygons:
                    f.write('0 ' + ' '.join(map(str, polygon)) + '\n')

# Run processing for train and val masks
process_masks(train_masks_dir, train_labels_dir)
process_masks(val_masks_dir, val_labels_dir)
