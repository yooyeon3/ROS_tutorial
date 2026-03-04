#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    # 메시지를 받았을 때 실행되는 함수
    rospy.loginfo(rospy.get_caller_id() + " I heard %s", data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    # 'chatter' 토픽을 구독하고, 메시지가 오면 callback 함수 실행
    rospy.Subscriber("chatter", String, callback)
    # 노드가 종료될 때까지 대기
    rospy.spin()

if __name__ == '__main__':
    listener()
