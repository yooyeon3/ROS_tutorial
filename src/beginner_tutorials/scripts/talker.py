#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    # 'chatter'라는 토픽으로 String 메시지를 보내는 publisher 설정
    pub = rospy.Publisher('chatter', String, queue_size=10)
    # 노드 이름 초기화
    rospy.init_node('talker', anonymous=True)
    # 10Hz 주기로 실행 (1초에 10번)
    rate = rospy.Rate(10) 
    
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str) # 터미널에 출력
        pub.publish(hello_str)   # 토픽 발행
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass