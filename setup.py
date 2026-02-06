from setuptools import setup

setup(
    name="Raspi-MotorHAT",
    version="1.0.0",
    description="Simple Raspberry Pi MotorHAT library for DC motors, steppers and servos",
    author="Your Name",
    py_modules=[
        "Raspi_MotorHAT",
        "Raspi_I2C",
        "Raspi_PWM_Servo_Driver"
    ],
    install_requires=[
        "smbus2"
    ],
)
