def increase_drive_settings(robot, RobotConfig, increment=70):
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


def run1_shark_and_coral(robot, RobotConfig):
    increase_drive_settings(robot, RobotConfig)
    robot.curve(360, 25)
    robot.gyro_drive(600)
    robot.gyro_turn_absolute(-90)
    robot.gyro_drive(120)
    robot.gyro_drive(-120)
    robot.gyro_turn_absolute(-50)
    robot.gyro_drive(230)
    robot.curve(-410, -140)
    robot._drive_base.stop()
    restore_default_settings(robot)


if __name__ == "__main__":
    from utils.base_robot import BaseRobot, RobotConfig

    test_robot = BaseRobot()
    run1_shark_and_coral(test_robot, RobotConfig)