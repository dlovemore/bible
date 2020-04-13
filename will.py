class Item:
    def __init__(self, bcvs):
        self.doc = bcvs
    def v(book,ch,v):
        vs = [x for x in self.doc if x[0]==book and x[1]==ch and x[2]==v]
        return vs[0]
    def __getitem__(self,x):
        ch,v = x.start,x.stop
        vs = [x for x in self.doc if x[1]==ch and x[2]==v]
        return '\n'.join([f'{x[0]} {ch}:{v} {x[3]}' for x in vs])

def getbook(item, s):
    return Item([v for v in item.doc if v[0]==s])

def fib(n):
    if n==0: return 0
    if n==1: return 1
    if n==2: return 1
    return fib(n-1)+fib(n-2)

# >>> from will import *
# >>> import kjv, pce
# >>> bible=Item(kjv.kjv)
# >>> pce=Item(pce.pce)
# >>> getbook(pce, '2 John')
# <will.Item object at 0xb531b3d0>
# >>> IIJohn=getbook(bible, '2 John')
# >>> IIJohn[1:1]
# '2 John 1:1 The elder unto the elect lady and her children, whom I love in the truth; and not I only, but also all they that have known the truth;'
# >>> 
# >>> fib(1)
# 1
# >>> fib(2)
# 1
# >>> 1+1
# 2
# >>> fib(3)
# 2
# >>> 2+1
# 3
# >>> 2+3
# 5
# >>> 3+5
# 8
# >>> 5+8
# 13
# >>> 8+13
# 21
# >>> 13+21
# 34
# >>> fib(9)
# 34
# >>> fib(10)
# 55
# >>> fib(11)
# 89
# >>> 1123+66
# 1189
# >>> from primes import *
# >>> Fn(11)
# 89
# >>> 
# >>> 
