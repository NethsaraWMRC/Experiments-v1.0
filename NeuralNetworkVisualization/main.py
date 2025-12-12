from dataset import generate_data
from network import SimpleNN
from trainer import Trainer
from animate import animate_learning
import torch

# Set random seed for reproducibility
torch.manual_seed(42)

# Choose function: "x2", "x3", "sin"
x, y = generate_data("sin", n_points=100)

# Build the network with more neurons for complex functions
nn = SimpleNN(hidden_neurons=20)

print("Training Neural Network...")
print(f"Network architecture: {sum(p.numel() for p in nn.parameters())} parameters")
print()

# Train
trainer = Trainer(nn)
trainer.train(x, y, epochs=200, lr=0.01)

print("\nTraining complete!")
print(f"Final Loss: {trainer.losses[-1]:.4f}")
print()

# Animate how the NN learns
animate_learning(x, y, trainer.predictions)
