from parle import *
from table import *
import re
import itertools
import functools
import unicodedata
c=299792458

ab='abcdefghijklmnopqrstuvwxyz'
αβ='αβγδεϝζηθικλμνξοπϙρστυφχψωϡ'
אב='אבגדהוזחטיכלמנסעפצקרשת'
nn='0123456789'
pos={c:i for i,c in enumerate(ab,start=1)}
pos.update({c:i for i,c in enumerate(αβ,start=1)})
pos.update({c:i for i,c in enumerate(אב,start=1)})
pos.update({c:i for i,c in enumerate(nn)})

characters={a:a for a in ab+αβ+אב+nn}
vowels=set('aeiou' + 'αεηιουω')

def begin():
    eqss=['αάἀἁἂἃἄἅἆἇὰάᾀᾁᾂᾃᾄᾅᾆᾇᾰᾱᾲᾳᾴᾶᾷ','εέἐἑἒἓἔἕὲέ','ηήἠἡἢἣἤἥἦἧὴήᾐᾑᾒᾓᾔᾕᾖᾗῂῃῄῆῇ',
    'οόὀὁὂὃὄὅὸό','ιίϊΐἰἱἲἳἴἵἶἷὶίῐῑῒΐῖῗ','υύϋΰὐὑὒὓὔὕὖὗὺύῠῡῢΰῦῧ',
    'ωώὠὡὢὣὤὥὦὧὼώᾠᾡᾢᾣᾤᾥᾦᾧῲῳῴῶῷ','ρῤῥ']
    eqss+=['כך','מם','נן','צץ','σς']
    for eqs in eqss:
        primary=eqs[0]
        for c in eqs[1:]:
            characters[c]=characters[primary]

    for c in 'ᾀᾁᾂᾃᾄᾅᾆᾇᾲᾳᾴᾷᾐᾑᾒᾓᾔᾕᾖᾗῂῃῄῇᾠᾡᾢᾣᾤᾥᾦᾧῲῳῴῷ':
        characters[c]+='ι'
begin()
characters.update({c.upper():v for c,v in characters.items()})

def isletter(c):
    if c.isalpha():
        if c not in characters:
            print(c)
            stop
    return c in characters

@functools.lru_cache(22222)
def letters(s):
    return ''.join([characters[c] for c in s.lower() if isletter(c)])

def ovals(s):
    return [pos[c] for c in letters(s)]

def count(s): return sum(ovals(s))

osum=count

pdigits=[0]+list(range(1,10))+list(range(10,100,10))+list(range(100,1000,100))
def ssum(s): return sum([pdigits[k] for k in ovals(s)])
def lsum(s): return sum((isletter(c) for c in letters(s)))
def ascsum(s): return sum((ord(l) for l in s if isletter(l)))
def sums(s): return lsum(s),osum(s),psum(s)
psum=ssum

def showalphas(ab=ab,f=osum):
    letters, vals = table(ab,[f(l) for l in ab])
    print(' '.join(letters))
    print(' '.join(vals))

def join(sep,l):
    r=[sep]*(len(l)*2-1)
    r[::2]=l
    return r

def tell(*ss):
    print(texttable(telltable(*ss)))

def tellmd(*ss):
    print(mdtable(telltable(*ss)))

def telltable(*ss):
    if not ss: return
    fs = [f for f in ss if callable(f)]
    ss = [s for s in ss if s is not None and not callable(s)]
    if not fs: fs = [count]
    for s in ss:
        if isinstance(s,str):
            words=s.split()
            if len(words)==1:
                word=words[0]
                words=splitat(positions([c in characters for c in word]),word)
        else:
            words=list(s)
        vv=[words+['=']]
        for f in fs:
            vals=[f(w) for w in words]
            vv.append(vals+[sum(vals)])
        return Table(vv)

def texttable(vv,sep=' '):
    return '\n'.join([sep.join(v).rstrip() for v in justify(vv)])

def mdtable(vv):
    vv=fill(vv@str,'')
    def j(s,l): return s+s.join(l)
    return '\n'.join([j('|',vv[0]),j('|','-'*len(vv[0]))]+[j('|',v) for v in vv[1:]])

# >>> from mene import *
# >>> from auto import *
# >>> 
# >>> p=print
# >>> telltable('God')
# Table(['G', 'o', 'd', '=', 7, 15, 4, 26],[Index([4,4])])
# >>> _[:]
# Table(['G', 'o', 'd', '=', 7, 15, 4, 26],[Index([4,4])])
# >>> print(_.values())
# [['G', 'o', 'd', '='], [7, 15, 4, 26]]
# >>> method.join('|',Table([1,2,3])@str)
# '1|2|3'
# >>> 
# >>> mdtable(telltable('AZ',ssum))
# '|A|Z|=\n|-|-|-\n|1|800|801'
# >>> tellmd('AV')
# |A|V|=
# |-|-|-
# |1|22|23
# >>> 
# >>> 
# >>> fill(_)
# Table(['|', 'A', '|', 'Z', '|', '=', '\n', '|', '-', '|', '-', '|', '-', '\n', '|', '1', '|', '8', '0', '0', '|', '8', '0', '1'],[])
# >>> texttable(_)
# '|\nA\n|\nZ\n|\n=\n\n|\n-\n|\n-\n|\n-\n\n|\n1\n|\n8\n0\n0\n|\n8\n0\n1'
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> fill([[1,2],[3]])
# Table([1, 2, 3, ''],[Index([2,2])])
# >>> 
# >>> 
# >>> 
# >>> 
# >>> mdtable(_)
# '|1|2\n|-|-\n|3|'
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> tale([1,2,3])
# [1, 3, 6]
# >>> functools.reduce(operator.add,[1,2,3])
# 6
# >>> 
# >>> 
# >>> 
# >>> 111*56
# 6216
# >>> 37*3*7*8
# 6216
# >>> 1216/64
# 19.0
# >>> 155*51
# 7905
# >>> 15*5*51
# 3825
# >>> 5055*55
# 278025
# >>> b.chapter(789)
# <console>:1: NameError: name 'b' is not defined
# >>> 
# >>> osum('God')
# 26
# >>> psum('God')
# 71
# >>> osum('Jesus')
# 74
# >>> osum('Christ')
# 77
# >>> osum('Jesus Christ')
# 151
# >>> osum('Lord Jesus Christ')
# 200
# >>> osum('is')
# 28
# >>> osum('JEHOVAH')
# 69
# >>> osum('JEHOVAH')
# 69
# >>> osum('את')
# 23
# >>> ssum('את')
# 401
# >>> ascsum('Lord')
# 401
# >>> ascsum('in')
# 215
# >>> ascsum('In')
# 183
# >>> sums('Lord')
# (4, 49, 184)
# >>> 
# >>> np(401)
# <console>:1: NameError: name 'np' is not defined
# >>> osum('יהוה')
# 26
# >>> psum('יהוה')
# 26
# >>> psum('יהוה')
# 26
# >>> osum('LORD OF LORDS')
# 138
# >>> psum('LORD OF LORDS')
# 534
# >>> psum('LORD OF LORDS')
# 534
# >>> sums('THE LORD')
# (82, 397)
# >>> sums('KING OF KINGS')
# (122, 338)
# >>> sums('Immanuel')
# (88, 475)
# >>> sums('Prince of Peace')
# (116, 377)
# >>> sums('eth')
# (33, 213)
# >>> sums('et')
# (25, 205)
# >>> from bible import *
# >>> John[1:1].tell(lsum,osum,ssum)
# In the beginning was the Word, and the Word was with God, and the Word was God.  =
# 2   3      9      3   3    4    3   3   4    3   4    3    3   3   4    3   3    60
# 23  33     81     43  33   60   19  33  60   43  60   26   19  33  60   43  26  695
# 59 213    189    601 213  654   55 213 654  601 717   71   55 213 654  601  71  5834
# >>> 
# >>> 
# >>> j11='ἐν ἀρχῇ ἦν ὁ λόγος καὶ ὁ λόγος ἦν πρὸς τὸν θεόν καὶ θεὸς ἦν ὁ λόγος'
# >>> tell(j11,lsum,osum,ssum)
# ἐν ἀρχῇ ἦν ὁ  λόγος καὶ ὁ  λόγος ἦν πρὸς τὸν θεόν καὶ θεὸς ἦν ὁ  λόγος  =
# 2   5   2  1    5    3  1    5   2   4    3   4    3   4   2  1    5    52
# 19  62  22 16   67   22 16   67  22  72   51  44   22  50  22 16   67  657
# 55 719  58 70  373   31 70  373  58 450  420 134   31 284  58 70  373  3627
# >>> 
# >>> from parle.primes import *
# >>> Row([373,31,719])@np
# Row([74, 11, 128])
# >>> print(factors(3627))
# [3, 3, 13, 31]
# >>> 39*93
# 3627
# >>> print(sof(3627))
# 5824
# >>> 888*1478
# 1312464
# >>> 888+1478
# 2366
# >>> table(['Tom',2],[3,45])
# [('Tom', '2 '), (' 3 ', '45')]
# >>> print(texttable(_))
# Tom 2
#  3  45
# >>> tell("Lord Jesus",lsum,osum,ssum)
# Lord Jesus
#  4  +  5  = 9
#  49 +  74 =123
# 184 + 515 =699
# >>> tell("Jesus Christ",lsum,osum,ssum)
# Jesus Christ
#   5  +  6   = 11
#   74 +  77  =151
#  515 + 410  =925
# >>> tell("Lord Jesus Christ",lsum,osum,ssum)
# Lord Jesus Christ
#  4  +  5  +  6   = 15
#  49 +  74 +  77  =200
# 184 + 515 + 410  =1109
# >>> 
# >>> tell('Κυριος Ιησους Χρηστος',lsum,osum,ssum)
# Κυριος Ιησους Χρηστος
#   6   +  6   +   7   = 19
#   98  +  96  +  128  =322
#  800  + 888  +  1478 =3166
# >>> tell("LORD JEHOVAH",lsum,osum,ssum)
# LORD JEHOVAH
#  4  +   7   = 11
#  49 +   69  =118
# 184 +  492  =676
# >>> 
# >>> 
# >>> 
# >>> 
# >>> from bible import *
# >>> b.Genesis[1:1].tell()
# In the beginning God created the heaven and the earth.
# 23+ 33+    81   + 26+   56  + 33+  55  + 19+ 33+  52  =411
# >>> factors(1478)
# [2, 739]
# >>> 
# >>> sums("οὗτος")
# (95, 1040)
# >>> lsum(Genesis[1:1].vs())
# 44
# >>> nt=b.Matthew-b.Revelation
# >>> 
# >>> nt
# Matthew 1:1-Revelation 22:21 (7957 verses)
# >>> factors(7957)
# [73, 109]
# >>> sums(b.v(1))
# (411, 2094)
# >>> factors(2094)
# [2, 3, 349]
# >>> sums(b.Gen[1:].vs())
# (34463, 233444)
# >>> 
# >>> b.Gen.wc()
# 38264
# >>> 
# >>> 
# >>> factors(233444)
# [2, 2, 17, 3433]
# >>> sums("lord jesus christ")
# (200, 1109)
# >>> sums("the")
# (33, 213)
# >>> pf(213)
# Counter({3: 1, 71: 1})
# >>> psum('Solomon')
# 400
# >>> b.chapter(666)
# Ecclesiastes 7:1-29 (29 verses)
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 4*3433
# 13732
# >>> allfactors(34463)
# [1, 11, 13, 143, 241, 2651, 3133, 34463]
# >>> 11*3133
# 34463
# >>> [b.Gen[i:].wc() for i in range(1,51)]
# [797, 632, 695, 632, 505, 579, 584, 586, 658, 496, 606, 536, 457, 606, 471, 412, 679, 867, 1108, 498, 775, 629, 539, 1816, 706, 889, 1262, 621, 829, 1022, 1417, 794, 508, 790, 664, 845, 942, 819, 666, 580, 1404, 977, 938, 874, 731, 766, 965, 639, 766, 687]
# >>> sum(_)
# 38264
# >>> b.Gen.wc()
# 38264
# >>> base(12,1123)
# [7, 9, 7]
# >>> rebase(12, _)
# 1123
# >>> rebase(12, 797)
# 1123
# >>> math.sqrt(797)
# 28.231188426986208
# >>> 
# >>> math.sqrt(31102)
# 176.35759127409287
# >>> 
# >>> sums("ἰουδαίας")
# (84, 696)
# >>> sums("ἡρῴδης")
# (95, 1130)
# >>> sums("herod")
# (50, 167)
# >>> sums("king")
# (41, 86)
# >>> sums("herodias")
# (79, 277)
# >>> sums("ἡρῴδου")
# (105, 1392)
# >>> sums("Judah")
# (44, 323)
# >>> sums("of")
# (21, 66)
# >>> tell('The Holy Bible',lsum,osum,ssum)
# The Holy Bible
#  3 + 4  +  5  = 12
#  33+ 60 +  30 =123
# 213+798 +  48 =1059
# >>> 
# >>> sums("judaea")
# (42, 321)
# >>> sums("ἡρώδης")
# (85, 1120)
# >>> list(map(sums,["Lord","Jesus","Christ"]))
# [(49, 184), (74, 515), (77, 410)]
# >>> 49+74+77
# 200
# >>> 184+515+410
# 1109
# >>> sums("ἰουδαίαν")
# (78, 546)
# >>> b.Ecc[7:27]
# Ecclesiastes 7:27 Behold, this have I found, saith the preacher, counting one by one, to find out the account:
# >>> _.ix[0]+1
# 17457
# >>> factors(_)
# [3, 11, 23, 23]
# >>> 33*23*23
# 17457
# >>> allfactors(17457)
# [1, 3, 11, 23, 33, 69, 253, 529, 759, 1587, 5819, 17457]
# >>> 17*457
# 7769
# >>> 
# >>> sums("αγαπει")
# (37, 100)
# >>> sums("love")
# (54, 495)
# >>> b.Gen-b.Num
# Genesis 1:1-Numbers 36:13 (4893 verses)
# >>> 
# >>> b/"tale"/"told"
# Psalms 90:9 For all our days are passed away in thy wrath: we spend our years as a tale that is told.
# >>> _.tell(lsum,osum,ssum)
# For all our days are passed away in thy wrath:  we spend our years  as a tale that  is told.
#  3 + 3 + 3 + 4  + 3 +  6   + 4  +2 + 3 +  5   + 2 +  5  + 3 +  5  + 2 +1+ 4  + 4  + 2 +  4  = 68
#  39+ 25+ 54+ 49 + 24+  64  + 50 +23+ 53+  70  + 28+  58 + 54+  68 + 20+1+ 38 + 49 + 28+  51 =846
# 156+ 61+450+805 + 96+ 280  +1202+59+908+ 799  +505+ 229 +450+ 896 +101+1+236 +409 +109+ 294 =8046
# >>> 
# >>> b.Ps[90]
# Psalms 90:1-17 (17 verses)
# >>> _.tell()
# Lord, thou hast been our dwelling place in all generations.
#   49 + 64 + 48 + 26 + 54+   86   +  37 +23+ 25+    127     =539
# Before the mountains were brought forth, or ever thou hadst formed the earth and the world, even from everlasting to everlasting, thou art God.
#   51  + 33+   126   + 51 +   91  +  67  +33+ 50 + 64 +  52 +  61  + 33+  52 + 19+ 33+  72  + 46 + 52 +    132    +35+    132     + 64 + 39+ 26 =1414
# Thou turnest man to destruction; and sayest, Return, ye children of men.
#  64 +  117  + 28+35+    148     + 19+   89  +   96  +30+   73   +21+ 32 =752
# For a thousand years in thy sight are but as yesterday when it is past, and as a watch in the night.
#  39+1+  102   +  68 +23+ 53+  63 + 24+ 43+20+   122   + 50 +29+28+  56 + 19+20+1+  55 +23+ 33+  58  =930
# Thou carriest them away as with a flood; they are as a sleep: in the morning they are like grass which groweth up.
#  64 +   93   + 46 + 50 +20+ 60 +1+  52  + 58 + 24+20+1+  57  +23+ 33+   90  + 58 + 24+ 37 +  64 +  51 +   96  + 37=1059
# In the morning it flourisheth, and groweth up; in the evening it is cut down, and withereth.
# 23+ 33+   90  +29+    141     + 19+   96  + 37+23+ 33+   76  +29+28+ 44+  56 + 19+   116    =892
# For we are consumed by thine anger, and by thy wrath are we troubled.
#  39+28+ 24+   94   +27+  56 +  45  + 19+27+ 53+  70 + 24+28+    97   =631
# Thou hast set our iniquities before thee, our secret sins in the light of thy countenance.
#  64 + 48 + 44+ 54+   132    +  51  +  38 + 54+  70  + 61 +23+ 33+  56 +21+ 53+    115     =917
# For all our days are passed away in thy wrath: we spend our years as a tale that is told.
#  39+ 25+ 54+ 49 + 24+  64  + 50 +23+ 53+  70  +28+  58 + 54+  68 +20+1+ 38 + 49 +28+  51 =846
# The days of our years are threescore years and ten; and if by reason of strength they be fourscore years, yet is their strength labour and sorrow; for it is soon cut off, and we fly away.
#  33+ 49 +21+ 54+  68 + 24+   116    +  68 + 19+ 39 + 19+15+27+  72  +21+  111   + 58 +7 +   120   +  68  + 50+28+  60 +  111   +  69  + 19+  108  + 39+29+28+ 63 + 44+ 27 + 19+28+ 43+  50 =1824
# Who knoweth the power of thine anger? even according to thy fear, so is thy wrath.
#  46+   96  + 33+  77 +21+  56 +  45  + 46 +    74   +35+ 53+  30 +34+28+ 53+  70  =797
# So teach us to number our days, that we may apply our hearts unto wisdom.
# 34+  37 +40+35+  73  + 54+  49 + 49 +28+ 39+  70 + 54+  71  + 70 +   83  =786
# Return, O  LORD, how long? and let it repent thee concerning thy servants.
#    96  +15+  49 + 46+  48 + 19+ 37+29+  78  + 38 +   102    + 53+   118   =728
# O  satisfy us early with thy mercy; that we may rejoice and be glad all our days.
# 15+   99  +40+  61 + 60 + 53+  64  + 49 +28+ 39+   65  + 19+7 + 24 + 25+ 54+  49 =751
# Make us glad according to the days wherein thou hast afflicted us, and the years wherein we have seen evil.
#  30 +40+ 24 +    74   +35+ 33+ 49 +   82  + 64 + 48 +    66   + 40+ 19+ 33+  68 +   82  +28+ 36 + 43 +  48 =942
# Let thy work appear unto thy servants, and thy glory unto their children.
#  37+ 53+ 67 +  57  + 70 + 53+   118   + 19+ 53+  77 + 70 +  60 +    73   =807
# And let the beauty of the LORD our God be upon us: and establish thou the work of our hands upon us; yea, the work of our hands establish thou it.
#  19+ 37+ 33+  74  +21+ 33+ 49 + 54+ 26+7 + 66 + 40+ 19+    95   + 64 + 33+ 67 +21+ 54+  46 + 66 + 40+ 31 + 33+ 67 +21+ 54+  46 +    95   + 64 + 29=1404
# >>> _.count()
# 16019
# >>> 
# >>> 
# >>> 19/c
# 6.337717808764889e-08
# >>> showalphas(αβ,ssum)
# α β γ δ ε ϝ ζ η θ ι  κ  λ  μ  ν  ξ  ο  π  ϙ   ρ   σ   τ   υ   φ   χ   ψ   ω   ϡ 
# 1 2 3 4 5 6 7 8 9 10 20 30 40 50 60 70 80 90 100 200 300 400 500 600 700 800 900
# >>> showalphas(אב,ssum)
# א ב ג ד ה ו ז ח ט י  כ  ל  מ  נ  ס  ע  פ  צ   ק   ר   ש   ת 
# 1 2 3 4 5 6 7 8 9 10 20 30 40 50 60 70 80 90 100 200 300 400
# >>> tell('מָשִׁיחַ')
#  מָ שִׁ  י  חַ
# 13+21+10+8=52
# >>> [(s, i) for i,s in [(i, failas(unicodedata.name,'')(chr(i))) for i in range(32,10000)] if s.find('HEBREW')>=0]
# [('HEBREW ACCENT ETNAHTA', 1425), ('HEBREW ACCENT SEGOL', 1426), ('HEBREW ACCENT SHALSHELET', 1427), ('HEBREW ACCENT ZAQEF QATAN', 1428), ('HEBREW ACCENT ZAQEF GADOL', 1429), ('HEBREW ACCENT TIPEHA', 1430), ('HEBREW ACCENT REVIA', 1431), ('HEBREW ACCENT ZARQA', 1432), ('HEBREW ACCENT PASHTA', 1433), ('HEBREW ACCENT YETIV', 1434), ('HEBREW ACCENT TEVIR', 1435), ('HEBREW ACCENT GERESH', 1436), ('HEBREW ACCENT GERESH MUQDAM', 1437), ('HEBREW ACCENT GERSHAYIM', 1438), ('HEBREW ACCENT QARNEY PARA', 1439), ('HEBREW ACCENT TELISHA GEDOLA', 1440), ('HEBREW ACCENT PAZER', 1441), ('HEBREW ACCENT ATNAH HAFUKH', 1442), ('HEBREW ACCENT MUNAH', 1443), ('HEBREW ACCENT MAHAPAKH', 1444), ('HEBREW ACCENT MERKHA', 1445), ('HEBREW ACCENT MERKHA KEFULA', 1446), ('HEBREW ACCENT DARGA', 1447), ('HEBREW ACCENT QADMA', 1448), ('HEBREW ACCENT TELISHA QETANA', 1449), ('HEBREW ACCENT YERAH BEN YOMO', 1450), ('HEBREW ACCENT OLE', 1451), ('HEBREW ACCENT ILUY', 1452), ('HEBREW ACCENT DEHI', 1453), ('HEBREW ACCENT ZINOR', 1454), ('HEBREW MARK MASORA CIRCLE', 1455), ('HEBREW POINT SHEVA', 1456), ('HEBREW POINT HATAF SEGOL', 1457), ('HEBREW POINT HATAF PATAH', 1458), ('HEBREW POINT HATAF QAMATS', 1459), ('HEBREW POINT HIRIQ', 1460), ('HEBREW POINT TSERE', 1461), ('HEBREW POINT SEGOL', 1462), ('HEBREW POINT PATAH', 1463), ('HEBREW POINT QAMATS', 1464), ('HEBREW POINT HOLAM', 1465), ('HEBREW POINT HOLAM HASER FOR VAV', 1466), ('HEBREW POINT QUBUTS', 1467), ('HEBREW POINT DAGESH OR MAPIQ', 1468), ('HEBREW POINT METEG', 1469), ('HEBREW PUNCTUATION MAQAF', 1470), ('HEBREW POINT RAFE', 1471), ('HEBREW PUNCTUATION PASEQ', 1472), ('HEBREW POINT SHIN DOT', 1473), ('HEBREW POINT SIN DOT', 1474), ('HEBREW PUNCTUATION SOF PASUQ', 1475), ('HEBREW MARK UPPER DOT', 1476), ('HEBREW MARK LOWER DOT', 1477), ('HEBREW PUNCTUATION NUN HAFUKHA', 1478), ('HEBREW POINT QAMATS QATAN', 1479), ('HEBREW LETTER ALEF', 1488), ('HEBREW LETTER BET', 1489), ('HEBREW LETTER GIMEL', 1490), ('HEBREW LETTER DALET', 1491), ('HEBREW LETTER HE', 1492), ('HEBREW LETTER VAV', 1493), ('HEBREW LETTER ZAYIN', 1494), ('HEBREW LETTER HET', 1495), ('HEBREW LETTER TET', 1496), ('HEBREW LETTER YOD', 1497), ('HEBREW LETTER FINAL KAF', 1498), ('HEBREW LETTER KAF', 1499), ('HEBREW LETTER LAMED', 1500), ('HEBREW LETTER FINAL MEM', 1501), ('HEBREW LETTER MEM', 1502), ('HEBREW LETTER FINAL NUN', 1503), ('HEBREW LETTER NUN', 1504), ('HEBREW LETTER SAMEKH', 1505), ('HEBREW LETTER AYIN', 1506), ('HEBREW LETTER FINAL PE', 1507), ('HEBREW LETTER PE', 1508), ('HEBREW LETTER FINAL TSADI', 1509), ('HEBREW LETTER TSADI', 1510), ('HEBREW LETTER QOF', 1511), ('HEBREW LETTER RESH', 1512), ('HEBREW LETTER SHIN', 1513), ('HEBREW LETTER TAV', 1514), ('HEBREW YOD TRIANGLE', 1519), ('HEBREW LIGATURE YIDDISH DOUBLE VAV', 1520), ('HEBREW LIGATURE YIDDISH VAV YOD', 1521), ('HEBREW LIGATURE YIDDISH DOUBLE YOD', 1522), ('HEBREW PUNCTUATION GERESH', 1523), ('HEBREW PUNCTUATION GERSHAYIM', 1524)]
# >>> pprint.pprint(_)
# [('HEBREW ACCENT ETNAHTA', 1425),
#  ('HEBREW ACCENT SEGOL', 1426),
#  ('HEBREW ACCENT SHALSHELET', 1427),
#  ('HEBREW ACCENT ZAQEF QATAN', 1428),
#  ('HEBREW ACCENT ZAQEF GADOL', 1429),
#  ('HEBREW ACCENT TIPEHA', 1430),
#  ('HEBREW ACCENT REVIA', 1431),
#  ('HEBREW ACCENT ZARQA', 1432),
#  ('HEBREW ACCENT PASHTA', 1433),
#  ('HEBREW ACCENT YETIV', 1434),
#  ('HEBREW ACCENT TEVIR', 1435),
#  ('HEBREW ACCENT GERESH', 1436),
#  ('HEBREW ACCENT GERESH MUQDAM', 1437),
#  ('HEBREW ACCENT GERSHAYIM', 1438),
#  ('HEBREW ACCENT QARNEY PARA', 1439),
#  ('HEBREW ACCENT TELISHA GEDOLA', 1440),
#  ('HEBREW ACCENT PAZER', 1441),
#  ('HEBREW ACCENT ATNAH HAFUKH', 1442),
#  ('HEBREW ACCENT MUNAH', 1443),
#  ('HEBREW ACCENT MAHAPAKH', 1444),
#  ('HEBREW ACCENT MERKHA', 1445),
#  ('HEBREW ACCENT MERKHA KEFULA', 1446),
#  ('HEBREW ACCENT DARGA', 1447),
#  ('HEBREW ACCENT QADMA', 1448),
#  ('HEBREW ACCENT TELISHA QETANA', 1449),
#  ('HEBREW ACCENT YERAH BEN YOMO', 1450),
#  ('HEBREW ACCENT OLE', 1451),
#  ('HEBREW ACCENT ILUY', 1452),
#  ('HEBREW ACCENT DEHI', 1453),
#  ('HEBREW ACCENT ZINOR', 1454),
#  ('HEBREW MARK MASORA CIRCLE', 1455),
#  ('HEBREW POINT SHEVA', 1456),
#  ('HEBREW POINT HATAF SEGOL', 1457),
#  ('HEBREW POINT HATAF PATAH', 1458),
#  ('HEBREW POINT HATAF QAMATS', 1459),
#  ('HEBREW POINT HIRIQ', 1460),
#  ('HEBREW POINT TSERE', 1461),
#  ('HEBREW POINT SEGOL', 1462),
#  ('HEBREW POINT PATAH', 1463),
#  ('HEBREW POINT QAMATS', 1464),
#  ('HEBREW POINT HOLAM', 1465),
#  ('HEBREW POINT HOLAM HASER FOR VAV', 1466),
#  ('HEBREW POINT QUBUTS', 1467),
#  ('HEBREW POINT DAGESH OR MAPIQ', 1468),
#  ('HEBREW POINT METEG', 1469),
#  ('HEBREW PUNCTUATION MAQAF', 1470),
#  ('HEBREW POINT RAFE', 1471),
#  ('HEBREW PUNCTUATION PASEQ', 1472),
#  ('HEBREW POINT SHIN DOT', 1473),
#  ('HEBREW POINT SIN DOT', 1474),
#  ('HEBREW PUNCTUATION SOF PASUQ', 1475),
#  ('HEBREW MARK UPPER DOT', 1476),
#  ('HEBREW MARK LOWER DOT', 1477),
#  ('HEBREW PUNCTUATION NUN HAFUKHA', 1478),
#  ('HEBREW POINT QAMATS QATAN', 1479),
#  ('HEBREW LETTER ALEF', 1488),
#  ('HEBREW LETTER BET', 1489),
#  ('HEBREW LETTER GIMEL', 1490),
#  ('HEBREW LETTER DALET', 1491),
#  ('HEBREW LETTER HE', 1492),
#  ('HEBREW LETTER VAV', 1493),
#  ('HEBREW LETTER ZAYIN', 1494),
#  ('HEBREW LETTER HET', 1495),
#  ('HEBREW LETTER TET', 1496),
#  ('HEBREW LETTER YOD', 1497),
#  ('HEBREW LETTER FINAL KAF', 1498),
#  ('HEBREW LETTER KAF', 1499),
#  ('HEBREW LETTER LAMED', 1500),
#  ('HEBREW LETTER FINAL MEM', 1501),
#  ('HEBREW LETTER MEM', 1502),
#  ('HEBREW LETTER FINAL NUN', 1503),
#  ('HEBREW LETTER NUN', 1504),
#  ('HEBREW LETTER SAMEKH', 1505),
#  ('HEBREW LETTER AYIN', 1506),
#  ('HEBREW LETTER FINAL PE', 1507),
#  ('HEBREW LETTER PE', 1508),
#  ('HEBREW LETTER FINAL TSADI', 1509),
#  ('HEBREW LETTER TSADI', 1510),
#  ('HEBREW LETTER QOF', 1511),
#  ('HEBREW LETTER RESH', 1512),
#  ('HEBREW LETTER SHIN', 1513),
#  ('HEBREW LETTER TAV', 1514),
#  ('HEBREW YOD TRIANGLE', 1519),
#  ('HEBREW LIGATURE YIDDISH DOUBLE VAV', 1520),
#  ('HEBREW LIGATURE YIDDISH VAV YOD', 1521),
#  ('HEBREW LIGATURE YIDDISH DOUBLE YOD', 1522),
#  ('HEBREW PUNCTUATION GERESH', 1523),
#  ('HEBREW PUNCTUATION GERSHAYIM', 1524)]
# >>> 
# >>> 
# >>> help(unicodedata)
# Help on built-in module unicodedata:
# 
# NAME
#     unicodedata
# 
# DESCRIPTION
#     This module provides access to the Unicode Character Database which
#     defines character properties for all Unicode characters. The data in
#     this database is based on the UnicodeData.txt file version
#     11.0.0 which is publicly available from ftp://ftp.unicode.org/.
#     
#     The module uses the same names and symbols as defined by the
#     UnicodeData File Format 11.0.0.
# 
# CLASSES
#     builtins.object
#         UCD
#     
#     class UCD(builtins.object)
#      |  Methods defined here:
#      |  
#      |  __getattribute__(self, name, /)
#      |      Return getattr(self, name).
#      |  
#      |  bidirectional(self, chr, /)
#      |      Returns the bidirectional class assigned to the character chr as string.
#      |      
#      |      If no such value is defined, an empty string is returned.
#      |  
#      |  category(self, chr, /)
#      |      Returns the general category assigned to the character chr as string.
#      |  
#      |  combining(self, chr, /)
#      |      Returns the canonical combining class assigned to the character chr as integer.
#      |      
#      |      Returns 0 if no combining class is defined.
#      |  
#      |  decimal(self, chr, default=None, /)
#      |      Converts a Unicode character into its equivalent decimal value.
#      |      
#      |      Returns the decimal value assigned to the character chr as integer.
#      |      If no such value is defined, default is returned, or, if not given,
#      |      ValueError is raised.
#      |  
#      |  decomposition(self, chr, /)
#      |      Returns the character decomposition mapping assigned to the character chr as string.
#      |      
#      |      An empty string is returned in case no such mapping is defined.
#      |  
#      |  digit(self, chr, default=None, /)
#      |      Converts a Unicode character into its equivalent digit value.
#      |      
#      |      Returns the digit value assigned to the character chr as integer.
#      |      If no such value is defined, default is returned, or, if not given,
#      |      ValueError is raised.
#      |  
#      |  east_asian_width(self, chr, /)
#      |      Returns the east asian width assigned to the character chr as string.
#      |  
#      |  lookup(self, name, /)
#      |      Look up character by name.
#      |      
#      |      If a character with the given name is found, return the
#      |      corresponding character.  If not found, KeyError is raised.
#      |  
#      |  mirrored(self, chr, /)
#      |      Returns the mirrored property assigned to the character chr as integer.
#      |      
#      |      Returns 1 if the character has been identified as a "mirrored"
#      |      character in bidirectional text, 0 otherwise.
#      |  
#      |  name(self, chr, default=None, /)
#      |      Returns the name assigned to the character chr as a string.
#      |      
#      |      If no name is defined, default is returned, or, if not given,
#      |      ValueError is raised.
#      |  
#      |  normalize(self, form, unistr, /)
#      |      Return the normal form 'form' for the Unicode string unistr.
#      |      
#      |      Valid values for form are 'NFC', 'NFKC', 'NFD', and 'NFKD'.
#      |  
#      |  numeric(self, chr, default=None, /)
#      |      Converts a Unicode character into its equivalent numeric value.
#      |      
#      |      Returns the numeric value assigned to the character chr as float.
#      |      If no such value is defined, default is returned, or, if not given,
#      |      ValueError is raised.
#      |  
#      |  ----------------------------------------------------------------------
#      |  Data descriptors defined here:
#      |  
#      |  unidata_version
# 
# FUNCTIONS
#     bidirectional(chr, /)
#         Returns the bidirectional class assigned to the character chr as string.
#         
#         If no such value is defined, an empty string is returned.
#     
#     category(chr, /)
#         Returns the general category assigned to the character chr as string.
#     
#     combining(chr, /)
#         Returns the canonical combining class assigned to the character chr as integer.
#         
#         Returns 0 if no combining class is defined.
#     
#     decimal(chr, default=None, /)
#         Converts a Unicode character into its equivalent decimal value.
#         
#         Returns the decimal value assigned to the character chr as integer.
#         If no such value is defined, default is returned, or, if not given,
#         ValueError is raised.
#     
#     decomposition(chr, /)
#         Returns the character decomposition mapping assigned to the character chr as string.
#         
#         An empty string is returned in case no such mapping is defined.
#     
#     digit(chr, default=None, /)
#         Converts a Unicode character into its equivalent digit value.
#         
#         Returns the digit value assigned to the character chr as integer.
#         If no such value is defined, default is returned, or, if not given,
#         ValueError is raised.
#     
#     east_asian_width(chr, /)
#         Returns the east asian width assigned to the character chr as string.
#     
#     lookup(name, /)
#         Look up character by name.
#         
#         If a character with the given name is found, return the
#         corresponding character.  If not found, KeyError is raised.
#     
#     mirrored(chr, /)
#         Returns the mirrored property assigned to the character chr as integer.
#         
#         Returns 1 if the character has been identified as a "mirrored"
#         character in bidirectional text, 0 otherwise.
#     
#     name(chr, default=None, /)
#         Returns the name assigned to the character chr as a string.
#         
#         If no name is defined, default is returned, or, if not given,
#         ValueError is raised.
#     
#     normalize(form, unistr, /)
#         Return the normal form 'form' for the Unicode string unistr.
#         
#         Valid values for form are 'NFC', 'NFKC', 'NFD', and 'NFKD'.
#     
#     numeric(chr, default=None, /)
#         Converts a Unicode character into its equivalent numeric value.
#         
#         Returns the numeric value assigned to the character chr as float.
#         If no such value is defined, default is returned, or, if not given,
#         ValueError is raised.
# 
# DATA
#     ucd_3_2_0 = <unicodedata.UCD object>
#     ucnhash_CAPI = <capsule object "unicodedata.ucnhash_CAPI">
#     unidata_version = '11.0.0'
# 
# FILE
#     (built-in)
# 
# 
# >>> dir(unicodedata)
# ['UCD', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'bidirectional', 'category', 'combining', 'decimal', 'decomposition', 'digit', 'east_asian_width', 'lookup', 'mirrored', 'name', 'normalize', 'numeric', 'ucd_3_2_0', 'ucnhash_CAPI', 'unidata_version']
# >>> 
# >>> 
# >>> 
# >>> s=('וְ')
# >>> list(map(unicodedata.category,s))
# ['Lo', 'Mn']
# >>> modifierlen('מְ')
# 1
# >>> 
# >>> 'מְ'.center(2)
# 'מְ'
# >>> ssum('JEHOVAH')
# 492
# >>> 
# >>> print(mdtable(Table([list(AB),Row(AB)@osum])))
# <console>:1: NameError: name 'AB' is not defined
# >>> tellmd('יְהֹוָה'[::-1])
# 
# |הָ||וֹ||הְ||י|||
# |-|-|-|-|-|-|-|-|-|
# |5|+|6|+|5|+|10|=|26|
# 
# >>> tellmd('God')
# 
# |G||o||d|||
# |-|-|-|-|-|-|-|
# |7|+|15|+|4|=|26|
# 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
