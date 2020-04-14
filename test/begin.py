>>> from bible import *
>>> # tell=tellmd
>>> sums('begin')
(5, 37, 73)
>>> b/'hair'/'numbered'
Matthew 10:30 But the very hairs of your head are all numbered.
Luke 12:7 But even the very hairs of your head are all numbered. Fear not therefore: ye are of more value than many sparrows.
>>> tell('account',osum,ssum)
a c c o   u  n   t   =
1 3 3 15  21 14  20  77
1 3 3 60 300 50 200 617
>>> 
>>> tell('בן',osum,ssum)
ב ן  =
2 14 16
2 50 52
>>> tell('stars')
s  t  a r  s  =
19 20 1 18 19 77
>>> 
>>> tell('שֶׁ֣מֶשׁ',lsum,osum,ssum)
 שֶׁ֣   מֶ  שׁ   =
 1  1   1   3
 21 13  21  55
300 40 300 640
>>> sums('son')
(48, 210)
>>> sums('sun')
(54, 450)
>>> tell('sun of-righteousness',osum,ssum)
sun of-righteousness  =
 54       200        254
450       1100       1550
>>> tell('like a lamb',lsum,osum,ssum)
like a lamb  =
 4   1  4    9
 37  1  28   66
 64  1  73  138
>>> tell('begin',osum,ssum)
b e g i n  =
2 5 7 9 14 37
2 5 7 9 50 73
>>> osum('דוד')
14
>>> sof(_)
24
>>> tell('',osum,ssum)
=
0
0
>>> tell('Jes us',osum,ssum)
Jes  us  =
 34  40  74
115 400 515
>>> tell('Lord Jes us christ',osum,ssum)
Lord Jes  us christ  =
 49   34  40   77   200
184  115 400  410   1109
>>> tell('the christ',lsum,osum,ssum)
the christ  =
 3    6     9
 33   77   110
213  410   623
>>> 
>>> tell('the sun of righteousness',osum,ssum)
the sun of righteousness  =
 33  54 21      179      287
213 450 66      1034     1763
>>> tell('ישוע',osum,ssum)
י   ש  ו ע   =
10  21 6 16  53
10 300 6 70 386
>>> tell('כּ֣וֹכָבִ֔ים')
כּ֣  וֹ  כָ בִ֔ י  ם  =
11 6 11 2 10 13 53
>>> 
>>> tell('כּ֣וֹכָבִ֔ים')
>>> Matthew[10:30].tell(lsum,osum,ssum)
But the very hairs of your head are all numbered.  =
 3   3   4     5   2   4    4    3   3      8      39
 43  33  70    55  21  79   18   24  25     82    450
502 213 1195  208  66 1150  18   96  61    496    4005
>>> Psalm[94:9].tell(lsum,osum,ssum)
He that planted the ear, shall he not hear? he that formed the eye, shall he not see?  =
2   4      7     3   3     5   2   3    4   2   4     6     3   3     5   2   3   3    64
13  49     72    33  24    52  13  49   32  13  49    61    33  35    52  13  49  29  671
13 409    360   213  96   169  13 310  104  13 409   205   213 710   169  13 310 110  3839
>>> 
