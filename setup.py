from setuptools import setup

setup(
    name="anel_pwrctrl",
    version="0.0.1",
    description='Discover and control ANEL NET-PwrCtrl devices.',
    install_requires=[
        "anel_pwrctrl",
    ],
    packages=['anel_pwrctrl'],
    author='Martin Weinelt',
    author_email='martin@linuxlounge.net',
    license='MIT'
)