from setuptools import setup, find_packages

setup(
    name="neopixel_mock",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "adafruit-circuitpython-neopixel",
    ],
    author="Fernando Guillén Suárez",
    description="Mock development version for the Adafruit NeoPixel library",
    url="https://no-yet-url.com",
)
