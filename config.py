import os
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Twitter Configuration
TWITTER_USERNAME = os.getenv('TWITTER_USERNAME', 'default_username')

# Machine Learning Model Configuration
MODEL_PATH = os.getenv('MODEL_PATH', 'default/path/to/your/saved_model')
DATA_PATH = os.getenv('DATA_PATH', 'default/path/to/your/dataset')

# Other configurations can be added here as needed
