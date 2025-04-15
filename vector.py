from __future__ import annotations

class Vector:
    def __init__(self, lValues: list[float]):
        self.lValues: list[float] = lValues
        self.iSize: int = len(lValues)

    @staticmethod
    def null(iSize: int) -> Vector:
        return Vector([0 for _ in range(iSize)])

    @staticmethod
    def one(iSize: int) -> Vector:
        return Vector([1 for _ in range(iSize)])

    def __repr__(self) -> str:
        sPrint = "("
        if (self.iSize > 0):
            sPrint += str(self.lValues[0])
            for iIndex in range(1, self.iSize):
                sPrint += ", " + str(self.lValues[iIndex])
        sPrint += ")"
        return sPrint

    def copy(self) -> Vector:
        return Vector([v for v in self.lValues])

    def __getitem__(self, iIndex: int) -> float:
        return self.lValues[iIndex]

    def __setitem__(self, iIndex: int, iValue: float):
        self.lValues[iIndex] = iValue

    def __add__(self, other: Vector | float) -> Vector:
        if (isinstance(other, Vector)):
            return self.__add__Vector(other)
        else:
            return self.__add__float(other)

    def __add__Vector(self, other: Vector) -> Vector:
        newVector = self.copy()
        if (self.iSize != other.iSize): raise ValueError
        for iIndex in range(self.iSize):
            newVector.lValues[iIndex] += other.lValues[iIndex]
        return newVector

    def __add__float(self, other: float) -> Vector:
        newVector = self.copy()
        for iIndex in range(self.iSize):
            newVector.lValues[iIndex] += other
        return newVector

    def __sub__(self, other: Vector | float) -> Vector:
        if (isinstance(other, Vector)):
            return self.__sub__Vector(other)
        else:
            return self.__sub__float(other)

    def __sub__Vector(self, other: Vector) -> Vector:
        newVector = self.copy()
        if (self.iSize != other.iSize): raise ValueError
        for iIndex in range(self.iSize):
            newVector.lValues[iIndex] -= other.lValues[iIndex]
        return newVector

    def __sub__float(self, other: float) -> Vector:
        newVector = self.copy()
        for iIndex in range(self.iSize):
            newVector.lValues[iIndex] -= other
        return newVector

    def __mul__(self, other: Vector | float) -> float | Vector:
        if (isinstance(other, Vector)):
            return self.__mul__Vector(other)
        else:
            return self.__mul__float(other)

    def __mul__Vector(self, other: Vector) -> float:
        if (self.iSize != other.iSize): raise ValueError
        fSum: int = 0
        for iSelfValue, iOtherValue in zip(self.lValues, other.lValues):
            fSum += iSelfValue * iOtherValue
        return fSum

    def __mul__float(self, other: float) -> Vector:
        newVector = self.copy()
        for iIndex in range(self.iSize):
            newVector.lValues[iIndex] *= other
        return newVector

    def __xor__(self, other: Vector) -> Vector:  # prodvect()
        newVector: Vector = Vector.null(self.iSize)
        i1: int;
        i2: int
        for i in range(self.iSize):
            i1 = (i + 1) % 3
            i2 = (i + 2) % 3
            newVector[i] = self[i1] * other[i2] - other[i1] * self[i2]
        return newVector

    def __truediv__(self, other: float) -> Vector:
        newVector = self.copy()
        for iIndex in range(self.iSize):
            newVector.lValues[iIndex] /= other
        return newVector

    def __bool__(self) -> bool:
        for iValue in self.lValues:
            if (iValue): return True
        return False

    def __eq__(self) -> bool:
        for iIndex in range(self.iSize):
            if (self.lValues[iIndex] != self.lValues[iIndex]): return False
        return True

    def __lt__(self, other: Vector) -> bool:
        for iIndex in range(self.iSize):
            if (self.lValues[iIndex] >= other.lValues[iIndex]): return False
        return True

    def __le__(self, other: Vector) -> bool:
        for iIndex in range(self.iSize):
            if (self.lValues[iIndex] > other.lValues[iIndex]): return False
        return True

    def __rt__(self, other: Vector) -> bool:
        for iIndex in range(self.iSize):
            if (self.lValues[iIndex] <= other.lValues[iIndex]): return False
        return True

    def __re__(self, other: Vector) -> bool:
        for iIndex in range(self.iSize):
            if (self.lValues[iIndex] < other.lValues[iIndex]): return False
        return True

    def x(self) -> float:
        return self.lValues[0]

    def y(self) -> float:
        return self.lValues[1]

    def z(self) -> float:
        return self.lValues[2]

    def norm(self) -> float:
        return (self * self) ** 0.5

    def normalizeToSelf(self) -> None:
        norm = self.norm()
        for iIndex in range(self.iSize):
            self.lValues[iIndex] /= norm

    def normalizeToNew(self) -> Vector:
        newVector: Vector = self.copy()
        newVector.normalizeToSelf()
        return newVector

    def distanceTo(self, other: Vector) -> float:
        return (other - self).norm()

    def cross(self, other : Vector) -> Vector:
        return Vector([self.lValues[1] * other.lValues[2] - self.lValues[2] * other.lValues[1],
                      self.lValues[2] * other.lValues[0] - self.lValues[0] * other.lValues[2],
                      self.lValues[0] * other.lValues[1] - self.lValues[1] * other.lValues[0]])


from matrix import Matrix