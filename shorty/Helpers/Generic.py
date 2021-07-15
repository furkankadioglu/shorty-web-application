def searchInObjectArray(list, filter):
    for x in list:
        if filter(x):
            return x
    return False