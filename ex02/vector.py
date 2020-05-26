from numbers import Real


class Vector:
    def __init__(self, param=None):
        if isinstance(param, list):
            for p in param:
                self.values.append(float(p))
        elif isinstance(param, int):
            for i in range(param):
                self.values.append(float(i))
        elif isinstance(param, tuple) and len(param) == 2:
            for i in range(param[0], param[1]):
                self.values.append(float(i))
        else:
            print("Param <{}> is not float, list or tuple".format(param))
        self.size = len(self.values)
    
    def __add__(self, other)
        if isinstance(other, Vector):
            if self.size == other.size:
                sum = []
                for i in self.size:
                    sum.append(self.values[i] + other.values[i])
                return Vector(sum)
            else:
                print("Vector <{}> has not a size of {}".format(other, self.size))
        elif isinstance(other, Real):
            sum = []
            for i in self.size:
                sum.append(self.values[i] + other)
            return Vector(sum)
        else:
            print("Can't add Vector with {}".format(other.type))
    
    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other)
        if isinstance(other, Vector):
            if self.size == other.size:
                sum = []
                for i in self.size:
                    sum.append(self.values[i] - other.values[i])
                return Vector(sum)
            else:
                print("Vector <{}> has not a size of {}".format(other, self.size))
        elif isinstance(other, Real):
            sum = []
            for i in self.size:
                sum.append(self.values[i] - other)
            return Vector(sum)
        else:
            print("Can't sub a Vector with {}".format(other.type))
    
    def __rsub__(self, other):
        if isinstance(other, Vector):
            return other - self
        elif isinstance(other, Real):
            sum = []
            for i in self.size:
                sum.append(other - self.values[i])
            return Vector(sum)
        else:
            print("Can't sub a Vector with {}".format(other.type))
    
    