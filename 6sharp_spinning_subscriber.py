#!/usr/bin/env python
# BEGIN ALL
#!/usr/bin/env python


import rospy
from std_msgs.msg import Int32


# BEGIN CALLBACK
def callback(msg):
    print msg.data
# END CALLBACK


rospy.init_node('sharp_subscriber')

# BEGIN SUBSCRIBER
sharp = rospy.Subscriber('sharp', Int32, callback)
left = rospy.Subscriber('left_servo', Int32, callback)
right = rospy.Subscriber('right_servo', Int32, callback)
# END SUBSCRIBER

rospy.spin()
# END ALL
