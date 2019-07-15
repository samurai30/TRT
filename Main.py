import numpy as np
import matplotlib.pyplot as plt


def init_function(number_vec, a, b, c, d):
    if not number_vec < 3:
        input_pts = []
        for i in range(number_vec):
            print("POINT PLOT =", i + 1)
            input_pts.append([int(input("X axis")), int(input("Y axis"))])
        pts = np.array(input_pts)
        sq_matrix = input_pts
        for i in range(len(sq_matrix)):
            sq_matrix[i].append(1)
        square_matrix = np.array(sq_matrix)
        p = plt.Polygon(pts, closed=True)
        ax = plt.gca()
        ax.add_patch(p)
        ax.set_xlim(a, b)
        ax.set_ylim(c, d)
        plt.show()
        print("Input the pivot points below")
        pivot_x = int(input("X axis"))
        pivot_y = int(input("Y axis"))
        degree = int(input("ENTER THE DEGREE TO ROTATE"))
        trt_matrix = np.array([[np.cos(np.deg2rad(degree)), np.negative(np.sin(np.deg2rad(degree))),
                               np.negative(pivot_x) * np.cos(np.deg2rad(degree)) + pivot_y * np.sin(
                                   np.deg2rad(degree)) + pivot_x],
                              [np.sin(np.deg2rad(degree)), np.cos(np.deg2rad(degree)),
                               np.negative(pivot_x) * np.sin(np.deg2rad(degree)) - pivot_x * np.cos(
                                   np.deg2rad(degree) + pivot_y)],
                              [0, 0, 1]])

        final_matrix = np.array(trt_matrix.dot(square_matrix.transpose())).transpose()
        print("ORIGINAL MATRIX")
        print(trt_matrix)
        print("SQUARE MATRIX")
        print(square_matrix)
        print("FINAL MATRIX")
        print(final_matrix)

        temp_list = []
        for i in range(len(final_matrix)):
            temp = np.delete(final_matrix[i], 2)
            temp_list.append(temp)

        p2 = plt.Polygon(temp_list, closed=True)
        ax2 = plt.gca()
        ax2.add_patch(p2)
        ax2.set_xlim(a, b)
        ax2.set_ylim(c, d)
        plt.show()
        exit()
    else:
        print("not allowed")
        inputfunc()


def inputfunc():

    print("X axis limit")
    limitx1 = int(input("Point X-a"))
    limitx2 = int(input("Point X-b"))

    print("Y axis limit")
    limity1 = int(input("Point Y-a"))
    limity2 = int(input("Point Y-b"))

    novec = int(input("How many vertices?"))
    init_function(novec, limitx1, limitx2, limity1, limity2)


inputfunc()










