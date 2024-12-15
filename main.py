from pybricks.tools import hub_menu, wait

from runs import *

from utils.base_robot import BaseRobot, RobotConfig


def main():
    robot = BaseRobot()
    config = RobotConfig()

    while True:
        # Show menu with numeric options: 0, 1, 2, 3, 4, 5
        selected = hub_menu("0", "1", "2", "3", "4", "5", "6", "7", "8")

        if selected == "0":
            # Run 0: Left Collecting
            run0_left_collecting(robot, config)
            print("Run 0: Left Collecting completed")
        elif selected == "1":
            # Run 2: Mast and Treasure
            run2_mast_and_treasure(robot, config)
            print("Run 1: Mast and Treasure completed")
        # elif selected == "3":
        elif selected == "2":
            # Run 3: Traverse
            run3_traverse(robot, config)
            print("Run 2: Traverse completed")
        elif selected == "3":
            # Placeholder for future run or functionality
            run5_krill_kollecter(robot, config)
            print("Run 3: Krill Kollector")
        elif selected == "4":
            # Placeholder for future run or functionality
            run6_sonar(robot, config)
            print("Run 4: Sonar Completed")
        elif selected == "5":
            # Placeholder for future run or functionality
            run7_krill_dumper(robot, config)
            print("Run 5: Krill dumped")
        elif selected == "6":
            run8_coral_move(robot, config)
        elif selected == "7":
            run4_octopus(robot, config)
        elif selected == "8":
            run9_submersible_angler(robot, config)
        # Add a small delay between runs
        wait(400)


if __name__ == "__main__":
    main()
