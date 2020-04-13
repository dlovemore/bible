>>> from bible import *
>>> b/'Jehovah'
Genesis 22:14;Exodus 6:3;17:15;Judges 6:24;Psalms 83:18;Isaiah 12:2;26:4 (7 verses)
>>> p(_)
Genesis 22:14 And Abraham called the name of that place Jehovahjireh: as it is said to this day, In the mount of the LORD it shall be seen.
Exodus 6:3 And I appeared unto Abraham, unto Isaac, and unto Jacob, by the name of God Almighty, but by my name JEHOVAH was I not known to them.
Exodus 17:15 And Moses built an altar, and called the name of it Jehovahnissi:
Judges 6:24 Then Gideon built an altar there unto the LORD, and called it Jehovahshalom: unto this day it is yet in Ophrah of the Abiezrites.
Psalms 83:18 That men may know that thou, whose name alone is JEHOVAH, art the most high over all the earth.
Isaiah 12:2 Behold, God is my salvation; I will trust, and not be afraid: for the LORD JEHOVAH is my strength and my song; he also is become my salvation.
Isaiah 26:4 Trust ye in the LORD for ever: for in the LORD JEHOVAH is everlasting strength:
>>> sums('JEHOVAH')
(69, 492)
>>> 3*23,12*41
(69, 492)
>>> tell('King')
K  i n  g =
11 9 14 7 41
>>> pf(86)
Counter({2: 1, 43: 1})
>>> 
>>> sums('LORD JEHOVAH')
(118, 676)
>>> count('God')
26
>>> count('God')**2
676
>>> tell('Jehovahjireh Jehovahnissi Jehovahshalom')
Jehovahjireh Jehovahnissi Jehovahshalom  =
    119          139           137      395
>>> tell('Jehovahjireh Jehovahnissi Jehovahshalom',ssum)
Jehovahjireh Jehovahnissi Jehovahshalom  =
    614          760           731      2105
>>> 
>>> lmap=F(list)@F(map)
>>> 
>>> (b/'jehovah').tell()
And Abraham called the name of that place Jehovahjireh: as it is said to this day, In the mount of the LORD it shall be seen.  =
 19    44     37    33  33  21  49    37       119      20 29 28  33  35  56   30  23  33   83  21  33  49  29   52  7    43  996
And I appeared unto Abraham, unto Isaac, and unto Jacob, by the name of God Almighty, but by my name JEHOVAH was I not known to them.  =
 19 9    66     70     44     70    33    19  70    31   27  33  33  21  26     95     43 27 38  33     69    43 9  49   77  35   46  1135
And Moses built an altar, and called the name of it Jehovahnissi:  =
 19   71    64  15   52    19   37    33  33  21 29      139      532
Then Gideon built an altar there unto the LORD, and called it Jehovahshalom: unto this day it is yet in Ophrah of the Abiezrites.  =
 47    54     64  15   52    56   70   33   49   19   37   29      137        70   56   30 29 28  50 23   66   21  33     114     1182
That men may know that thou, whose name alone is JEHOVAH, art the most high over all the earth.  =
 49   32  39  63   49    64    70   33    47  28    69     39  33  67   32   60   25  33   52   884
Behold, God is my salvation; I will trust, and not be afraid: for the LORD JEHOVAH is my strength and my song; he also is become my salvation.  =
   46    26 28 38    113     9  56    98    19  49 7     39    39  33  49     69   28 38   111     19 38   55  13  47  28   43   38    113     1289
Trust ye in the LORD for ever: for in the LORD JEHOVAH is everlasting strength:  =
  98  30 23  33  49   39   50   39 23  33  49     69   28     132        111    806
>>> np(139)
34
>>>
>>> 
>>> tell('Holy Ghost',lsum,osum,ssum)
Holy Ghost  =
 4     5    9
 60    69  129
798   375  1173
>>> 
