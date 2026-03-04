#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    # 메시지를 받았을 때 실행되는 함수입니다. 받은 내용을 출력합니다.
    rospy.loginfo(rospy.get_caller_id() + " I heard %s", data.data)

def listener():
    # 노드 이름을 'listener'라고 정합니다.
    rospy.init_node('listener', anonymous=True)
    # 'chatter'라는 토픽을 구독하고, 메시지가 오면 callback 함수를 실행합니다.
    rospy.Subscriber("chatter", String, callback)
    # 노드가 종료될 때까지 계속 기다립니다.
    rospy.spin()

if __name__ == '__main__':
    listener()