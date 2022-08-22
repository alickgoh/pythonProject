a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# first solution, in 1 line
print([b for b in a if b % 2 == 0])

# second solution, same logic but longer approach and need to define an empty list
c = []
for b in a:
    if b % 2 == 0:
        c.append(b)
print(c)
