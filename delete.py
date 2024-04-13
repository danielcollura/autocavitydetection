import os

# Define the directory where your images are stored
images_dir = '/Users/danielcollura/Desktop/cavity_dataset/uoft_dataset/images'

# Starting image number for deletion
start_deleting_from = 146

# Counter for deleted images
deleted_images_count = 0

# List all files in the directory
files = os.listdir(images_dir)

# Loop through files to find and delete the specified images
for file in files:
    if file.startswith("cIMG") and file.endswith(".png"):
        # Extract the image number and check if it should be deleted
        image_number = int(file[4:9])
        if image_number >= start_deleting_from:
            # Delete the image
            os.remove(os.path.join(images_dir, file))
            deleted_images_count += 1

print(f"Deleted {deleted_images_count} images.")
