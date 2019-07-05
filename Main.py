import numpy as np
import matplotlib.pyplot as plt

print("X axis limit")
a = int(input("Point a"))
b = int(input("Point b"))

print("Y axis limit")
c = int(input("Point a"))
d = int(input("Point b"))

number_vec = int(input("How many vertices?"))

if not number_vec < 3:
    inputPts = []
    SqMatrix = []
    for i in range(number_vec):
        print("POINT PLOT =", i+1)
        inputPts.append([int(input("X axis")), int(input("Y axis"))])
    pts = np.array(inputPts)
    SqMatrix = inputPts
    for i in range(len(SqMatrix)):
        SqMatrix[i].append(1)
    SquareMatrix = np.array(SqMatrix)
    print(SquareMatrix)
    p = plt.Polygon(pts, closed=True)
    ax = plt.gca()
    ax.add_patch(p)
    ax.set_xlim(a, b)
    ax.set_ylim(c, d)
    plt.show()
    print("Input the pivot points below")
    pivotX = int(input("X axis"))
    pivotY = int(input("Y axis"))
    degree = int(input("ENTER THE DEGREE TO ROTATE"))
    TRTMatrix = np.array([[np.cos(np.deg2rad(degree)), np.negative(np.sin(np.deg2rad(degree))),
                           np.negative(pivotX) * np.cos(np.deg2rad(degree)) + pivotY * np.sin(
                               np.deg2rad(degree)) + pivotX],
                          [np.sin(np.deg2rad(degree)), np.cos(np.deg2rad(degree)),
                           np.negative(pivotX) * np.sin(np.deg2rad(degree)) - pivotX * np.cos(
                               np.deg2rad(degree) + pivotY)],
                          [0, 0, 1]])

    FinalMatrix = np.array(TRTMatrix.dot(SquareMatrix.transpose())).transpose()
    print("FINAL MATRIX")
    print(FinalMatrix)
    TempList = []
    for i in range(len(FinalMatrix)):
        temp = np.delete(FinalMatrix[i],2)
        TempList.append(temp)

    p2 = plt.Polygon(TempList, closed=True)
    ax2 = plt.gca()
    ax2.add_patch(p2)
    ax2.set_xlim(a, b)
    ax2.set_ylim(c, d)
    plt.show()


else:
    print("not allowed")






