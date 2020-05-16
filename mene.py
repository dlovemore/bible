from parle import *
from table import *
import re
import itertools
import functools
import unicodedata
c=299792458

ab='abcdefghijklmnopqrstuvwxyz'
alphabeta=αβ='αβγδεϝζηθικλμνξοπϙρστυφχψωϡ'
alephbeth=אב='אבגדהוזחטיכלמנסעפצקרשת'
аб='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
hira=あい='あいうえおかがきぎくぐけげこごさざしじすずせぜそぞただちぢつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもやゆよらりるれろわゐゑをんゔ'
hirasmall={'ぁ': 'あ', 'ぃ': 'い', 'ぅ': 'う', 'ぇ': 'え', 'ぉ': 'お', 'っ': 'つ', 'ゃ': 'や', 'ゅ': 'ゆ', 'ょ': 'よ', 'ゎ': 'わ', 'ゕ': 'か', 'ゖ': 'け'}
nn='0123456789'
pos={c:i for i,c in enumerate(ab,start=1)}
pos.update({c:i for i,c in enumerate(αβ,start=1)})
pos.update({c:i for i,c in enumerate(אב,start=1)})
pos.update({c:i for i,c in enumerate(аб,start=1)})
pos.update({c:i for i,c in enumerate(あい,start=1)})
pos.update({small:pos[c] for small,c in hirasmall.items()})
pos.update({c:i for i,c in enumerate(nn)})

characters={a:a for a in pos.keys()}
vowels=set('aeiou' + 'αεηιουω' + 'аеёийоуыьэюя'+'аеёийоуъ?ыь?эюя'+
    ''.join(hirasmall))

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

@Func
@functools.lru_cache(22222)
def letters(s):
    return ''.join([characters[c] for c in s.lower() if isletter(c)])

@Func
def ovals(s):
    return [pos[c] for c in letters(s)]

@Func
def count(s): return sum(ovals(s))

osum=count

pdigits=[0]+list(range(1,10))+list(range(10,100,10))+list(range(100,1000,100))
def ssum(s): return sum([pdigits[k] for k in ovals(s)])
def lsum(s): return sum((isletter(c) for c in letters(s)))
def ascsum(s): return sum((ord(l) for l in s if isletter(l)))
def sums(s): return lsum(s),osum(s),psum(s)
psum=ssum

@Func
def showalphas(ab=ab,f=osum):
    letters, vals = table(ab,[f(l) for l in ab])
    print(' '.join(letters))
    print(' '.join(vals))

@Func
def join(sep,l):
    r=[sep]*(len(l)*2-1)
    r[::2]=l
    return r

@Func
def tell(*ss):
    print(texttable(telltable(*ss)))

tells=partial(tell,lsum,osum,ssum)

@Func
def tellmd(*ss):
    print(mdtable(telltable(*ss)))

@Func
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

@Func
def texttable(vv,sep=' '):
    return '\n'.join([sep.join(v).rstrip() for v in justify(vv)])

@Func
def mdtable(vv):
    vv=fill(vv@str,'')
    def j(s,l): return s+s.join(l)
    return '\n'.join([j('|',vv[0]),j('|','-'*len(vv[0]))]+[j('|',v) for v in vv[1:]])

@Func
def ns(n):
    fs=factors(n)
    fi=[np(f) for f in fs]
    print(fs,fi)

@Func
def issquare(n): return int(math.sqrt(n))**2==n

@Func
def sos(n):
    r=span(0,int((n/2)**.5))/F((lambda x: issquare(n-x*x)))
    return [[i,int(math.sqrt(n-i*i))]@(I+I) for i in r]

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
# >>> issquare(11)
# False
# >>> math.sqrt(11)**2
# 11.0
# >>> 
# >>> 
# >>> span(1000)/issquare
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961]
# >>> len(_)
# 31
# >>> 
# >>> sos(100)
# [[(0, 0), (10, 10)], [(6, 6), (8, 8)]]
# >>> sos(50)
# [[(1, 1), (7, 7)], [(5, 5), (5, 5)]]
# >>> sos(18)
# [[(3, 3), (3, 3)]]
# >>> sos(1189)
# [[(10, 10), (33, 33)], [(17, 17), (30, 30)]]
# >>> sos(73)
# [[(3, 3), (8, 8)]]
# >>> sos(930)
# []
# >>> 
# >>> 
# >>> 
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
# <67>:1: NameError: name 'b' is not defined
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
# 79
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
# (7, 82, 397)
# >>> sums('KING OF KINGS')
# (11, 122, 338)
# >>> sums('Immanuel')
# (8, 88, 475)
# >>> sums('Prince of Peace')
# (13, 116, 377)
# >>> sums('eth')
# (3, 33, 213)
# >>> sums('et')
# (2, 25, 205)
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
# 74 11 128
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
# Lord Jesus  =
#  4     5    9
#  49    74  123
# 184   515  699
# >>> tell("Jesus Christ",lsum,osum,ssum)
# Jesus Christ  =
#   5     6     11
#   74    77   151
#  515   410   925
# >>> tell("Lord Jesus Christ",lsum,osum,ssum)
# Lord Jesus Christ  =
#  4     5     6     15
#  49    74    77   200
# 184   515   410   1109
# >>> tell("Lord Jesus",lsum,osum,ssum)
# Lord Jesus  =
#  4     5    9
#  49    74  123
# 184   515  699
# >>> 
# >>> tell('Κυριος Ιησους Χρηστος',lsum,osum,ssum)
# Κυριος Ιησους Χρηστος  =
#   6      6       7     19
#   98     96     128   322
#  800    888     1478  3166
# >>> tell("LORD JEHOVAH",lsum,osum,ssum)
# LORD JEHOVAH  =
#  4      7     11
#  49     69   118
# 184    492   676
# >>> 
# >>> 
# >>> 
# >>> 
# >>> from bible import *
# >>> b.Genesis[1:1].tell()
# In the beginning God created the heaven and the earth.  =
# 23  33     81     26    56    33   55    19  33   52   411
# >>> factors(1478)
# [2, 739]
# >>> 
# >>> sums("οὗτος")
# (5, 95, 1040)
# >>> lsum(Genesis[1:1].vs())
# 44
# >>> nt=b.Matthew-b.Revelation
# >>> 
# >>> nt
# Matthew 1:1-Revelation 22:21 (7957 verses)
# >>> factors(7957)
# [73, 109]
# >>> sums(b.v(1))
# (44, 411, 2094)
# >>> factors(2094)
# [2, 3, 349]
# >>> sums(b.Gen[1:].vs())
# (3167, 34463, 233444)
# >>> 
# >>> b.Gen.wc()
# 38264
# >>> 
# >>> 
# >>> factors(233444)
# [2, 2, 17, 3433]
# >>> sums("lord jesus christ")
# (15, 200, 1109)
# >>> sums("the")
# (3, 33, 213)
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
# (8, 84, 696)
# >>> sums("ἡρῴδης")
# (7, 95, 1130)
# >>> sums("herod")
# (5, 50, 167)
# >>> sums("king")
# (4, 41, 86)
# >>> sums("herodias")
# (8, 79, 277)
# >>> sums("ἡρῴδου")
# (7, 105, 1392)
# >>> sums("Judah")
# (5, 44, 323)
# >>> sums("of")
# (2, 21, 66)
# >>> tell('The Holy Bible',lsum,osum,ssum)
# The Holy Bible  =
#  3   4     5    12
#  33  60    30  123
# 213 798    48  1059
# >>> 
# >>> sums("judaea")
# (6, 42, 321)
# >>> sums("ἡρώδης")
# (6, 85, 1120)
# >>> list(map(sums,["Lord","Jesus","Christ"]))
# [(4, 49, 184), (5, 74, 515), (6, 77, 410)]
# >>> 49+74+77
# 200
# >>> 184+515+410
# 1109
# >>> sums("ἰουδαίαν")
# (8, 78, 546)
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
# (6, 37, 100)
# >>> sums("love")
# (4, 54, 495)
# >>> b.Gen-b.Num
# Genesis 1:1-Numbers 36:13 (4893 verses)
# >>> 
# >>> b/"tale"/"told"
# Psalms 90:9 For all our days are passed away in thy wrath: we spend our years as a tale that is told.
# >>> _.tell(lsum,osum,ssum)
# For all our days are passed away in thy wrath:  we spend our years  as a tale that  is told.  =
#  3   3   3   4    3    6     4   2   3    5     2    5    3    5    2  1  4    4    2    4    68
#  39  25  54  49   24   64    50  23  53   70    28   58   54   68   20 1  38   49   28   51  846
# 156  61 450 805   96  280   1202 59 908  799   505  229  450  896  101 1 236  409  109  294  8046
# >>> 
# >>> b.Ps[90]
# Psalms 90:1-17 (17 verses)
# >>> _.tell()
# Lord, thou hast been our dwelling place in all generations.  =
#   49   64   48   26   54    86      37  23  25     127      539
# Before the mountains were brought forth, or ever thou hadst formed the earth and the world, even from everlasting to everlasting, thou art God.  =
#   51    33    126     51     91     67   33  50   64    52    61    33   52   19  33   72    46   52      132     35     132       64   39  26  1414
# Thou turnest man to destruction; and sayest, Return, ye children of men.  =
#  64    117    28 35     148       19    89      96   30    73    21  32  752
# For a thousand years in thy sight are but as yesterday when it is past, and as a watch in the night.  =
#  39 1   102      68  23  53   63   24  43 20    122     50  29 28   56   19 20 1   55  23  33   58   930
# Thou carriest them away as with a flood; they are as a sleep: in the morning they are like grass which groweth up.  =
#  64     93     46   50  20  60  1   52    58   24 20 1   57   23  33    90    58   24  37    64    51     96    37 1059
# In the morning it flourisheth, and groweth up; in the evening it is cut down, and withereth.  =
# 23  33    90   29     141       19    96    37 23  33    76   29 28  44   56   19    116     892
# For we are consumed by thine anger, and by thy wrath are we troubled.  =
#  39 28  24    94    27   56    45    19 27  53   70   24 28     97    631
# Thou hast set our iniquities before thee, our secret sins in the light of thy countenance.  =
#  64   48   44  54    132       51     38   54   70    61  23  33   56  21  53     115      917
# For all our days are passed away in thy wrath: we spend our years as a tale that is told.  =
#  39  25  54  49   24   64    50  23  53   70   28   58   54   68  20 1  38   49  28   51  846
# The days of our years are threescore years and ten; and if by reason of strength they be fourscore years, yet is their strength labour and sorrow; for it is soon cut off, and we fly away.  =
#  33  49  21  54   68   24    116       68   19  39   19 15 27   72   21   111     58  7     120      68    50 28   60    111      69    19   108    39 29 28  63   44  27   19 28  43   50  1824
# Who knoweth the power of thine anger? even according to thy fear, so is thy wrath.  =
#  46    96    33   77  21   56    45    46      74    35  53   30  34 28  53   70   797
# So teach us to number our days, that we may apply our hearts unto wisdom.  =
# 34   37  40 35   73    54   49   49  28  39   70   54   71    70     83   786
# Return, O  LORD, how long? and let it repent thee concerning thy servants.  =
#    96   15   49   46   48   19  37 29   78    38     102      53    118    728
# O  satisfy us early with thy mercy; that we may rejoice and be glad all our days.  =
# 15    99   40   61   60   53   64    49  28  39    65    19 7   24   25  54   49  751
# Make us glad according to the days wherein thou hast afflicted us, and the years wherein we have seen evil.  =
#  30  40  24      74    35  33  49     82    64   48      66     40  19  33   68     82   28  36   43    48  942
# Let thy work appear unto thy servants, and thy glory unto their children.  =
#  37  53  67    57    70   53    118     19  53   77   70    60      73    807
# And let the beauty of the LORD our God be upon us: and establish thou the work of our hands upon us; yea, the work of our hands establish thou it.  =
#  19  37  33   74   21  33  49   54  26 7   66   40  19     95     64   33  67  21  54   46   66   40  31   33  67  21  54   46      95     64   29 1404
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
#  מָ שִׁ  י  חַ =
# 13 21 10 8 52
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
# <219>:1: NameError: name 'AB' is not defined
# >>> tellmd('יְהֹוָה'[::-1])
# |הָ|וֹ|הְ|י|=
# |-|-|-|-|-
# |5|6|5|10|26
# >>> tellmd('God')
# |G|o|d|=
# |-|-|-|-
# |7|15|4|26
# >>> 
# >>> ns(123)
# [3, 41] [2, 13]
# >>> tell('Бог')
# Б о  г =
# 2 16 4 22
# >>> tell('Иегова')
# И  е г о  в а =
# 10 6 4 16 3 1 40
# >>> tell('Жэхова')
# Ж э  х  о  в а =
# 8 31 23 16 3 1 82
# >>> tell(аб)
# а б в г д е ё ж з и  й  к  л  м  н  о  п  р  с  т  у  ф  х  ц  ч  ш  щ  ъ  ы  ь  э  ю  я   =
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 561
# >>> span('\u3041','\u3096')
# 'ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖ'
# >>> hira=_
# >>> 
# >>> 'あ'*F(unicodedata.name)*Binop(op.contains)*'SMALL'*op.not_
# True
# >>> notsmall=F(unicodedata.name)*(Binop(op.contains)*'SMALL')*op.not_
# >>> 'あ'*notsmall
# True
# >>> 'ぁ'*notsmall
# False
# >>> hira
# 'ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖ'
# >>> hira/notsmall
# 'あいうえおかがきぎくぐけげこごさざしじすずせぜそぞただちぢつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもやゆよらりるれろわゐゑをんゔ'
# >>> len(_),len(hira)
# (74, 86)
# >>> 
# >>> あい
# 'あいうえおかがきぎくぐけげこごさざしじすずせぜそぞただちぢつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもやゆよらりるれろわゐゑをんゔ'
# >>> showalphas(_)
# あ い う え お か が き ぎ く  ぐ  け  げ  こ  ご  さ  ざ  し  じ  す  ず  せ  ぜ  そ  ぞ  た  だ  ち  ぢ  つ  づ  て  で  と  ど  な  に  ぬ  ね  の  は  ば  ぱ  ひ  び  ぴ  ふ  ぶ  ぷ  へ  べ  ぺ  ほ  ぼ  ぽ  ま  み  む  め  も  や  ゆ  よ  ら  り  る  れ  ろ  わ  ゐ  ゑ  を  ん  ゔ 
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74
# >>> import htmldraw
# >>> dr(htmldraw)
# 'Attr' 'Binop' 'DataRow' 'Dict' 'F' 'FR' 'Fun' 'Func' 'FuncRow' 'GetItem' 'I' 'K' 'L' 'LeftOp' 'Lookup' 'RightOp' 'TAG' 'Unique' 'X' 'add' 'apply' 'aslist' 'builtins' 'callmethod' 'compose' 'const' 'delay' 'divide' 'dmap' 'draw' 'e' 'escape' 'failas' 'fggf' 'filter' 'first' 'firstn' 'floordiv' 'fun' 'functools' 'getitem' 'getprop' 'html' 'htmltable' 'inks' 'l' 'li' 'lmap' 'meth' 'method' 'mod' 'mul' 'op' 'operator' 'orr' 'p' 'pairs' 'partial' 'perm' 'permargs' 'plain' 'pmap' 'positions' 'pow' 'prop' 'push' 'q' 'qstr' 'redparts' 'reduce' 'rowtype' 'scale' 'show' 'showfile' 'showt' 'span' 'splitat' 'star' 'sub' 'subprocess' 'svg' 'swap' 'swapargs' 'table' 'th' 'threes' 'translate' 'trrow' 'truediv' 'trystr' 'twos' 'unstar' 'webbrowser' 'windows' 'withoutrepeats'
# >>> htmldraw.table(あい@+osum)
# ['table', ['tr', ['td', 'あ'], ['td', 1]], ['tr', ['td', 'い'], ['td', 2]], ['tr', ['td', 'う'], ['td', 3]], ['tr', ['td', 'え'], ['td', 4]], ['tr', ['td', 'お'], ['td', 5]], ['tr', ['td', 'か'], ['td', 6]], ['tr', ['td', 'が'], ['td', 7]], ['tr', ['td', 'き'], ['td', 8]], ['tr', ['td', 'ぎ'], ['td', 9]], ['tr', ['td', 'く'], ['td', 10]], ['tr', ['td', 'ぐ'], ['td', 11]], ['tr', ['td', 'け'], ['td', 12]], ['tr', ['td', 'げ'], ['td', 13]], ['tr', ['td', 'こ'], ['td', 14]], ['tr', ['td', 'ご'], ['td', 15]], ['tr', ['td', 'さ'], ['td', 16]], ['tr', ['td', 'ざ'], ['td', 17]], ['tr', ['td', 'し'], ['td', 18]], ['tr', ['td', 'じ'], ['td', 19]], ['tr', ['td', 'す'], ['td', 20]], ['tr', ['td', 'ず'], ['td', 21]], ['tr', ['td', 'せ'], ['td', 22]], ['tr', ['td', 'ぜ'], ['td', 23]], ['tr', ['td', 'そ'], ['td', 24]], ['tr', ['td', 'ぞ'], ['td', 25]], ['tr', ['td', 'た'], ['td', 26]], ['tr', ['td', 'だ'], ['td', 27]], ['tr', ['td', 'ち'], ['td', 28]], ['tr', ['td', 'ぢ'], ['td', 29]], ['tr', ['td', 'つ'], ['td', 30]], ['tr', ['td', 'づ'], ['td', 31]], ['tr', ['td', 'て'], ['td', 32]], ['tr', ['td', 'で'], ['td', 33]], ['tr', ['td', 'と'], ['td', 34]], ['tr', ['td', 'ど'], ['td', 35]], ['tr', ['td', 'な'], ['td', 36]], ['tr', ['td', 'に'], ['td', 37]], ['tr', ['td', 'ぬ'], ['td', 38]], ['tr', ['td', 'ね'], ['td', 39]], ['tr', ['td', 'の'], ['td', 40]], ['tr', ['td', 'は'], ['td', 41]], ['tr', ['td', 'ば'], ['td', 42]], ['tr', ['td', 'ぱ'], ['td', 43]], ['tr', ['td', 'ひ'], ['td', 44]], ['tr', ['td', 'び'], ['td', 45]], ['tr', ['td', 'ぴ'], ['td', 46]], ['tr', ['td', 'ふ'], ['td', 47]], ['tr', ['td', 'ぶ'], ['td', 48]], ['tr', ['td', 'ぷ'], ['td', 49]], ['tr', ['td', 'へ'], ['td', 50]], ['tr', ['td', 'べ'], ['td', 51]], ['tr', ['td', 'ぺ'], ['td', 52]], ['tr', ['td', 'ほ'], ['td', 53]], ['tr', ['td', 'ぼ'], ['td', 54]], ['tr', ['td', 'ぽ'], ['td', 55]], ['tr', ['td', 'ま'], ['td', 56]], ['tr', ['td', 'み'], ['td', 57]], ['tr', ['td', 'む'], ['td', 58]], ['tr', ['td', 'め'], ['td', 59]], ['tr', ['td', 'も'], ['td', 60]], ['tr', ['td', 'や'], ['td', 61]], ['tr', ['td', 'ゆ'], ['td', 62]], ['tr', ['td', 'よ'], ['td', 63]], ['tr', ['td', 'ら'], ['td', 64]], ['tr', ['td', 'り'], ['td', 65]], ['tr', ['td', 'る'], ['td', 66]], ['tr', ['td', 'れ'], ['td', 67]], ['tr', ['td', 'ろ'], ['td', 68]], ['tr', ['td', 'わ'], ['td', 69]], ['tr', ['td', 'ゐ'], ['td', 70]], ['tr', ['td', 'ゑ'], ['td', 71]], ['tr', ['td', 'を'], ['td', 72]], ['tr', ['td', 'ん'], ['td', 73]], ['tr', ['td', 'ゔ'], ['td', 74]]]
# >>> # htmldraw.show(_)
# >>> texttable(あい@+osum)
# 'あ 1\nい 2\nう 3\nえ 4\nお 5\nか 6\nが 7\nき 8\nぎ 9\nく 10\nぐ 11\nけ 12\nげ 13\nこ 14\nご 15\nさ 16\nざ 17\nし 18\nじ 19\nす 20\nず 21\nせ 22\nぜ 23\nそ 24\nぞ 25\nた 26\nだ 27\nち 28\nぢ 29\nつ 30\nづ 31\nて 32\nで 33\nと 34\nど 35\nな 36\nに 37\nぬ 38\nね 39\nの 40\nは 41\nば 42\nぱ 43\nひ 44\nび 45\nぴ 46\nふ 47\nぶ 48\nぷ 49\nへ 50\nべ 51\nぺ 52\nほ 53\nぼ 54\nぽ 55\nま 56\nみ 57\nむ 58\nめ 59\nも 60\nや 61\nゆ 62\nよ 63\nら 64\nり 65\nる 66\nれ 67\nろ 68\nわ 69\nゐ 70\nゑ 71\nを 72\nん 73\nゔ 74'
# >>> p(_)
# あ 1
# い 2
# う 3
# え 4
# お 5
# か 6
# が 7
# き 8
# ぎ 9
# く 10
# ぐ 11
# け 12
# げ 13
# こ 14
# ご 15
# さ 16
# ざ 17
# し 18
# じ 19
# す 20
# ず 21
# せ 22
# ぜ 23
# そ 24
# ぞ 25
# た 26
# だ 27
# ち 28
# ぢ 29
# つ 30
# づ 31
# て 32
# で 33
# と 34
# ど 35
# な 36
# に 37
# ぬ 38
# ね 39
# の 40
# は 41
# ば 42
# ぱ 43
# ひ 44
# び 45
# ぴ 46
# ふ 47
# ぶ 48
# ぷ 49
# へ 50
# べ 51
# ぺ 52
# ほ 53
# ぼ 54
# ぽ 55
# ま 56
# み 57
# む 58
# め 59
# も 60
# や 61
# ゆ 62
# よ 63
# ら 64
# り 65
# る 66
# れ 67
# ろ 68
# わ 69
# ゐ 70
# ゑ 71
# を 72
# ん 73
# ゔ 74
# >>> 
# >>> span('\u3041','\u3096')
# 'ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖ'
# >>> span('\u3041','\u3096')*L
# ['ぁ', 'あ', 'ぃ', 'い', 'ぅ', 'う', 'ぇ', 'え', 'ぉ', 'お', 'か', 'が', 'き', 'ぎ', 'く', 'ぐ', 'け', 'げ', 'こ', 'ご', 'さ', 'ざ', 'し', 'じ', 'す', 'ず', 'せ', 'ぜ', 'そ', 'ぞ', 'た', 'だ', 'ち', 'ぢ', 'っ', 'つ', 'づ', 'て', 'で', 'と', 'ど', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ば', 'ぱ', 'ひ', 'び', 'ぴ', 'ふ', 'ぶ', 'ぷ', 'へ', 'べ', 'ぺ', 'ほ', 'ぼ', 'ぽ', 'ま', 'み', 'む', 'め', 'も', 'ゃ', 'や', 'ゅ', 'ゆ', 'ょ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'ゎ', 'わ', 'ゐ', 'ゑ', 'を', 'ん', 'ゔ', 'ゕ', 'ゖ']
# >>> span('\u3041','\u3096')*L@F(unicodedata.name)
# ['HIRAGANA LETTER SMALL A', 'HIRAGANA LETTER A', 'HIRAGANA LETTER SMALL I', 'HIRAGANA LETTER I', 'HIRAGANA LETTER SMALL U', 'HIRAGANA LETTER U', 'HIRAGANA LETTER SMALL E', 'HIRAGANA LETTER E', 'HIRAGANA LETTER SMALL O', 'HIRAGANA LETTER O', 'HIRAGANA LETTER KA', 'HIRAGANA LETTER GA', 'HIRAGANA LETTER KI', 'HIRAGANA LETTER GI', 'HIRAGANA LETTER KU', 'HIRAGANA LETTER GU', 'HIRAGANA LETTER KE', 'HIRAGANA LETTER GE', 'HIRAGANA LETTER KO', 'HIRAGANA LETTER GO', 'HIRAGANA LETTER SA', 'HIRAGANA LETTER ZA', 'HIRAGANA LETTER SI', 'HIRAGANA LETTER ZI', 'HIRAGANA LETTER SU', 'HIRAGANA LETTER ZU', 'HIRAGANA LETTER SE', 'HIRAGANA LETTER ZE', 'HIRAGANA LETTER SO', 'HIRAGANA LETTER ZO', 'HIRAGANA LETTER TA', 'HIRAGANA LETTER DA', 'HIRAGANA LETTER TI', 'HIRAGANA LETTER DI', 'HIRAGANA LETTER SMALL TU', 'HIRAGANA LETTER TU', 'HIRAGANA LETTER DU', 'HIRAGANA LETTER TE', 'HIRAGANA LETTER DE', 'HIRAGANA LETTER TO', 'HIRAGANA LETTER DO', 'HIRAGANA LETTER NA', 'HIRAGANA LETTER NI', 'HIRAGANA LETTER NU', 'HIRAGANA LETTER NE', 'HIRAGANA LETTER NO', 'HIRAGANA LETTER HA', 'HIRAGANA LETTER BA', 'HIRAGANA LETTER PA', 'HIRAGANA LETTER HI', 'HIRAGANA LETTER BI', 'HIRAGANA LETTER PI', 'HIRAGANA LETTER HU', 'HIRAGANA LETTER BU', 'HIRAGANA LETTER PU', 'HIRAGANA LETTER HE', 'HIRAGANA LETTER BE', 'HIRAGANA LETTER PE', 'HIRAGANA LETTER HO', 'HIRAGANA LETTER BO', 'HIRAGANA LETTER PO', 'HIRAGANA LETTER MA', 'HIRAGANA LETTER MI', 'HIRAGANA LETTER MU', 'HIRAGANA LETTER ME', 'HIRAGANA LETTER MO', 'HIRAGANA LETTER SMALL YA', 'HIRAGANA LETTER YA', 'HIRAGANA LETTER SMALL YU', 'HIRAGANA LETTER YU', 'HIRAGANA LETTER SMALL YO', 'HIRAGANA LETTER YO', 'HIRAGANA LETTER RA', 'HIRAGANA LETTER RI', 'HIRAGANA LETTER RU', 'HIRAGANA LETTER RE', 'HIRAGANA LETTER RO', 'HIRAGANA LETTER SMALL WA', 'HIRAGANA LETTER WA', 'HIRAGANA LETTER WI', 'HIRAGANA LETTER WE', 'HIRAGANA LETTER WO', 'HIRAGANA LETTER N', 'HIRAGANA LETTER VU', 'HIRAGANA LETTER SMALL KA', 'HIRAGANA LETTER SMALL KE']
# >>> 
# >>> span('\u3041','\u3096')/(F(unicodedata.name)*(Binop(op.contains)*'SMALL'))
# 'ぁぃぅぇぉっゃゅょゎゕゖ'
# >>> 
