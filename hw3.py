from turtle import *
import random
# Tarik Muzughi
# 4500 Miller
# 9/30/19
# This program "paints" blobs on a grid until each cell is painted, it runs K times
# and takes a really long time to test...GLHF!

# get input from user for N and error check
# def getN():
while (True):
    N = input("Please enter an integer between 2 and 15 inclusive:")
    # check if input is digit
    if (N.isdigit()):
        N = int(N)  # casting
        if ((N < 2) or (N > 15)):
            print("Error: Invalid integer")
        else:
            break
    else:
        print("Error: %s is not valid" % N)


# get input from user for K and error check
# def getK():
while (True):
    K = input("Please enter an integer between 1 and 10 inclusive:")
    # check if input is digit
    if (K.isdigit()):
        K = int(K)  # casting
        if ((K < 1) or (K > 10)):
            print("Error: Invalid integer")
        else:
            break
    else:
        print("Error: %s is not valid" % K)

def find(l, elem):
    for row, i in enumerate(l):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return 1
    return 0


# get user input

#print("got here")
#draws grid
def drawGrid():
    up()
    setx(-400)
    sety(-325)
    speed(100)
    down()
    for x in range(N):
        for i in range(N):
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)
            right(90)
            forward(50)

            right(90)
            forward(50)
        if (x < (N - 1)):
            setx(-400)
            sety(-325 + (50 * (x + 1)))


matrix = [[0 for x in range(N)] for y in range(N)]
matrix2 = [0]* (N * N)
# paints grid
def letsPaint():
    while(True):

        rollX = random.randint(0, (N - 1))
        rollY = random.randint(0, (N - 1))


    ################################### indicate tile
        up()
        setx(-400 + (rollX * 50))
        sety(-325 + (rollY * 50))
        down()
        seth(0)
        speed(10)
        color('blue')
        forward(50)
        right(90)
        forward(50)
        right(90)
        forward(50)
        right(90)
        forward(50)
    ################################### paint blob
        up()
        setx(-400 + (rollX * 50))
        sety(-325 + (rollY * 50))

        color('red')
        seth(0)
        forward(5)
        right(90)
        forward(45)

        begin_fill()


        down()
        circle(5)
        end_fill()
        speed(100)
    #################################### end paint blob

        up()
        setx(-400 + (rollX * 50))
        sety(-325 + (rollY * 50))
        down()
        seth(0)
        color('black')
        forward(50)
        right(90)
        forward(50)
        right(90)
        forward(50)
        right(90)
        forward(50)
    #################################### erase tile indication
        matrix[rollX][rollY] += 1
        numberOfBlobs[i] += 1



        if not (find(matrix, 0)):
            break

    # end_fill()
    done()

# some variables i use and some variables i dont use :)
minOverall = 0
maxOverall = 0
avgOverall = 0
minCell = [0] * K
maxCell = 0
avgCell = 0
numberOfBlobs = [0] * K
temp = []
flat_list = []
total1 = 0
total2 = 0
# handles painting iterations
#  print("got here too")
i = 0
while(i < K):
    matrix = [[0 for x in range(N)] for y in range(N)]
    try:
        drawGrid()
        letsPaint()

    except:
        drawGrid()
        letsPaint()

    for sublist in matrix:
        for item in sublist:
            flat_list.append(item)

    arbitrary = input("Press Enter to continue")
    i += 1


# here comes data

print("The minimum blobs it took to paint a picture was %d" % min(numberOfBlobs))
print("The maximum blobs it took to paint a picture was %d" % max(numberOfBlobs))
for x in numberOfBlobs:
    total1 += x
print("The average blobs it took to paint a picture was %d" % (total1/K))
print("The minimum blobs it took for any one cell was %d" % min(flat_list))
print("The maximum blobs it took for any one cell was %d" % max(flat_list))
for x in flat_list:
    total2 += x
print("The average blobs it took for any one cell was %d" % (total2/(N * K)))
