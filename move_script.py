#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

desc_flag1 = 0
desc_flag2 = 0

def move_joints():

    global desc_flag1,desc_flag2
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_state_publisher', anonymous=True)
    rate = rospy.Rate(5) 
    move = JointState()
    move.header = Header()
    move.header.stamp = rospy.Time.now()
    move.name = ['base_to_head_link', 'headlink_to_head']
    move.position = [ 0, 0]
    move.velocity = []
    move.effort = [] 

    while not rospy.is_shutdown():
        move.header.stamp = rospy.Time.now()
        if  desc_flag1 == 1 :
            move.position[0] -= 0.05
            if move.position[0] < -0.866: 
                desc_flag1 = 0
        elif  desc_flag1 == 0  :
            move.position[0] += 0.05
            if move.position[0] > 0:
		desc_flag1 = 1
        if  desc_flag2 == 1 :
            move.position[1] -= 0.1
            if move.position[1] <  -3:
		desc_flag2 = 0
        elif desc_flag2 == 0  :
            move.position[1] += 0.1
            if move.position[0] > 3:
		desc_flag2 = 1

        rospy.loginfo(move)
	pub.publish(move)
        rate.sleep()
	
if __name__ == '__main__':
    try:
        move_joints()
    except rospy.ROSInterruptException:
        pass