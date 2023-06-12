import rclpy as rp
from rclpy.node import Node
from std_msgs.msg import String
from beagle_msgs.msg import CmdAndPoseVel

class posecal(Node) :

    def __init__(self) :
        super().__init__('beagle_target_node')
        self.sub_pose = self.create_subscription()