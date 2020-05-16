# >>> from math import *
# >>> from bible import *
# >>> from search import *
# >>> pi
# 3.141592653589793
# >>> g1=b.Gen[1:]
# >>> g1.wc()
# 797
# >>> g1/"God"
# Genesis 1:1-12,14,16-18,20-22,24-29,31 (26 verses)
# >>> 9900*pi
# 31101.767270538952
# >>> 66+150
# 216
# >>> 3**6
# 729
# >>> b.Gen[1:1]
# Genesis 1:1 In the beginning God created the heaven and the earth.
# >>> p(_)
# Genesis 1:1 In the beginning God created the heaven and the earth.
# >>> g1.wcs()
# [10, 29, 11, 17, 22, 23, 26, 16, 25, 24, 34, 33, 10, 34, 22, 26, 16, 25, 10, 29, 34, 23, 10, 30, 34, 50, 22, 46, 42, 39, 25]
# >>> n=0; l=[];
# >>> for x in g1.wcs(): n+=x;l.append(n)
# ... 
# >>> l
# [10, 39, 50, 67, 89, 112, 138, 154, 179, 203, 237, 270, 280, 314, 336, 362, 378, 403, 413, 442, 476, 499, 509, 539, 573, 623, 645, 691, 733, 772, 797]
# >>> [x*(x+1)//2 for x in g1.wcs()]
# [55, 435, 66, 153, 253, 276, 351, 136, 325, 300, 595, 561, 55, 595, 253, 351, 136, 325, 55, 435, 595, 276, 55, 465, 595, 1275, 253, 1081, 903, 780, 325]
# >>> sum(_)
# 12314
# >>> g1.count()
# 34463
# >>> gv=[x.count() for x in b.Gen.chapters()]
# >>> [x*(x+1)//2 for x in gv]
# [593866416, 334408591, 432165300, 354458625, 241901010, 324882795, 337779036, 353819901, 418371201, 247230966, 354352131, 273721503, 197756328, 378881628, 215478420, 149705556, 452538570, 717201001, 1244730565, 248455486, 532048510, 348730845, 273043396, 3116432826, 469879840, 749793450, 1411425015, 327641601, 618482035, 961477026, 2041061886, 621827745, 230512656, 650432278, 392070003, 663955020, 869382451, 587713470, 397042110, 340826886, 1918436653, 987923475, 912477840, 768810078, 545143690, 576352176, 943712290, 396619530, 622992051, 510736780]
# >>> _[24:26]
# [469879840, 749793450]
# >>> 
# >>> 
# >>> sum(_)
# 1219673290
# >>> _//2
# 609836645
# >>> gv=[x.count() for x in b.Gen.chapters()]
# >>> 50*51//2
# 1275
# >>> base(6,37)
# [1, 0, 1]
# >>> bases(73)
# 2 [1, 0, 0, 1, 0, 0, 1]
# 3 [2, 2, 0, 1]
# 4 [1, 0, 2, 1]
# 5 [2, 4, 3]
# 6 [2, 0, 1]
# 7 [1, 3, 3]
# 8 [1, 1, 1]
# 9 [8, 1]
# 10 [7, 3]
# 11 [6, 7]
# 12 [6, 1]
# 13 [5, 8]
# 14 [5, 3]
# 15 [4, 13]
# 16 [4, 9]
# 17 [4, 5]
# 18 [4, 1]
# 19 [3, 16]
# 20 [3, 13]
# 21 [3, 10]
# 22 [3, 7]
# 23 [3, 4]
# 24 [3, 1]
# 25 [2, 23]
# 26 [2, 21]
# 27 [2, 19]
# 28 [2, 17]
# 29 [2, 15]
# 30 [2, 13]
# 31 [2, 11]
# 32 [2, 9]
# 33 [2, 7]
# 34 [2, 5]
# 35 [2, 3]
# 36 [2, 1]
# 37 [1, 36]
# 38 [1, 35]
# 39 [1, 34]
# 40 [1, 33]
# >>> 
# >>> 31*16
# 496
# >>> b.chapters()[495]
# Psalms 18:1-50 (50 verses)
# >>> 930/2
# 465.0
# >>> 
# >>> 
# >>> 17*35
# 595
# >>> 25*51
# 1275
# >>> 23*47
# 1081
# >>> 13*27
# 351
# >>> 25*13
# 325
# >>> 12*25
# 300
# >>> 192/2/2/2/2/2/2
# 3.0
# >>> 3*2**6
# 192
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> x,l = 0,[]
# >>> for i in g1.wcs(): x+=i; l.append(x)
# ... 
# >>> l
# [10, 39, 50, 67, 89, 112, 138, 154, 179, 203, 237, 270, 280, 314, 336, 362, 378, 403, 413, 442, 476, 499, 509, 539, 573, 623, 645, 691, 733, 772, 797]
# >>> 138*pi*2
# 867.0795723907829
# >>> 867/138
# 6.282608695652174
# >>> _/2
# 3.141304347826087
# >>> pi/7
# 0.4487989505128276
# >>> e=exp(1)
# >>> 797*e
# 2166.4706172818587
# >>> 797*14
# 11158
# >>> 11158*2
# 22316
# >>> 11158*3
# 33474
# >>> 314/7
# 44.857142857142854
# >>> 1190/2
# 595.0
# >>> 3e9/789629
# 3799.252560379621
# >>> int('797', base=12)
# 1123
# >>> base(32,1189)
# [1, 5, 5]
# >>> base(33,1189)
# [1, 3, 1]
# >>> base(12, 31102)
# [1, 5, 11, 11, 10]
# >>> 3167
# 3167
# >>> 
# >>> p(g1131)
# <71>:1: NameError: name 'g1131' is not defined
# >>> g1131.wc()
# <72>:1: NameError: name 'g1131' is not defined
# >>> 
# >>> p(b.Gen[1:16])
# Genesis 1:16 And God made two great lights; the greater light to rule the day, and the lesser light to rule the night: he made the stars also.
# >>> b.Gen[1:16].wc()
# 26
# >>> 
# >>> g1/"and"
# Genesis 1:1-31 (31 verses)
# >>> g1/"god"
# Genesis 1:1-12,14,16-18,20-22,24-29,31 (26 verses)
# >>> g1/"create"
# Genesis 1:1,21,27 (3 verses)
# >>> g1/"created"
# Genesis 1:1,21,27 (3 verses)
# >>> g1/"made"
# Genesis 1:7,16,25,31 (4 verses)
# >>> g1/"kind"
# Genesis 1:11-12,21,24-25 (5 verses)
# >>> g1/"heaven"
# Genesis 1:1,8-9,14-15,17,20 (7 verses)
# >>> g1/"earth"
# Genesis 1:1-2,10-12,15,17,20,22,24-26,28-30 (15 verses)
# >>> p(g1)
# Genesis 1
# 1 In the beginning God created the heaven and the earth.
# 2 And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.
# 3 And God said, Let there be light: and there was light.
# 4 And God saw the light, that it was good: and God divided the light from the darkness.
# 5 And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day.
# 6 And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters.
# 7 And God made the firmament, and divided the waters which were under the firmament from the waters which were above the firmament: and it was so.
# 8 And God called the firmament Heaven. And the evening and the morning were the second day.
# 9 And God said, Let the waters under the heaven be gathered together unto one place, and let the dry land appear: and it was so.
# 10 And God called the dry land Earth; and the gathering together of the waters called he Seas: and God saw that it was good.
# 11 And God said, Let the earth bring forth grass, the herb yielding seed, and the fruit tree yielding fruit after his kind, whose seed is in itself, upon the earth: and it was so.
# 12 And the earth brought forth grass, and herb yielding seed after his kind, and the tree yielding fruit, whose seed was in itself, after his kind: and God saw that it was good.
# 13 And the evening and the morning were the third day.
# 14 And God said, Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days, and years:
# 15 And let them be for lights in the firmament of the heaven to give light upon the earth: and it was so.
# 16 And God made two great lights; the greater light to rule the day, and the lesser light to rule the night: he made the stars also.
# 17 And God set them in the firmament of the heaven to give light upon the earth,
# 18 And to rule over the day and over the night, and to divide the light from the darkness: and God saw that it was good.
# 19 And the evening and the morning were the fourth day.
# 20 And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl that may fly above the earth in the open firmament of heaven.
# 21 And God created great whales, and every living creature that moveth, which the waters brought forth abundantly, after their kind, and every winged fowl after his kind: and God saw that it was good.
# 22 And God blessed them, saying, Be fruitful, and multiply, and fill the waters in the seas, and let fowl multiply in the earth.
# 23 And the evening and the morning were the fifth day.
# 24 And God said, Let the earth bring forth the living creature after his kind, cattle, and creeping thing, and beast of the earth after his kind: and it was so.
# 25 And God made the beast of the earth after his kind, and cattle after their kind, and every thing that creepeth upon the earth after his kind: and God saw that it was good.
# 26 And God said, Let us make man in our image, after our likeness: and let them have dominion over the fish of the sea, and over the fowl of the air, and over the cattle, and over all the earth, and over every creeping thing that creepeth upon the earth.
# 27 So God created man in his own image, in the image of God created he him; male and female created he them.
# 28 And God blessed them, and God said unto them, Be fruitful, and multiply, and replenish the earth, and subdue it: and have dominion over the fish of the sea, and over the fowl of the air, and over every living thing that moveth upon the earth.
# 29 And God said, Behold, I have given you every herb bearing seed, which is upon the face of all the earth, and every tree, in the which is the fruit of a tree yielding seed; to you it shall be for meat.
# 30 And to every beast of the earth, and to every fowl of the air, and to every thing that creepeth upon the earth, wherein there is life, I have given every green herb for meat: and it was so.
# 31 And God saw every thing that he had made, and, behold, it was very good. And the evening and the morning were the sixth day.
# >>> factors(2701)
# [37, 73]
# >>> factors(2960)
# [2, 2, 2, 2, 5, 37]
# >>> factors(360)
# [2, 2, 2, 3, 3, 5]
# >>> factors(365)
# [5, 73]
# >>> 6*74
# 444
# >>> ps=primes(20000)
# >>> ps.index(2)
# 0
# >>> ps[1]
# 3
# >>> ps[2]
# 5
# >>> sum(ps[:11+1])
# 197
# >>> sum(ps[:1+307])
# 287137
# >>> 3*59
# 177
# >>> factors(326)
# [2, 163]
# >>> 3*26
# 78
# >>> factors(219)
# [3, 73]
# >>> factors(502)
# [2, 251]
# >>> factors(502411)
# [7, 13, 5521]
# >>> sum(ps[:1+359])
# 403611
# >>> 74*77*7*7
# 279202
# >>> 74+77+49
# 200
# >>> base(12, 1123)
# [7, 9, 7]
# >>> base(12, 1189)
# [8, 3, 1]
# >>> 1189-1123
# 66
# >>> base(12, 797)
# [5, 6, 5]
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 11*77
# 847
# >>> 
# >>> 
# >>> list(map(factors,[23,56,137,163,219,252,307,326,359,411]))
# [[23], [2, 2, 2, 7], [137], [163], [3, 73], [2, 2, 3, 3, 7], [307], [2, 163], [359], [3, 137]]
# >>> list(map(sums,[g1.v(i) for i in range(1,32)]))
# [(44, 411, 2094), (110, 1238, 8546), (41, 408, 2262), (66, 706, 4351), (91, 908, 5660), (87, 967, 6376), (116, 1266, 9240), (72, 713, 4430), (98, 1047, 7095), (95, 968, 6359), (136, 1523, 9479), (136, 1493, 9854), (41, 443, 3197), (128, 1371, 8463), (79, 897, 5478), (100, 1130, 7043), (61, 684, 4077), (90, 1025, 7379), (42, 472, 3550), (127, 1404, 10548), (158, 1786, 14665), (97, 1124, 8432), (41, 433, 3115), (122, 1274, 6908), (134, 1412, 8873), (194, 2149, 13552), (81, 734, 3119), (188, 2128, 14557), (152, 1642, 12559), (145, 1676, 13394), (95, 1031, 8789)]
# >>> b.G.wc()
# <121>:1: AttributeError: No attribute G
# /home/pi/python/bible/search.py:103: AttributeError: No attribute G
#   __getattr__(
#     self=Genesis 1
#     1 In the beginning God created the heaven and the eart...
#     name=G
#   )
#     bs=[0, 47]
# >>> factors(41348)
# [2, 2, 10337]
# >>> 
# >>> 
# >>> 
# >>> [(i,sum(ps[:1+i])) for i in [10601, 11311,11411,12421,12721,12821,13331,13831,13931,14341,14741,15451,15551]]
# [(10601, 561343769), (11311, 643681871), (11411, 655753547), (12421, 784185319), (12721, 824653279), (12821, 838369849), (13331, 910173393), (13831, 983618985), (13931, 998658581), (14341, 1061540933), (14741, 1124852453), (15451, 1242037649), (15551, 1259043463)]
# >>> factors(39)
# [3, 13]
# >>> 
# >>> 
# >>> 
# >>> 
# >>> exp(1)
# 2.718281828459045
# >>> exp(7.97)
# 2892.857364220396
# >>> exp(79.7)
# 4.104594016275709e+34
# >>> exp(7.337)
# 1536.0969036017116
# >>> 1536*2
# 3072
# >>> exp(2.301)
# 9.984161626023544
# >>> log(10)
# 2.302585092994046
# >>> 9*98.41616
# 885.74544
# >>> (5055+1)//2
# 2528
# >>> b.v(2528)
# 'And Moses called unto them; and Aaron and all the rulers of the congregation returned unto him: and Moses talked with them.'
# >>> p(b.Jos[23:11])
# Joshua 23:11 Take good heed therefore unto yourselves, that ye love the LORD your God.
# >>> (b.Gen-b.Jos[23:])
# Genesis 1:1-Joshua 23:16 (6477 verses)
# >>> len(_.chapters())
# 210
# >>> base(12, 2701)
# [1, 6, 9, 1]
# >>> 7*144+9*12+7
# 1123
# >>> Fn(23)
# 28657
# >>> Fn(23)
# 28657
# >>> factors(_)
# [28657]
# >>> 
# >>> sums('actg')
# (4, 31, 211)
# >>> b.v(211)
# "And surely your blood of your lives will I require; at the hand of every beast will I require it, and at the hand of man; at the hand of every man's brother will I require the life of man."
# >>> b/"life"
# Genesis 1:20,30;2:7,9;3:14,17,22,24;6:17;7:11,15,22;9:4-5;18:10,14;19:17,19;23:1;25:7,17;27:46;32:30;42:15-16;44:30;45:5;47:9;48:15;Exodus 4:19;6:16,18,20;21:23,30;Leviticus 17:11,14;18:18;Numbers 35:31;Deuteronomy 4:9;6:2;12:23;16:3;17:19;19:21;20:19;24:6;28:66;30:15,19-20;32:47;Joshua 1:5;2:14;4:14;Judges 9:17;12:3;16:30;18:25;Ruth 4:15;1 Samuel 1:11;7:15;18:18;19:5,11;20:1;22:23;23:15;25:29;26:24;28:9,21;2 Samuel 1:9;4:8;14:7;15:21;16:11;18:13,18;19:5;1 Kings 1:12;2:23;3:11;4:21;11:34;15:5-6;19:2-4,10,14;20:31,39,42;2 Kings 1:13-14;4:16-17;7:7;8:1,5;10:24;25:29-30;2 Chronicles 1:11;Ezra 6:10;Nehemiah 6:11;Esther 7:3,7;8:11;Job 2:4,6;3:20;6:11;7:7,15;9:21;10:1,12;13:14;24:22;31:39;33:4,18,20,22,28;36:6,14;Psalms 7:5;16:11;17:14;21:4;23:6;26:9;27:1,4;30:5;31:10,13;34:12;36:9;38:12;42:8;61:6;63:3;64:1;66:9;78:50;88:3;91:16;103:4;128:5;133:3;143:3;Proverbs 1:19;2:19;3:2,18,22;4:10,13,22-23;5:6;6:23,26;7:23;8:35;9:11;10:11,16-17;11:19,30;12:10,28;13:3,8,12,14;14:27,30;15:4,24,31;16:15,22;18:21;19:23;21:21;22:4;31:12;Ecclesiastes 2:3,17;3:12;5:18,20;6:12;7:12,15;8:15;9:9;Isaiah 15:4;38:12,16,20;43:4;57:10;Jeremiah 4:30;8:3;11:21;21:7-9;22:25;34:20-21;38:2,16;39:18;44:30;45:5;49:37;52:33-34;Lamentations 2:19;3:53,58;Ezekiel 3:18;7:13;13:22;32:10;33:15;Daniel 12:2;Jonah 1:14;2:6;4:3;Malachi 2:5;Matthew 2:20;6:25;7:14;10:39;16:25;18:8-9;19:16-17,29;20:28;25:46;Mark 3:4;8:35;9:43,45;10:17,30,45;Luke 1:75;6:9;8:14;9:24;10:25;12:15,22-23;14:26;16:25;17:33;18:18,30;21:34;John 1:4;3:15-16,36;4:14,36;5:24,26,29,39-40;6:27,33,35,40,47-48,51,53-54,63,68;8:12;10:10-11,15,17,28;11:25;12:25,50;13:37-38;14:6;15:13;17:2-3;20:31;Acts 2:28;3:15;5:20;8:33;11:18;13:46,48;17:25;20:10,24;26:4;27:22;Romans 2:7;5:10,17-18,21;6:4,22-23;7:10;8:2,6,10,38;11:3,15;16:4;1 Corinthians 3:22;6:3-4;14:7;15:19;2 Corinthians 1:8;2:16;3:6;4:10-12;5:4;Galatians 2:20;3:21;6:8;Ephesians 4:18;Philippians 1:20;2:16,30;4:3;Colossians 3:3-4;1 Timothy 1:16;2:2;4:8;6:12,19;2 Timothy 1:1,10;2:4;3:10;Titus 1:2;3:7;Hebrews 2:15;7:3,16;11:35;James 1:12;4:14;1 Peter 3:7,10;4:3;2 Peter 1:3;1 John 1:1-2;2:16,25;3:14-16;5:11-13,16,20;Jude 1:21;Revelation 2:7,10;3:5;8:9;11:11;13:8,15;17:8;20:12,15;21:6,27-22:2,14,17,19 (412 verses)
# >>> sums("a son")
# (4, 49, 211)
# >>> sums("lord")
# (4, 49, 184)
# >>> 211-184
# 27
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
