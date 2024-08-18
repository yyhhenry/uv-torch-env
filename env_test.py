def test_python():
    import sys

    print("python", sys.version)


def test_numpy():
    import numpy as np

    print("numpy", np.__version__)

    x = np.array([1, 2, 3])
    y = np.array([1, 4, 9])
    assert (x * x == y).all()
    print("numpy works")


def test_torch():
    import torch

    print("torch", torch.__version__)

    x = torch.Tensor([1, 2, 3])
    y = torch.Tensor([1, 4, 9])
    assert bool((x * x == y).all().item())
    print("torch works")


def test_torchaudio():
    import torchaudio

    print("torchaudio", torchaudio.__version__)


def test_torchvision():
    import torchvision

    print("torchvision", torchvision.__version__)


def test_cuda():
    import torch

    print("cuda", torch.cuda.is_available())

    x = torch.Tensor([1, 2, 3]).cuda()
    y = torch.Tensor([1, 4, 9]).cuda()
    assert bool((x * x == y).all().item())
    print("torch.cuda works")


if __name__ == "__main__":
    test_python()
    test_numpy()
    test_torch()
    test_torchaudio()
    test_torchvision()
    test_cuda()
