>>> from bible import *
>>> from math import *
>>> log(pi)
1.1447298858494002
>>> b[11:44]
Leviticus 11:44;1 Chronicles 11:44;Daniel 11:44;Luke 11:44;John 11:44 (5 verses)
>>> b[114:4]
Psalms 114:4 The mountains skipped like rams, and the little hills like lambs.
>>> Psalm[114]
Psalms 114:1-8 (8 verses)
>>> p(_)
Psalms 114
1 When Israel went out of Egypt, the house of Jacob from a people of strange language;
2 Judah was his sanctuary, and Israel his dominion.
3 The sea saw it, and fled: Jordan was driven back.
4 The mountains skipped like rams, and the little hills like lambs.
5 What ailed thee, O thou sea, that thou fleddest? thou Jordan, that thou wast driven back?
6 Ye mountains, that ye skipped like rams; and ye little hills, like lambs?
7 Tremble, thou earth, at the presence of the Lord, at the presence of the God of Jacob;
8 Which turned the rock into a standing water, the flint into a fountain of waters.
>>> Psalm[114].tell(lsum)
When Israel went out of Egypt, the house of Jacob from a people of strange language; =
 4     6     4    3  2    5     3    5   2    5    4   1   6    2     7        8     67
Judah was his sanctuary, and Israel his dominion. =
  5    3   3      9       3    6     3      8     40
The sea saw it, and fled: Jordan was driven back. =
 3   3   3   2   3    4     6     3    6      4   37
The mountains skipped like rams, and the little hills like lambs. =
 3      9        7     4     4    3   3    6      5    4     5    53
What ailed thee, O thou sea, that thou fleddest? thou Jordan, that thou wast driven back? =
 4     5     4   1  4    3    4    4       8      4      6     4    4    4     6      4   69
Ye mountains, that ye skipped like rams; and ye little hills, like lambs? =
2      9       4   2     7     4     4    3  2    6      5     4     5    57
Tremble, thou earth, at the presence of the Lord, at the presence of the God of Jacob; =
   7      4     5    2   3     8     2   3    4   2   3     8     2   3   3  2    5    66
Which turned the rock into a standing water, the flint into a fountain of waters. =
  5     6     3   4    4   1    8       5     3    5    4   1    8     2     6    65
>>> tale([67,40,37,53,69,57,66,65])
[67, 107, 144, 197, 266, 323, 389, 454]
>>> Psalm[114].tell(osum)
When Israel went out of Egypt, the house of Jacob from a people of strange language;  =
 50    64    62   56 21   73    33   68  21   31   52  1   69   21    84       68    774
Judah was his sanctuary, and Israel his dominion.  =
  44   43  36    122      19   64    36     93    457
The sea saw it, and fled: Jordan was driven back.  =
 33  25  43  29  19   27    62    43   72     17  370
The mountains skipped like rams, and the little hills like lambs.  =
 33    126       80    37    51   19  33   78     60   37    47   601
What ailed thee, O  thou sea, that thou fleddest? thou Jordan, that thou wast driven back?  =
 52    31    38  15  64   25   49   64      75     64     62    49   64   63    72     17  804
Ye mountains, that ye skipped like rams; and ye little hills, like lambs?  =
30    126      49  30    80    37    51   19 30   78     60    37    47   674
Tremble, thou earth, at the presence of the Lord, at the presence of the God of Jacob;  =
   75     64    52   21  33    85    21  33   49  21  33    85    21  33  26 21   31   704
Which turned the rock into a standing water, the flint into a fountain of waters.  =
  51    82    33  47   58  1    88      67    33   61   58  1   100    21    86   787
>>> 
