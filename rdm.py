import os

def delete_unnecessary_txt_files(directory):
    # List all files in the directory
    for filename in os.listdir(directory):
        # Check if the filename contains an underscore and ends with '.txt'
        if '_' in filename and filename.endswith('.txt'):
            # Construct the full path to the file
            file_path = os.path.join(directory, filename)
            # Delete the file
            os.remove(file_path)
            print(f"Deleted {file_path}")

# Specify the paths to your train and val folders
train_dir = '/Users/danielcollura/Desktop/DENTAL NEURAL NET/Dataset/Misc/UoftTSeg/labels/train'
val_dir = '/Users/danielcollura/Desktop/DENTAL NEURAL NET/Dataset/Misc/UoftTSeg/labels/val'

# Run the function for both train and val directories
delete_unnecessary_txt_files(train_dir)
delete_unnecessary_txt_files(val_dir)

print("Cleanup complete.")
