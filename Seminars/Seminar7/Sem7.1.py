values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

transformed_values = list(map(lambda x: x, values))

if values == transformed_values:
    print("ok")
else:
    print("fail")
