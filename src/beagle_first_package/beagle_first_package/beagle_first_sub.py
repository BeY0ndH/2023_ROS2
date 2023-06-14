import rclpy as rp
from rclpy.node import Node
from roboid import *
import roboidai as ai
from std_msgs.msg import String
import time


beagle  = Beagle()
timer_bucket = 0
end_game = 1                        # 1이면 일반 모드, 2면 멸망전; 주사위 눈 수 x2
wheel_pulse = 1440
wheel_speed = 15*end_game



class direct_mode_sub(Node) :
     def __init__(self) :
        super().__init__('beagle_first_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listner_callback,
            10
        )
        self.subscription
        self.move_point = self.load_move_point()

     def listner_callback(self,msg):
          move_point = self.move_point
          move_point = self.move_point
          if msg.data == "DICE1" :
               print("dice1")
               self.get_logger().info('Subscribing: "DICE1"')

               print("beagle go 1")
               for i in range(1*end_game) :
                    move_point += 1
                    beagle.move_forward_pulse(wheel_pulse, wheel_speed)
                    if (move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16) :
                         #beagle.stop()
                         beagle.turn_right_pulse(705,30)
                    if move_point > 16 :
                         move_point -= 16
               self.move_point = move_point

          elif msg.data == "DICE2" :
               print("DICE2")
               self.get_logger().info('Subscribing: "DICE2"')

               print("beagle go 2")
               for i in range(2*end_game) :
                    move_point += 1
                    beagle.move_forward_pulse(wheel_pulse, wheel_speed)
                    if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
                         #beagle.stop()
                         beagle.turn_right_pulse(705,30)
                    if move_point > 16 :
                         move_point -= 16
               self.move_point = move_point

          elif msg.data == "DICE3" :
               print("DICE3")
               self.get_logger().info('Subscribing: "DICE3"')

               print("beagle go 3")
               for i in range(3*end_game) :
                    beagle.move_forward_pulse(wheel_pulse, wheel_speed)
                    move_point += 1
                    if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
                         #beagle.stop()
                         beagle.turn_right_pulse(705,30)
                    if move_point > 16 :
                         move_point -= 16
               self.move_point = move_point

          elif msg.data == "DICE4" :
               print("DICE4")
               self.get_logger().info('Subscribing: "DICE4"')

               print("beagle go 4")
               for i in range(4*end_game) :
                    move_point += 1
                    beagle.move_forward_pulse(wheel_pulse, wheel_speed)
                    if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
                         #beagle.stop()
                         beagle.turn_right_pulse(705,30)
                    if move_point > 16 :
                         move_point -= 16
               self.move_point = move_point

          elif msg.data == "DICE5" :
               print("DICE5")
               self.get_logger().info('Subscribing: "DICE5"')

               print("beagle go 5")
               for i in range(5*end_game) :
                    beagle.move_forward_pulse(wheel_pulse, wheel_speed)
                    move_point += 1
                    if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
                         #eagle.stop()
                         beagle.turn_right_pulse(705,30)
                    if move_point > 16 :
                         move_point -= 16
               self.move_point = move_point

          elif msg.data == "DICE6" :
               print("DICE6")
               self.get_logger().info('Subscribing: "DICE6"')

               print("beagle go 6")
               for i in range(6*end_game) :
                    beagle.move_forward_pulse(wheel_pulse, wheel_speed)
                    move_point += 1
                    if move_point == 3 or move_point == 8 or move_point == 11 or move_point == 16 :
                         #beagle.stop()
                         beagle.turn_right_pulse(705,30)
                    if move_point > 16 :
                         move_point -= 16
               self.move_point = move_point
          self.save_move_point(self.move_point)

     def load_move_point(self):
        try:
          with open("move_point.txt", "r") as file:
               return int(file.read())
        except FileNotFoundError:
            return 0

     def save_move_point(self, value):
          with open("move_point.txt", "w") as file:
               file.write(str(value))





def main(args =None) :
    rp .init(args = args)
    direct_mode_subscribe = direct_mode_sub()
    rp.spin(direct_mode_subscribe)
    direct_mode_subscribe.destroy_node()
    rp.shutdown()

if __name__== '__main__' :

    main()