>>> from bible import *
>>> b.verse(15551)
Psalms 103:1 Bless the LORD, O my soul: and all that is within me, bless his holy name.
>>> (Psalm[1]-Psalm[103:1]).vc()
1611
>>> Numbers[27:7]
Numbers 27:7 The daughters of Zelophehad speak right: thou shalt surely give them a possession of an inheritance among their father's brethren; and thou shalt cause the inheritance of their father to pass unto them.
>>> 
>>> 
>>> Luke[1:20]
Luke 1:20 And, behold, thou shalt be dumb, and not able to speak, until the day that these things shall be performed, because thou believest not my words, which shall be fulfilled in their season.
>>> 
>>> b.verse(500)
Genesis 20:4 But Abimelech had not come near her: and he said, LORD, wilt thou slay also a righteous nation?
>>> 
>>> b.vc()
31102
>>> Genesis[1]-Genesis[19]
Genesis 1:1-19:38 (496 verses)
>>> Genesis-Psalms
Genesis 1:1-Psalms 150:6 (16401 verses)
>>> p(_.chc())
628
>>> isperfect(6),isperfect(28),isperfect(496)
(True, True, True)
>>> pf (628)
Counter({2: 2, 157: 1})
>>> pf(257)
Counter({257: 1})
>>> np(257)
55
>>> 3088286401
3088286401
>>> 23<<27|39<<15|11<<6|1
3088286401
>>> pf(_)
Counter({6619: 1, 466579: 1})
>>> pf(3088286400)
Counter({2: 6, 5: 2, 3: 1, 37: 1, 17389: 1})
>>> b.verse(17389)
Ecclesiastes 4:7 Then I returned, and I saw vanity under the sun.
>>> 
>>> [bk.vc() for bk in bible.books()]
[1533, 1213, 859, 1288, 959, 658, 618, 85, 810, 695, 816, 719, 942, 822, 280, 406, 167, 1070, 2461, 915, 222, 117, 1292, 1364, 154, 1273, 357, 197, 73, 146, 21, 48, 105, 47, 56, 53, 38, 211, 55, 1071, 678, 1151, 879, 1007, 433, 437, 257, 149, 155, 104, 95, 89, 47, 113, 83, 46, 25, 303, 108, 105, 61, 105, 13, 14, 25, 404]
>>> tale(_)
[1533, 2746, 3605, 4893, 5852, 6510, 7128, 7213, 8023, 8718, 9534, 10253, 11195, 12017, 12297, 12703, 12870, 13940, 16401, 17316, 17538, 17655, 18947, 20311, 20465, 21738, 22095, 22292, 22365, 22511, 22532, 22580, 22685, 22732, 22788, 22841, 22879, 23090, 23145, 24216, 24894, 26045, 26924, 27931, 28364, 28801, 29058, 29207, 29362, 29466, 29561, 29650, 29697, 29810, 29893, 29939, 29964, 30267, 30375, 30480, 30541, 30646, 30659, 30673, 30698, 31102]
>>> Jeremiah
Jeremiah 1:1-52:34 (1364 verses)
>>> [(Genesis-ch).vc() for ch in Jeremiah.chapters()]
[18966, 19003, 19028, 19059, 19090, 19120, 19154, 19176, 19202, 19227, 19250, 19267, 19294, 19316, 19337, 19358, 19385, 19408, 19423, 19441, 19455, 19485, 19525, 19535, 19573, 19597, 19619, 19636, 19668, 19692, 19732, 19776, 19802, 19824, 19843, 19875, 19896, 19924, 19942, 19958, 19976, 19998, 20011, 20041, 20046, 20074, 20081, 20128, 20167, 20213, 20277, 20311]
>>> Jeremiah[48]
Jeremiah 48:1-47 (47 verses)
>>> b.verse(23456)
Matthew 10:38 And he that taketh not his cross, and followeth after me, is not worthy of me.
>>> b.verse(22334)
Joel 2:22 Be not afraid, ye beasts of the field: for the pastures of the wilderness do spring, for the tree beareth her fruit, the fig tree and the vine do yield their strength.
>>> b.verse(12345)
Nehemiah 3:17 After him repaired the Levites, Rehum the son of Bani. Next unto him repaired Hashabiah, the ruler of the half part of Keilah, in his part.
>>> 
>>> 
>>> 
>>> 
>>> b.chapter(629)
Proverbs 1:1-33 (33 verses)
>>> b[20]
Proverbs 1:1-31:31 (915 verses)
>>> b[19]
Psalms 1:1-150:6 (2461 verses)
>>> b[18]
Job 1:1-42:17 (1070 verses)
>>> b.verse(20000)
Jeremiah 43:2 Then spake Azariah the son of Hoshaiah, and Johanan the son of Kareah, and all the proud men, saying unto Jeremiah, Thou speakest falsely: the LORD our God hath not sent thee to say, Go not into Egypt to sojourn there:
>>> Revelation.vn()
30699
>>> Matthew.vn()
23146
>>> Acts.vn()
26925
>>> Colossians.vn()
29467
>>> Romans.vn()
27932
>>> Galatians.vn()
29059
>>> Ephesians.vn()
29208
>>> Colossians
Colossians 1:1-4:18 (95 verses)
>>> IThessalonians
1 Thessalonians 1:1-5:28 (89 verses)
>>> IIThessalonians
2 Thessalonians 1:1-3:18 (47 verses)
>>> ITimothy
1 Timothy 1:1-6:21 (113 verses)
>>> IITimothy
2 Timothy 1:1-4:22 (83 verses)
>>> Titus
Titus 1:1-3:15 (46 verses)
>>> Philemon
Philemon 1:1-25 (25 verses)
>>> Hebrews
Hebrews 1:1-13:25 (303 verses)
>>> _.verse(303)
Hebrews 13:25 Grace be with you all. Amen.
>>> 
>>> b.wc()
789629
>>> b.midword()
['soul:']
>>> tell('The Father, the Word, the Holy Ghost')
The Father, the Word, the Holy Ghost
 33+   58  + 33+  60 + 33+ 60 +  69 =346
>>> nt.ci(251)
Revelation 13:1-18 (18 verses)
>>> 
>>> (Psalm[59:1]-4).words()
['Deliver', 'me', 'from', 'mine', 'enemies,', 'O', 'my', 'God:', 'defend', 'me', 'from', 'them', 'that', 'rise', 'up', 'against', 'me.', 'Deliver', 'me', 'from', 'the', 'workers', 'of', 'iniquity,', 'and', 'save', 'me', 'from', 'bloody', 'men.', 'For,', 'lo,', 'they', 'lie', 'in', 'wait', 'for', 'my', 'soul:', 'the', 'mighty', 'are', 'gathered', 'against', 'me;', 'not', 'for', 'my', 'transgression,', 'nor', 'for', 'my', 'sin,', 'O', 'LORD.', 'They', 'run', 'and', 'prepare', 'themselves', 'without', 'my', 'fault:', 'awake', 'to', 'help', 'me,', 'and', 'behold.']
>>> p(len(_))
69
>>> tell('JEHOVAH')

=0
>>> _[34]
'in'
>>> (Psalm[59:1]-5).words()
['Deliver', 'me', 'from', 'mine', 'enemies,', 'O', 'my', 'God:', 'defend', 'me', 'from', 'them', 'that', 'rise', 'up', 'against', 'me.', 'Deliver', 'me', 'from', 'the', 'workers', 'of', 'iniquity,', 'and', 'save', 'me', 'from', 'bloody', 'men.', 'For,', 'lo,', 'they', 'lie', 'in', 'wait', 'for', 'my', 'soul:', 'the', 'mighty', 'are', 'gathered', 'against', 'me;', 'not', 'for', 'my', 'transgression,', 'nor', 'for', 'my', 'sin,', 'O', 'LORD.', 'They', 'run', 'and', 'prepare', 'themselves', 'without', 'my', 'fault:', 'awake', 'to', 'help', 'me,', 'and', 'behold.', 'Thou', 'therefore,', 'O', 'LORD', 'God', 'of', 'hosts,', 'the', 'God', 'of', 'Israel,', 'awake', 'to', 'visit', 'all', 'the', 'heathen:', 'be', 'not', 'merciful', 'to', 'any', 'wicked', 'transgressors.', 'Selah.']
>>> p(len(_))
94
>>> p(middle(_))
['for', 'my']
>>> 
>>> 
>>> _.index('soul:')
38
>>> Psalm[59:2].wc()
13
>>> sums('LORD JEHOVAH')
(118, 676)
>>> factors(676)
[2, 2, 13, 13]
>>> count('God')**2
676
>>> 
>>> 
>>> 40+77
117
>>> sums('son')
(48, 210)
>>> tell('lord son')
lord son
 49 + 48=97
>>> tell('lord son',ssum)
lord son
184 +210=394
>>> b/'Jesus'
Matthew 1:1,16,18,21,25-2:1;3:13,15-16;4:1,7,10,12,17-18,23;7:28;8:3-5,7,10,13-14,18,20,22,29,34;9:2,4,9-10,12,15,19,22-23,27-28,30,35;10:5;11:1,4,7,25;12:1,15,25;13:1,34,36,51,53,57;14:1,12-14,16,22,25,27,29,31;15:1,16,21,28-30,32,34;16:6,8,13,17,20-21,24;17:1,4,7-9,11,17-20,22,25-26;18:1-2,22;19:1,14,18,21,23,26,28;20:17,22,25,30,32,34-21:1,6,11-12,16,21,24,27,31,42;22:1,18,29,37,41;23:1;24:1-2,4;26:1,4,6,10,17,19,26,31,34,36,49-52,55,57,59,63-64,69,71,75-27:1,11,17,20,22,26-27,37,46,50,54-55,57-58;28:5,9-10,16,18;Mark 1:1,9,14,17,24-25,41,45;2:5,8,15,17,19;3:7;5:6,13,15,19-21,24,27,30,36;6:4,30,34;7:27;8:1,17,27;9:2,4-5,8,23,25,27,39;10:5,14,18,21,23-24,27,29,32,38-39,42,47,49-52;11:6-7,11,14-15,22,29,33;12:17,24,29,34-35,41;13:2,5;14:6,18,22,27,30,48,53,55,60,62,67,72-15:1,5,15,34,37,43;16:6,9;Luke 1:31;2:21,27,43,52;3:21,23;4:1,4,8,12,14,34-35;5:8,10,12,19,22,31;6:3,9,11;7:3-4,6,9,19,22,37,40;8:28,30,35,38-41,45-46,50;9:33,36,41-43,47,50,58,60,62;10:21,29-30,37,39,41;13:2,12,14;14:3;17:13,17;18:16,19,22,24,37-38,40,42;19:1,3,5,9,35;20:8,34;22:47-48,51-52,63;23:8,20,25-26,28,34,42-43,46,52;24:3,15,19,36;John 1:17,29,36-38,42-43,45,47-48,50;2:1-4,7,11,13,19,22,24;3:2-3,5,10,22;4:1-2,6-7,10,13,16-17,21,26,34,44,46-48,50,53-5:1,6,8,13-17,19;6:1,3,5,10-11,14-15,17,19,22,24,26,29,32,35,42-43,53,61,64,67,70;7:1,6,14,16,21,28,33,37,39,50;8:1,6,9-12,14,19-21,25,28,31,34,39,42,49,54,58-9:1,3,11,14,35,37,39,41;10:6-7,23,25,32,34;11:4-5,9,13-14,17,20-21,23,25,30,32-33,35,38-41,44-46,51,54,56;12:1,3,7,9,11-12,14,16,21-23,30,35-36,44;13:1,3,7-8,10,21,23,25-27,29,31,36,38;14:6,9,23;16:19,31;17:1,3;18:1-2,4-5,7-8,11-12,15,19-20,22-23,28,32-34,36-37;19:1,5,9,11,13,16,18-20,23,25-26,28,30,33,38-40,42;20:2,12,14-17,19,21,24,26,29-21:1,4-5,7,10,12-15,17,20-23,25-Acts 1:1,11,14,16,21;2:22,32,36,38;3:6,13,20,26;4:2,10,13,18,27,30,33;5:30,40,42;6:14;7:45,55,59;8:12,16,35,37;9:5,17,27,29,34;10:36,38;11:17,20;13:23,33;15:11,26;16:18,31;17:3,7,18;18:5,28;19:4-5,10,13,15,17;20:21,24,35;21:13;22:8;25:19;26:9,15;28:23,31-Romans 1:1,3,6-8;2:16;3:22,24,26;4:24;5:1,11,15,17,21;6:3,11,23;7:25-8:2,11,39;10:9;13:14;14:14;15:5-6,8,16-17,30;16:3,18,20,24-25,27-1 Corinthians 1:4,7-10,30;2:2;3:11;4:15;5:4-5;6:11;8:6;9:1;11:23;12:3;15:31,57;16:22-2 Corinthians 1:3,14,19;4:5-6,10-11,14;5:18;8:9;11:4,31;13:5,14-Galatians 1:1,3,12;2:4,16;3:1,14,22,26,28;4:14;5:6;6:14-15,17-Ephesians 1:3,5,15,17;2:6-7,10,13,20;3:1,9,11,14,21;4:21;5:20;6:23-Philippians 1:2,6,8,11,19,26;2:5,10-11,19,21;3:3,8,12,14,20;4:7,19,21,23-Colossians 1:4,28;2:6;3:17;4:11;1 Thessalonians 1:1,3,10;2:14-15,19;3:11,13-4:2,14;5:9,18,23,28-2 Thessalonians 1:2,7-8,12-2:1,14,16;3:6,12,18-1 Timothy 1:2,12,14-16;2:5;3:13;4:6;5:21;6:3,13-14;2 Timothy 1:1-2,9-10,13;2:1,3,8,10;3:12,15;4:1,22-Titus 1:1,4;2:13;3:6;Philemon 1:1,3,5-6,9,23,25;Hebrews 2:9;3:1;4:8,14;6:20;7:22;10:10,19;12:2,24;13:8,12,20-21;James 1:1;2:1;1 Peter 1:1-3,7,13;2:5;3:21;4:11;5:10,14-2 Peter 1:2,8,11,14,16;2:20;3:18;1 John 1:3,7;2:1,22;3:23;4:2-3,15;5:1,5-6,20;2 John 1:3,7;Jude 1:1,4,17,21;Revelation 1:1-2,5,9;12:17;14:12;17:6;19:10;20:4;22:16,20-21 (942 verses)
>>> b/'jehovah'
Genesis 22:14;Exodus 6:3;17:15;Judges 6:24;Psalms 83:18;Isaiah 12:2;26:4 (7 verses)
>>> 6827
6827
>>> b/'beersheba'
Genesis 21:14,31-33;22:19;26:23,33;28:10;46:1,5;Joshua 15:28;19:2;Judges 20:1;1 Samuel 3:20;8:2;2 Samuel 3:10;17:11;24:2,7,15;1 Kings 4:25;19:3;2 Kings 12:1;23:8;1 Chronicles 4:28;21:2;2 Chronicles 19:4;24:1;30:5;Nehemiah 11:27,30;Amos 5:5;8:14 (33 verses)
>>> b.count('beersheba')
34
>>> Amos[5:5]
Amos 5:5 But seek not Bethel, nor enter into Gilgal, and pass not to Beersheba: for Gilgal shall surely go into captivity, and Bethel shall come to nought.
>>> (Luke[1]-Luke[17:35]).vc()
793
>>> (Matthew[1]-Luke[17:35]).vc()
2542
>>> 2542*2
5084
>>> nt.vi(5084)
Romans 11:19 Thou wilt say then, The branches were broken off, that I might be graffed in.
>>> (Luke-Romans).vi(793*2)
John 9:39 And Jesus said, For judgment I am come into this world, that they which see not might see; and that they which see might be made blind.
>>> rebase(8,2020)
1040
>>> 1123-1040
83
>>> 1189-1040
149
>>> base(2,2020)
[1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0]
>>> 
