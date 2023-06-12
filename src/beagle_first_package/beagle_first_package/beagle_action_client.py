import rclpy
from rclpy.action import ActionClient, CancelResponse, GoalResponse
from rclpy.node import Node
from std_msgs.msg import Float64
from beagle_msgs.action import Distbeagle
import time
from roboid import *

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

    '''def cancel_callback(self, goal_handle):
        self.get_logger().info('Received cancel request')
        return CancelResponse.ACCEPT'''

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)

    def get_result_callback(self, future):
        result = future.result().result
        self.get_logger().info('Result: {0}'.format(result.current_distance))
        '''rclpy.shutdown()'''

def main(args=None):
    rclpy.init(args=args)

    ridar_action_client = RidarActionClient()

    ridar_action_client.send_goal(600.0)

    rclpy.spin(ridar_action_client)

    ridar_action_client.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()