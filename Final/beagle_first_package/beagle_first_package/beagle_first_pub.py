import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from beagle_msgs.srv import Beagleposition
import roboidai as ai
import time
msg = String()
tmi = ai.TmImage()
tmi.load_model('/home/youhobae/RobotProgramming/Dice_V3/converted_keras_150')

cam = ai.Camera('ip0', square=True)

print("countdown start")
cam.count_down(5)
print("countdown off")

class DICE_CHECKER(Node):
    def __init__(self):
        super().__init__('beagle_first_publisher')
        self.publisher_dice0 = self.create_publisher(String, 'topic', 10)
        self.publisher_dice1 = self.create_publisher(String, 'topic', 10)
        self.publisher_dice2 = self.create_publisher(String, 'topic', 10)
        self.publisher_dice3 = self.create_publisher(String, 'topic', 10)
        self.publisher_dice4 = self.create_publisher(String, 'topic', 10)
        self.publisher_dice5 = self.create_publisher(String, 'topic', 10)
        self.publisher_dice6 = self.create_publisher(String, 'topic', 10)
        self.service_client = self.create_client(
            Beagleposition,
            'service_name')
        self.service_server = self.create_service(
            Beagleposition,
            'service_name',
            self.service_callback)
        self.cam = cam
        self.tmi = tmi
        self.current_dice_label = None
        timer_period = 7.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        image = self.cam.read()
        if self.tmi.predict(image):
            label = self.tmi.get_label()
            conf = self.tmi.get_conf()
            time.sleep(1)
            print("Predicted Label:", label)
            print("Confidence:", conf)
            if conf > 0.8 and label != self.current_dice_label:
                self.current_dice_label = label
                if label == 'DICE0':

                    msg.data = 'DICE0'
                    self.publisher_dice1.publish(msg)
                    self.get_logger().info('Publishing: "DICE0"')
                elif label == 'DICE1':

                    msg.data = 'DICE1'
                    self.publisher_dice1.publish(msg)
                    self.get_logger().info('Publishing: "DICE1"')
                elif label == 'DICE2':

                    msg.data = 'DICE2'
                    self.publisher_dice2.publish(msg)
                    self.get_logger().info('Publishing: "DICE2"')
                elif label == 'DICE3':

                    msg.data = 'DICE3'
                    self.publisher_dice3.publish(msg)
                    self.get_logger().info('Publishing: "DICE3"')
                elif label == 'DICE4':

                    msg.data = 'DICE4'
                    self.publisher_dice4.publish(msg)
                    self.get_logger().info('Publishing: "DICE4"')
                elif label == 'DICE5':

                    msg.data = 'DICE5'
                    self.publisher_dice5.publish(msg)
                    self.get_logger().info('Publishing: "DICE5"')
                elif label == 'DICE6':

                    msg.data = 'DICE6'
                    self.publisher_dice6.publish(msg)
                    self.get_logger().info('Publishing: "DICE6"')

                if msg.data in ['DICE0', 'DICE1', 'DICE2', 'DICE3', 'DICE4', 'DICE5', 'DICE6']:
                    request = Beagleposition.Request()
                    request.dice_label = msg.data

                    while not self.service_client.wait_for_service(timeout_sec=1.0):
                        self.get_logger().info('Service not available, waiting again...')
                    self.future = self.service_client.call_async(request)
                    self.future.add_done_callback(self.service_response_callback)
        time.sleep(2)

    def service_response_callback(self, future):
        try:
            response = future.result()
            if msg.data == "DICE0" :
                response.move_point += 0
            elif msg.data == "DICE1" :
                response.move_point += 1
            elif msg.data == "DICE2" :
                response.move_point += 2
            elif msg.data == "DICE3" :
                response.move_point += 3
            elif msg.data == "DICE4" :
                response.move_point += 4
            elif msg.data == "DICE5" :
                response.move_point += 5
            elif msg.data == "DICE6" :
                response.move_point += 6

            self.get_logger().info('Service Response: %s' % response.move_point)
        except Exception as e:
            self.get_logger().info('Service call failed %r' % (e,))

    def service_callback(self, request, response):
        self.get_logger().info('Incoming Request: %s' % request.dice_label)
        # Process the request and set response.success accordingly
        response.beagle_event = 1
        return response


def main(args=None):
    rclpy.init(args=args)

    dice_checker = DICE_CHECKER()

    rclpy.spin(dice_checker)

    dice_checker.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()