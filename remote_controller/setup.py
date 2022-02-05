from setuptools import setup, find_packages


setup(
    name="remote_controller",
    version="1.0",
    install_requires=["vlc_controller", "evdev", "logbook"],
    packages=find_packages(),
)
