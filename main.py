# Jenny, Nicolo, Connor
# CS 102
# Program: skip
"""
Program Description:

"""


####################################SKIP########################################
# Function description
# Inputs:
# Prints:
# Returns:
def skipsearch(mylist, target, skip):
    x = 0
    if mylist[x] == target:
        return True

    else:
        # skip front
        while (x + skip) < len(mylist) and mylist[x] < target:
            x += skip

        # check if the item in the list is equal to the target
        if mylist[x] == target:
            return True

        # steps going back
        elif mylist[x] > target:
            # if the spot on step is more than target then we go
            # as much as skip-1 steps back
            for i in range(skip - 1):
                x -= 1

                if mylist[x] == target:
                    return True

        # steps going forward
        else:
            while x < len(mylist):
                if mylist[x] == target:
                    return True
                x += 1

    return False
####################################END########################################


####################################FORMULA########################################
# Function description
# Inputs:
# Prints:
# Returns:
def formula(mylist, m):
    n = len(mylist)

    # first find out the most amount of steps forward
    index = n // m
    # m-1 is the most you can go back (or front if needed)
    return index + m - 1
####################################END########################################


####################################AUX########################################
# Function description
# Inputs:
# Prints:
# Returns:
def auxiliaryloop(mylist, move, skipAmt, leapAmt, target, index):
    placeholder = index
    newskip = skipAmt
    # moving front
    if move == 'leap':
        while (index + leapAmt) < len(mylist) and mylist[index] < target:
            index += leapAmt
            print("index has leaped to: ", index, mylist[index])

    # moving back
    elif move == 'skip':
        while (index - skipAmt) > (placeholder - leapAmt) \
                and mylist[index] > target:
            index -= skipAmt
            print("index has skipped to: ", index, mylist[index])
    elif move == 'step':
        while index < len(mylist) and index < placeholder + skipAmt:
            if mylist[index] == target:
                print("3-Leap target is at ", index)
                return True
                #return index
            else:
                index += 1
                print("index has stepped to: ", index, mylist[index])

    return index
####################################END########################################


####################################AUX########################################
# Function description
# Inputs:
# Prints:
# Returns:
def leapsearchAUX(mylist, target, leap, skip):
    index = 0
    if mylist[index] == target:
        return True
    else:

        ## AUX leap
        skipT = 'leap'
        index2 = auxiliaryloop(mylist, skipT, skip, leap, target, index)

        if mylist[index2] == target:
            print("1-LeapAUX target is at ", index)
            return True
        elif mylist[index2] < target:
            ## AUX step
            skipT = 'step'
            index2 = auxiliaryloop(mylist, skipT, skip, leap, target, index2)

        elif mylist[index2] > target:
            ## AUX skip
            newskip = skip
            skipT = 'skip'
            index2 = auxiliaryloop(mylist, skipT, skip, leap, target, index2)
            if mylist[index2] == target:
                print("2-LeapAUX target is at ", index2)
                return True

            else:
                # Step after skip
                skipT = 'step'
                return auxiliaryloop(mylist, skipT, newskip, leap, target, index2)



        else:
            # AUX step if not skip, after leap
            index = auxiliaryloop(mylist, 'step', skip, leap, target, index2)

    return False


####################################END########################################


####################################LEAP########################################
# Connor
# leapsearch for larger lists
# leaps forward then skips backwards then steps to target
def leapsearch(mylist, target, leap, skip):
    index = 0
    if mylist[index] == target:
        return True
    else:
        while (index + leap) < len(mylist) and mylist[index] < target:
            index += leap
            print("index has leaped to: ", index, mylist[index])

        if mylist[index] == target:
            print("1-Leap target is at ", index)
            return True

        elif mylist[index] > target:
            # for i in range(skip - 1):
            placeholder = index
            newskip = skip
            while (index - skip) > (placeholder - leap) \
                    and mylist[index] > target:
                index -= skip
                print("index has skipped to: ", index, mylist[index])

            if mylist[index] == target:
                print("2-Leap target is at ", index)
                return True
            else:
                for i in range(newskip - 1):
                    index += 1
                    print("index has stepped to: ", index, mylist[index])
                    if mylist[index] == target:
                        print("3-Leap target is at ", index)
                        return True

        else:
            while index < len(mylist):
                if mylist[index] == target:
                    print("4-Leap target is at ", index)
                    print("index has stepped to: ", index, mylist[index])
                    return True
                else:
                    index += 1
    return False


####################################END########################################


def main2():
    mylist1 = [1, 3, 5, 7, 12, 24, 25, 34, 42, 45, 54, 65, 76]
    target1 = 24
    skip1 = 4

    mylist2 = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40,
        41, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60,
        61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78,
        80, 81, 82, 83, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98,
        99, 100
    ]
    target2 = 69
    skip2 = 17
    leap = 40

    print("\nNormal skip:")
    print(skipsearch(mylist2, target2, skip2), formula(mylist2, skip2))
    print("\nLeap, Skip, Step:")
    print(leapsearch(mylist2, target2, leap, skip2), formula(mylist2, skip2))
    print("\nLeap AUX:")
    print(leapsearchAUX(mylist2, target2, leap, skip2), formula(mylist2, skip2))

    ## DANGER ZONE! BIG LISTS AHEAD
    import random
    randomlist = []
    for i in range(0, 999):
        n = random.randint(1, 999)
        randomlist.append(n)
    mylist3 = randomlist

    mylist3.sort()
    target3 = randomlist[60]
    print("Random target:")
    print(randomlist[60])
    skip3 = 50
    leap2 = 400
    print("\nNote: this may take awhile...")
    print("\nNormal skip:")
    print(skipsearch(mylist3, target3, skip3), formula(mylist3, skip3))
    print("\nLeap, Skip, Step:")
    print(leapsearch(mylist3, target3, leap2, skip3), formula(mylist3, skip3))
    print("\nLeap AUX:")
    print(leapsearchAUX(mylist3, target3, leap2, skip3), formula(mylist3, skip3))


main2()

'''
from random import randrange
import time
#Nicolo

def main():
    size = int(input("How large is our set? "))
    #s = set of positive integers
    mylist = []
    #maxx is the largest integer possible in our set
    maxx = 1000
    target = randrange(size * maxx) // 4
    skip = 5
    repetitions = 100

    #now create a list of size-many integers from 1 to maxx
    #Use a for loop with a test to the entries are unique
    #sort it at end, for pretty
    while len(mylist) < size:
        newint = randrange(1, maxx)
        if not newint in mylist:
            mylist.append(newint)
    mylist.sort()
    #print("The set mylist is", mylist)
    print("The target is", target)
    print(skipsearch(mylist, target, skip), formula(mylist, skip))

    start = time.time()
    for j in range(repetitions):
        target = randrange(1, maxx)
        skipsearch(mylist, target, skip)
    end = time.time()

    print("For size=", size, "this took", end - start, "seconds")
    size = size * 5


main()
'''
