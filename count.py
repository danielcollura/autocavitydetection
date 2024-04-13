import os

# Define a function to count bounding boxes in .txt files across a directory and its subdirectories
def count_bboxes_in_dir(directory_path):
    bbox_count = 0
    # Check if the directory exists
    if not os.path.exists(directory_path):
        print(f"The directory {directory_path} does not exist.")
        return 0
    
    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            # Check if the file is a .txt file
            if file_name.endswith('.txt'):
                file_path = os.path.join(root, file_name)
                # Open and read the file
                with open(file_path, 'r') as file:
                    for line in file:
                        # Each non-empty line in a label file represents a bounding box
                        if line.strip():
                            bbox_count += 1
    
    return bbox_count

# Set the directory path with your provided path
directory_path = '/Users/danielcollura/Desktop/DENTAL NEURAL NET/Dataset/CombinedYOLO/labels'

# Call the function and print out the result
total_bboxes = count_bboxes_in_dir(directory_path)
print(f"Total number of bounding boxes: {total_bboxes}")
