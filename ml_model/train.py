import torch
import torch.optim as optim
from torch.utils.data import DataLoader
from model import ImageRegressor  # Import the model from model.py
from your_dataset_class import YourImageDataset

def train_model(model, dataloaders, criterion, optimizer, num_epochs=25):
    for epoch in range(num_epochs):
        model.train()
        for inputs, scores in dataloaders['train']:
            inputs, scores = inputs.to(device), scores.to(device)
            optimizer.zero_grad()
            predicted_scores = model(inputs)
            loss = criterion(predicted_scores, scores.view_as(predicted_scores))
            loss.backward()
            optimizer.step()
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
train_dataset = YourImageDataset(...)  # Add appropriate arguments
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
dataloaders = {'train': train_loader}

# Train the model
trained_model = train_model(model, dataloaders, criterion, optimizer, num_epochs=25)
