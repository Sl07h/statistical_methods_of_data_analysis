﻿import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy import stats
from sympy import *
from sys import argv, path


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
class lab1():
    def __init__(self):
        self.x = sample_x()
        self.u = np.ndarray(n)
        for i in range(n):
            self.u[i] = f(theta_true, self.x[i])
        u_mean = np.full((n), np.mean(self.u))
        w_squared = np.dot((self.u - u_mean), (self.u - u_mean)) / (n-1)
        self.dist = rho * w_squared
        self.y = np.copy(self.u)
        for i in range(n):
            self.y[i] += np.random.normal(0, self.dist)

    def save_table_1(self):
        with open('1/report/table_1_u_y_' + str(int(rho*100)) + '.txt', 'w') as file:
            file.write('i\t')
            for i in range(1, m+1):
                file.write('x%d\t' % i)
            file.write('u\ty\n')
            for i in range(n):
                file.write('{:d}\t'.format(i))
                for j in range(m):
                    file.write('{:.17f}\t'.format(self.x[i][j]))

                file.write('{:.17f}\t{:.17f}\n'.format(self.u[i], self.y[i]))

    def draw(self, doDrawWithNoize, title, name, elevation, azimuth):
        path_to_save = '1/pics/' + name + '_' + \
            str(int(rho*100)) + '_' + str(elevation) + '_' + str(azimuth) + '.png'
        fig = plt.figure('1')
        ax = fig.gca(projection='3d')
        tmp_range = np.linspace(a, b, sqrt(n))
        x1, x2 = np.meshgrid(tmp_range, tmp_range)
        u = f_2_parameters(theta_true, x1, x2)
        fig.subplots_adjust(bottom=-0.05, top=1, left=-0.05, right=1.05)
        ax.view_init(elevation, azimuth)
        ax.plot_surface(x1, x2, u, zorder=2, alpha=0.2)
        if doDrawWithNoize:
            title += ' ' + str(int(rho * 100)) + '%'
            ax.scatter(self.x1, self.x2, self.y, c='black', zorder=1)
        else:
            ax.scatter(self.x1, self.x2, self.u, c='black', zorder=1)
        plt.title(title, fontsize=19)
        plt.xlabel('x1')
        plt.ylabel('x2')
        plt.grid(alpha=0.5)
        plt.savefig(path_to_save)
        plt.clf()


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    path.insert(1, '')
    global rho
    rho = float(argv[1])

    params_count = int(argv[2])
    if params_count == 3:
        from model_3parameters import *
    elif params_count == 4:
        from model_4parameters import *
    elif params_count == 6:
        from model_6parameters import *

    doDraw = bool(argv[3])

    print('Запушен код 1 лабораторной работы: {:d} параметров, шум {:d}%'.format(int(argv[2]), int(rho*100)))

    l1 = lab1()
    l1.save_table_1()
    doDraw = False
    if doDraw:
        l1.draw(False, 'исходная модель', 'before', None, None)
        l1.draw(False, 'исходная модель', 'before', 0, 0)
        l1.draw(False, 'исходная модель', 'before', 0, 90)
        l1.draw(True, 'помеха', 'after', None, None)
        l1.draw(True, 'помеха', 'after', 0, 0)
        l1.draw(True, 'помеха', 'after', 0, 90)
