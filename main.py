def main():
    import torch
    x = torch.randn(4, 4)
    x = x.reshape(2, 8)
    print(x)


if __name__ == "__main__":
    main()
