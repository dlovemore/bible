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
    >>> sorted(set(b.words()@meth.rstrip(',.:;?)')))/meth.startswith('tru')
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
    >>> 
    >>> 
    >>> 
