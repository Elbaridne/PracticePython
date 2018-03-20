def readfile(path):
    Darth, Lea, Luke = 0, 0, 0
    with open('{0}'.format(path),'r') as f:
        elem = f.readline()
        while elem != '':
            if elem == "Darth\n":
                Darth += 1
            elif elem == "Lea\n":
                Lea += 1
            elif elem == "Luke\n":
                Luke += 1
            elem = f.readline()
        print(elem)



        print("Darth Vader : {0}  Luke : {1}  Lea : {2}".format(Darth,Luke,Lea))

readfile("nameslist.txt")
