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
>>> tell(lsum,osum,ssum,'Authorised Version')
Authorised Version  =
    10        7     17
   120       102   222
   777       714   1491
>>> 
>>> tell('NIV',osum,ssum)
N  I  V   =
14 9  22  45
50 9 400 459
>>> tell('New International Version',osum,ssum)
New International Version  =
 42      152        102   296
555      755        714   2024
>>> tell('Authorised Version',lsum,osum,ssum)
Authorised Version  =
    10        7     17
   120       102   222
   777       714   1491
>>> tell('ישראל, Israel')
ישר אל, Israel  =
 51  13   64   128
>>> tell('Authorised King James Version',lsum,osum,ssum)
Authorised King James Version  =
    10      4     5      7     26
   120      41    48    102   311
   777      86   156    714   1733
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
 יְ ה וֹ  שֻׁ֣  עַ =
10 5 6 21 16 58
>>> tell('יְהוֹשֻׁ֣עַ',ssum)
 יְ ה וֹ  שֻׁ֣   עַ  =
10 5 6 300 70 391
>>> tell('jehoshuah',osum,ssum)
j  e h o   s  h  u  a h  =
10 5 8 15  19 8  21 1 8  95
10 5 8 60 100 8 300 1 8 500
>>> sum(sums('Jehoshuah'))
595
>>> sums('light')
(56, 254)
>>> sums('sun of righteousness')
(254, 1550)
>>> 
>>> tell('I AM THAT I AM',osum,ssum)
I AM THAT I AM
9+14+ 49 +9+14= 95
9+41+409 +9+41=509
>>> 
>>> sums('bible')
(30, 48)
>>> sums('book')
(43, 142)
>>> sums('version')
(102, 714)
>>> tell('ESV')
E S  V
5+19+22=46
>>> tell('NIV')
N  I V
14+9+22=45
>>> tell('New International Version',osum,ssum)
New International Version
 42+     152     +  102  =296
555+     755     +  714  =2024
>>> tell('new things',osum,ssum)
new things
 42+  77  =119
555+ 374  =929
>>> b/'new things'
Isaiah 42:9 Behold, the former things are come to pass, and new things do I declare: before they spring forth I tell you of them.
Isaiah 48:6 Thou hast heard, see all this; and will not ye declare it? I have shewed thee new things from this time, even hidden things, and thou didst not know them.
>>> _.tell(lsum,osum,ssum)
Behold, the former things are come  to pass, and new things do I declare: before they spring forth I tell you  of them.
   6   + 3 +  6   +  6   + 3 + 4  + 2 +  4  + 3 + 3 +  6   +2 +1+   7    +  6   + 4  +  6   +  5  +1+ 4  + 3  +2 +  4  = 91
   46  + 33+  75  +  77  + 24+ 36 + 35+  55 + 19+ 42+  77  +19+9+   48   +  51  + 58 +  83  +  67 +9+ 49 + 61 +21+  46 =1040
  109  +213+ 291  + 374  + 96+108 +260+ 271 + 55+555+ 374  +64+9+  138   + 168  +913 + 326  + 364 +9+265 +1060+66+ 253 =6341
Thou hast heard, see all this; and will not  ye declare it? I have shewed thee new things from this time, even hidden things, and thou didst not know them.
 4  + 4  +  5   + 3 + 3 +  4  + 3 + 4  + 3 + 2 +   7   + 2 +1+ 4  +  6   + 4  + 3 +  6   + 4  + 4  +  4  + 4  +  6   +   6   + 3 + 4  +  5  + 3 + 4  +  4  =119
 64 + 48 +  36  + 29+ 25+  56 + 19+ 56 + 49+ 30+   48  + 29+9+ 36 +  64  + 38 + 42+  77  + 52 + 56 +  47 + 46 +  44  +   77  + 19+ 64 +  56 + 49+ 63 +  46 =1374
568 +309 + 108  +110+ 61+ 317 + 55+569 +310+705+  138  +209+9+414 + 622  +218 +555+ 374  +196 +317 + 254 +460 +  80  +  374  + 55+568 + 317 +310+630 + 253 =9465
>>> tell('you of them',osum,ssum)
you  of them
 61 +21+ 46 =128
1060+66+253 =1379
>>> tell('and new',osum,ssum)
and new
 19+ 42= 61
 55+555=610
>>> tell('new things',osum,ssum)
new things
 42+  77  =119
555+ 374  =929
>>> 555+555
1110
>>> 2*555
1110
>>> 
