import torch
import torch.optim as optim
from torch.utils.data import DataLoader
import datetime  # Import for generating a timestamp
from model import ImageRegressor  # Import the model from model.py
from dataset_class import YourImageDataset
from dataset import train_dataset

def train_model(model, dataloaders, criterion, optimizer, num_epochs=25):
    for epoch in range(num_epochs):
        model.train()
        for inputs, scores in dataloaders['train']:
            try:
                # Ensure inputs and scores are FloatTensors and move them to the correct device
                inputs, scores = inputs.float().to(device), scores.float().to(device)

                optimizer.zero_grad()

                # Forward pass
                predicted_scores = model(inputs)

                # Ensure the output is the correct shape and type
                predicted_scores = predicted_scores.float()
                scores = scores.view_as(predicted_scores)

                # Compute loss
                loss = criterion(predicted_scores, scores)

                # Backward pass and optimize
                loss.backward()
                optimizer.step()

            except Exception as e:
                print(f"Error during training: {e}")
                continue

        print(f'Epoch {epoch}/{num_epochs - 1}, Loss: {loss.item()}')

    return model

# Device configuration
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Initialize the ImageRegressor model
model = ImageRegressor(1).to(device)

# Loss and optimizer
criterion = torch.nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# DataLoader
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
dataloaders = {'train': train_loader}

# Train the model
try:
    trained_model = train_model(model, dataloaders, criterion, optimizer, num_epochs=25)
    
    # Generate a timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    
    # Save the model with the timestamp to avoid overwriting
    model_save_path = f'./saved_models/model_{timestamp}.pth'
    torch.save(trained_model.state_dict(), model_save_path)
    print(f"Model saved to {model_save_path}")
    
except Exception as e:
    print(f"Error during model training: {e}")
