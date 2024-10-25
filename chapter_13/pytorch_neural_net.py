import torch
import torch.nn as nn
import torch.optim as optim
 
# Define a simple neural network
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(10, 50)
        self.fc2 = nn.Linear(50, 1)
 
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x
 
# Create the model, loss function, and optimizer
model = SimpleNet()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)
 
# Example input and target data
inputs = torch.randn(10)
target = torch.tensor([1.0])
 
# Forward pass
output = model(inputs)
loss = criterion(output, target)
 
# Backward pass and optimization
loss.backward()
optimizer.step()
 
print(f"Loss: {loss.item()}")
