def find_nb(m):
    # your code
    numCubes = 0
    i = 1
    if m <= 0:
        return -1
    else:
        while m > 0:
            m -= i**3
            # print("m = " + str(m) + ", i = " + str(i))
            if m == 0:
                return numCubes + 1
            elif m <= 0:
                return -1
            else:
                numCubes += 1
                i += 1


# Test Case
print(find_nb(1071225)) #--> 45
print(find_nb(91716553919377)) #--> -1