
'''
from rcl_interfaces.msg import Parameter
from rcl_interfaces.msg import ParameterType
from rcl_interfaces.msg import ParameterValue
from rcl_interfaces.msg import SetParametersResult
'''
'''
from beagle_msgs.srv import Beagleposition
import rclpy as rp
from rclpy.node import Node
from beagle_first_package.beagle_first_pub import msg


class beaglePosition(Node):

    def __init__(self) :

        super().__init__('beagle_service_server')
        self.server =self.create_service(
            Beagleposition,
            'check_beagle_position',
            self.callback_service
        )

        self.client = self.create_client(
         Beagleposition, 
        '/beagle_first_package/beagle'
        )
        self.check_absoloute_node = Beagleposition.Request()
        self.check_position = Beagleposition.Response()
        self.check_trap = Beagleposition.Response()
        

    def callback_service(self, request, response) :
       
        if request.dice_label == "DICE1":
            #self.check_absoloute_node.move_point += 1
            request.move_point += 1
            print(self.check_absoloute_node.move_point)
        elif request.dice_label == "DICE2" :
            self.check_absoloute_node.move_point += 2
            print(self.check_absoloute_node.move_point)
        elif request.dice_label == "DICE3" :
            self.check_absoloute_node.move_point += 3
            print(self.check_absoloute_node.move_point)
        elif request.dice_label == "DICE4" :
            self.check_absoloute_node.move_point += 4
            print(self.check_absoloute_node.move_point)
        elif request.dice_label == "DICE5" :
            self.check_absoloute_node.move_point += 5
            print(self.check_absoloute_node.move_point)
        elif request.dice_label == "DICE6" :
            self.check_absoloute_node.move_point += 6
            print(self.check_absoloute_node.move_point)
        
        self.check_position.beagle_position = self.check_absoloute_node.move_point
        if self.check_position.beagle_position > 16 :
            self.check_position.beagle_position = 0
        self.client.call_async(self.check_absoloute_node)
        
        return response
        
    #def random_gimic(self,request, response) :




def main(args = None) :

    rp.init(args = args)
    beagle_position = beaglePosition()
    rp.spin(beagle_position)

    rp.shutdown()

if __name__ == '__main__' :

    main()

'''

from beagle_msgs.srv import Beagleposition
import rclpy as rp
from rclpy.node import Node
from beagle_first_package.beagle_first_pub import msg
print("service start")

class beaglePosition(Node):

    def __init__(self):

        super().__init__('beagle_service_server')
        self.server = self.create_service(
            Beagleposition,
            'check_beagle_position',
            self.callback_service
        )
        print("making server")
        self.client = self.create_client(
            Beagleposition,
            '/beagle_first_package/beagle'
        )
        print("making client")
        self.check_absoloute_node = Beagleposition.Request()
        self.check_position = Beagleposition.Response()
        self.check_trap = Beagleposition.Response()

    def callback_service(self, request, response, msg ):
        
        print("callback start")
        print("Request : " ,request )
        request.dice_label = msg.data
        if request.dice_label == "DICE1":
            request.move_point += 1
            print(self.check_absoloute_node.move_point)
        elif request.dice_label == "DICE2":
            self.check_absoloute_node.move_point += 2
            print(self.check_absoloute_node.move_point)
        elif request.dice_label == "DICE3":
            self.check_absoloute_node.move_point += 3
            print(self.check_absoloute_node.move_point)
        elif request.dice_label == "DICE4":
            self.check_absoloute_node.move_point += 4
            print(self.check_absoloute_node.move_point)
        elif request.dice_label == "DICE5":
            self.check_absoloute_node.move_point += 5
            print(self.check_absoloute_node.move_point)
        elif request.dice_label == "DICE6":
            self.check_absoloute_node.move_point += 6
            print(self.check_absoloute_node.move_point)

        self.check_position.beagle_position = self.check_absoloute_node.move_point
        if self.check_position.beagle_position > 16:
            self.check_position.beagle_position = 0
        self.client.call_async(self.check_absoloute_node)

        return response


def main(args=None):

    rp.init(args=args)
    beagle_position = beaglePosition()
    rp.spin(beagle_position)

    rp.shutdown()

if __name__ == '__main__':

    main()

