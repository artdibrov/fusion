from collections import Counter


def find_duplicates(collection):

    names = [
        photo["file"]
        for photo in collection
    ]

    counter = Counter(names)

    return [
        name
        for name, amount in counter.items()
        if amount > 1
    ]
