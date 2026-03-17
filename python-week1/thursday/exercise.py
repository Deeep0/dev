def total():
    i = 1
    grains = 1
    for i in range(65):
        if i != 1:
            grains = grains * 2
        i += 1
    print(grains)

total()