#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from geometry_msgs.msg import PoseStamped

class Template:
    def __init__(self):
    	################## param input
    	###### private pram
        self._clock = rospy.get_param("~clock")
        input_topic = rospy.get_param("~input_topic")
        output_topic = rospy.get_param("~output_topic")
        ###### group yaml
        
        ##### central yaml
        
        ##################
        
        self.dt = 1.0/ self._clock
        self._pub = rospy.Publisher(output_topic, PoseStamped, queue_size=1)
        rospy.Subscriber(input_topic, PoseStamped, self.callback)
        rospy.Timer(rospy.Duration(self.dt), self.timer_callback)

    #############################################################
    # callback
    #############################################################

    def callback(self, msg):
        pass

    def timer_callback(self, event):
        pass
    #############################################################
    # main function
    #############################################################
    
    #############################################################
    # functions
    #############################################################


    #############################################################
    # spin
    #############################################################

    def spin(self):
        rate = rospy.Rate(self._clock)
        while not rospy.is_shutdown():
            rate.sleep()
    

if __name__ == "__main__":
    rospy.init_node("template", anonymous=True)
    node = Template()
    rospy.spin()
