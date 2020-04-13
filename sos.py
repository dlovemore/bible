>>> # sum of squares
>>> from bible import *
>>> Genesis-Micah
Genesis 1:1-Micah 7:20 (22685 verses)
>>> b[1]-b[33]
Genesis 1:1-Micah 7:20 (22685 verses)
>>> _.chc()
900
>>> b[34]-b[66]
Nahum 1:1-Revelation 22:21 (8417 verses)
>>> _.chc()
289
>>> 30**2,17**2
(900, 289)
>>> sum(_)
1189
>>> Row([b[1]-b[33],b[34]-b[66]])
Row([Genesis 1:1-Micah 7:20 (22685 verses), Nahum 1:1-Revelation 22:21 (8417 verses)])
>>> _@method.chc
900 289
>>> _@math.sqrt
<console>:1: TypeError: must be real number, not Sel
/home/pi/python/parle/table.py:48: TypeError: must be real number, not Sel
    f=<built-in function sqrt>
    self=Genesis 1
1 In the beginning God created the heaven and the ...
/home/pi/python/parle/func.py:19: TypeError: must be real number, not Sel
    k=<map object at 0xb58b2d10>
    self=<func.GetItem object at 0xb646edd0>
>>> 
>>> 
>>> 
