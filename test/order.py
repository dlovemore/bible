>>> from bible import *
>>> lbs=[(b.wc(), b) for b in bible.books()]
>>> lbs.sort()
>>> lbs
[(294, 3 John 1:1-14 (14 verses)), (298, 2 John 1:1-13 (13 verses)), (430, Philemon 1:1-25 (25 verses)), (608, Jude 1:1-25 (25 verses)), (669, Obadiah 1:1-21 (21 verses)), (896, Titus 1:1-3:15 (46 verses)), (1022, 2 Thessalonians 1:1-3:18 (47 verses)), (1130, Haggai 1:1-2:23 (38 verses)), (1284, Nahum 1:1-3:19 (47 verses)), (1320, Jonah 1:1-4:11 (48 verses)), (1475, Habakkuk 1:1-3:19 (56 verses)), (1553, 2 Peter 1:1-3:18 (61 verses)), (1617, Zephaniah 1:1-3:20 (53 verses)), (1666, 2 Timothy 1:1-4:22 (83 verses)), (1781, Malachi 1:1-4:6 (55 verses)), (1837, 1 Thessalonians 1:1-5:28 (89 verses)), (1979, Colossians 1:1-4:18 (95 verses)), (2033, Joel 1:1-3:21 (73 verses)), (2183, Philippians 1:1-4:23 (104 verses)), (2244, 1 Timothy 1:1-6:21 (113 verses)), (2304, James 1:1-5:20 (108 verses)), (2475, 1 Peter 1:1-5:14 (105 verses)), (2516, 1 John 1:1-5:21 (105 verses)), (2574, Ruth 1:1-4:22 (85 verses)), (2658, Song of Solomon 1:1-8:14 (117 verses)), (3022, Ephesians 1:1-6:24 (155 verses)), (3084, Galatians 1:1-6:18 (149 verses)), (3152, Micah 1:1-7:20 (105 verses)), (3411, Lamentations 1:1-5:22 (154 verses)), (4216, Amos 1:1-9:15 (146 verses)), (5174, Hosea 1:1-14:9 (197 verses)), (5579, Ecclesiastes 1:1-12:14 (222 verses)), (5631, Esther 1:1-10:3 (167 verses)), (6065, 2 Corinthians 1:1-13:14 (257 verses)), (6443, Zechariah 1:1-14:21 (211 verses)), (6897, Hebrews 1:1-13:25 (303 verses)), (7440, Ezra 1:1-10:44 (280 verses)), (9422, Romans 1:1-16:27 (433 verses)), (9462, 1 Corinthians 1:1-16:24 (437 verses)), (10480, Nehemiah 1:1-13:31 (406 verses)), (11603, Daniel 1:1-12:13 (357 verses)), (11995, Revelation 1:1-22:21 (404 verses)), (15038, Proverbs 1:1-31:31 (915 verses)), (15166, Mark 1:1-16:20 (678 verses)), (18098, Job 1:1-42:17 (1070 verses)), (18852, Joshua 1:1-24:33 (658 verses)), (18966, Judges 1:1-21:25 (618 verses)), (19094, John 1:1-21:25 (879 verses)), (20365, 1 Chronicles 1:1-29:30 (942 verses)), (20599, 2 Samuel 1:1-24:25 (695 verses)), (23521, 2 Kings 1:1-25:30 (719 verses)), (23684, Matthew 1:1-28:20 (1071 verses)), (24246, Acts 1:1-28:31 (1007 verses)), (24512, 1 Kings 1:1-22:53 (816 verses)), (24541, Leviticus 1:1-27:34 (859 verses)), (25047, 1 Samuel 1:1-31:13 (810 verses)), (25939, Luke 1:1-24:53 (1151 verses)), (26069, 2 Chronicles 1:1-36:23 (822 verses)), (28351, Deuteronomy 1:1-34:12 (959 verses)), (32684, Exodus 1:1-40:38 (1213 verses)), (32893, Numbers 1:1-36:13 (1288 verses)), (37038, Isaiah 1:1-66:24 (1292 verses)), (38264, Genesis 1:1-50:26 (1533 verses)), (39401, Ezekiel 1:1-48:35 (1273 verses)), (42654, Jeremiah 1:1-52:34 (1364 verses)), (42685, Psalms 1:1-150:6 (2461 verses))]
>>> for x,y in lbs: print(x,y.ref())
... 
294 3 John 1:1-14
298 2 John 1:1-13
430 Philemon 1:1-25
608 Jude 1:1-25
669 Obadiah 1:1-21
896 Titus 1:1-3:15
1022 2 Thessalonians 1:1-3:18
1130 Haggai 1:1-2:23
1284 Nahum 1:1-3:19
1320 Jonah 1:1-4:11
1475 Habakkuk 1:1-3:19
1553 2 Peter 1:1-3:18
1617 Zephaniah 1:1-3:20
1666 2 Timothy 1:1-4:22
1781 Malachi 1:1-4:6
1837 1 Thessalonians 1:1-5:28
1979 Colossians 1:1-4:18
2033 Joel 1:1-3:21
2183 Philippians 1:1-4:23
2244 1 Timothy 1:1-6:21
2304 James 1:1-5:20
2475 1 Peter 1:1-5:14
2516 1 John 1:1-5:21
2574 Ruth 1:1-4:22
2658 Song of Solomon 1:1-8:14
3022 Ephesians 1:1-6:24
3084 Galatians 1:1-6:18
3152 Micah 1:1-7:20
3411 Lamentations 1:1-5:22
4216 Amos 1:1-9:15
5174 Hosea 1:1-14:9
5579 Ecclesiastes 1:1-12:14
5631 Esther 1:1-10:3
6065 2 Corinthians 1:1-13:14
6443 Zechariah 1:1-14:21
6897 Hebrews 1:1-13:25
7440 Ezra 1:1-10:44
9422 Romans 1:1-16:27
9462 1 Corinthians 1:1-16:24
10480 Nehemiah 1:1-13:31
11603 Daniel 1:1-12:13
11995 Revelation 1:1-22:21
15038 Proverbs 1:1-31:31
15166 Mark 1:1-16:20
18098 Job 1:1-42:17
18852 Joshua 1:1-24:33
18966 Judges 1:1-21:25
19094 John 1:1-21:25
20365 1 Chronicles 1:1-29:30
20599 2 Samuel 1:1-24:25
23521 2 Kings 1:1-25:30
23684 Matthew 1:1-28:20
24246 Acts 1:1-28:31
24512 1 Kings 1:1-22:53
24541 Leviticus 1:1-27:34
25047 1 Samuel 1:1-31:13
25939 Luke 1:1-24:53
26069 2 Chronicles 1:1-36:23
28351 Deuteronomy 1:1-34:12
32684 Exodus 1:1-40:38
32893 Numbers 1:1-36:13
37038 Isaiah 1:1-66:24
38264 Genesis 1:1-50:26
39401 Ezekiel 1:1-48:35
42654 Jeremiah 1:1-52:34
42685 Psalms 1:1-150:6
>>> 
>>> 
