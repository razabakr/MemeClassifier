import os

def rename_images_sequentially(directory, prefix="meme"):
    # List all jpg files in the directory
    files = [f for f in os.listdir(directory) if f.lower().endswith('.jpg')]

    # Sort files for consistency
    files.sort()

    # Rename each file
    for idx, filename in enumerate(files):
        # Define the new filename
        new_filename = f"{prefix}{idx + 1}.jpg"
        
        # Define full file paths
        old_file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(directory, new_filename)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed '{filename}' to '{new_filename}'")

# Replace with the path to your images directory
directory = '/Users/razabakr/Desktop/MemeClassifier/ml_model/data/Images'
rename_images_sequentially(directory)
