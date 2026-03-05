#!/usr/bin/env python3
import sys
import rospy
from beginner_tutorials.srv import StringLength

def string_length_client(text):
    rospy.wait_for_service('string_length')  # 서버 대기
    try:
        get_length = rospy.ServiceProxy('string_length', StringLength)
        resp = get_length(text)
        return resp.length
    except rospy.ServiceException as e:
        rospy.logerr("서비스 호출 실패: %s", e)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("사용법: rosrun beginner_tutorials string_length_client.py [문자열]")
        sys.exit(1)

    rospy.init_node('string_length_client')
    text = sys.argv[1]
    result = string_length_client(text)
    rospy.loginfo("'%s'의 길이: %d", text, result)