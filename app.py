import yaml

if __name__ == "__main__":
    stream = open("test.yaml")
    dictionary = yaml.safe_load(stream)

    for key, value in dictionary.items():
        print(f"{key}: {value} ")

    