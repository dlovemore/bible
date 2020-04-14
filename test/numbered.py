>>> from bible import *
>>> # tell=tellmd
>>> b/'hair'/'numbered'
Matthew 10:30 But the very hairs of your head are all numbered.
Luke 12:7 But even the very hairs of your head are all numbered. Fear not therefore: ye are of more value than many sparrows.
>>> _.tell(lsum,osum,ssum)
But the very hairs of your head are all numbered.  =
 3   3   4     5   2   4    4    3   3      8      39
 43  33  70    55  21  79   18   24  25     82    450
502 213 1195  208  66 1150  18   96  61    496    4005
But even the very hairs of your head are all numbered. Fear not therefore:  ye are of more value than many sparrows.  =
 3   4    3   4     5   2   4    4    3   3      8      4    3      9       2   3  2   4     5    4    4       8      91
 43  46   33  70    55  21  79   18   24  25     82     30   49    100      30  24 21  51    61   43   53     129    1087
502 460  213 1195  208  66 1150  18   96  61    496    102  310    469     705  96 66 195   736  259  791     1011   9205
>>> 
>>> 
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
>>> tell('son')
s  o  n  =
19 15 14 48
>>> tell('sun')
s  u  n  =
19 21 14 54
>>> tell('sun of righteousness',osum,ssum)
sun of righteousness  =
 54 21      179      254
450 66      1034     1550
>>> tell('the sun of righteousness',osum,ssum)
the sun of righteousness  =
 33  54 21      179      287
213 450 66      1034     1763
>>> tell('ישוע')
י  ש  ו ע  =
10 21 6 16 53
>>> tell('ישוע',ssum)
י   ש  ו ע   =
10 300 6 70 386
>>> tell('כּ֣וֹכָבִ֔ים')
כּ֣  וֹ  כָ בִ֔ י  ם  =
11 6 11 2 10 13 53
>>> 
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
