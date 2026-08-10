import threading
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class InputNode(Node):

    def __init__(self):
        super().__init__('input_node')

        self.publisher_ = self.create_publisher(String, 'input_text', 10)

        self.thread = threading.Thread(target=self.input_loop, daemon=True)
        self.thread.start()

    def input_loop(self):
        while rclpy.ok():
            command = input("Enter command: ")
            msg = String()
            msg.data = command
            self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = InputNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
