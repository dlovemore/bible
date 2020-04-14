>>> from bible import *
>>> 116+31102
31218
>>> pf(_)
Counter({11: 2, 2: 1, 3: 1, 43: 1})
>>> 11*66*43
31218
>>> 11*43
473
>>> 473*66
31218
>>> 1189/66
18.015151515151516
>>> 18*66
1188
>>> 9*66
594
>>> 3*6*66+1
1189
>>> rebase(33, [1,3,1])
1189
>>> 31102/1189
26.15811606391926
>>> sums('Jesus wept')
(138, 1290)
>>> John[11:35]
John 11:35 Jesus wept.
>>> 
>>> 
>>> 
>>> Esther[8:9].wc()
90
>>> b[17][8:9]
Esther 8:9 Then were the king's scribes called at that time in the third month, that is, the month Sivan, on the three and twentieth day thereof; and it was written according to all that Mordecai commanded unto the Jews, and to the lieutenants, and the deputies and rulers of the provinces which are from India unto Ethiopia, an hundred twenty and seven provinces, unto every province according to the writing thereof, and unto every people after their language, and to the Jews according to their writing, and according to their language.
>>> Genesis.wc()
38264
>>> pf(38262)
Counter({2: 1, 3: 1, 7: 1, 911: 1})
>>> pf(38264)
Counter({2: 3, 4783: 1})
>>> pf(38263)
Counter({83: 1, 461: 1})
>>> [(book,book.wc()) for book in bible.books()]
[(Genesis 1:1-50:26 (1533 verses), 38264), (Exodus 1:1-40:38 (1213 verses), 32684), (Leviticus 1:1-27:34 (859 verses), 24541), (Numbers 1:1-36:13 (1288 verses), 32893), (Deuteronomy 1:1-34:12 (959 verses), 28351), (Joshua 1:1-24:33 (658 verses), 18852), (Judges 1:1-21:25 (618 verses), 18966), (Ruth 1:1-4:22 (85 verses), 2574), (1 Samuel 1:1-31:13 (810 verses), 25047), (2 Samuel 1:1-24:25 (695 verses), 20599), (1 Kings 1:1-22:53 (816 verses), 24512), (2 Kings 1:1-25:30 (719 verses), 23521), (1 Chronicles 1:1-29:30 (942 verses), 20365), (2 Chronicles 1:1-36:23 (822 verses), 26069), (Ezra 1:1-10:44 (280 verses), 7440), (Nehemiah 1:1-13:31 (406 verses), 10480), (Esther 1:1-10:3 (167 verses), 5631), (Job 1:1-42:17 (1070 verses), 18098), (Psalms 1:1-150:6 (2461 verses), 42685), (Proverbs 1:1-31:31 (915 verses), 15038), (Ecclesiastes 1:1-12:14 (222 verses), 5579), (Song of Solomon 1:1-8:14 (117 verses), 2658), (Isaiah 1:1-66:24 (1292 verses), 37038), (Jeremiah 1:1-52:34 (1364 verses), 42654), (Lamentations 1:1-5:22 (154 verses), 3411), (Ezekiel 1:1-48:35 (1273 verses), 39401), (Daniel 1:1-12:13 (357 verses), 11603), (Hosea 1:1-14:9 (197 verses), 5174), (Joel 1:1-3:21 (73 verses), 2033), (Amos 1:1-9:15 (146 verses), 4216), (Obadiah 1:1-21 (21 verses), 669), (Jonah 1:1-4:11 (48 verses), 1320), (Micah 1:1-7:20 (105 verses), 3152), (Nahum 1:1-3:19 (47 verses), 1284), (Habakkuk 1:1-3:19 (56 verses), 1475), (Zephaniah 1:1-3:20 (53 verses), 1617), (Haggai 1:1-2:23 (38 verses), 1130), (Zechariah 1:1-14:21 (211 verses), 6443), (Malachi 1:1-4:6 (55 verses), 1781), (Matthew 1:1-28:20 (1071 verses), 23684), (Mark 1:1-16:20 (678 verses), 15166), (Luke 1:1-24:53 (1151 verses), 25939), (John 1:1-21:25 (879 verses), 19094), (Acts 1:1-28:31 (1007 verses), 24246), (Romans 1:1-16:27 (433 verses), 9422), (1 Corinthians 1:1-16:24 (437 verses), 9462), (2 Corinthians 1:1-13:14 (257 verses), 6065), (Galatians 1:1-6:18 (149 verses), 3084), (Ephesians 1:1-6:24 (155 verses), 3022), (Philippians 1:1-4:23 (104 verses), 2183), (Colossians 1:1-4:18 (95 verses), 1979), (1 Thessalonians 1:1-5:28 (89 verses), 1837), (2 Thessalonians 1:1-3:18 (47 verses), 1022), (1 Timothy 1:1-6:21 (113 verses), 2244), (2 Timothy 1:1-4:22 (83 verses), 1666), (Titus 1:1-3:15 (46 verses), 896), (Philemon 1:1-25 (25 verses), 430), (Hebrews 1:1-13:25 (303 verses), 6897), (James 1:1-5:20 (108 verses), 2304), (1 Peter 1:1-5:14 (105 verses), 2475), (2 Peter 1:1-3:18 (61 verses), 1553), (1 John 1:1-5:21 (105 verses), 2516), (2 John 1:1-13 (13 verses), 298), (3 John 1:1-14 (14 verses), 294), (Jude 1:1-25 (25 verses), 608), (Revelation 1:1-22:21 (404 verses), 11995)]
>>> tri(89)
4005
>>> nt.verse(4005)
Acts 7:33 Then said the Lord to him, Put off thy shoes from thy feet: for the place where thou standest is holy ground.
>>> nt.verse(4000)
Acts 7:28 Wilt thou kill me, as thou diddest the Egyptian yesterday?
>>> nt.verse(4048)
Acts 8:16 (For as yet he was fallen upon none of them: only they were baptized in the name of the Lord Jesus.)
>>> nt.verse(4044)
Acts 8:12 But when they believed Philip preaching the things concerning the kingdom of God, and the name of Jesus Christ, they were baptized, both men and women.
>>> Acts[8]
Acts 8:1-40 (40 verses)
>>> Acts[8].wc()
883
>>> np(883)
153
>>> pf(153)
Counter({3: 2, 17: 1})
>>> allfactors(153)
[1, 3, 9, 17, 51, 153]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> [ch.wc() for ch in Matthew.chapters()]
[473, 619, 387, 557, 1081, 794, 626, 773, 837, 919, 668, 1168, 1367, 721, 785, 688, 620, 869, 719, 779, 1126, 828, 833, 1047, 995, 1625, 1359, 421]
>>> 23684-23343
341
>>> 
>>> 
