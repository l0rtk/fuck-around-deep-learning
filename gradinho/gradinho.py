import math


class Scalar:
    def __init__(self, value,label = '', _children = (), _op = ''):
        self.value = value
        self._prev = _children 
        self._op = _op
        self.grad = 0.0
        self.label = label
        
    def __add__(self, other):
        other = other if isinstance(other, Scalar) else Scalar(other)
        out = self.value + other.value
        return Scalar(out, _children = (self, other), _op = '+')

    def __radd__(self, other):
        other = other if isinstance(other, Scalar) else Scalar(other)
        out = self.value + other.value
        return Scalar(out, _children = (self, other), _op = '+')
    
    def __sub__(self, other):
        other = other if isinstance(other, Scalar) else Scalar(other)
        out = self.value - other.value
        return Scalar(out, _children = (self, other), _op = '-')
    
    def __rsub__(self, other):
        other = other if isinstance(other, Scalar) else Scalar(other)
        out = other.value - self.value
        return Scalar(out, _children = (self, other), _op = '-')
        
    def __mul__(self, other):
        other = other if isinstance(other, Scalar) else Scalar(other)
        out = self.value * other.value
        return Scalar(out, _children = (self, other), _op = '*')

    def __rmul__(self, other):
        other = other if isinstance(other, Scalar) else Scalar(other)
        out = self.value * other.value
        return Scalar(out, _children = (self, other), _op = '*')

    def __pow__(self, other):
        other = other if isinstance(other, Scalar) else Scalar(other)
        out = self.value ** other.value
        return Scalar(out, _children = (self, other), _op = '**')
    
    def tanh(self):
        return Scalar(math.tanh(self.value), _children = (self, ), _op = "tanh")
        
    
    def __repr__(self):
        return f"Scalar(value={str(self.value)})"