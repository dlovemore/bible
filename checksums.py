>>> from bible import *
>>> 
>>> def csb(n=1189): return sum([i*bible.chapter(i).vc() for i in span(1,n)])
... 
>>> csb(1189)
18055094
>>> csb(500)
3365134
>>> csb(256)
982156
>>> csb(128)
274094
>>> csb(64)
63450
>>> csb(32)
17304
>>> csb(16)
3207
>>> csb(8)
893
>>> csb(4)
257
>>> csb(3)
153
>>> csb(6)
549
>>> csb(5)
417
>>> 
>>> 94-29
65
>>> fs(65)
[5, 13]
>>> 
>>> 
>>> def cs1(l): return sum([(i*x) for i,x in enumerate(l,start=1)])
... 
>>> cs1(l),cs1(l2)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "<console>", line 1, in cs1
TypeError: 'functools.partial' object is not iterable
>>> cs1([v.vn() for v in bible])
10029161883455
>>> tell(ssum,'Solomon')
o  l  o  m  o  n
60+30+60+40+60+50=300
>>> ssum('Solomon')//2
200
>>> tell('Lord Jesus Christ')
Lord Jesus Christ
 49 +  74 +  77  =200
>>> 
>>> b/'half was not told'
1 Kings 10:7 Howbeit I believed not the words, until I came, and mine eyes had seen it: and, behold, the half was not told me: thy wisdom and prosperity exceedeth the fame which I heard.
>>> 
>>> 
>>> for c in enumerate('fred'): print(c)
... 
(0, 'f')
(1, 'r')
(2, 'e')
(3, 'd')
>>> for i,c in enumerate('fred'): print(i,c)
... 
0 f
1 r
2 e
3 d
>>> from auto import *
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_os', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>> random.choice('abcdef')
'a'
>>> random.choice('abcdef')
'd'
>>> 
>>> 
>>> sum([v.verse()+v.chapter() for v in bible])
1171756
>>> sum([v.verse()*v.chapter() for v in bible])
11626744
>>> sum([v.vn()*v.verse()*v.chapter() for v in bible][:120])
304565
>>> b.verse(121)
Genesis 5:15 And Mahalaleel lived sixty and five years, and begat Jared:
>>> 
>>> 
>>> sum([v.vn()*v.verse()*v.chapter() for v in bible])
168968085881
>>> Jude[1].vn()
30674
>>> 31102*22*21
14369124
>>> 
>>> 
>>> fs(_)
[2, 2, 3, 7, 11, 15551]
>>> 
>>> 2**32
4294967296
>>> 31102/299792458
0.00010374510488852925
>>> 31102/66/150
3.1416161616161618
>>> math.pi
3.141592653589793
>>> 31102-29979
1123
>>> 1189-1123
66
>>> math.exp(1)
2.718281828459045
>>> 31102-27183
3919
>>> np(_)
543
>>> 
>>> sum([i*v.chapter()*v.verse() for i,v in enumerate(bible)])
168956459137
>>> sum([i*v.chapter()*v.verse() for i,v in enumerate(bible,start=1)])
168968085881
>>> 
>>> 
