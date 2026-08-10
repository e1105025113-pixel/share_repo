import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class DisplayNode(Node):

    def __init__(self):
        super().__init__('display_node')

        self.sub = self.create_subscription(
            String,
            'robot_command',
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info(f'Robot Action: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = DisplayNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
