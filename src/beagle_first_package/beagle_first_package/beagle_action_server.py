import rclpy
from rclpy.action import ActionServer, CancelResponse, GoalResponse
from rclpy.node import Node
from std_msgs.msg import Float64
from beagle_msgs.action import Distbeagle
import time
from roboid import *

beagle = Beagle()
beagle.start_lidar()
beagle.wait_until_lidar_ready()
print('lidar starts')

class RidarActionServer(Node):
    def __init__(self):
        super().__init__('beagle_action')
        self._action_server = ActionServer(
            self,
            Distbeagle,
            'distbeagle',
            self.execute_callback)
        
        self.publisher = self.create_publisher(Float64, 'target_distance', 10)
        self.current_distance = 0.0

    '''def goal_callback(self, goal_handle):
        self.get_logger().info('Received goal request')
        return GoalResponse.ACCEPT

    def cancel_callback(self, goal_handle):
        self.get_logger().info('Received cancel request')
        return CancelResponse.ACCEPT'''

    def execute_callback(self, goal_handle):

        self.get_logger().info('Executing goal...')

        feedback_msg = Distbeagle.Feedback()
        result_msg = Distbeagle.Result()

        while rclpy.ok():
            rear_distance = beagle.rear_lidar()
            right_distance = beagle.right_lidar()
            right_rear_distance = beagle.right_rear_lidar()
            front_distance = beagle.front_lidar()
            right_front_distance = beagle.right_front_lidar()

            if 250 <= rear_distance <= 400 or 250 <= right_distance <= 400 or 250 <= right_rear_distance <= 400:
                beagle.sound("engine", 1)
                time.sleep(1)

            if 60 < rear_distance < 250 or 60 < right_distance < 250 or 60 < right_rear_distance < 250:
                beagle.sound("siren", 1)
                time.sleep(1)

            if beagle.rear_lidar() <= 60:
                beagle.sound("sad", 1)
                time.sleep(1)
                print('Loser..')
                dispose()
                break

            if 250 <= front_distance <= 400 or 250 <= right_front_distance <= 400:
                beagle.sound("march", 1)
                time.sleep(1)

            if 60 < front_distance < 250 or 60 < right_front_distance < 250:
                beagle.sound("good job", 1)
                time.sleep(1)

            if front_distance <= 60:
                beagle.sound("happy", 1)
                time.sleep(1)
                print('Winner!!')
                beagle.dispose()
                break

            self.current_distance = beagle.front_lidar()
            msg = Float64()
            msg.data = self.current_distance
            self.publisher.publish(msg)

            if self.current_distance <= goal_handle.request.target_distance:
                self.get_logger().info('Goal reached!')
                result_msg.current_distance = self.current_distance
                return Distbeagle.Result(success=True, result=result_msg)

            feedback_msg.current_distance = self.current_distance
            goal_handle.publish_feedback(feedback_msg)

            time.sleep(0.1)

        return Distbeagle.Result(success=False)

def main(args=None):
    rclpy.init(args=args)

    ridar_action_server = RidarActionServer()

    rclpy.spin(ridar_action_server)

    ridar_action_server.destroy_node()
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()