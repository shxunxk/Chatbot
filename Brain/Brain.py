import torch.nn as nn

class NeuralNet(nn.Module):
    def __init__(self, inp_size, hid_size, num_classes) -> None:
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(inp_size, hid_size)
        self.l2 = nn.Linear(hid_size, hid_size)
        self.l3 = nn.Linear(hid_size, num_classes)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        return(out)