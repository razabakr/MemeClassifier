from PIL import Image
import torchvision.transforms as transforms
import os
from dotenv import load_dotenv

load_dotenv()  # This loads the variables from .env

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

#set the directory as the directory with my images
image_directory = os.getenv('IMAGE_DIRECTORY')
preprocess_images(image_directory)
