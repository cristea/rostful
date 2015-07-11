# This setup is usable by catkin, or on its own as usual python setup.py

_CATKIN = False
try:
    from distutils.core import setup
    from catkin_pkg.python_setup import generate_distutils_setup
    _CATKIN = True
except Exception, e:
    from setuptools import setup

# CAREFUL distutils and setuptools take different argument sand have different behaviors
if _CATKIN:  # using distutils : https://docs.python.org/2/distutils
    # fetch values from package.xml
    setup_args = generate_distutils_setup(
        packages=[
            'rostful',
        ],
        package_data={
            'rostful': [
                'static/js/jquery/*',
                'static/js/jquery-mobile/*',
                'static/js/jquery-mobile/images/*',
                'static/js/jquery-mobile/images/icons-png/*',
                'static/js/jquery-mobile/images/icons-svg/*',
                'templates/*',
                'templates/security/*',
                'templates/security/email/*',
            ],
        },
    )
    setup(**setup_args)

else:  # using setuptools : http://pythonhosted.org/setuptools/

    setup(name='rostful',
        version='0.0.7',
        description='REST API for ROS',
        url='http://github.com/asmodehn/rostful',
        author='AlexV',
        author_email='asmodehn@gmail.com',
        license='BSD',
        packages=['rostful'],
        # this is better than using package data ( since behavior is a bit different from distutils... )
        include_package_data=True,  # use MANIFEST.in during install.
        install_requires=[
            'Rostful-node',
            'Flask',
            'Flask-Celery-Helper',
            'Flask-Cors',
            'Flask-Script',
            'Flask-Restful',
        ],
        zip_safe=False,  # TODO testing...
    )
