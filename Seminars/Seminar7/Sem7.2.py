def find_farthest_orbit(orbits):
    maximum = 0
    for i, j in orbits:
        if i != j and i * j > maximum:
            maximum = i * j
            orbits1 = (i, j)
    return orbits1


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
