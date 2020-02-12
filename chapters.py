from auto import *

def portions(l):
    """
    Return iterator of contiguous sublists of l.
        >>> from chapters import *
        >>> list(portions('abcde'))
        ['a', 'ab', 'abc', 'abcd', 'abcde', 'b', 'bc', 'bcd', 'bcde', 'c', 'cd', 'cde', 'd', 'de', 'e']
        >>> 
    """
    return (l[i:j] for i,j in itertools.combinations(range(len(l)+1),2))

def partialsum(l,i,j):
    return sum(l[i:j+1]) if i<=j else ''

def functiontable(f,ra):
    return list(map(f, ra))

def functiontable2(f,ra,rb):
    return [[f(a,b) for b in rb] for a in ra]

def partialsums(l):
    ps=functools.partial(partialsum,l)
    return functiontable2(ps,range(len(l)),range(len(l)))


# >>> from bible import *
# >>> from htmldraw import *
# >>> from chapters import *
# >>> functools.partial(partialsum,[1,1,2,3])
# functools.partial(<function partialsum at 0xb65dc3d8>, [1, 1, 2, 3])
# >>> f=_
# >>> f(1,3)
# 6
# >>> functiontable2(f,range(4),range(4))
# [[1, 2, 4, 7], ['', 1, 3, 6], ['', '', 2, 5], ['', '', '', 3]]
# >>> table(_)
# ['table', ['tr', ['td', 1], ['td', 2], ['td', 4], ['td', 7]], ['tr', ['td', ''], ['td', 1], ['td', 3], ['td', 6]], ['tr', ['td', ''], ['td', ''], ['td', 2], ['td', 5]], ['tr', ['td', ''], ['td', ''], ['td', ''], ['td', 3]]]
# >>> 
## >>> chns=[b.chaptercount() for b in bible.books()]
## >>> t=table([[b.name() for b in bible.books()]]+partialsums(chns))
### >>> show(t)
## >>> bps=[a-b for a,b in itertools.combinations(bible.books(),2)]
## >>> [p for p in bps if p.chc()==100]
## [2 Samuel 1:1-1 Chronicles 29:30 (3172 verses), 2 Kings 1:1-Ezra 10:44 (2763 verses), John 1:1-Galatians 6:18 (3162 verses), Romans 1:1-Hebrews 13:25 (2336 verses)]
## >>> [p for p in bps if p.chc()==200]
## [1 Samuel 1:1-Esther 10:3 (5657 verses), Isaiah 1:1-Joel 3:21 (4710 verses), Lamentations 1:1-Luke 24:53 (5734 verses), Hosea 1:1-Romans 16:27 (6269 verses), Habakkuk 1:1-Ephesians 6:24 (6630 verses), Zechariah 1:1-Colossians 4:18 (6682 verses), Malachi 1:1-1 Timothy 6:21 (6720 verses), Matthew 1:1-2 Timothy 4:22 (6748 verses)]
## >>> [p for p in bps if p.chc()==300]
## [Lamentations 1:1-Galatians 6:18 (8896 verses), Jonah 1:1-Revelation 22:21 (8570 verses)]
## >>> [p for p in bps if p.chc()==400]
## []
## >>> [p for p in bps if p.chc()==500]
## [Ezra 1:1-Nahum 3:19 (10715 verses), Ecclesiastes 1:1-2 Peter 3:18 (13225 verses)]
## >>> [p for p in bps if p.chc()==600]
## [Psalms 1:1-1 Corinthians 16:24 (14861 verses)]
## >>> [p for p in bps if p.chc()==700]
## [Judges 1:1-Haggai 2:23 (16369 verses), Ezra 1:1-Ephesians 6:24 (17345 verses)]
## >>> [p for p in bps if p.chc()==800]
## [Exodus 1:1-Ezekiel 48:35 (20205 verses), 1 Kings 1:1-2 Corinthians 13:14 (20340 verses), 2 Chronicles 1:1-Jude 1:25 (19503 verses)]
## >>> [p for p in bps if p.chc()==900]
## [Genesis 1:1-Micah 7:20 (22685 verses), Judges 1:1-Colossians 4:18 (23051 verses), Ruth 1:1-Titus 3:15 (22811 verses), 2 Samuel 1:1-Jude 1:25 (22675 verses)]
## >>> [p for p in bps if p.chc()==1111]
## [Genesis 1:1-Colossians 4:18 (29561 verses)]
## >>> [p for p in bps if p.chc()==666]
## [1 Kings 1:1-Matthew 28:20 (15498 verses)]
## >>> [p for p in bps if p.chc()==797]
## [Genesis 1:1-Jeremiah 52:34 (20311 verses), 2 Chronicles 1:1-1 John 5:21 (19451 verses)]
## >>> [p for p in bps if p.chc()==117]
## [Genesis 1:1-Leviticus 27:34 (3605 verses), Proverbs 1:1-Isaiah 66:24 (2546 verses), Jeremiah 1:1-Daniel 12:13 (3148 verses), Matthew 1:1-Acts 28:31 (4786 verses)]
## >>> [p for p in bps if p.chc()==1117]
## [Exodus 1:1-Jude 1:25 (29165 verses)]
## >>> [p for p in bps if p.chc()==153]
## [Genesis 1:1-Numbers 36:13 (4893 verses), Micah 1:1-Acts 28:31 (5351 verses), Haggai 1:1-Romans 16:27 (5523 verses), Malachi 1:1-1 Corinthians 16:24 (5711 verses)]
## >>> [p for p in bps if p.chc()==711]
## [2 Chronicles 1:1-1 Corinthians 16:24 (17606 verses), Psalms 1:1-Revelation 22:21 (17162 verses)]
## >>> [p for p in bps if p.chc()==789]
## [Leviticus 1:1-Joel 3:21 (19619 verses), Numbers 1:1-Habakkuk 3:19 (19183 verses), 2 Chronicles 1:1-1 Peter 5:14 (19285 verses)]
## >>> [p for p in bps if p.chc()==251]
## [Proverbs 1:1-Joel 3:21 (5964 verses), Nahum 1:1-James 5:20 (7690 verses)]
## >>> [p for p in bps if p.chc()==346]
## [Leviticus 1:1-Esther 10:3 (10124 verses), 2 Kings 1:1-Proverbs 31:31 (7782 verses), Jeremiah 1:1-2 Corinthians 13:14 (10111 verses)]
## >>> 
# >>> Joel.bookn()
# 29
# >>> James.bookn()
# 59
# >>> 
# >>> 
