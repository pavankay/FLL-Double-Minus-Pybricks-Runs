from pybricks.parameters import Stop

def increase_drive_settings(robot, RobotConfig, increment=30):
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


def run6_sonar(robot, RobotConfig):
    increase_drive_settings(robot, RobotConfig)
    robot.curve(680, -66)
    robot.gyro_turn_absolute(0)
    robot.gyro_drive(100)
    robot.rotate_motor_degrees(-900, 200)
    robot.curve(-140, 50)
    robot.gyro_drive(-320)
    robot.gyro_turn_absolute(-10)
    robot.gyro_drive(-700)
    robot._drive_base.stop()

    restore_default_settings(robot)
if __name__ == "__main__":
    from utils.base_robot import BaseRobot, RobotConfig

    test_robot = BaseRobot()
    run6_sonar(test_robot, RobotConfig)