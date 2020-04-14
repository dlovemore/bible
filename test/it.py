>>> for i in range(10): print(i)
... 
0
1
2
3
4
5
6
7
8
9
>>> range(10)
range(0, 10)
>>> it=iter(range(10))
>>> it
<range_iterator object at 0xb65c0848>
>>> next(it)
0
>>> next(it)
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
4
>>> next(it)
5
>>> next(it)
6
>>> next(it)
7
>>> next(it)
8
>>> next(it)
9
>>> next(it)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
StopIteration
>>> def pots():
...   x=1
...   while True:
...     yield x
...     x*=2
... 
>>> i=iter(pots())
>>> next(i)
1
>>> next(i)
2
>>> next(i)
4
>>> next(i)
8
>>> for i in pots():
...    print(i)
...    if i>100000000000000: break
... 
1
2
4
8
16
32
64
128
256
512
1024
2048
4096
8192
16384
32768
65536
131072
262144
524288
1048576
2097152
4194304
8388608
16777216
33554432
67108864
134217728
268435456
536870912
1073741824
2147483648
4294967296
8589934592
17179869184
34359738368
68719476736
137438953472
274877906944
549755813888
1099511627776
2199023255552
4398046511104
8796093022208
17592186044416
35184372088832
70368744177664
140737488355328
>>> 6**3
216
>>> 2**24
16777216
>>> from auto import *
>>> itertools.islice(pots(),24,25)
<itertools.islice object at 0xb64c3270>
>>> list(_)
[16777216]
>>> list(itertools.islice(pots(),29))
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456]
>>> 2**28
268435456
>>> help(log)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'log' is not defined
>>> help(math.log)
Help on built-in function log in module math:

log(...)
    log(x, [base=math.e])
    Return the logarithm of x to the given base.
    
    If the base not specified, returns the natural logarithm (base e) of x.

>>> from math import *
>>> log(1000000,2)
19.931568569324174
>>> 600*12345
7407000
>>> 2**9.2
588.1335577584816
>>> 2**13.6
12416.750112853179
>>> 2**22.8
7302707.419670377
>>> 
