from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Axis, Stop
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait

class RobotConfig:
    """
    Configuration constants for the BaseRobot class.
    """
    TIRE_DIAMETER = 88
    AXLE_TRACK = 104
    STRAIGHT_SPEED = 400
    STRAIGHT_ACCEL = 600
    TURN_RATE = 150
    TURN_ACCEL = 360
    MAX_SPEED = 977
    MIN_SPEED = -977

class BaseRobot:
    """
    Base class for controlling a LEGO SPIKE Prime robot using Pybricks.
    Provides methods for driving, turning, and other basic operations.
    """
    def __init__(self):
        """
        Initializes the BaseRobot with motors, hub, and drive base.
        """
        self._hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
        self._left_motor = Motor(Port.E, Direction.CLOCKWISE)
        self._right_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        self._drive_base = DriveBase(
            self._left_motor,
            self._right_motor,
            RobotConfig.TIRE_DIAMETER,
            RobotConfig.AXLE_TRACK,
        )

        self.leftAttachmentMotor = Motor(Port.C)


        self._drive_base.use_gyro(True)
        self._set_default_settings()

    def _set_default_settings(self):
        """
        Sets the default settings for the drive base, including speed and acceleration.
        """
        self._drive_base.settings(
            straight_speed=RobotConfig.STRAIGHT_SPEED,
            straight_acceleration=RobotConfig.STRAIGHT_ACCEL,
            turn_rate=RobotConfig.TURN_RATE,
            turn_acceleration=RobotConfig.TURN_ACCEL
        )

    @staticmethod
    def update_settings(drive_base, straight_speed=RobotConfig.STRAIGHT_SPEED, straight_acceleration=RobotConfig.STRAIGHT_ACCEL, turn_rate=RobotConfig.TURN_RATE, turn_acceleration=RobotConfig.TURN_ACCEL):
        """
        Updates the settings for the drive base.

        :param drive_base: The drive base to update settings for.
        :param straight_speed: New straight speed.
        :param straight_acceleration: New straight acceleration.
        :param turn_rate: New turn rate.
        :param turn_acceleration: New turn acceleration.
        """
        drive_base.settings(
            straight_speed=straight_speed,
            straight_acceleration=straight_acceleration,
            turn_rate=turn_rate,
            turn_acceleration=turn_acceleration
        )

    def gyro_drive(self, distance, speed=None, then=Stop.BRAKE, wait=True):
        """
        Drives the robot in a straight line using the gyro sensor to maintain heading.

        :param distance: Distance to drive in millimeters.
        :param speed: Optional speed to override the default straight speed.
        :param then: What to do after reaching the target (e.g., Stop.BRAKE).
        :param wait: Whether to wait until the action is complete.
        """
        initial_heading = self._hub.imu.heading()
        if speed:
            speed = max(RobotConfig.MIN_SPEED, min(RobotConfig.MAX_SPEED, speed))
            self._drive_base.settings(
                straight_speed=speed,
                straight_acceleration=RobotConfig.STRAIGHT_ACCEL,
                turn_rate=RobotConfig.TURN_RATE,
                turn_acceleration=RobotConfig.TURN_ACCEL
            )
        self._drive_base.straight(distance, then=then, wait=wait)
        final_heading = self._hub.imu.heading()
        heading_drift = final_heading - initial_heading
        if speed:
            self._set_default_settings()

    def gyro_turn_absolute(self, angle, speed=None, then=Stop.BRAKE, wait=True):
        """
        Turns the robot to an absolute angle using the gyro sensor.

        :param angle: Target angle to turn to (in degrees).
        :param speed: Optional speed to override the default turn rate.
        :param then: What to do after reaching the target (e.g., Stop.BRAKE).
        :param wait: Whether to wait until the action is complete.
        """
        # Get the initial heading from the gyro sensor
        initial_heading = self._hub.imu.heading()
        print(f"Initial Heading: {initial_heading}")

        # Calculate the target heading
        target_heading = angle + 2
        print(f"Target Heading: {target_heading}")

        # Set custom speed settings if provided
        if speed:
            self._drive_base.settings(
                straight_speed=RobotConfig.STRAIGHT_SPEED,
                straight_acceleration=RobotConfig.STRAIGHT_ACCEL,
                turn_rate=speed,
                turn_acceleration=RobotConfig.TURN_ACCEL
            )
            print(f"Custom Speed Set: {speed}")

        # Calculate the initial turn difference and execute the turn
        initial_turn_diff = target_heading - initial_heading
        print(f"Initial Turn Difference: {initial_turn_diff}")
        self._drive_base.turn(initial_turn_diff, then=then, wait=wait)

        # Get the final heading after the first turn
        final_heading = self._hub.imu.heading()
        print(f"Final Heading After First Turn: {final_heading}")

        # Calculate any remaining error and perform correction if needed
        turn_error = target_heading - final_heading
        print(f"Turn Error After First Turn: {turn_error}")
        if abs(turn_error) > 1:# Threshold to avoid unnecessary small corrections
            print("Turn error be")
            self._drive_base.turn(turn_error, then=then, wait=wait)
            print(f"Corrected Turn Error: {turn_error}")

        # Reset speed settings to default if they were changed
        if speed is not None:
            self._set_default_settings()
            print("Speed settings reset to default.")

    def curve(self, radius, angle, speed=RobotConfig.STRAIGHT_SPEED, then=Stop.HOLD, wait=True):
        """
        Drives the robot in a curve with a specified radius and angle.

        :param radius: Radius of the curve (in millimeters).
        :param angle: Angle to turn along the curve (in degrees).
        :param speed: Speed to drive along the curve.
        :param then: What to do after reaching the target (e.g., Stop.HOLD).
        :param wait: Whether to wait until the action is complete.
        """
        initial_heading = self._hub.imu.heading()
        self._drive_base.curve(radius, angle, then=then, wait=wait)
        final_heading = self._hub.imu.heading()
        actual_turn = final_heading - initial_heading
        turn_error = angle - actual_turn

    def drive_and_steer(self, speed, turn_rate, time):
        """
        Drives the robot with a specified speed and turn rate for a given time.

        :param speed: Speed to drive forward.
        :param turn_rate: Rate at which to turn (in degrees per second).
        :param time: Time to drive (in milliseconds).
        """
        initial_heading = self._hub.imu.heading()
        speed = max(RobotConfig.MIN_SPEED, min(RobotConfig.MAX_SPEED, speed))
        self._drive_base.drive(speed, turn_rate)
        wait(time)
        self._drive_base.stop()
        final_heading = self._hub.imu.heading()
        heading_change = final_heading - initial_heading

    def rotate_motor_degrees(self, angle, speed=200, then=Stop.BRAKE, wait=True):
        """
        Rotates the motor by a specified number of degrees.
        :param angle: Amount to rotate the motor by (in degrees).
        :param speed: Speed at which to rotate the motor.
        :param then: Action to take after rotation (default is Stop.BRAKE).
        :param wait: Whether to wait for the action to complete (default is True).
        """
        print(speed)
        self.leftAttachmentMotor.run_angle(speed=speed, rotation_angle=angle, then=then, wait=wait)

    def wait_for_button(self, button):
        """
        Waits until the specified button is pressed on the hub.

        :param button: The button to wait for.
        """
        while True:
            pressed = self._hub.buttons.pressed()
            if button in pressed:
                break
            wait(50)

    @staticmethod
    def wait_for_millis(millis):
        """
        Waits for a specified amount of time (in milliseconds).

        :param millis: Time to wait (in milliseconds).
        """
        wait(millis)
