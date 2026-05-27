from abc import ABC, abstractmethod

class Shape(ABC):
    """
    A base class representing a general geometric shape.
    """

    @abstractmethod
    def get_area(self):
        """
        Calculate and return the area of the shape.
        """
        pass

    @abstractmethod
    def get_perimeter(self):
        """
        Calculate and return the perimeter of the shape.
        """
        pass

    def __str__(self):
        """
        Return a clear string representation of the object.
        """
        return f"shape: {self.__class__.__name__},"\
            f"Area: {self.get_area()}, Perimeter: {self.get_perimeter()}"
    