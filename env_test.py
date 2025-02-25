def test_python():
    import sys

    print(f"{sys.version=}")


def test_numpy():
    import numpy

    print(f"{numpy.__version__=}")


def test_torch():
    import torch

    print(f"{torch.__version__=}")


def test_torchaudio():
    import torchaudio

    print(f"{torchaudio.__version__=}")


def test_torchvision():
    import torchvision

    print(f"{torchvision.__version__=}")


def test_cuda():
    import torch

    print(f"{torch.cuda.is_available()=}")

    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    x = torch.Tensor([1, 2, 3]).to(device)
    y = torch.Tensor([1, 4, 9]).to(device)
    assert bool((x * x == y).all().item())
    print(f"torch on {device} works")


if __name__ == "__main__":
    test_python()
    test_numpy()
    test_torch()
    test_torchaudio()
    test_torchvision()
    test_cuda()
