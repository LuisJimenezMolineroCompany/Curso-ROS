#!/usr/bin/env python
# BEGIN ALL
# BEGIN SHEBANG
#!/usr/bin/env python
# END SHEBANG

# Publisher of the distance data of the Sharp sensor of JUS

# BEGIN IMPORT
import rospy
#Library of controller Maestro
import maestro as m
# END IMPORT

# BEGIN STD_MSGS
from std_msgs.msg import Int32
# END STD_MSGS

# Maestro channel assignment
sharp=0

rospy.init_node('topic_sharp')

# BEGIN PUB
pub = rospy.Publisher('sharp', Int32,queue_size=10)
# END PUB

# BEGIN LOOP
s= m.Controller()
rate = rospy.Rate(2)

while not rospy.is_shutdown():
        d_min=s.getPosition(sharp)
        d_max=s.getPosition(sharp)
        dist=0.5*(d_min+d_max)
        pub.publish(dist)
        rate.sleep()
# END LOOP
# END ALL
