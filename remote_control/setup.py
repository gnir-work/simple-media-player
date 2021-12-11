from setuptools import setup, find_packages


setup(
    name="remote_control",
    version="1.0",
    requires=["vlc_controller"],
    packages=find_packages(),
)