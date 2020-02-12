# >>> from math import *
# >>> from primes import *
# >>> from search import *
# >>> from mean import *
# >>> pi
# 3.141592653589793
# >>> g1=b.Gen[1:]
# >>> g1.wc()
# 797
# >>> g1/"God"
# 26 verses, Genesis 1:1...31
# >>> 9900*pi
# 31101.767270538952
# >>> 66+150
# 216
# >>> 3**6
# 729
# >>> b.Gen[1:1]
# 1 verses, Genesis 1:1
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
# 31
# >>> gv=[x.count() for x in b.Gen.chapters()]
# >>> [x*(x+1)//2 for x in gv]
# [496, 325, 300, 351, 528, 253, 300, 253, 435, 528, 528, 210, 171, 300, 231, 136, 378, 561, 741, 171, 595, 300, 210, 2278, 595, 630, 1081, 253, 630, 946, 1540, 528, 210, 496, 435, 946, 666, 465, 276, 276, 1653, 741, 595, 595, 406, 595, 496, 253, 561, 351]
# >>> _[24:26]
# [595, 630]
# >>> 1190//2
# 595
# >>> 
# >>> 
# >>> sum(_)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# TypeError: 'int' object is not iterable
# >>> _//2
# 297
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
# 50 verses, Psalms 18:1-50
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
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'g1131' is not defined
# >>> g1131.wc()
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'g1131' is not defined
# >>> 
# >>> p(b.Gen[1:16])
# Genesis 1:16 And God made two great lights; the greater light to rule the day, and the lesser light to rule the night: he made the stars also.
# >>> b.Gen[1:16].wc()
# 26
# >>> 
# >>> g1/"and"
# 31 verses, Genesis 1:1-31
# >>> g1/"god"
# 26 verses, Genesis 1:1...31
# >>> g1/"create"
# 3 verses, Genesis 1:1...27
# >>> g1/"created"
# 3 verses, Genesis 1:1...27
# >>> g1/"made"
# 4 verses, Genesis 1:7...31
# >>> g1/"kind"
# 5 verses, Genesis 1:11...25
# >>> g1/"heaven"
# 7 verses, Genesis 1:1...20
# >>> g1/"earth"
# 15 verses, Genesis 1:1...30
# >>> p(g1)
# Genesis 1:1 In the beginning God created the heaven and the earth.
# Genesis 1:2 And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.
# Genesis 1:3 And God said, Let there be light: and there was light.
# Genesis 1:4 And God saw the light, that it was good: and God divided the light from the darkness.
# Genesis 1:5 And God called the light Day, and the darkness he called Night.  And the evening and the morning were the first day.
# Genesis 1:6 And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters.
# Genesis 1:7 And God made the firmament, and divided the waters which were under the firmament from the waters which were above the firmament: and it was so.
# Genesis 1:8 And God called the firmament Heaven. And the evening and the morning were the second day.
# Genesis 1:9 And God said, Let the waters under the heaven be gathered together unto one place, and let the dry land appear: and it was so.
# Genesis 1:10 And God called the dry land Earth; and the gathering together of the waters called he Seas: and God saw that it was good.
# Genesis 1:11 And God said, Let the earth bring forth grass, the herb yielding seed, and the fruit tree yielding fruit after his kind, whose seed is in itself, upon the earth: and it was so.
# Genesis 1:12 And the earth brought forth grass, and herb yielding seed after his kind, and the tree yielding fruit, whose seed was in itself, after his kind: and God saw that it was good.
# Genesis 1:13 And the evening and the morning were the third day.
# Genesis 1:14 And God said, Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days, and years:
# Genesis 1:15 And let them be for lights in the firmament of the heaven to give light upon the earth: and it was so.
# Genesis 1:16 And God made two great lights; the greater light to rule the day, and the lesser light to rule the night: he made the stars also.
# Genesis 1:17 And God set them in the firmament of the heaven to give light upon the earth,
# Genesis 1:18 And to rule over the day and over the night, and to divide the light from the darkness: and God saw that it was good.
# Genesis 1:19 And the evening and the morning were the fourth day.
# Genesis 1:20 And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl that may fly above the earth in the open firmament of heaven.
# Genesis 1:21 And God created great whales, and every living creature that moveth, which the waters brought forth abundantly, after their kind, and every winged fowl after his kind: and God saw that it was good.
# Genesis 1:22 And God blessed them, saying, Be fruitful, and multiply, and fill the waters in the seas, and let fowl multiply in the earth.
# Genesis 1:23 And the evening and the morning were the fifth day.
# Genesis 1:24 And God said, Let the earth bring forth the living creature after his kind, cattle, and creeping thing, and beast of the earth after his kind: and it was so.
# Genesis 1:25 And God made the beast of the earth after his kind, and cattle after their kind, and every thing that creepeth upon the earth after his kind: and God saw that it was good.
# Genesis 1:26 And God said, Let us make man in our image, after our likeness: and let them have dominion over the fish of the sea, and over the fowl of the air, and over the cattle, and over all the earth, and over every creeping thing that creepeth upon the earth.
# Genesis 1:27 So God created man in his own image, in the image of God created he him; male and female created he them.
# Genesis 1:28 And God blessed them, and God said unto them, Be fruitful, and multiply, and replenish the earth, and subdue it: and have dominion over the fish of the sea, and over the fowl of the air, and over every living thing that moveth upon the earth.
# Genesis 1:29 And God said, Behold, I have given you every herb bearing seed, which is upon the face of all the earth, and every tree, in the which is the fruit of a tree yielding seed; to you it shall be for meat.
# Genesis 1:30 And to every beast of the earth, and to every fowl of the air, and to every thing that creepeth upon the earth, wherein there is life, I have given every green herb for meat: and it was so.
# Genesis 1:31 And God saw every thing that he had made, and, behold, it was very good. And the evening and the morning were the sixth day.
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
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'primes' is not defined
# >>> ps.index(2)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'ps' is not defined
# >>> ps[1]
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'ps' is not defined
# >>> ps[2]
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'ps' is not defined
# >>> sum(ps[:11+1])
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'ps' is not defined
# >>> sum(ps[:1+307])
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'ps' is not defined
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
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'ps' is not defined
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
# [(411, 2094), (1238, 8546), (408, 2262), (706, 4351), (908, 5660), (967, 6376), (1266, 9240), (713, 4430), (1047, 7095), (968, 6359), (1523, 9479), (1493, 9854), (443, 3197), (1371, 8463), (897, 5478), (1130, 7043), (684, 4077), (1025, 7379), (472, 3550), (1404, 10548), (1786, 14665), (1124, 8432), (433, 3115), (1274, 6908), (1412, 8873), (2149, 13552), (734, 3119), (2128, 14557), (1642, 12559), (1676, 13394), (1031, 8789)]
# >>> b.G.wc()
# 41348
# >>> factors(41348)
# [2, 2, 10337]
# >>> 
# >>> 
# >>> 
# >>> [(i,sum(ps[:1+i])) for i in [10601, 11311,11411,12421,12721,12821,13331,13831,13931,14341,14741,15451,15551]]
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "<console>", line 1, in <listcomp>
# NameError: name 'ps' is not defined
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
# '34:31 And Moses called unto them; and Aaron and all the rulers of the congregation returned unto him: and Moses talked with them.'
# >>> p(b.Jos[23:11])
# Joshua 23:11 Take good heed therefore unto yourselves, that ye love the LORD your God.
# >>> (b.Gen-b.Jos[23:])
# 6477 verses, Genesis 1:1-Joshua 23:16
# >>> len(_.chapters())
# 210
# >>> base(12, 2701)
# [1, 6, 9, 1]
# >>> 7*144+9*12+7
# 1123
# >>> fi(23)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'fi' is not defined
# >>> fib(23)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'fib' is not defined
# >>> factors(_)
# [1123]
# >>> 
# >>> sums('actg')
# (31, 211)
# >>> b.v(211)
# "9:5 And surely your blood of your lives will I require; at the hand of every beast will I require it, and at the hand of man; at the hand of every man's brother will I require the life of man."
# >>> b/"life"
# 412 verses, Genesis 1:20...Revelation 22:19
# >>> sums("a son")
# (49, 211)
# >>> sums("lord")
# (49, 184)
# >>> 211-184
# 27
# >>>
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
