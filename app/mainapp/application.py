import random
from typing import List


def word() -> str:
    return "hoge"


def score() -> int:
    result = random.randint(1, 100)
    print(result)
    return result


def greeting(name: str) -> str:
    return ("hello " + name)


def load_numbers_sorted(file_path: str) -> List[int]:
    numbers = []

    with open(file_path) as f:
        for line in f:
            numbers.append(int(line))
    return sorted(numbers)


def main():
    print(word())
    print(score())
    print(greeting(name="john"))


if __name__ == "__main__":
    main()
