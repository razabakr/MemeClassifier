import os
import random
import csv
from dotenv import load_dotenv

load_dotenv()  # This loads the variables from .env

def auto_rate_images(directory, output_csv):
    scores = {}
    for filename in sorted(os.listdir(directory)):
        if filename.endswith('.jpg'):
            # Generate a random score between 1 and 10
            score = round(random.uniform(8, 10), 1)  # One decimal place
            scores[filename] = score

    # Write scores to the output CSV file
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['filename', 'score'])
        for filename, score in scores.items():
            writer.writerow([filename, score])

    print(f"Scores written to {output_csv}")

# Replace with your images directory and desired output CSV file path
directory = os.getenv('IMAGE_DIRECTORY')
output_csv = os.getenv('SCORES_CSV')
auto_rate_images(directory, output_csv)
