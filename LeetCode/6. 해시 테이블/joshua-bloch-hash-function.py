HASHSIZE = 1009


def hash(s: str) -> int:
    hashval = 0

    for c in s:
        hashval = ord(c) + 31 * hashval

    return hashval


print(hash('hello world'))
