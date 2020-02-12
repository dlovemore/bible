import re

ab='abcdefghijklmnopqrstuvwxyz'
αβ='αβγδεςζηθικλμνξοπϙρστυφχξψωϡ'
אב='אבגדהוזחטיכלמנסעפצקרשת'
pos={c:i for i,c in enumerate(ab,start=1)}
pos.update({c:i for i,c in enumerate(αβ,start=1)})
pos.update({c:i for i,c in enumerate(אב,start=1)})

letters={a:a for a in ab+αβ+אב}
vowels=set('aeiou' + 'αεηιουω')

eqss=['αάἀἁἂἃἄἅἆἇὰάᾀᾁᾂᾃᾄᾅᾆᾇᾰᾱᾲᾳᾴᾶᾷ','εέἐἑἒἓἔἕὲέ','ηήἠἡἢἣἤἥἦἧὴήᾐᾑᾒᾓᾔᾕᾖᾗῂῃῄῆῇ',
'οόὀὁὂὃὄὅὸό','ιίϊΐἰἱἲἳἴἵἶἷὶίῐῑῒΐῖῗ','υύϋΰὐὑὒὓὔὕὖὗὺύῠῡῢΰῦῧ',
'ωώὠὡὢὣὤὥὦὧὼώᾠᾡᾢᾣᾤᾥᾦᾧῲῳῴῶῷ','ρῤῥ']
eqss+=['כך','מם','נן'] #,'σς']
for eqs in eqss:
    primary=eqs[0]
    for c in eqs[1:]:
        letters[c]=letters[primary]

for c in 'ᾀᾁᾂᾃᾄᾅᾆᾇᾲᾳᾴᾷᾐᾑᾒᾓᾔᾕᾖᾗῂῃῄῇᾠᾡᾢᾣᾤᾥᾦᾧῲῳῴῷ':
    letters[c]+='ι'

def chars(s):
    return ''.join([letters[c] for c in s.lower() if c.isalpha()])

def ovals(s):
    return [pos[c] for c in chars(s)]

def osum(s): return sum(ovals(s))

pdigits=[0]+list(range(1,10))+list(range(10,100,10))+list(range(100,1000,100))
def psum(s): return sum([pdigits[k] for k in ovals(s)])
def sums(s): return osum(s),psum(s)

# >>> from mean1 import *
# >>> from primes import *
# >>> from math import *
# >>> dir(re)
# ['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'Match', 'Pattern', 'RegexFlag', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_cache', '_compile', '_compile_repl', '_expand', '_locale', '_pickle', '_special_chars_map', '_subx', 'compile', 'copyreg', 'enum', 'error', 'escape', 'findall', 'finditer', 'fullmatch', 'functools', 'match', 'purge', 'search', 'split', 'sre_compile', 'sre_parse', 'sub', 'subn', 'template']
# >>> re.findall('[a-z]','Abc, def'.lower())
# ['a', 'b', 'c', 'd', 'e', 'f']
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
# >>> osum('את')
# 23
# >>> psum('את')
# 401
# >>> osum('יהוה')
# 26
# >>> psum('יהוה')
# 26
# >>> osum('LORD OF LORDS')
# 138
# >>> psum('LORD OF LORDS')
# 534
# >>> osum('THE LORD')
# 82
# >>> osum('KING OF KINGS')
# 122
# >>> psum('KING OF KINGS')
# 338
# >>> osum('Immanuel')
# 88
# >>> osum('Prince of Peace')
# 116
# >>> osum('eth')
# 33
# >>> osum('et')
# 25
# >>> j11='ἐν ἀρχῇ ἦν ὁ λόγος καὶ ὁ λόγος ἦν πρὸς τὸν θεόν καὶ θεὸς ἦν ὁ λόγος'
# >>> osum(j11),psum(j11)
# (587, 2657)
# >>> factors(_[1])
# [2657]
# >>> 2701-_[0]
# 44
# >>> 
# >>> psum('Κυριος'),psum('Ιησους'),psum('Χρηστος')
# (606, 694, 1284)
# >>> sum(_)
# 2584
# >>> osum('Κυριος'),osum('Ιησους'),osum('Χρηστος')
# (84, 82, 114)
# >>> sum(_)
# 280
# >>> 
# >>> 888*1478
# 1312464
# >>> 888+1478
# 2366
# >>> factors(1478)
# [2, 739]
# >>> 
# >>> sums("οὗτος")
# (81, 846)
# >>> 
# >>> 
# >>> from search import *
# >>> nt=b.Matt[1:1]-b.Rev[22:21]
# >>> nt
# 7957 verses, Matthew 1:1...Revelation 22:21
# >>> factors(7957)
# [73, 109]
# >>> sums(b.v(1))
# (411, 2094)
# >>> factors(2094)
# [2, 3, 349]
# >>> sums(b.Gen[1:].vs())
# (34463, 233444)
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
# >>> b.chapters()[666-1]
# 29 verses, Ecclesiastes 7:1...Ecclesiastes 7:29
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
# >>> sqrt(31102)
# 176.35759127409287
# >>> 
# >>> sums("ἰουδαίας")
# (70, 502)
# >>> sums("ἡρῴδης")
# (82, 1036)
# >>> sums("herod")
# (50, 167)
# >>> sums("king")
# (41, 86)
# >>> sums("herodias")
# (79, 277)
# >>> sums("ἡρῴδου")
# (106, 1492)
# >>> sums("Judah")
# (44, 323)
# >>> sums("of")
# (21, 66)
# >>> sums("judaea")
# (42, 321)
# >>> sums("ἡρώδης")
# (72, 1026)
# >>> list(map(sums,["Lord","Jesus","Christ"]))
# [(49, 184), (74, 515), (77, 410)]
# >>> 49+74+77
# 200
# >>> 184+515+410
# 1109
# >>> sums("ἰουδαίαν")
# (78, 546)
# >>> b.Ecc[7:27]
# 1 verses, Ecclesiastes 7:27
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
# >>> factors(9801)
# [3, 3, 3, 3, 11, 11]
# >>> 99*99
# 9801
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
