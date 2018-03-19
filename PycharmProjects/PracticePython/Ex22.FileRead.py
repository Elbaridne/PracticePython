def readfile(path):
    with open('{0}'.format(path),'r') as f:
        elem = f.readline()
        Darth, Lea , Luke = 0, 0, 0
        while elem :
            if elem == "Darth":
                Darth += 1
            elif elem == "Lea":
                Lea += 1
            elif elem == "Luke":
                Luke += 1
            elem = f.readline()
        print("Darth Vader : {0}    Luke : {1}  Lea : {2}".format(Darth,Luke,Lea))

readfile("nameslist.txt")
