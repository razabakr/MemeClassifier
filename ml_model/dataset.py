import os
from torchvision import transforms
from dataset_class import YourImageDataset  # Make sure this class is defined in your project
from dotenv import load_dotenv

load_dotenv()  # This loads the variables from .env

# Fetch paths from environment variables
csv_file_path = os.getenv('SCORES_CSV')
images_directory = os.getenv('IMAGE_DIRECTORY')

# Apply necessary image transformations
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Initialize your dataset
train_dataset = YourImageDataset(
    csv_file=csv_file_path,
    img_dir=images_directory, 
    transform=transform
)

# DataLoader and training code follows...
