# service_node.py

import rclpy
from rclpy.node import Node
from example_interfaces.srv import Trigger


class ServiceNode(Node):

    def __init__(self):
        super().__init__('service_node')

        self.srv = self.create_service(
            Trigger,
            'robot_status',
            self.callback
        )

    def callback(self, request, response):
        response.success = True
        response.message = 'Robot is running normally'
        return response


def main(args=None):
    rclpy.init(args=args)

    node = ServiceNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()#service_node.py

import rclpy
from rclpy.node import Node
from example_interfaces.srv import Trigger


class ServiceNode(Node):

    def __init__(self):
        super().__init__('service_node')

        self.srv = self.create_service(Trigger, 'robot_status', self.callback)

    def callback(self, request, response):
        response.success = True
        response.message = 'Robot is running normally'
        return response

