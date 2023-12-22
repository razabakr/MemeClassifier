from PIL import Image
import torchvision.transforms as transforms
import os

def preprocess_images(directory, target_size=(256, 256)):
    transform = transforms.Compose([
        transforms.Resize(target_size),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    for filename in os.listdir(directory):
        if filename.lower().endswith('.jpg'):
            file_path = os.path.join(directory, filename)
            image = Image.open(file_path)
            image = transform(image)
            # Save or use the processed image as needed
            # For example, you can save it back to disk or collect them in a list

# Replace with the path to your images directory
preprocess_images('/Users/razabakr/Desktop/MemeClassifier/ml_model/data/Images')
