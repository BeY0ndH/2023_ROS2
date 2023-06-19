from setuptools import setup
import os
import glob
package_name = 'beagle_first_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob.glob(os.path.join('launch','*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='k',
    maintainer_email='hoperes2@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            #'beagle_first_node = beagle_first_package.beagle_first_node:main',
            'beagle_first_pub = beagle_first_package.beagle_first_pub:main',
            'beagle_first_sub = beagle_first_package.beagle_first_sub:main',
            #'beagle_service_server = beagle_first_package.beagle_service_server:main',
            #'beagle_action_server = beagle_first_package.beagle_action_server:main',
            'beagle_action_client = beagle_first_package.beagle_action_client:main',
            'multi_thread = beagle_first_package.multi_thread:main',
            'beagle_my_pos = beagle_first_package.beagle_my_pos:main'
        ],
    },
)