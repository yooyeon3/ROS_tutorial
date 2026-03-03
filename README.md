#  ROS development 
- Ubuntu 20.04 
- ROS neotic

# ROS install 
1. source list  
```bash 
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```
2. Set up your keys
```bash 
sudo apt install curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```
3. Installation 
```bash
sudo apt update
```
```bash
sudo apt install ros-noetic-desktop-full
```

4. Environment setup
```bash 
source /opt/ros/noetic/setup.bash
```
```bash 
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
```
5. Create a ROS Workspace

```bash 
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```
```bash
source devel/setup.bash
```
```bash
echo $ROS_PACKAGE_PATH
```


# 거북이 제어 과제 
- 거북이를 제어하기에 앞서, 터미널창 3개를 키고 
- 첫번째 창에서
```bash
 rscore
```
- 두번째 창 (거북이 화면 실행)
```bash
turtlesim turtlesim_node 
```
- 세번째 창 (키보드로 거북이를 제어, 
그 cmd 창에서 거북이 창을 켜 방향키로 제어)
  
```bash
rosrun turtlesim turtle_teleop_key
```
# 2번째 과제 
- 과제 2: /turtle1/pose 관찰
---
# 확인 방법
```bash
$ rostopic echo /turtle1/pose
```
이 커맨드를 실행하게 되면,
<pre>x: 2.1755874156951904
y: 5.136660099029541
theta: -1.0351853370666504
linear_velocity: 2.0
angular_velocity: 0.0
</pre>
---
- 이런식으로 결과값이 나오게 되는데, x의 값은 좌우조정할 때 마다, 변경되고( 가로축 기준이며, 오른쪽으로 갈 수록 값이 커진다 )
- y값은 세로축이 변경될때마다( 즉, 위로올라갈때는 값이 커지고 반대는 작아진다. )
- theta는 라디안을 의미하며, 방향을 의미한다. 
좌회전을 할수록 값이 커진다
- linear_velocity와 angular_velocity는 
각각 직진속도와 회전속도를 의미하는데, 
회전을 하게되면  angular_velocity(각도 속도)로
좌회전시에는 , 2.0 우회전 시 - 2.0으로 설정돼있다.
- linear_velocity는 직진속도로 2.0으로 조정돼있다. 

# 3번째 과제
  토픽/메시지 구조 정리
-- 
- rostopic list의 모든 토픽에 대해 rostopic type + rosmsg show로 메시지 구조를 확인하고 README에 정리


# 1단계: 토픽 목록 확인

```bash
$ rostopic list

결과값 
-----------------------------
/turtle1/cmd_vel

/turtle1/color_sensor

/turtle1/pose
-----------------------------
```

- rostopic은 현재 실행중인 토픽들의 리스트를 나타냄
여기서 cmd_vel은 command_velocity로 
거북이에게 속도 명령을 내리는 토픽

- color_sensor은 거북이가 지나가는 바닥 색의 정보를 나타내는 토픽
(R G B 각각 레드,그린,블루를 나타냄)

- pose는 거북이의 자세로, 위치와 방향을 나타내는 토픽이다.(x좌표, y좌표, 라디안값, linear_velocity, angular_velocity)


# 2단계: 토픽의 메시지 타입 확인

```bash
$ rostopic type /turtle1/cmd_vel
----------------------------------------
결과값
----------------------------------------
geometry_msgs/Twist
```
-메세지 타입을 확인할 수 있는데, geometry_msgs/Twist에서 twist는, 내부값을 확인해야만 보인다.
그래서 밑의 명령어를 실행하여 내부값을 확인해보면,

# 3단계: 메시지 구조 확인

```bash
$ rosmsg show geometry_msgs/Twist
---------------------------------
결과값
---------------------------------
geometry_msgs/Vector3 linear
  float64 x
  float64 y
  float64 z

geometry_msgs/Vector3 angular
  float64 x
  float64 y
  float64 z
```
위와  같이 나오게 된다. 
--
- 위의 linear은 직진속도(위,아래 방향키 값을 나타내고)

- angular는 회전(좌우 방향키 값(방향)을 나타낸다)

정리 : linear.x → 앞뒤 이동

angular.z → 회전

** 나머지는 사용하지 않음. ( 거북이 실행창은 
2D 평면이므로 )

---
# 과제 4:  rostopic pub으로 정사각형 그리기

