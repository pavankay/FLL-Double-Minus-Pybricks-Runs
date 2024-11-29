from pybricks.hubs import PrimeHub
from pybricks.tools import hub_menu, wait


from runs import *
from runs.run7_krill_dumper import run7_krill_dumper

from utils.base_robot import BaseRobot, RobotConfig

# from runs.run4_octopus import run4_octopus
# from runs.run3_traverse import run3_traverse

# from runs.run0_left_collecting import run0_left_collecting
# from runs.run1_shark_and_coral import run1_shark_and_coral
# from runs.run2_mast_and_treasure import run2_mast_and_treasure
# from


def main():
    hub = PrimeHub()
    robot = BaseRobot()
    config = RobotConfig()

    while True:
        # Show menu with numeric options: 0, 1, 2, 3, 4, 5
        selected = hub_menu("0", "1", "2", "3", "4", "5", "6")

        if selected == "0":
            # Run 0: Left Collecting
            run0_left_collecting(robot, config)
            print("Run 0: Left Collecting completed")
        elif selected == "1":
            # Run 1: Shark and Coral
            run1_shark_and_coral(robot, config)
            print("Run 1: Shark and Coral completed")
        elif selected == "2":
            # Run 2: Mast and Treasure
            run2_mast_and_treasure(robot, config)
            print("Run 2: Mast and Treasure completed")
        elif selected == "3":
            # Run 3: Traverse
            run3_traverse(robot, config)
            print("Run 3: Traverse completed")
        elif selected == "4":
            # Run 4: Octopus
            run4_octopus(robot, config)
            print("Run 4: Octopus completed")
        elif selected == "5":
            # Placeholder for future run or functionality
            print("Run 5: Placeholder - Not implemented")
        elif selected == "6":
            # Placeholder for future run or functionality
            run6_sonar(robot, config)
            print("Run 6: Sonar Completed")
        elif selected == "7":
            # Placeholder for future run or functionality
            run7_krill_dumper(robot, config)
            print("Run 7: Krill dumped")
        # Add a small delay between runs
        wait(400)


if __name__ == "__main__":
    main()
