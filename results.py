from ultralytics import YOLO

# Path to the trained weights
weights_path = '/Users/danielcollura/Desktop/Automatic Cavity Detection/YOLOv8/runs/detect/train11/weights/best.pt'

# Load the trained model with the specified weights
model = YOLO(weights_path)

# Path to the new, unlabeled images
unlabeled_images_path = '/Users/danielcollura/Downloads/Dental caries in bitewing radiographs/dental_rtg_test/images/test'

# Perform inference on the new images
results = model(unlabeled_images_path)

# Directory where you want to save the prediction images
save_directory = '/Users/danielcollura/Desktop/practice'

# Process the results and save the predictions
for i, result in enumerate(results):
    # Define the save path for each prediction image
    save_path = f'{save_directory}/result_{i}.jpg'
    
    # Display the prediction
    result.show()
    
    # Save the prediction image
    result.save(filename=save_path)
