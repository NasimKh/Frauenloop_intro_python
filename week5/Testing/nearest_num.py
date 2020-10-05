def nearest_square(number):
    '''calculates the nearest square root
    to the given number '''
    root = 0
    while (root + 1) ** 2 <= number :
        root+=1
    return root**2

