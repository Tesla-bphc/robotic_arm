#!/usr/bin/env python3
import rospy 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
from grid_arm_lite.msg import location
from detect import detect
bridge = CvBridge()
pub = rospy.Publisher('location', location, queue_size=1)
def callback(data):
    frame = bridge.imgmsg_to_cv2(data, "bgr8")
    boxes = detect(frame) 
    box = location()
    if boxes != []:
        box.x = boxes[0]
        box.y = boxes[1]
        box.width = boxes[2]
        box.height = boxes[3]
        rospy.loginfo(box)
        pub.publish(box)
    boxes=[]
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/camera/color/image_raw", Image, callback, queue_size=1)
    rospy.spin()

if __name__ == '__main__':
    listener()
