#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import Twist, PoseStamped
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from math import atan2
import csv

# PID gains (will change via simulation)
kp = 2
kd = 0.0
ki = 0.0

class Robot:
    def __init__(self):
        
        rospy.init_node('robot_control')
        
        #self.path = []
        self.current_pose = None
        self.waypoints = []
        
        # Read waypoints from file
        with open('/home/parthag/mech_ws/src/mp_controls/scripts/output_array.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            
            for row in reader:
                self.waypoints.append((float(row[0]), float(row[1])))
        
        #self.path_sub = rospy.Subscriber('/path', Path, self.path_callback)
        self.sub_odom = rospy.Subscriber('/odom', Odometry, self.pose_callback)
        self.vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        
        # Initialize PID controller variables
        self.prev_error = 0.0
        self.integral_error = 0.0
        self.rate = rospy.Rate(10)

# class Robot:
#     def __init__(self):
        
#         rospy.init_node('robot_control', anonymous=False)
        
#         #self.path = []
#         self.waypoints = []
#         self.current_pose = None
        
#         self.path_sub = rospy.Subscriber('/path', Path, self.path_callback)
#         self.sub_odom = rospy.Subscriber('/odom', Odometry, self.pose_callback)
#         self.vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        
#         # Initialize PID controller variables
#         self.prev_error = 0.0
#         self.integral_error = 0.0
        
#         self.rate = rospy.Rate(10)
    
    def path_callback(self, msg):
        self.waypoints=msg.poses 
    
    def pose_callback(self, msg):
        self.current_pose = msg.pose.pose
        #global robot_angle
        #euler_angles= euler_from_quaternion(
        #[msg.pose.pose.orientation.x,
        #msg.pose.pose.orientation.y,
        #msg.pose.pose.orientation.z,
        #msg.pose.pose.orientation.w])
        #robot_angle = euler_angles[2]
    
    def run(self):
        while not rospy.is_shutdown():
            if not self.current_pose:
                continue
            
            x = self.current_pose.position.x
            y = self.current_pose.position.y
            
            orientation = self.current_pose.orientation
            (roll, pitch, yaw) = euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])
            
            # Angle to the next point in the path
            i=0
            next_point = self.waypoints[i]
            dx = next_point[0] - x
            dy = next_point[1] - y
            target_angle = atan2(dy, dx)
            
            # Error
            error = target_angle - yaw
            
            # Derivative and integral errors
            derivative_error = error - self.prev_error
            self.prev_error = error
            self.integral_error += error
            
            # Computing control command
            angular_vel = kp * error + kd * derivative_error + ki * self.integral_error
            twist = Twist()
            
            # Checking if the robot has reached the next point
            if abs(dx) > 0.1 or abs(dy) > 0.1:
                
                # Only move if the robot is pointing to the target point
                if abs(error) < 0.1:
                    twist.angular.z = 0.0
                    twist.linear.x = 0.4
                    self.vel_pub.publish(twist)
                else:
                    twist.angular.z = angular_vel
                    twist.linear.x = 0.0
                    self.vel_pub.publish(twist)
                    
            else:    
                self.waypoints.pop(0)
                self.prev_error = 0.0
                self.integral_error = 0.0
                i=i+1
            
            # Stop the robot if there are no more waypoints
            if not self.waypoints:
                twist.angular.z = 0.0
                twist.linear.x = 0.0
                self.vel_pub.publish(twist)
            
            self.rate.sleep()


if __name__ == '__main__':
    robot = Robot()
    robot.run()