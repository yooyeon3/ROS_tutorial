#!/usr/bin/env python3
import rospy
# turtlesim 패키지의 Pose 메시지를 가져옵니다.
from turtlesim.msg import Pose

def callback(msg):
    # rosmsg show에서 확인한 필드명(x, y, theta)으로 접근합니다.
    rospy.loginfo("위치: x=%.2f, y=%.2f, 방향=%.2f", msg.x, msg.y, msg.theta)

def listener():
    rospy.init_node('pose_listener')
    # '/turtle1/pose' 토픽을 구독하고 메시지가 오면 callback 실행
    rospy.Subscriber('/turtle1/pose', Pose, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()