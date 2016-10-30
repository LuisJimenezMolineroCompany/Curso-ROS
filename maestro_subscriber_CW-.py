#!/usr/bin/env python
# BEGIN ALL
#!/usr/bin/env python

# Subscriber to make JUS rotate clockwise to the speed published in topic '/speed'

# ROS libraries
import rospy
from std_msgs.msg import Int32

#Library of controller Maestro
import maestro as m

# Maestro channel assignment
izq = 4
dcho = 5

# BEGIN CALLBACK
def callback(msg):
    print "speed= ",msg.data
    # Maestro- (servomotors rotate in the same direction)
    s= m.Controller()
    speed=msg.data
    s.setTarget(izq,-speed)
    s.setTarget(dcho,-speed)
# END CALLBACK

rospy.init_node('Maestro_subscriber')

# BEGIN SUBSCRIBER
sub = rospy.Subscriber('speed', Int32, callback)
# END SUBSCRIBER

rospy.spin()
# END ALL
