from typing import TypeVar, TypeVarTuple

DType = TypeVar('DType')
Shape = TypeVarTuple('Shape')

class Array(Generic[DType, *Shape]):

    def __abs__(self) -> Array[DType, *Shape]: ...

    def __add__(self, other: Array[DType, *Shape]) -> Array[DType, *Shape]: ...
