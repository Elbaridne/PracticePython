def gameboard(size):
    name = []
    for num in range(size):
        name.append([0]*size)

        '''
            str = "--- " * size
            str2= "|   " * size
            print(str)
            print(str2)
        '''
    for num in name:
        print(num)


gameboard(5)