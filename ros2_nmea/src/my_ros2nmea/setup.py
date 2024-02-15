from setuptools import setup

package_name = 'my_ros2nmea'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hyeeun',
    maintainer_email='hyeeun1116@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub = my_ros2nmea.pub:main',
            'sub = my_ros2nmea.sub:main',
            'sub2 = my_ros2nmea.sub2:main',
            
        ],
    },
)
