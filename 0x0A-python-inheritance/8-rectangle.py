#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""here you can find the class BaseGeometry"""


class Rectangle(BaseGeometry):
    """here create the class"""
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
