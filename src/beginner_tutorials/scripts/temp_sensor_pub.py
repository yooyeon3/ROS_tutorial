#!/usr/bin/env python3
import rospy
import random
from std_msgs.msg import Float32

def temp_publisher():
    # 'temperature' 토픽으로 Float32 메시지를 발행하도록 설정
    pub = rospy.Publisher('temperature', Float32, queue_size=10)
    rospy.init_node('temp_sensor_simulator', anonymous=True)
    rate = rospy.Rate(1)  # 1Hz (1초에 1번)

    while not rospy.is_shutdown():
        # 20.0 ~ 40.0 사이의 랜덤 실수 생성
        current_temp = random.uniform(20.0, 40.0)
        rospy.loginfo(f"발행 중인 온도: {current_temp:.2f}°C")
        pub.publish(current_temp)
        rate.sleep()

if __name__ == '__main__':
    try:
        temp_publisher()
    except rospy.ROSInterruptException:
        pass
