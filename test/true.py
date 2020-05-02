    >>> from bible import *
    >>> tell('truth')
    t  r  u  t  h =
    20 18 21 20 8 87
    >>> tell('true')
    t  r  u  e =
    20 18 21 5 64
    >>> b[64]
    3 John 1:1-14 (14 verses)
    >>> p(_)
    3 John 1
    1 The elder unto the wellbeloved Gaius, whom I love in the truth.
    2 Beloved, I wish above all things that thou mayest prosper and be in health, even as thy soul prospereth.
    3 For I rejoiced greatly, when the brethren came and testified of the truth that is in thee, even as thou walkest in the truth.
    4 I have no greater joy than to hear that my children walk in truth.
    5 Beloved, thou doest faithfully whatsoever thou doest to the brethren, and to strangers;
    6 Which have borne witness of thy charity before the church: whom if thou bring forward on their journey after a godly sort, thou shalt do well:
    7 Because that for his name's sake they went forth, taking nothing of the Gentiles.
    8 We therefore ought to receive such, that we might be fellowhelpers to the truth.
    9 I wrote unto the church: but Diotrephes, who loveth to have the preeminence among them, receiveth us not.
    10 Wherefore, if I come, I will remember his deeds which he doeth, prating against us with malicious words: and not content therewith, neither doth he himself receive the brethren, and forbiddeth them that would, and casteth them out of the church.
    11 Beloved, follow not that which is evil, but that which is good. He that doeth good is of God: but he that doeth evil hath not seen God.
    12 Demetrius hath good report of all men, and of the truth itself: yea, and we also bear record; and ye know that our record is true.
    13 I had many things to write, but I will not with ink and pen write unto thee:
    14 But I trust I shall shortly see thee, and we shall speak face to face. Peace be to thee. Our friends salute thee. Greet the friends by name.
    >>> _.count('truth')
    6
    >>> b.count('truth')
    237
    >>> pf(_)
    Counter({3: 1, 79: 1})
    >>> b.count('true')
    81
    >>> 237+81
    318
    >>> b.count('truly')
    42
    >>> b[64].count('true')
    1
    >>> b.count('tru')
    670
    >>> sorted(set(b.ws()))/meth.startswith('tru')
    ['trucebreakers', 'true', 'truly', 'trump', 'trumpet', 'trumpeters', 'trumpets', 'trust', 'trusted', 'trustedst', 'trustest', 'trusteth', 'trusting', 'trusty', 'truth', "truth's"]
    >>> _**p
    trucebreakers true truly trump trumpet trumpeters trumpets trust trusted trustedst trustest trusteth trusting trusty truth truth's
    >>> _@p
    trucebreakers
    true
    truly
    trump
    trumpet
    trumpeters
    trumpets
    trust
    trusted
    trustedst
    trustest
    trusteth
    trusting
    trusty
    truth
    truth's
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    >>> 
    >>> tell(ssum,'true')
     t  r   u  e  =
    200 90 300 5 595
    >>> 
    >>> 66**2+1
    4357
    >>> np(_)
    595
    >>> sos(pn(595))
    [[(1, 1), (66, 66)]]
    >>> pn(66)
    317
    >>> sos(_)
    [[(11, 11), (14, 14)]]
    >>> pn(37)
    157
    >>> sos(_)
    [[(6, 6), (11, 11)]]
    >>> pn(73)
    367
    >>> sos(_),sos(74)
    ([], [[(5, 5), (7, 7)]])
    >>> sos(77)
    []
    >>> sos(151)
    []
    >>> np(151)
    36
    >>> span(40)@F(pn)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173]
    >>> pn(151)
    877
    >>> pn(36)
    151
    >>> ns(28657)
    [28657] [3121]
    >>> ns(3121)
    [3121] [445]
    >>> ns(445)
    [5, 89] [3, 24]
    >>> pn(pn(5*89))
    28657
    >>> Fn(23)
    28657
    >>> sos(3121)
    [[(39, 39), (40, 40)]]
    >>> 
    >>> 
    >>> Fn(40)
    102334155
    >>> 2**10*10000
    10240000
    >>> Fn(40)**.5
    10116.034549169946
    >>> 10116/32
    316.125
    >>> 5058/16
    316.125
    >>> _**2
    99935.015625
    >>> pi=math.pi
    >>> pi**2
    9.869604401089358
    >>> divmod(9869,49)
    (201, 20)
    >>> 201*49
    9849
    >>> 161*49
    7889
    >>> int('30213',2*3)
    3969
    >>> base(64,3969)
    [62, 1]
    >>> 64**2
    4096
    >>> 4096-3969
    127
    >>> 
    >>> 
    >>> 
    >>> _**2
    16129
    >>> 
    >>> 
    >>> 10000**.5
    100.0
    >>> 
    >>> b.vi(28657)
    1 Corinthians 12:22 Nay, much more those members of the body, which seem to be more feeble, are necessary:
    >>> 
    >>> 28657-23145
    5512
    >>> b.vi(5512)
    Deuteronomy 23:11 But it shall be, when evening cometh on, he shall wash himself with water: and when the sun is down, he shall come into the camp again.
    >>> _.tells()
    But  it shall be, when evening cometh on, he shall wash himself with water: and when the sun  is down, he shall come into the camp again.  =
     3   2    5    2   4      7      6     2  2    5    4      7     4     5     3   4    3   3   2    4   2    5    4    4    3   4     5    104
     43  29   52   7   50     76     64    29 13   52   51     72    60    67    19  50   33  54  28   56  13   52   36   58   33  33    32   1162
    502 209  169   7  563    526    316   110 13  169  609    198   717   796    55 563  213 450 109  614  13  169  108  319  213 114    68   7912
    >>> 
    >>> 
    >>> 
