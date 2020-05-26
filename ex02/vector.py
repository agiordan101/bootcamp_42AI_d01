from numbers import Real


class Vector:

    def __str__(self):
        return "Vector: {}".format(self.values)

    def __init__(self, param=None):
        self.values = []
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

    def __add__(self, other):
        if isinstance(other, Vector):
            if self.size == other.size:
                sum = []
                for i in range(self.size):
                    sum.append(self.values[i] + other.values[i])
                return Vector(sum)
            else:
                print("Vector <{}> has not a size of {}".format(other,
                      self.size))
        elif isinstance(other, Real):
            sum = []
            for i in range(self.size):
                sum.append(self.values[i] + other)
            return Vector(sum)
        else:
            print("Can't add Vector with {}".format(type(other)))

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Vector):
            return self + (-1 * other)
        elif isinstance(other, Real):
            return self + (-other)
        else:
            print("Can't sub a Vector with {}".format(type(other)))

    def __rsub__(self, other):
        if isinstance(other, Real):
            return other + (-1 * self)
        else:
            print("Can't sub a Vector with {}".format(type(other)))

    def __mul__(self, other):
        if isinstance(other, Vector):
            if self.size == other.size:
                sum = []
                for i in range(self.size):
                    sum.append(self.values[i] * other.values[i])
                return Vector(sum)
            else:
                print("Vector <{}> has not a size of {}".format(other,
                      self.size))
        elif isinstance(other, Real):
            sum = []
            for i in range(self.size):
                sum.append(self.values[i] * other)
            return Vector(sum)
        else:
            print("Can't mult Vector with {}".format(type(other)))

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, Real):
            if other == 0:
                print("Can't div by 0 !")
            else:
                return self * (1.0 / other)
        else:
            print("Can't div Vector with {}".format(type(other)))

    def __rtruediv__(self, other):
        if isinstance(other, Real):
            sum = []
            for value in self.values:
                if value == 0:
                    print("Can't div by 0 !")
                    return None
                else:
                    sum.append(other / value)
            return Vector(sum)
        else:
            print("Can't div {} by a Vector".format(type(other)))

    def __repr__(self):
        print(str(self))
        print("Dimension: {}x1".format(self.size))
        return self.values
