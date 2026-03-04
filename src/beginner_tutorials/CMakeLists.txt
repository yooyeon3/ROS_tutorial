cmake_minimum_required(VERSION 3.0.2)
project(beginner_tutorials)

## C++ 11 표준 사용
add_compile_options(-std=c++11)

## 의존 패키지 검색
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

## 패키지 구성 설정
catkin_package(
  CATKIN_DEPENDS roscpp rospy std_msgs message_runtime
)

## 인클루드 경로 설정
include_directories(
  ${catkin_INCLUDE_DIRS}
)

## 실행 파일 설정 예시 (필요 시 주석 해제 후 파일명 수정)
# add_executable(${PROJECT_NAME}_node src/beginner_tutorials_node.cpp)
# target_link_libraries(${PROJECT_NAME}_node ${catkin_LIBRARIES})

# 파일 맨 마지막에 정확히 붙여넣으세요
catkin_install_python(PROGRAMS
  scripts/talker.py
  scripts/listener.py
  scripts/counter_pub.py
  scripts/counter_sub.py
  scripts/counter_even_sub.py
  scripts/temp_sensor_pub.py
  scripts/temp_monitor_sub.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
