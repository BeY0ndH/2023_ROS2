import rclpy as rp
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node

from beagle_first_package.beagle_first_pub import BeaglePublisher
from beagle_first_package.beagle_first_sub import BeagleSubscriber
from beagle_first_package.beagle_action_client import BeagleServerClient

def main(args = None):
    rp.init()

    pub = BeaglePublisher()
    sub = BeagleSubscriber()
    #cli = BeagleServerClient()

    executor = MultiThreadedExecutor()

    executor.add_node(pub)
    executor.add_node(sub)
    #executor.add_node(cli)

    try:
        executor.spin()

    finally:
        executor.shutdown()
        pub.destroy_node()
        sub.destroy_node()
        #cli.destroy_node()
        rp.shutdown()

if __name__ == '__main__':
    main()
    