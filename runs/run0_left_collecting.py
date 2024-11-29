


def increase_drive_settings(robot, RobotConfig, increment=60):
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
    increase_drive_settings(robot, RobotConfig)

    try:
        robot.curve(360, 25)
        robot.gyro_drive(600)
        robot.wait_for_millis(200)
        robot.gyro_drive(-300)
        robot.gyro_drive(-500)

    finally:
        restore_default_settings(robot)


if __name__ == "__main__":
    from utils.base_robot import BaseRobot, RobotConfig

    test_robot = BaseRobot()
    run0_left_collecting(test_robot, RobotConfig)