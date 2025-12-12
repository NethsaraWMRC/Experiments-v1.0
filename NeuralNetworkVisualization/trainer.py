import torch
import torch.optim as optim
import torch.nn as nn

class Trainer:
    def __init__(self, network):
        self.network = network
        self.predictions = []
        self.losses = []
        self.optimizer = optim.Adam(network.parameters(), lr=0.01)
        self.criterion = nn.MSELoss()

    def train(self, x, y, epochs=500, lr=0.01):
        # Update learning rate if different from default
        for param_group in self.optimizer.param_groups:
            param_group['lr'] = lr
        
        # Convert to PyTorch tensors
        x_tensor = torch.FloatTensor(x)
        y_tensor = torch.FloatTensor(y)
        
        self.network.train()
        for i in range(epochs):
            # Forward pass
            self.optimizer.zero_grad()
            y_pred = self.network(x_tensor)
            
            # Compute loss
            loss = self.criterion(y_pred, y_tensor)
            
            # Backward pass and optimization
            loss.backward()
            torch.nn.utils.clip_grad_norm_(self.network.parameters(), max_norm=1.0)
            self.optimizer.step()
            
            # Save predictions and loss for animation
            with torch.no_grad():
                self.predictions.append(y_pred.numpy().copy())
                self.losses.append(loss.item())
            
            # Print progress
            if (i + 1) % 50 == 0:
                print(f"Epoch [{i+1}/{epochs}], Loss: {loss.item():.4f}")
