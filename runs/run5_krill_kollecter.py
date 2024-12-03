from pybricks.parameters import Stop

def increese_drive_settings(robot, RobotConfig, increment=-10):
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


def run5_krill_kollecter(robot, RobotConfig):
    increese_drive_settings(robot, RobotConfig)
    robot.curve(150, -20)
    robot.gyro_drive(620)
    robot.gyro_turn_absolute(20)

    robot.update_settings(
        robot._drive_base,
        straight_speed=600,
        straight_acceleration=600,
        turn_rate=150,
        turn_acceleration=360
    )

    robot.gyro_drive(150)
    robot._set_default_settings()

    robot.gyro_drive(-155)
    robot.curve(-400, 70)
    # robot.curve(3500, -35)
    # robot.gyro_drive(150)
    # robot.curve(325, 45)
    # robot.gyro_drive(125)
    robot._drive_base.stop()
    restore_default_settings(robot)

if __name__ == "__main__":
    from utils.base_robot import BaseRobot, RobotConfig

    test_robot = BaseRobot()
    run5_krill_kollecter(test_robot, RobotConfig)