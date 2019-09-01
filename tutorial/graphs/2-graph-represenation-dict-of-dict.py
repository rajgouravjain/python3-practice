## """A dict of dict will have connected nodes details in dict with weight """

g = {
    "n1" : {"n2": 5, "n3": 6},
    "n2" : { "n1": 2 , "n4": 9 },
    "n3" : {"n1" : 6, "n4" : 3},
    "n4" : {"n1" : 3, "n2" : 5, "n3" : 8}
}

if __name__ == '__main__':
    print(repr(g))

