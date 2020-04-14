>>> from bible import *
>>> np(103)
27
>>> prime(39)
167
>>> Psalms.chn()
479
>>> 478+167
645
>>> b.chapter(645)
Proverbs 17:1-28 (28 verses)
>>> Proverbs
Proverbs 1:1-31:31 (915 verses)
>>> Genesis
Genesis 1:1-50:26 (1533 verses)
>>> [ch.vc() for ch in Genesis.chapters()]
[31, 25, 24, 26, 32, 22, 24, 22, 29, 32, 32, 20, 18, 24, 21, 16, 27, 33, 38, 18, 34, 24, 20, 67, 34, 35, 46, 22, 35, 43, 55, 32, 20, 31, 29, 43, 36, 30, 23, 23, 57, 38, 34, 34, 28, 34, 31, 22, 33, 26]
>>> tale(_)
[31, 56, 80, 106, 138, 160, 184, 206, 235, 267, 299, 319, 337, 361, 382, 398, 425, 458, 496, 514, 548, 572, 592, 659, 693, 728, 774, 796, 831, 874, 929, 961, 981, 1012, 1041, 1084, 1120, 1150, 1173, 1196, 1253, 1291, 1325, 1359, 1387, 1421, 1452, 1474, 1507, 1533]
>>> b.v(1611)
'And it shall come to pass, if they will not believe also these two signs, neither hearken unto thy voice, that thou shalt take of the water of the river, and pour it upon the dry land: and the water which thou takest out of the river shall become blood upon the dry land.'
>>> Psalm.verse(1611)
Psalms 103:1 Bless the LORD, O my soul: and all that is within me, bless his holy name.
>>> pf(1611)
Counter({3: 2, 179: 1})
>>> 
