#!/usr/bin/env python
import csv
import numpy as np
import matplotlib.pyplot as plt


def main():
    angular_x = []
    angular_y = []
    angular_z = []
    acc_x = []
    acc_y = []
    acc_z = []
    with open('imu_data.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            angular_x.append(float(row[0]))
            angular_y.append(float(row[1]))
            angular_z.append(float(row[2]))
            acc_x.append(float(row[3]))
            acc_y.append(float(row[4]))
            acc_z.append(float(row[5]))

    data = np.array([angular_x, angular_y, angular_z, acc_x, acc_y, acc_z])
    print(f'convariance_matrix in order of[angular_x, angular_y, angular_z, '
          f'acc_x, acc_y, acc_z] :\n{np.cov(data)}')

    # histogram
    fig = plt.figure(num='histogram', figsize=[12, 9])
    vx = fig.add_subplot(2, 3, 1)
    vy = fig.add_subplot(2, 3, 2)
    vz = fig.add_subplot(2, 3, 3)
    ax = fig.add_subplot(2, 3, 4)
    ay = fig.add_subplot(2, 3, 5)
    az = fig.add_subplot(2, 3, 6)
    vx.hist(np.array(angular_x), bins=50)
    vx.set_title('angular_x')
    vx.set_xlabel('rad/s')
    vy.hist(np.array(angular_y), bins=50)
    vy.set_title('angular_y')
    vy.set_xlabel('rad/s')
    vz.hist(np.array(angular_z), bins=50)
    vz.set_title('angular_z')
    vz.set_xlabel('rad/s')
    ax.hist(np.array(acc_x), bins=50)
    ax.set_title('acc_x')
    ax.set_xlabel('m/s^2')
    ay.hist(np.array(acc_y), bins=50)
    ay.set_title('acc_y')
    ay.set_xlabel('m/s^2')
    az.hist(np.array(acc_z), bins=50)
    az.set_title('acc_z')
    az.set_xlabel('m/s^2')

    # covariance
    point_size = 0.5
    fig = plt.figure(num='covariance', figsize=[20, 9])
    plt.subplots_adjust(wspace=0.4, hspace=0.6)
    ###
    vx_vy = fig.add_subplot(3, 5, 1)
    vx_vy.scatter(np.array(angular_x), np.array(angular_y), s=point_size)
    vx_vy.set_xlabel('angular_vel_x[rad/s]')
    vx_vy.set_ylabel('angular_vel_y[rad/s]')

    vx_vz = fig.add_subplot(3, 5, 2)
    vx_vz.scatter(np.array(angular_x), np.array(angular_z), s=point_size)
    vx_vz.set_xlabel('angular_vel_x[rad/s]')
    vx_vz.set_ylabel('angular_vel_y[rad/s]')

    vy_vz = fig.add_subplot(3, 5, 3)
    vy_vz.scatter(np.array(angular_y), np.array(angular_z), s=point_size)
    vy_vz.set_xlabel('angular_vel_y[rad/s]')
    vy_vz.set_ylabel('angular_vel_z[rad/s]')
    #####
    vx_ax = fig.add_subplot(3, 5, 4)
    vx_ax.scatter(np.array(angular_x), np.array(acc_x), s=point_size)
    vx_ax.set_xlabel('angular_vel_x[rad/s]')
    vx_ax.set_ylabel('acceleration_x[m/s^2]')

    vx_ay = fig.add_subplot(3, 5, 5)
    vx_ay.scatter(np.array(angular_x), np.array(acc_y), s=point_size)
    vx_ay.set_xlabel('angular_vel_x[rad/s]')
    vx_ay.set_ylabel('acceleration_y[m/s^2]')

    vx_az = fig.add_subplot(3, 5, 6)
    vx_az.scatter(np.array(angular_x), np.array(acc_z), s=point_size)
    vx_az.set_xlabel('angular_vel_x[rad/s]')
    vx_az.set_ylabel('acceleration_z[m/s^2]')
    #####
    vy_ax = fig.add_subplot(3, 5, 7)
    vy_ax.scatter(np.array(angular_y), np.array(acc_x), s=point_size)
    vy_ax.set_xlabel('angular_vel_y[rad/s]')
    vy_ax.set_ylabel('acceleration_x[m/s^2]')

    vy_ay = fig.add_subplot(3, 5, 8)
    vy_ay.scatter(np.array(angular_y), np.array(acc_y), s=point_size)
    vy_ay.set_xlabel('angular_vel_y[rad/s]')
    vy_ay.set_ylabel('acceleration_y[m/s^2]')

    vy_az = fig.add_subplot(3, 5, 9)
    vy_az.scatter(np.array(angular_y), np.array(acc_z), s=point_size)
    vy_az.set_xlabel('angular_vel_y[rad/s]')
    vy_az.set_ylabel('acceleration_z[m/s^2]')
    ####
    vz_ax = fig.add_subplot(3, 5, 10)
    vz_ax.scatter(np.array(angular_z), np.array(acc_x), s=point_size)
    vz_ax.set_xlabel('angular_vel_z[rad/s]')
    vz_ax.set_ylabel('acceleration_x[m/s^2]')

    vz_ay = fig.add_subplot(3, 5, 11)
    vz_ay.scatter(np.array(angular_z), np.array(acc_y), s=point_size)
    vz_ay.set_xlabel('angular_vel_z[rad/s]')
    vz_ay.set_ylabel('acceleration_y[m/s^2]')

    vz_az = fig.add_subplot(3, 5, 12)
    vz_az.scatter(np.array(angular_z), np.array(acc_z), s=point_size)
    vz_az.set_xlabel('angular_vel_z[rad/s]')
    vz_az.set_ylabel('acceleration_z[m/s^2]')
    ###
    ax_ay = fig.add_subplot(3, 5, 13)
    ax_ay.scatter(np.array(acc_x), np.array(acc_y), s=point_size)
    ax_ay.set_xlabel('acceleration_x[m/s^2]')
    ax_ay.set_ylabel('acceleration_y[m/s^2]')

    ax_az = fig.add_subplot(3, 5, 14)
    ax_az.scatter(np.array(acc_x), np.array(acc_z), s=point_size)
    ax_az.set_xlabel('acceleration_x[m/s^2]')
    ax_az.set_ylabel('acceleration_z[m/s^2]')

    ay_az = fig.add_subplot(3, 5, 15)
    ay_az.scatter(np.array(acc_y), np.array(acc_z), s=point_size)
    ay_az.set_xlabel('acceleration_y[m/s^2]')
    ay_az.set_ylabel('acceleration_z[m/s^2]')

    plt.show()


if __name__ == '__main__':
    main()
