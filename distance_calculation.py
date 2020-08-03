#!/usr/bin/env python3
import rospy 
from sensor_msgs.msg import Image
from grid_arm_lite.msg import location
from cv_bridge import CvBridge, CvBridgeError
import cv2
from detect import detect
bridge = CvBridge()
box = []
def callback1(data):
    global box
    box=[data.x, data.y, data.width, data.height]
def callback2(data):
    global box
    cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="32FC1")
    print(box)
    image = cv2.rectangle(cv_image, (box[0],box[1]), (box[2] + box[0],box[3]+box[1]),(255, 0, 0), 2) 
    cv2.imshow("output",image)
    cv2.waitKey(1)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("location", location, callback1, queue_size=1)
    rospy.Subscriber("/camera/depth/image_raw", Image, callback2, queue_size=1)
    rospy.spin()

if __name__ == '__main__':
    listener()
