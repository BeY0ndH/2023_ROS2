import rclpy
from rclpy.action import ActionClient, CancelResponse, GoalResponse
from rclpy.node import Node
from std_msgs.msg import Float64
from beagle_msgs.action import Distbeagle
import time
from roboid import *
my_goal = 0

class RidarActionClient(Node):

    def __init__(self):
        super().__init__('beagle_action_client')
        self._action_client = ActionClient(
            self,
            Distbeagle,
            'distbeagle'
            )

    def send_goal(self, order):
        goal_msg = Distbeagle.Goal()
        goal_msg.target_distance = order

        self._action_client.wait_for_server()

        self._send_goal_future = self._action_client.send_goal_async(goal_msg)

        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal Rejected :(')
            return

        self.get_logger().info('Goal Accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.current_distance))
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    print('rclpy.init')

    ridar_action_client = RidarActionClient()
    print('ridar_action_server = RidarActionServer()')

    print('sending goal 70.0') 
    ridar_action_client.send_goal(80.0)

    print('ridar_action_server is on spin')
    rclpy.spin(ridar_action_client)
    print('ridar_action_server spin ended')

    ridar_action_client.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()