import rclpy as rp
from rclpy.node import Node
from roboid import *
import roboidai as ai
from std_msgs.msg import String
import time


beagle  = Beagle()
timer_bucket = 0
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

    def listner_callback(self,msg):
        
          if msg.data == "DICE1" :
               print("dice1")
               self.get_logger().info('Subscribing: "DICE1"')
               beagle.move_forward(1)
               
          elif msg.data == "DICE2" :
               print("DICE2") 
               self.get_logger().info('Subscribing: "DICE2"')
               beagle.move_forward(1)
               time.sleep(0.5)
               beagle.move_forward(1)
          elif msg.data == "DICE3" :
               print("DICE3") 
               self.get_logger().info('Subscribing: "DICE3"')
               beagle.move_forward(1)
               time.sleep(0.5)
               beagle.move_forward(1)
               time.sleep(0.5)
               beagle.move_forward(1)

          elif msg.data == "DICE4" :
               print("DICE4") 
               self.get_logger().info('Subscribing: "DICE4"')
               beagle.move_forward(1)
               time.sleep(0.5)
               beagle.move_forward(1)
               time.sleep(0.5)
               beagle.move_forward(1)
               time.sleep(0.5)
               beagle.move_forward(1)

          elif msg.data == "DICE5" :
               print("DICE5") 
               self.get_logger().info('Subscribing: "DICE5"')
               beagle.move_forward(1)
               time.sleep(0.5)
               beagle.move_forward(1)
               time.sleep(0.5)
               beagle.move_forward(1)
               time.sleep(0.5)
               beagle.move_forward(1)
               time.sleep(0.5)
               beagle.move_forward(1)


          elif msg.data == "DICE6" :
               print("DICE6") 
               self.get_logger().info('Subscribing: "DICE6"')





def main(args =None) :
    rp .init(args = args)
    direct_mode_subscribe = direct_mode_sub()

    rp.spin(direct_mode_subscribe)
    direct_mode_subscribe.destroy_node()
    rp.shutdown()

if __name__== '__main__' :

    main()
