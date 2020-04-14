>>> from bible import *
>>> b.vi(1)
Genesis 1:1 In the beginning God created the heaven and the earth.
>>> b.vi(2)
Genesis 1:2 And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.
>>> b.vi(3)
Genesis 1:3 And God said, Let there be light: and there was light.
>>> b.vi(5)
Genesis 1:5 And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day.
>>> b.vi(8)
Genesis 1:8 And God called the firmament Heaven. And the evening and the morning were the second day.
>>> b.vi(13)
Genesis 1:13 And the evening and the morning were the third day.
>>> b.vi(21)
Genesis 1:21 And God created great whales, and every living creature that moveth, which the waters brought forth abundantly, after their kind, and every winged fowl after his kind: and God saw that it was good.
>>> Genesis/'it was good'
Genesis 1:4,10,12,18,21,25 (6 verses)
>>> Genesis/'forth'
Genesis 1:11-12,20-21,24;3:16,18,22-23;8:7-10,12,16-19;9:7,18;10:11;11:31;12:5;14:18;15:4-5;19:10,16-17;22:10;24:43,45,53;30:39;38:24-25,29;39:13;40:10;41:47;42:15 (41 verses)
>>> b.vi(34)
Genesis 2:3 And God blessed the seventh day, and sanctified it: because that in it he had rested from all his work which God created and made.
>>> b.vi(55)
Genesis 2:24 Therefore shall a man leave his father and his mother, and shall cleave unto his wife: and they shall be one flesh.
>>> b.vi(89)
Genesis 4:9 And the LORD said unto Cain, Where is Abel thy brother? And he said, I know not: Am I my brother's keeper?
>>> 123471
123471
>>> pf(_)
Counter({3: 3, 17: 1, 269: 1})
>>> 123471/3
41157.0
>>> 123471/math.pi
39302.03995699882
>>> 12347/math.pi
3930.1721647112636
>>> 12347**.5
111.11705539655017
>>> 111.117**2
12346.987689000001
>>> 111.11**2
12345.4321
>>> pf(12347)
Counter({12347: 1})
>>> np(12347)
1475
>>> 12347+26
12373
>>> np(12373)
1476
>>> 
>>> divmod(12347,49)
(251, 48)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> from bible import *
>>> nF(31102)
<console>:1: NameError: name 'F' is not defined
/home/pi/python/parle/primes.py:168: NameError: name 'F' is not defined
    p=31102
>>> nF(15551)
<console>:1: NameError: name 'F' is not defined
/home/pi/python/parle/primes.py:168: NameError: name 'F' is not defined
    p=15551
>>> [(x,Fibonacci(x)) for x in range(51)]
[(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34), (10, 55), (11, 89), (12, 144), (13, 233), (14, 377), (15, 610), (16, 987), (17, 1597), (18, 2584), (19, 4181), (20, 6765), (21, 10946), (22, 17711), (23, 28657), (24, 46368), (25, 75025), (26, 121393), (27, 196418), (28, 317811), (29, 514229), (30, 832040), (31, 1346269), (32, 2178309), (33, 3524578), (34, 5702887), (35, 9227465), (36, 14930352), (37, 24157817), (38, 39088169), (39, 63245986), (40, 102334155), (41, 165580141), (42, 267914296), (43, 433494437), (44, 701408733), (45, 1134903170), (46, 1836311903), (47, 2971215073), (48, 4807526976), (49, 7778742049), (50, 12586269025)]
>>> Fn(23)
28657
>>> _-31102
-2445
>>> (Genesis[1:1]-(2,3)).wc()
864
>>> nF(_)
(15, 610, -254, 864, 123, 987, 16)
>>> nF(1189)
(16, 987, -202, 1189, 408, 1597, 17)
>>>
