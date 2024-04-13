import os

def update_class_ids_to_zero(root_dir):
    for subdir, dirs, files in os.walk(root_dir):
        for filename in files:
            if filename.endswith(".txt"):  # Ensure we're only processing text files
                filepath = os.path.join(subdir, filename)
                with open(filepath, 'r') as file:
                    lines = file.readlines()

                # Update each line with class ID 0
                with open(filepath, 'w') as file:
                    for line in lines:
                        parts = line.strip().split()
                        if len(parts) == 5:  # Ensure the line format is correct
                            # Update class ID to 0 and write the line back
                            updated_line = f"0 {parts[1]} {parts[2]} {parts[3]} {parts[4]}\n"
                            file.write(updated_line)

# Example usage
root_dir = '/Users/danielcollura/Downloads/Dental caries in bitewing radiographs/dental_rtg_test/labels'
update_class_ids_to_zero(root_dir)
