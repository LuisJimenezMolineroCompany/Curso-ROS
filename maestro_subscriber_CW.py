#!/usr/bin/env python
# BEGIN ALL
#!/usr/bin/env python


# ROS libraries
import rospy
from std_msgs.msg import Int32

#Library of controller Maestro
import maestro as m

# BEGIN CALLBACK
def callback(msg):
    print "speed= ",msg.data
    # Maestro- (servomotors rotate in the same direction)
    s= m.Controller()
    s.setTarget(4,msg.data)
    s.setTarget(5,msg.data)
# END CALLBACK

rospy.init_node('Maestro_subscriber')

# BEGIN SUBSCRIBER
sub = rospy.Subscriber('speed', Int32, callback)
# END SUBSCRIBER

rospy.spin()
# END ALL
