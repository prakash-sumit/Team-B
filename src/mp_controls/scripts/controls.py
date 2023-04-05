#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import Twist, PoseStamped
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from math import atan2

# PID gains (will change via simulation)
kp = 1.0
kd = 0.2
ki = 0.02

class Robot:
    def __init__(self):
        
        rospy.init_node('robot_control')
        
        self.path = []
        self.current_pose = None
        
        self.path_sub = rospy.Subscriber('/path', Path, self.path_callback)
        #self.pose_sub = rospy.Subscriber('/pose', PoseStamped, self.pose_callback)
        self.sub_odom = rospy.Subscriber('/odom', Odometry, self.pose_callback)
        self.vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        
        # Initialize PID controller variables
        self.prev_error = 0.0
        self.integral_error = 0.0
        
        self.rate = rospy.Rate(10)
    
    def path_callback(self, msg):
        self.path = msg.poses
    
    def pose_callback(self, msg):
        #self.current_pose = msg.pose
        self.current_pose =msg.pose.pose
    
    def run(self):
        while not rospy.is_shutdown():
            if not self.path or not self.current_pose:
                continue
            
            x = self.current_pose.position.x
            y = self.current_pose.position.y
            
            orientation = self.current_pose.orientation
            (roll, pitch, yaw) = euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])
            
            # Angle to the next point in the path
            next_point = self.path[0].pose.position
            dx = next_point.x - x
            dy = next_point.y - y
            target_angle = atan2(dy, dx)
            
            # Error
            error = target_angle - yaw
            
            # Derivative and integral errors
            derivative_error = error - self.prev_error
            self.prev_error = error
            self.integral_error += error
            
            # Computing control command
            angular_vel = kp * error + kd * derivative_error + ki * self.integral_error
            
            # Publish control command
            twist = Twist()
            twist.linear.x = 0.2 
            twist.angular.z = angular_vel
            self.vel_pub.publish(twist)
            
            # Checking if the robot has reached the next point
            if abs(dx) < 0.1 and abs(dy) < 0.1:
                self.path.pop(0) #have to understand from mp peeps
                self.prev_error = 0.0
                self.integral_error = 0.0
            
            self.rate.sleep()


if __name__ == '__main__':
    robot = Robot()
    robot.run()
    