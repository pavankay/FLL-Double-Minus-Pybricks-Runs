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

    robot.rotate_motor_degrees(140, 200, wait=False)
    robot.curve(360, 24)
    robot.gyro_drive(530)
    robot.wait_for_millis(200)
    robot.rotate_motor_degrees(-180, 200)
    robot.gyro_drive(-100)
    robot.curve(100, -30)
    robot.rotate_motor_degrees(angle=500, motor="floopy",speed=600, wait=True)
    robot.wait_for_millis(200)
    robot.rotate_motor_degrees(angle=-500, motor="floopy", speed=600, wait=True)
    robot.curve(100, 10)
    robot.gyro_drive(250)
    robot.gyro_drive(-70)
    robot.curve(100, -15)
    robot.rotate_motor_degrees(angle=690, motor="floopy", speed=600, wait=True)
    robot.wait_for_millis(200)
    robot.rotate_motor_degrees(angle=-690, motor="floopy", speed=600, wait=True)
    robot.gyro_drive(-300)
    robot.gyro_turn_absolute(50)
    robot.gyro_drive(-850)
    restore_default_settings(robot)
    # robot.rotate_motor_degrees(-140, 200, wait=True)
    robot._drive_base.stop()

if __name__ == "__main__":
    from utils.base_robot import BaseRobot, RobotConfig

    test_robot = BaseRobot()
    run0_left_collecting(test_robot, RobotConfig)