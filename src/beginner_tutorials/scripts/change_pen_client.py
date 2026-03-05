#!/usr/bin/env python3
import rospy
# turtlesim 패키지의 SetPen 서비스 타입을 가져옵니다.
from turtlesim.srv import SetPen

def change_pen(r, g, b, width):
    # 서비스가 사용 가능해질 때까지 기다립니다.
    rospy.wait_for_service('/turtle1/set_pen')
    try:
        # 서비스 프록시 생성
        set_pen = rospy.ServiceProxy('/turtle1/set_pen', SetPen)
        # r, g, b, width, off(0이면 펜 사용, 1이면 펜 끄기)
        set_pen(r, g, b, width, 0)
        rospy.loginfo("펜 변경 완료: R=%d G=%d B=%d 두께=%d", r, g, b, width)
    except rospy.ServiceException as e:
        rospy.logerr("서비스 호출 실패: %s", e)

if __name__ == '__main__':
    rospy.init_node('change_pen_client')
    # 초록색(R:0, G:255, B:0), 두께 5로 변경 요청
    change_pen(255, 0, 255, 3)
    #보라색: change_pen(255, 0, 255, 3)
    #노란색: change_pen(255, 255, 0, 10)