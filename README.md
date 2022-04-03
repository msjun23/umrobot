# umrobot_description
**Capstone Design 2022, Universal Mobile Robot Platform for gazebo simulation.**

3D Model Designer: [Taegyeom Gim](https://github.com/GYEOMGYEOM)

---

|||
|---|---|
|OS| Ubuntu 18.04|
|ROS| Melodic|
|Sensor| Realsense|
||2D LiDAR|

# Requirement
Sensor plugin must be installed.

- [Intel RealSense gazebo plugin](https://github.com/nilseuropa/realsense_ros_gazebo)
```bash
$ cd ~/catkin_ws/src
$ git clone https://github.com/nilseuropa/realsense_ros_gazebo.git
$ cd ~/catkin_ws && catkin_make
```

- [velodyne_description](https://bitbucket.org/DataspeedInc/velodyne_simulator/src/master/)
```bash
$ cd ~/catkin_ws/src
$ git clone https://bitbucket.org/DataspeedInc/velodyne_simulator.git
$ cd ~/catkin_ws && catkin_make
```

# About LiDAR
Used Velodyne VLP-16 3d model, but applied [RPLiDAR S1](https://www.slamtec.com/en/Lidar/S1) spcification.

![gazebo](images/gazebo.png)

![rviz](images/rviz.png)

# Nuri building 3rd floor gazebo world

**2022.04.02**: Updated Nuri building gazebo world(not real size).

![gazebo](images/nuri_gazebo.png)

![rviz](images/nuri_rviz.png)
