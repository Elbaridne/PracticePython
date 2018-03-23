def gameboard(size):
    for num in range(size):
        str = "--- " * size
        str2= "|   " * size
        print(str)
        print(str2)

gameboard(4)