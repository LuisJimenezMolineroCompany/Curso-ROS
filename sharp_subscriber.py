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
sub = rospy.Subscriber('sharp', Int32, callback)
# END SUBSCRIBER

rospy.spin()
# END ALL
