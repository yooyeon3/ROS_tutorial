# 온도 조정 
#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

def callback(msg):
    # 온도가 35.0도 이상이면 경고 출력 (필터링 패턴)
    if msg.data >= 35.0:
        rospy.logwarn(f" [경고] 고온 감지! 현재 온도: {msg.data:.2f}°C")
    else:
        rospy.loginfo(f"정상 온도: {msg.data:.2f}°C")

def temp_subscriber():
    rospy.init_node('temp_monitor_node', anonymous=True)
    # 'temperature' 토픽을 구독하고 메시지가 오면 callback 실행
    rospy.Subscriber('temperature', Float32, callback)
    rospy.spin()

if __name__ == '__main__':
    temp_subscriber()


