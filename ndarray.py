from numpy import *

a = arange(15).reshape(3,5)
print 'a  ',a
# rank, number of axsis
print 'ndim  ',a.ndim
print 'shape  ',a.shape
print 'size  ',a.size
print 'dtype  ',a.dtype
# byte size of each item
print 'itemisize  ',a.itemsize
print 'data  ',a.data

## CREATION
# from python list and tuple
b = array([1, 2, 3])
c = array((2, 4, 5, 6))
print 'b', b
print 'c', c

d = array([ (1, 3), (4, 5)])
e = array([ [2, 5], [6, 8]], dtype=complex)
print 'd', d
print 'e', e

# zero-initialized
z = zeros((3,4), dtype=float)
print 'z', z

#random initialized
f = empty((3,4), dtype=int64)
print 'f', f

# range-like
g = arange(10, 30, 5)
print 'g', g
h = arange(0, 2, 0.3)
print 'h', h
# linspace - do not need step size, but need item numbers
i = linspace(0, 2, 8)
print 'i', i
# useful to plot function
x = linspace(0, 2*pi, 100)
y = sin(x)
print zip(x, y)

# print shape
set_printoptions(threshold=10)
print arange(1000)
print arange(10)
print arange(9)
set_printoptions(threshold=9)
print arange(10)
