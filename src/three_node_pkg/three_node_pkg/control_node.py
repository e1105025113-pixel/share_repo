import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ControlNode(Node):

    def __init__(self):
        super().__init__('control_node')

        self.sub = self.create_subscription(
            String,
            'input_text',
            self.callback,
            10
        )

        self.pub = self.create_publisher(String, 'robot_command', 10)

    def callback(self, msg):
        command = msg.data

        if 'forward' in command:
            out = 'MOVE_FORWARD'
        elif 'left' in command:
            out = 'TURN_LEFT'
        else:
            out = 'STOP'

        out_msg = String()
        out_msg.data = out
        self.pub.publish(out_msg)


def main(args=None):
    rclpy.init(args=args)
    node = ControlNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
