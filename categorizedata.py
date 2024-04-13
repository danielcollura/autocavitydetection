import json

# Function to filter out annotations except those with category_id corresponding to "E0"
def filter_annotations(data, category_name):
    # Find the category_id for the given category_name ('E0')
    category_id = next((cat['id'] for cat in data['categories'] if cat['name'] == category_name), None)
    
    # Filter annotations to only keep those with category_id of 'E0'
    if category_id is not None:
        data['annotations'] = [anno for anno in data['annotations'] if anno['category_id'] == category_id]
    else:
        print(f"No category found with name {category_name}")
        
    return data

# Path to your JSON data
file_path = '/Users/danielcollura/Desktop/Dental Neural Net/Neural Net/dental_rtg_test/test_annotations_anonymized.json'

# Load the data
with open(file_path, 'r') as file:
    data = json.load(file)

# Now 'data' is a Python dictionary that contains your JSON data
# Call the filter function to modify 'data' in place
data = filter_annotations(data, 'E0')

# Optionally, save the filtered data back to a file
filtered_file_path = '/Users/danielcollura/Desktop/Dental Neural Net/Neural Net/dental_rtg_test/filtered_annotations.json'
with open(filtered_file_path, 'w') as file:
    json.dump(data, file, indent=4)

print(f"Filtered data saved to {filtered_file_path}")
