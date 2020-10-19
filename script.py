def check():
    with open('library.txt') as f:
        datafile = f.readlines()
    found = False  # This isn't really necessary
    for line in datafile:
        if blabla in line:
            # found = True # Not necessary
            return True
    return False  # Because you finished the search without finding