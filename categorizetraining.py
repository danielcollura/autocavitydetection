import os
from sklearn.model_selection import train_test_split

# Path to the directory containing your UofT dataset images
image_directory = '/Users/danielcollura/Desktop/Dental Neural Net/Neural Net/UofT Dataset'
image_filenames = [f for f in os.listdir(image_directory) if f.endswith('.png') and '_' not in f]

# Ensure we only process the expected number of images (145 in your case)
assert len(image_filenames) == 145, "Unexpected number of images found."

# Split the dataset
train_filenames, val_filenames = train_test_split(image_filenames, test_size=0.2, random_state=42)

# Optionally, save the lists to files or proceed with further processing
print(f"Training set size: {len(train_filenames)} images")
print(f"Validation set size: {len(val_filenames)} images")

# Example: print out the filenames (or you can save them to a file)
print("Training filenames:", train_filenames)
print("Validation filenames:", val_filenames)

# If needed, here's a simple way to write these lists to files for later use
with open('train_filenames.txt', 'w') as f:
    for filename in train_filenames:
        f.write(f"{filename}\n")

with open('val_filenames.txt', 'w') as f:
    for filename in val_filenames:
        f.write(f"{filename}\n")
