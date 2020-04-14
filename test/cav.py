    >>> from bible import *
    >>> 715+36
    751
    >>> 
    >>> np(751)
    133
    >>> 
    >>> 
    >>> pf(744)
    Counter({2: 3, 3: 1, 31: 1})
    >>> 
    >>> tell('the son of')
    the son of  =
     33  48 21 102
    >>> 3567-102*12
    2343
    >>> pf(2343)
    Counter({3: 1, 11: 1, 71: 1})
    >>> 33*71
    2343
    >>> 
    >>> sum([(lambda x: x*(x+1)//2)(ch.vc()) for ch in bible.chapters()])
    530083
    >>> pf(530083)
    Counter({113: 1, 4691: 1})
    >>> npf(530083)
    {113: 30, 4691: 634}
    >>> sum([(lambda x,y: x*(x+1)//2+y)(ch.vc(), ch.chapter()) for ch in bible.chapters()])
    557422
    >>> sum([(lambda x,y: x*(x+1)//2-1+y)(ch.vc(), ch.chapter()) for ch in bible.chapters()])
    556233
    >>> p(pf(_))
    Counter({3: 1, 31: 1, 5981: 1})
    >>> npf(_)
    {3: 2, 31: 11, 5981: 782}
    >>> sum([(lambda x,y: x*(x+1)//2+y*x)(ch.vc(), ch.chapter()) for ch in bible.chapters()])
    1171756
    >>> pf(_)
    Counter({2: 2, 197: 1, 1487: 1})
    >>> 
    >>> sum([(lambda x,y: x*(x+1)//2+y*x)(ch.vc(), ch.chapter()) for ch in bible.chapters()])+(1+2)*6+1+2+3
    1171780
    >>> pf(_)
    Counter({2: 2, 5: 1, 41: 1, 1429: 1})
    >>> 
    >>> [book.vc()+1 for book in bible.books() if book.chaptercount()==1]
    [22, 26, 14, 15, 26]
    >>> sum(_)
    103
    >>> 1171780-103
    1171677
Sum of all verse numbers + sum of all chapter numbers (ch*vs)
plus 1 and 2 for Samuel, Kings, Chronicles, Corinthians, Thessalonians, Timothy, Peter
plus 1 2 3 for letters of John
- 1 for chapter number and versecount for chapters of single chapter books.
    >>> sum([(lambda vs,ch: tri(vs)+vs*ch)(ch.vc(), ch.chapter()) for ch in bible.chapters()])+(1+2)*7+1+2+3-sum([book.vc() for book in bible.books() if book.chaptercount()==1])
    1171685
    >>> p(pf(_))
    Counter({5: 1, 89: 1, 2633: 1})
    >>> _-8
    1171677
    >>> pf(_)
    Counter({13: 2, 3: 1, 2311: 1})
    >>> 13**2*3*2311
    1171677
    >>> np(2311)
    344
    >>> np(1123)
    188
    >>> 
    >>> npf(_)
    {2: 1, 47: 15}
    >>> pf(_)
    <console>:1: TypeError: 'dict' object cannot be interpreted as an integer
    /home/pi/python/parle/primes.py:82: TypeError: 'dict' object cannot be interpreted as an integer
        n={2: 1, 47: 15}
    /home/pi/python/parle/primes.py:69: TypeError: 'dict' object cannot be interpreted as an integer
        n={2: 1, 47: 15}
        k={2: 1, 47: 15}
    >>> 
    >>> 
    >>> 
    >>> 
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==1]; p(x,sum(x))
    [22, 26, 14, 15, 26] 103
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==2]; p(x,sum(x))
    [39] 39
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==3]; p(x,sum(x))
    [74, 48, 57, 54, 48, 47, 62] 390
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==4]; p(x,sum(x))
    [86, 49, 56, 105, 96, 84] 476
    >>> pf(476)
    Counter({2: 2, 7: 1, 17: 1})
    >>> 119*4
    476
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==5]; p(x,sum(x))
    [155, 90, 109, 106, 106] 566
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==6]; p(x,sum(x))
    [150, 156, 114] 420
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==7]; p(x,sum(x))
    [106] 106
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==8]; p(x,sum(x))
    [118] 118
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==9]; p(x,sum(x))
    [147] 147
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==10]; p(x,sum(x))
    [281, 168] 449
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==11]; p(x,sum(x))
    [] 0
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==12]; p(x,sum(x))
    [223, 358] 581
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==13]; p(x,sum(x))
    [407, 258, 304] 969
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==14]; p(x,sum(x))
    [198, 212] 410
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==15]; p(x,sum(x))
    [] 0
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==16]; p(x,sum(x))
    [679, 434, 438] 1551
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==17]; p(x,sum(x))
    [] 0
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==18]; p(x,sum(x))
    [] 0
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==19]; p(x,sum(x))
    [] 0
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==20]; p(x,sum(x))
    [] 0
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==21]; p(x,sum(x))
    [619, 880] 1499
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==22]; p(x,sum(x))
    [817, 405] 1222
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==23]; p(x,sum(x))
    [] 0
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==24]; p(x,sum(x))
    [659, 696, 1152] 2507
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==25]; p(x,sum(x))
    [720] 720
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==26]; p(x,sum(x))
    [] 0
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==27]; p(x,sum(x))
    [860] 860
    >>> x=[book.vc()+1 for book in bible.books() if book.chaptercount()==28]; p(x,sum(x))
    [1072, 1008] 2080
    >>> ITimothy
    1 Timothy 1:1-6:21 (113 verses)
    >>> [book.vc() for book in bible.books()]
    [1533, 1213, 859, 1288, 959, 658, 618, 85, 810, 695, 816, 719, 942, 822, 280, 406, 167, 1070, 2461, 915, 222, 117, 1292, 1364, 154, 1273, 357, 197, 73, 146, 21, 48, 105, 47, 56, 53, 38, 211, 55, 1071, 678, 1151, 879, 1007, 433, 437, 257, 149, 155, 104, 95, 89, 47, 113, 83, 46, 25, 303, 108, 105, 61, 105, 13, 14, 25, 404]
    >>> sorted(_)
    [13, 14, 21, 25, 25, 38, 46, 47, 47, 48, 53, 55, 56, 61, 73, 83, 85, 89, 95, 104, 105, 105, 105, 108, 113, 117, 146, 149, 154, 155, 167, 197, 211, 222, 257, 280, 303, 357, 404, 406, 433, 437, 618, 658, 678, 695, 719, 810, 816, 822, 859, 879, 915, 942, 959, 1007, 1070, 1071, 1151, 1213, 1273, 1288, 1292, 1364, 1533, 2461]
    >>> pf(2461)
    Counter({23: 1, 107: 1})
    >>> np(107)
    28
    >>> 
