import random


def word():
    return "hoge"


def score():
    return random.randint(1, 100)


def main():
    print(word())
    print(score())


if __name__ == "__main__":
    main()
