from pybricks.parameters import Stop

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
    robot.curve(360, 24)
    robot.gyro_drive(500)
    robot.wait_for_millis(200)
    robot.rotate_motor_degrees(-120, 200,wait=Stop.HOLD)
    robot.gyro_drive(-350)
    robot.gyro_turn_absolute(80)
    robot.gyro_drive(-350)
    # restore_default_settings(robot)
    # robot.curve(-360, -24)
if __name__ == "__main__":
    from utils.base_robot import BaseRobot, RobotConfig

    test_robot = BaseRobot()
    run0_left_collecting(test_robot, RobotConfig)