import os

# Function to generate text files listing image names in each directory
def generate_image_lists(images_dirs):
    for images_dir in images_dirs:
        image_list_path = f'{os.path.basename(images_dir)}_image_list.txt'
        with open(image_list_path, 'w') as file:
            for filename in os.listdir(images_dir):
                if filename.endswith('.png'):
                    file.write(filename + '\n')

# Function to read image names from text files
def read_image_lists(image_list_paths):
    image_lists = {}
    for image_list_path in image_list_paths:
        image_list_name = os.path.basename(image_list_path).split('_')[0] + '_images'
        with open(image_list_path, 'r') as file:
            image_lists[image_list_name] = [line.strip() for line in file.readlines()]
    return image_lists

# Main function
def main():
    # Paths and directories
    test_images_dir = '/Users/danielcollura/Desktop/cavity_dataset/nonaugdatasetfinal/images/test_images'
    train_images_dir = '/Users/danielcollura/Desktop/cavity_dataset/nonaugdatasetfinal/images/train_images'
    val_images_dir = '/Users/danielcollura/Desktop/cavity_dataset/nonaugdatasetfinal/images/val_images'
    
    images_dirs = [test_images_dir, train_images_dir, val_images_dir]
    image_list_paths = [f'{os.path.basename(images_dir)}_image_list.txt' for images_dir in images_dirs]
    
    # Generate text files listing image names in each directory
    generate_image_lists(images_dirs)
    
    # Read image names from text files
    image_lists = read_image_lists(image_list_paths)
    
    # Now you can use these image names for your YOLO conversion and organization logic
    print("Test images:", image_lists.get('test_images'))
    print("Train images:", image_lists.get('train_images'))
    print("Validation images:", image_lists.get('val_images'))

if __name__ == "__main__":
    main()
