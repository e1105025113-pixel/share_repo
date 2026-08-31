from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'independent_steering'

setup(
    name=package_name,
    version='0.0.0',

    packages=find_packages(exclude=['test']),

    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
        (
            'share/' + package_name + '/urdf',
            glob('urdf/*')
        ),
        (
            'share/' + package_name + '/launch',
            glob('launch/*')
        ),
    ],

    install_requires=['setuptools'],
    zip_safe=True,

    maintainer='yuchel',
    maintainer_email='e1105025113@oit.ac.jp',

    description='TR independent steering simulation',

    license='TODO: License declaration',

    extras_require={
        'test': [
            'pytest',
        ],
    },

    entry_points={
        'console_scripts': [],
    },
)

