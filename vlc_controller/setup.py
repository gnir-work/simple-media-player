from setuptools import setup, find_packages


setup(
    name="vlc_controller",
    version="1.0",
    install_requires=[
        "python-vlc",
        "logbook",
    ],
    packages=find_packages(),
)
