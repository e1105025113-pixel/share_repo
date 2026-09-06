import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import sys
import termios
import tty


class OneWheelController(Node):

    def __init__(self):
        super().__init__('onewheel_controller')

        self.steering_pub = self.create_publisher(
            Float64,
            '/model/one_wheel_robot/joint/steering_joint/cmd_pos',
            10
        )

        self.wheel_pub = self.create_publisher(
            Float64,
            '/model/one_wheel_robot/joint/wheel_joint/cmd_pos',
            10
        )

        self.steering_angle = 0.0
        self.wheel_angle = 0.0

        self.get_logger().info('One Wheel Controller started')
        self.get_logger().info('W/S: wheel  A/D: steering  Q: quit')

    def publish_steering(self):
        msg = Float64()
        msg.data = self.steering_angle
        self.steering_pub.publish(msg)

    def publish_wheel(self):
        msg = Float64()
        msg.data = self.wheel_angle
        self.wheel_pub.publish(msg)


def get_key():
    settings = termios.tcgetattr(sys.stdin)

    tty.setraw(sys.stdin.fileno())
    key = sys.stdin.read(1)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

    return key


def main(args=None):

    rclpy.init(args=args)

    node = OneWheelController()

    try:
        while rclpy.ok():

            key = get_key()

            # ステアリング左
            if key == 'a':
                node.steering_angle += 0.1745

                if node.steering_angle > 1.57:
                    node.steering_angle = 1.57

                node.publish_steering()

            # ステアリング右
            elif key == 'd':
                node.steering_angle -= 0.1745

                if node.steering_angle < -1.57:
                    node.steering_angle = -1.57

                node.publish_steering()

            # 車輪正転
            elif key == 'w':
                node.wheel_angle += 0.5236
                node.publish_wheel()

            # 車輪逆転
            elif key == 's':
                node.wheel_angle -= 0.5236
                node.publish_wheel()

            # 終了
            elif key == 'q':
                break

            node.get_logger().info(
                f'Steering: {node.steering_angle:.2f} rad '
                f'Wheel: {node.wheel_angle:.2f} rad'
            )

    except KeyboardInterrupt:
        pass

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
