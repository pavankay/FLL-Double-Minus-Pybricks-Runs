def increase_drive_settings(robot, RobotConfig, increment=50):
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


def run2_mast_and_treasure(robot, RobotConfig):
    increase_drive_settings(robot, RobotConfig)
    robot.gyro_drive(235)
    robot.curve(300, 95)
    robot.gyro_drive(100)
    robot.wait_for_millis(100)
    robot.gyro_drive(-75)
    robot.curve(-200, 60)
    robot.gyro_drive(-475)
    restore_default_settings(robot)


if __name__ == "__main__":
    from utils.base_robot import BaseRobot, RobotConfig

    test_robot = BaseRobot()
    run2_mast_and_treasure(test_robot, RobotConfig)