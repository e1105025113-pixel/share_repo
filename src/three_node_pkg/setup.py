from setuptools import find_packages, setup

package_name = 'three_node_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/'+ package_name + '/launch',
        ['launch/system.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yuchel',
    maintainer_email='e1105025113@oit.ac.jp',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
		'input=three_node_pkg.input_node:main',
		'control=three_node_pkg.control_node:main',
		'display=three_node_pkg.display_node:main',
        ],
    },
)
