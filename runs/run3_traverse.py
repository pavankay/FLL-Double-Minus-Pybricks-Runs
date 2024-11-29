from pybricks.parameters import Stop

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


def run3_traverse(robot, RobotConfig):
    increase_drive_settings(robot, RobotConfig)
    robot.curve(860, 65)
    robot.gyro_turn_absolute(96)
    robot.gyro_drive(350)
    robot.gyro_drive(-230)
    robot.gyro_drive(40)
    robot.gyro_turn_absolute(70)
    robot.curve(1100, 35)
    robot.curve(460, 60)
    robot.gyro_drive(250)
    restore_default_settings(robot)

if __name__ == "__main__":
    from utils.base_robot import BaseRobot, RobotConfig

    test_robot = BaseRobot()
    run3_traverse(test_robot, RobotConfig)