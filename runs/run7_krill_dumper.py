

def increase_drive_settings(robot, RobotConfig, increment=20):
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


def run7_krill_dumper(robot, RobotConfig):
    restore_default_settings(robot)
    increase_drive_settings(robot, RobotConfig)
    robot.curve(600, -48)
    robot.curve(120, 91)
    robot.update_settings(
        robot._drive_base,
        straight_speed=100,
        straight_acceleration=200,
        turn_rate=RobotConfig.TURN_RATE,
        turn_acceleration=RobotConfig.TURN_ACCEL
    )
    robot.gyro_drive(400)
    robot.wait_for_millis(400)
    restore_default_settings(robot)
    robot.gyro_drive(-100)
    robot.curve(-250, 70)
    robot.gyro_drive(-650)
    restore_default_settings(robot)

if __name__ == "__main__":
    from utils.base_robot import BaseRobot, RobotConfig

    test_robot = BaseRobot()
    run7_krill_dumper(test_robot, RobotConfig)