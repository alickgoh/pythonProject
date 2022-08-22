def list_unique(n):
    return set(n)


n = [1, 2, 4, 6, 7, 8, 8, 10, 13, 14, 15, 16, 16]
print(list(list_unique(n)))


def list_unique_loop(n):
    m = []
    for i in n:
        if i not in m:
            m.append(i)
    return m


n = [1, 2, 4, 6, 7, 8, 8, 10, 13, 14, 15, 16, 16]
print(list_unique_loop(n))
