from pybricks.parameters import Stop

def decreese_drive_settings(robot, RobotConfig, increment=-20):
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


def run4_octopus(robot, RobotConfig):
    decreese_drive_settings(robot, RobotConfig)
    robot.curve(130, -46)
    robot.gyro_drive(550)
    robot.gyro_drive(-400)
    robot.gyro_turn_absolute(-30)
    robot.gyro_drive(-400)
    restore_default_settings(robot)
if __name__ == "__main__":
    from utils.base_robot import BaseRobot, RobotConfig

    test_robot = BaseRobot()
    run4_octopus(test_robot, RobotConfig)