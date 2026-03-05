#!/usr/bin/env python3
import rospy
from beginner_tutorials.srv import AddTwoInts, AddTwoIntsResponse

def handle_calc(req):
    # 파라미터 서버에서 'operator' 값을 읽어옵니다. (없을 경우 기본값 'add')
    op = rospy.get_param('/operator', 'add')

    if op == 'add':
        result = req.a + req.b
    elif op == 'sub':
        result = req.a - req.b
    elif op == 'mul':
        result = req.a * req.b
    else:
        rospy.logwarn("알 수 없는 연산: %s → 기본값 add 사용", op)
        result = req.a + req.b
        op = 'add'

    rospy.loginfo("[%s] %d, %d → %d", op, req.a, req.b, result)
    return AddTwoIntsResponse(result)

def server():
    rospy.init_node('calc_server')
    # 서비스 이름은 'calc'로 등록합니다.
    rospy.Service('calc', AddTwoInts, handle_calc)
    rospy.loginfo("계산기 서버 시작 (operator 파라미터로 연산 변경)")
    rospy.spin()

if __name__ == '__main__':
    server()