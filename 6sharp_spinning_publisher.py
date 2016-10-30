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
izq=4
dcho=5

rospy.init_node('topic_sharp')

# BEGIN PUB
pub = rospy.Publisher('sharp', Int32,queue_size=10)
pub = rospy.Publisher('left_servo', Int32,queue_size=10)
pub = rospy.Publisher('right_servo', Int32,queue_size=10)
# END PUB

# BEGIN LOOP
s= m.Controller()
rate = rospy.Rate(0.5)

while not rospy.is_shutdown():
        d_min=s.getPosition(sharp)
        d_max=s.getPosition(sharp)
        dist=0.5*(d_min+d_max)
        #Publish sharp data
        pub.publish(dist)
        # Wait 2 seconds [when rospy.Rate(0.5)]
        rate.sleep()

        s.setTarget(izq,1)
        s.setTarget(dcho,1)
        pos_servo_izq=s.getPosition(izq)
        pos_servo_dcho=s.getPosition(dcho)
        # Publish both servos positions
        pub.publish(pos_servo_izq)
        pub.publish(pos_servo_dcho)
        # Wait 2 seconds [when rospy.Rate(0.5)]
        rate.sleep()

        s.setTarget(izq,0)
        s.setTarget(dcho,0)
        rate.sleep()
        
# END LOOP
# END ALL
