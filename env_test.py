import sys

import torch
import torchaudio
import torchvision
from torch import Tensor

print("python", sys.version)

print("torch", torch.__version__)

print("torchaudio", torchaudio.__version__)

print("torchvision", torchvision.__version__)

print("cuda", torch.cuda.is_available())

x = Tensor([1, 2, 3]).cuda()
y = Tensor([1, 4, 9]).cuda()
assert bool((x * x == y).all().item())
print("torch.cuda works")
