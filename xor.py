import torch

x = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)

input_size = 2
hidden_size = 2
output_size = 1

w1 = torch.randn(input_size, hidden_size, requires_grad=True)
b1 = torch.randn(hidden_size, requires_grad=True)
w2 = torch.randn(hidden_size, output_size, requires_grad=True)
b2 = torch.randn(output_size, requires_grad=True)

def forward(x):
    z1 = torch.matmul(x,w1) + b1
    a1 = torch.sigmoid(z1)
    z2 = torch.matmul(a1,w2) + b2
    y_pred = torch.sigmoid(z2)
    return y_pred

learning_rate = 0.1
num_epochs = 100000

for epoch in range(num_epochs):
    y_pred = forward(x)

    loss = torch.nn.functional.binary_cross_entropy(y_pred, y)
    
    loss.backward()

    with torch.no_grad():
        w1 -= learning_rate * w1.grad
        b1 -= learning_rate * b1.grad
        w2 -= learning_rate * w2.grad
        b2 -= learning_rate * b2.grad

        w1.grad.zero_()
        b1.grad.zero_()
        w2.grad.zero_()
        b2.grad.zero_()

    if (epoch+1) % 1000 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')
