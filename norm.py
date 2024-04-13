import json

def normalize_annotations(data):
    normalized_annotations = {
        "info": data["info"],
        "licenses": data["licenses"],
        "images": data["images"],
        "annotations": [],
        "categories": data["categories"]
    }
    
    for annotation in data["annotations"]:
        image_id = annotation["image_id"]
        image_entry = next((entry for entry in data['images'] if entry['image_id'] == image_id), None)
        if image_entry:
            print("Keys of image entry:", image_entry.keys())  # Add this line
            width = image_entry["width"]
            height = image_entry["height"]
            bbox = annotation["bbox"]
            normalized_bbox = [
                bbox[0] / width,
                bbox[1] / height,
                bbox[2] / width,
                bbox[3] / height
            ]
            normalized_annotation = {
                "image_id": image_id,
                "category_id": annotation["category_id"],
                "bbox": normalized_bbox,
                "area": annotation["area"],
                "iscrowd": annotation["iscrowd"]
            }
            normalized_annotations["annotations"].append(normalized_annotation)
    
    return normalized_annotations


def main():
    # Load JSON file
    with open('/Users/danielcollura/Desktop/cavity_dataset/nonaugdatasetfinal/labels/label.json', 'r') as f:
        data = json.load(f)
    
    # Normalize annotations
    normalized_data = normalize_annotations(data)
    
    # Save normalized annotations
    with open('/Users/danielcollura/Desktop/cavity_dataset/nonaugdatasetfinal/labels/normalized_label.json', 'w') as f:
        json.dump(normalized_data, f)

if __name__ == "__main__":
    main()
