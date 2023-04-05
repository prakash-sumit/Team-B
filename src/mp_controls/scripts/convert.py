#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped
import csv

def convert():
    pub = rospy.Publisher('/path', Path, queue_size=10)
    rospy.init_node('convert', anonymous=False)
    rate = rospy.Rate(10) # 10hz
    p = Path()
    p.poses = []  # initialize poses as an empty list
    while not rospy.is_shutdown():
        with open('/home/parthag/mech_ws/src/mp_controls/scripts/output_array.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            
            for row in reader:
                pose = PoseStamped()
                pose.pose.position.x = float(row[0])
                pose.pose.position.y = float(row[1])
                p.poses.append(pose)
                
        pub.publish(p)
        rate.sleep()


if __name__ == '__main__':
    try:
        convert()
    except rospy.ROSInterruptException:
        pass
