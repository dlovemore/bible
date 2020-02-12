>>> from bible import *
>>> from math import *
>>> sums('Eve')
(32, 410)
>>> sums('beginning')
(81, 189)
>>> sums('the end')
(56, 272)
>>> 16*17
272
>>> log(2)
0.6931471805599453
>>> log(pi)
1.1447298858494002
>>> sums('bible')
(30, 48)
>>> sums('Holy Bible')
(90, 846)
>>> sums('The Holy Bible')
(123, 1059)
>>> sums('Authorized Version')
(229, 2191)
>>> sums('Authorised Version')
(222, 1491)
>>> sums('Authorised')
(120, 777)
>>> pf(777)
Counter({3: 1, 7: 1, 37: 1})
>>> sof(777)
1216
>>> sums('Apochrypha')
(111, 1011)
>>> sums('Apochryphal')
(123, 1041)
>>> sums('seventy')
(110, 1460)
>>> tell('יְהוֹשֻׁ֣עַ')
 יְ ה וֹ  שֻׁ֣  עַ
10+5+6+21+16=58
>>> tell('יְהוֹשֻׁ֣עַ',ssum)
 יְ ה וֹ  שֻׁ֣   עַ
10+5+6+300+70=391
>>> tell('jehoshuah')
j  e h o  s  h u  a h
10+5+8+15+19+8+21+1+8=95
>>> tell('I AM THAT I AM')
I AM THAT I AM
9+14+ 49 +9+14=95
>>> sums('bible')
(30, 48)
>>> sums('book')
(43, 142)
>>> sums('version')
(102, 714)
>>> 
