def increase_drive_settings(robot, RobotConfig, increment=120):
    straight_speed = RobotConfig.STRAIGHT_SPEED + increment
    straight_accel = RobotConfig.STRAIGHT_ACCEL + increment
    turn_rate = RobotConfig.TURN_RATE + increment
    turn_accel = RobotConfig.TURN_ACCEL + increment

    robot.update_settings(
        robot._drive_base,
        straight_speed=straight_speed,
        straight_acceleration=straight_accel,
        turn_rate=turn_rate,
        turn_acceleration=turn_accel
    )


def restore_default_settings(robot):
    robot._set_default_settings()


def run0_left_collecting(robot, RobotConfig):
    # increase_drive_settings(robot, RobotConfig)
    robot.rotate_motor_degrees(120, 200, wait=False)
    robot.curve(360, 24)
    robot.gyro_drive(530)
    robot.wait_for_millis(200)
    robot.rotate_motor_degrees(-180, 200)
    #robot.gyro_drive(-150)
    robot.gyro_drive(-50)
    robot.curve(50, -40)
    robot.rotate_motor_degrees(angle=530, speed=600, motor="floopy")
    robot.rotate_motor_degrees(angle=-530, speed=600, motor="floopy")
    robot.curve(50, 20)
    robot.gyro_drive(155)
    robot.curve(25, -25)
    robot.rotate_motor_degrees(angle=550, speed=400, motor="floopy")
    robot.rotate_motor_degrees(angle=-550, speed=400, motor="floopy")
    robot.curve(-500, -110)
    robot._drive_base.stop()
    # restore_default_settings(robot)
    # robot.curve(-360, -24)
if __name__ == "__main__":
    from utils.base_robot import BaseRobot, RobotConfig

    test_robot = BaseRobot()
    run0_left_collecting(test_robot, RobotConfig)