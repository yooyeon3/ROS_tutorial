cmake_minimum_required(VERSION 3.0.2)
project(beginner_tutorials)

## C++ 11 표준 사용
add_compile_options(-std=c++11)

## 의존 패키지 검색 (message_generation이 반드시 포함되어야 합니다)
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

## 서비스 파일 등록 (이 부분이 빠져서 모듈을 찾지 못한 것입니다)
add_service_files(
  FILES
  AddTwoInts.srv
)

## 메시지 및 서비스 생성 호출
generate_messages(
  DEPENDENCIES
  std_msgs
)

## 패키지 구성 설정 (message_runtime이 포함되어야 합니다)
catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs message_runtime
)

## 인클루드 경로 설정
include_directories(
  ${catkin_INCLUDE_DIRS}
)

## 파이썬 스크립트 설치 설정 (오타 PROGRAMS 수정 완료)
catkin_install_python(PROGRAMS
  scripts/temp_sensor_pub.py
  scripts/temp_monitor_sub.py
  scripts/add_two_ints_server.py
  scripts/add_two_ints_client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
