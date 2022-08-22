from collections import Counter


def check_anagram(atr1, atr2):
    return Counter(atr1) == Counter(atr2)


if __name__ == "__main__":
    print(check_anagram("stressed", "desserts"))


def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)


if __name__ == "__main__":
    print(is_anagram("stressed", "desserts"))