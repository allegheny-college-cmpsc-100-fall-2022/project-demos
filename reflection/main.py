import importlib

def main():
    filename = input("Enter name of file to load: ")
    filename = f"{filename}"
    obj = importlib.import_module(filename)
    print(getattr(obj, filename)().price)


if __name__ == "__main__":
    main()