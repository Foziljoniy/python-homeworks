import math

class Vector:
    def init(self, *components):
        """
        Initialize a vector with given components.
        """
        self.components = tuple(components)
    
    def repr(self):
        """
        Return a string representation of the vector.
        """
        return f"Vector{self.components}"
    
    def add(self, other):
        """
        Add two vectors component-wise.
        """
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))
    
    def sub(self, other):
        """
        Subtract two vectors component-wise.
        """
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))
    
    def mul(self, other):
        """
        Compute the dot product if multiplying by another vector, otherwise perform scalar multiplication.
        """
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions")
            return sum(a * b for a, b in zip(self.components, other.components))
        return Vector(*(a * other for a in self.components))
    
    def rmul(self, scalar):
        """
        Support scalar multiplication from the left.
        """
        return self * scalar
    
    def truediv(self, scalar):
        """
        Divide a vector by a scalar.
        """
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return Vector(*(a / scalar for a in self.components))
    
    def magnitude(self):
        """
        Compute the magnitude (length) of the vector.
        """
        return math.sqrt(sum(a**2 for a in self.components))
    
    def normalize(self):
        """
        Return a unit vector in the same direction.
        """
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return self / mag


