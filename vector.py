from __future__ import annotations

class Vector:
    def __init__(self, x : float, y : float, z : float):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other : Vector) -> Vector :
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __iadd__(self, other : Vector) :
        self.x += other.x
        self.y += other.y
        self.z += other.z
    
    def __mul__(self, scalar : float):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __imul__(self, other : Vector):
        self.x *= other.x
        self.y *= other.y
        self.z *= other.z

    def __div__(self, scalar : float) -> Vector :
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)

    def __idiv__(self, other : Vector):
        self.x /= other.x
        self.y /= other.y
        self.z /= other.z

    def dot(self, other : Vector) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other : Vector) -> Vector:
        return Vector(self.y * other.z - self.z * other.y,
                      self.z * other.x - self.x * other.z,
                      self.x * other.y - self.y * other.x)

    def __str__(self):
        print("x :", self.x, " y :", self.y, " z : ", self.z)
    
