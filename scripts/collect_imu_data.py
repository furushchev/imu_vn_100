import os
import csv
import rospy
from sensor_msgs.msg import Imu

SAMPLE_NUM = 1E4
FILE = 'imu_data.csv'
g_count = 0


def imu_cb(data):
    global g_count
    if g_count < SAMPLE_NUM:
        with open(FILE, 'a') as f:
            writer = csv.writer(f)
            line = (
                f'{data.angular_velocity.x}{data.angular_velocity.y}'
                f'{data.angular_velocity.z}{data.linear_acceleration.x}'
                f'{data.linear_acceleration.y}{data.linear_acceleration.z}')
            writer.writerow(line)

    if g_count == SAMPLE_NUM:
        print('collect finish')
        rospy.signal_shutdown('collect finish')

    g_count += 1


def main():
    if os.path.exists(FILE):
        os.remove(FILE)
    rospy.init_node('imu_data_collector')
    rospy.Subscriber('/imu/data', Imu, imu_cb, queue_size=10)
    # rospy.Subscriber('/base_link/imu', Imu, imu_cb, queue_size=100)
    rospy.spin()


if __name__ == '__main__':
    main()
