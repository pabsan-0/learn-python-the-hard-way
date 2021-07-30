class X(object):
    def __init__(self):
        self.foo = 2

class Y(X):
    def __init__(self):
        self.foo = 3
    def wow(self):
        print self.foo
        print 2

foo = X()
Y = Y()
print Y.foo