# >>> from search import *
# >>> from mean import *
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# ModuleNotFoundError: No module named 'mean'
# >>> from primes import *
# >>> b/"heart"/"mouth"
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> b/"heart"/"word"
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> p(_)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name '_' is not defined
# >>> 
# >>> b.Gen[4:2].vn()
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> factors(82)
# [2, 41]
# >>> sums('sheep')
# (53, 188)
# >>> sums('lamb')
# (28, 73)
# >>> sums('The Lamb of God')
# (108, 423)
# >>> factors(201)
# [3, 67]
# >>> sof(39)
# 56
# >>> sof(27)
# 40
# >>> sof(66)
# 144
# >>> sheba=(b/"sheep"/"lamb").vns(); sheba
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> tale(sheba)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'sheba' is not defined
# >>> factors(78327)
# [3, 3, 3, 3, 967]
# >>> whichprime(967)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'whichprime' is not defined
# >>> factors(162)
# [2, 3, 3, 3, 3]
# >>> 3*967
# 2901
# >>> 27*2901
# 78327
# >>> list(map(factors,sheba))
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'sheba' is not defined
# >>> whichprime(18719)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'whichprime' is not defined
# >>> factors(2136)
# [2, 2, 2, 3, 89]
# >>> b.Heb[9:13]
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> p(_);p(_.vn())
# [2, 2, 2, 3, 89]
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: 'list' object has no attribute 'vn'
# >>> b.Heb[10:4]
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> p(_);p(_.vn())
# [2, 2, 2, 3, 89]
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: 'list' object has no attribute 'vn'
# >>> 31102-30119
# 983
# >>> 31102-30138
# 964
# >>> b.vi(31102)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> p(b.vi(311))
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> p(b.vi(411))
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> b.vi(622)-b.vi(624)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> p(_)
# 964
# >>> sums("sheba")
# (35, 116)
# >>> sums("beer")
# (30, 102)
# >>> sums("water")
# (67, 796)
# >>> sums("blood")
# (48, 156)
# >>> sums("ghost")
# (69, 375)
# >>> sums("spirit")
# (91, 478)
# >>> sums("holy")
# (60, 798)
# >>> sums("the water and the blood")
# (200, 1433)
# >>> sums("Lord Jesus Christ")
# (200, 1109)
# >>> sof(200)
# 465
# >>> b.chapters().index(b.Ps[1:])+1
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> 930/2
# 465.0
# >>> b.chapters()[465-1]
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> p(b['1 John'][5:7]-8)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> sums('the Father the Word and the Holy Ghost')
# (365, 2831)
# >>> factors(2831)
# [19, 149]
# >>> whichprime(149)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'whichprime' is not defined
# >>> sums('Father')
# (58, 310)
# >>> sums('the Father')
# (91, 523)
# >>> sums('heavenly Father')
# (150, 1509)
# >>> factors(1509)
# [3, 503]
# >>> sof(150)
# 372
# >>> factors(372)
# [2, 2, 3, 31]
# >>> 12*31
# 372
# >>> 3*72
# 216
# >>> factors(_)
# [2, 2, 2, 3, 3, 3]
# >>> sof(360)
# 1170
# >>> b.chapter(1170)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> sof(365)
# 444
# >>> onm=(b/"opened"/"mouth"/"not")
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> 
# >>> onm.vns()
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'onm' is not defined
# >>> onm.chn()
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'onm' is not defined
# >>> 
# >>> sums("DNA")
# (19, 55)
# >>> sums("heaven")
# (55, 469)
# >>> sof(469)
# 544
# >>> sof(496)/2
# 496.0
# >>> 496-469
# 27
# >>> pn(23)
# 83
# >>> pn(9)
# 23
# >>> whichprime(1123)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'whichprime' is not defined
# >>> sums('rib')
# (29, 101)
# >>> sums('Deoxyribonucleic acid')
# (201, 1947)
# >>> sums('Deoxyribonucleic')
# (184, 1930)
# >>> sums('deoxy')
# (73, 1369)
# >>> sums('onucleic')
# (82, 460)
# >>> sums('acid')
# (17, 17)
# >>> 184*17
# 3128
# >>> factors(184)
# [2, 2, 2, 23]
# >>> factors(201)
# [3, 67]
# >>> sof(24)
# 60
# >>> sums('aleph')
# (42, 114)
# >>> sums('tau')
# (42, 501)
# >>> [sums(w) for w in 'aleph beth gimel daleth he vau zain cheth teth jod caph lamed mem nun samech ain pe tzaddi koph resh schin tau'.split()]
# [(42, 114), (35, 215), (46, 91), (50, 248), (13, 13), (44, 701), (50, 860), (44, 224), (53, 413), (29, 74), (28, 82), (35, 80), (31, 85), (49, 400), (49, 157), (24, 60), (21, 75), (64, 1018), (50, 158), (50, 203), (53, 170), (42, 501)]
# >>> sums('alpha'),sums('omega')
# ((38, 110), (41, 113))
# >>> 38+41
# 79
# >>> sums('first'),sums('last')
# ((72, 405), (52, 331))
# >>> 72+52
# 124
# >>> 
# >>> sums('first'),sums('last')
# ((72, 405), (52, 331))
# >>> 72+52
# 124
# >>> tell(b.Ecc[7:27].vs())
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> b/"seek"/"find"/"ask"
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> tell(_.v(1))
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: 'int' object has no attribute 'v'
# >>> tri(22)
# 253
# >>> pf(803)
# Counter({11: 1, 73: 1})
# >>> tell('open')
#  o  p e  n
# 15+16+5+14 = 50
# >>> tell('Solomon')
#  S  o  l  o  m  o  n
# 19+15+12+15+13+15+14 = 103
# >>> tell('king')
#  k i  n g
# 11+9+14+7 = 41
# >>> tell('genes is')
# genes is
#    50+28 = 78
# >>> tell('exod us')
# exod us
#   48+40 = 88
# >>> tell('l ev it ic us')
#  l ev it ic us
# 12+27+29+12+40 = 120
# >>> tell('n umb ers')
#  n umb ers
# 14+ 36+ 42 = 92
# >>> pf(92)
# >>> tell('Deuteronomy')
# Counter({2: 2, 23: 1})
# >>> tell('numbered number tale tell account')
# numbered number tale tell account
#       82+    73+  38+  49+     77 = 319
# >>> tell('counting')
# c  o  u  n  t i  n g
# 3+15+21+14+20+9+14+7 = 103
# >>> b/'mene'
# Daniel 5:25 And this is the writing that was written, MENE, MENE, TEKEL, UPHARSIN.
# Daniel 5:26 This is the interpretation of the thing: MENE; God hath numbered thy kingdom, and finished it.
# >>> p(_)
# Daniel 5:25 And this is the writing that was written, MENE, MENE, TEKEL, UPHARSIN.
# Daniel 5:26 This is the interpretation of the thing: MENE; God hath numbered thy kingdom, and finished it.
# >>> 
# >>> tale(b.Genesis[1:].wcs())
# [10, 39, 50, 67, 89, 112, 138, 154, 179, 203, 237, 270, 280, 314, 336, 362, 378, 403, 413, 442, 476, 499, 509, 539, 573, 623, 645, 691, 733, 772, 797]
# >>> b.Genesis[1:].wcs()
# [10, 29, 11, 17, 22, 23, 26, 16, 25, 24, 34, 33, 10, 34, 22, 26, 16, 25, 10, 29, 34, 23, 10, 30, 34, 50, 22, 46, 42, 39, 25]
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
