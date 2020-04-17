import re
from parle import *
from mene import *
from bisect import bisect_right
from itertools import chain
from word2num import word2num
from func import aslist

def get(l,*xs):
    return [l[x] for x in xs]

def middle(l):
    n=len(l)
    return l[(n-1)//2:n//2+1]

def tekel(l):
    n=len(l)
    return l[(n-2)//3:n//3+1]

def upharsin(l):
    n=len(l)
    return l[n-n//3-1:n-(n-2)//3]

def wc(s): len(s.split(' '))

@aslist
def contranges(ix,a=0,b=None):
    if b is None: b=len(ix)
    if ix[b-1]-ix[a]==b-1-a:
        return [(ix[a],ix[a]-a+b)]
    m=a+(b-a)//2
    r0,r1 = contranges(ix,a,m),contranges(ix,m,b)
    if ix[m-1]==ix[m]-1:
        return r0[:-1]+[(r0[-1][0],r1[0][1])]+r1[1:]
    return r0+r1

class Sel:
    def __init__(self, doc, ix=None):
        if isinstance(doc, Sel):
            self.doc=doc.doc
            self.booknames=doc.booknames
            self.bookix=doc.bookix
            self.chapterix=doc.chapterix
        else:
            self.doc = doc
            self.booknames, self.bookix = [], []
            self.chapterix = []
            obook, och, ov = None, None, 2
            for i, line in enumerate(self.doc):
                book, ch, v, text = line
                if v<=ov:
                    self.chapterix.append(i)
                    if book!=obook:
                        self.booknames.append(book)
                        self.bookix.append(i)
                obook, och, ov, _ = line
            self.booknames = {b:i for i,b in enumerate(self.booknames)}
            self.bookix.append(len(self.doc))
            self.chapterix.append(len(self.doc))
        if ix is None: ix=range(len(self.doc))
        self.ix = ix
    def __eq__(self, other):
        if len(self.ix)!=len(other.ix) or list(self.ix)!=list(other.ix):
            return False
        return all((self.doc[i]==other.doc[i]) for i in self.ix)
    def __lt__(self, other):
        if self.doc==other.doc:
            return tuple(self.ix)<tuple(other.ix)
    def __div__(self, s):
        return Sel(self,[i for i in self.ix if re.search(s,self.doc[i][3])])
    def __truediv__(self, s):
        if isinstance(s, int):
            return Sel(self,[i for i in self.ix if s in word2num(self.doc[i][3])])
        if isinstance(s,Sel):
            other=s
            if self.doc!=other.doc: raise ValueError
            return Sel(self,sorted(set(self.ix).difference(set(other.ix))))
        s=r'\b'+s
        return Sel(self,[i for i in self.ix if re.search(s,self.doc[i][3], flags=re.IGNORECASE)])
    def pattern(self, s):
        return set.union(*[set(re.findall(s,v.v())) for v in self if re.search(s, v.v())])
    def __getattr__(self, name):
        if name in self.booknames:
            i = self.booknames[name]
        else:
            bs = [i for book,i in self.booknames.items() if book.startswith(name)]
            if len(bs)!=1: raise AttributeError('No attribute '+name)
            i=bs[0]
        return Sel(self,range(*self.bookix[i:i+2]))
    def vc(self): return len(self.ix)
    def versecount(self): return self.vc()
    def text(self, i=None,j=None):
        if i is None:
            i,j = 1,self.vc()
        else:
            j=i if j is None else j
        return '\n'.join([self.doc[i][3] for i in self.ix[i-1:j]])
    def verse(self, i=None,j=None):
        if i is None:
            return self.doc[self.ix[0]][2]
        j=i if j is None else j
        return self.vi(i,j)
        return Sel(self, self.ix[i-1:j])
    def verses(self, *l):
        if l:
            return [self.verse(i) for i in l]
        else:
            return [v for v in self]
    def vi(self, i,j=None):
        j=i if j is None else j
        return Sel(self,self.ix[i-1:j])
    def chapter(self, i=None,j=None):
        if i is None:
            return self.doc[self.ix[0]][1]
        if j is None: j=i
        return Sel(self, range(self.chapterix[i-1],self.chapterix[j]))
    def ci(self, i): return self.chapters()[i-1]
    def book(self, b):
        if isinstance(b, int):
            return Sel(self, range(self.bookix[b-1],self.bookix[b]))
        if isinstance(b, str):
            ix=[i for i,name in enumerate(booknames) if name.startswith(b)]
        if len(b)==0: return
        if len(b)==1: return self.book(b[0])
        else:
            return [self.book(i) for i in b]
        return Sel(self, range(*self.bookix[b-1:b+1]))
    def v(self, i=1): return self.doc[self.ix[i-1]][3]
    def vs(self, a=1 ,b=None):
        if b is None: b=self.vc()
        return '\n'.join((self.v(i) for i in range(a,b+1)))
    def midword(self,middle=middle):
        return middle(self.words())
    def midv(self,middle=middle):
        return Sel(self,middle(self.ix))
    def midverse(self,middle=middle):
        return self.midv(middle)
    def midch(self,middle=middle):
        return sum(middle(self.chapters()), Sel(self,[]))
    def midchapter(self,middle=middle):
        return self.midch(middle)
    def letters(self):
        return letters(self.vs())
    def lc(self):
        return sum(self.lcs())
    def lcs(self):
        return [lsum(v.vs()) for v in self]
    def wordcount(self):
        return sum([len(self.doc[i][3].split()) for i in self.ix])
    def wc(self): return self.wordcount()
    def wcs(self):
        return [len(self.doc[i][3].split()) for i in self.ix]
    def chc(self):
        return self.chaptercount()
    def chaptercount(self):
        return len(self.chapters())
    def vn(self):
        return self.ix[0]+1
    def chn(self):
        return bisect_right(self.chapterix, self.ix[0])
    def cav(self):
        return self.doc[self.ix[0]][1:3]
    def chapterandverse(self): return self.cav()
    def bookn(self):
        return bisect_right(self.bookix, self.ix[0])
    def name(self):
        return self.doc[self.ix[0]][0]
    def bookname(self): return self.name()
    def vns(self):
        return [x+1 for x in self.ix]
    def count(self,s=None):
        if isinstance(s, str):
            s=r'\b'+s
            return sum([len(re.findall(s,self.vs(), flags=re.IGNORECASE))])
        if s is None:
            s=count
        return sum([s(v.vs()) for v in self])

    def tell(self,*fs):
        for i in span(self.vc()):
            tell(self.verse(i).vs(),*fs)
    def words(self):
        ws=[]
        for i in self.ix:
            ws+=self.doc[i][3].split()
        return ws
    def __getitem__(self,k):
        if isinstance(k, str):
            return getattr(self,k)
        if isinstance(k, slice):
            ch = k.start
            v = k.stop
            w = k.step or v
            vr = span(v,w)
            return Sel(self, [i for i in self.ix if (ch is None or ch==self.doc[i][1]) and (v is None or self.doc[i][2] in vr)])
        if isinstance(k, int):
            xs = self.books()
            if len(xs)==1:
                xs = self.chapters()
                if len(xs)==1:
                    return self.verse(k)
            return xs[k-1]
        raise IndexError
    def __iter__(self):
        return (self.verse(i) for i in span(self.vc()))
    def __pos__(self): return Sel(self,range(len(self.doc)))
    def __or__(self, other):
        if callable(other):
            return other(self)
        if self.doc!=other.doc: raise ValueError
        return Sel(self,sorted(set(self.ix)|set(other.ix)))
    def __sub__(self, other):
        if isinstance(other, int):
            x=[]
            include = None
            for i in range(len(self.doc)):
                if i in self.ix:
                    include = self.doc[i][:2]
                if self.doc[i][:2]!=include:
                    include = False
                if include:
                    x.append(i)
                if self.doc[i][2]==other:
                    include = False
            return Sel(self,x)
        if isinstance(other, tuple) and len(other)==2:
            x=[]
            include = None
            for i in range(len(self.doc)):
                if i in self.ix:
                    include = self.doc[i][:2]
                if include:
                    x.append(i)
                if tuple(self.doc[i][1:3])==other:
                    include = False
            return Sel(self,x)
        if self.doc!=other.doc: raise ValueError
        a = self.ix[-1]+1 if self.ix else 0
        b = other.ix[0] if other.ix else len(self.doc)-1
        return Sel(self, sorted(set(chain(self.ix,range(a,b),other.ix))))
    def __add__(self, other):
        if self.doc!=other.doc: raise ValueError
        return Sel(self,sorted(list(self.ix)+list(other.ix)))
    def __mul__(self, other):
        if self.doc!=other.doc: raise ValueError
        return Sel(self,sorted(set(self.ix).intersection(set(other.ix))))
    def ref(self):
        s=''
        book,ch,v = None, None, None
        for i,j in contranges(self.ix):
            book1 , ch1, v1, t = self.doc[i]
            book2 , ch2, v2, t = self.doc[j-1]
            if book!=book1:
                if s: s+=';'
                s+=f'{book1} {ch1}:{v1}'
            elif ch!=ch1:
                if s: s+=';'
                s+=f'{ch1}:{v1}'
            else:
                s+=f',{v1}'
            if j-1>i:
                sep='-'
                if book1==book2:
                    if ch1==ch2:
                        if v!=v2:
                            s+=f'{sep}{v2}'
                    else:
                        s+=f'{sep}{ch2}:{v2}'
                else:
                    s+=f'{sep}{book2} {ch2}:{v2}'
            book, ch, v = book2, ch2, v2
        return s

    def divide(self,index):
        i=0
        l=[]
        while i<len(self.ix):
            ci= bisect_right(index, self.ix[i])
            vi= index[ci]
            j = bisect_right(self.ix, vi-1)
            l.append(Sel(self, self.ix[i:j]))
            i=j
        return l
    def chapters(self):
        return self.divide(self.chapterix)
    def books(self):
        return self.divide(self.bookix)
    def __str__(self):
        if self.vc()<=2:
            return '\n'.join([f'{v.bookname()} {v.chapter()}:{v.verse()} {v.text()}' for v in self])
        bs=self.books()
        if len(bs)==1:
            chs=self.chapters()
            if len(chs)==1:
                ch=chs[0]
                return f'{ch.bookname()} {ch.chapter()}\n'+'\n'.join([f'{self.doc[i][2]} {self.doc[i][3]}' for i in ch.ix])
            else:
                return '\n'.join(map(str,chs))
        return '\n'.join(map(str,bs))
    def __repr__(self):
        if self.vc()<=2: return str(self)
        return f'{self.ref()} ({self.vc()} verses)'

def verselist(bible):
    for bi,book in enumerate(bible):
        title = book[1][1]
        for i,chapter in enumerate(book[2:],start=1):
            for j,verse in enumerate(chapter[1:],start=1):
                text = verse[1]
                yield title,i,j,text

# >>> from bible import *
# >>> contranges([0,1,2,3,6,9,10,11,14,22,23,24,25,26,31])
# [(0, 4), (6, 7), (9, 12), (14, 15), (22, 27), (31, 32)]
# >>> 
# >>> 
# >>> Genesis[1:1]
# Genesis 1:1 In the beginning God created the heaven and the earth.
# >>> 
# >>> 
# >>> (Genesis[1:1]-(2,3))
# Genesis 1:1-2:3 (34 verses)
# >>> len(_)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# TypeError: object of type 'Sel' has no len()
# >>> b.chapter(595)
# Psalms 117:1 O praise the LORD, all ye nations: praise him, all ye people.
# Psalms 117:2 For his merciful kindness is great toward us: and the truth of the LORD endureth for ever. Praise ye the LORD.
# >>> Psalm[103].chn()
# 581
# >>> 
# >>> b.James.chapters()
# [James 1:1-27 (27 verses), James 2:1-26 (26 verses), James 3:1-18 (18 verses), James 4:1-17 (17 verses), James 5:1-20 (20 verses)]
# >>> James.name()
# 'James'
# >>> p(Malachi[4]-Matthew[1:10])
# Malachi 4
# 1 For, behold, the day cometh, that shall burn as an oven; and all the proud, yea, and all that do wickedly, shall be stubble: and the day that cometh shall burn them up, saith the LORD of hosts, that it shall leave them neither root nor branch.
# 2 But unto you that fear my name shall the Sun of righteousness arise with healing in his wings; and ye shall go forth, and grow up as calves of the stall.
# 3 And ye shall tread down the wicked; for they shall be ashes under the soles of your feet in the day that I shall do this, saith the LORD of hosts.
# 4 Remember ye the law of Moses my servant, which I commanded unto him in Horeb for all Israel, with the statutes and judgments.
# 5 Behold, I will send you Elijah the prophet before the coming of the great and dreadful day of the LORD:
# 6 And he shall turn the heart of the fathers to the children, and the heart of the children to their fathers, lest I come and smite the earth with a curse.
# Matthew 1
# 1 The book of the generation of Jesus Christ, the son of David, the son of Abraham.
# 2 Abraham begat Isaac; and Isaac begat Jacob; and Jacob begat Judas and his brethren;
# 3 And Judas begat Phares and Zara of Thamar; and Phares begat Esrom; and Esrom begat Aram;
# 4 And Aram begat Aminadab; and Aminadab begat Naasson; and Naasson begat Salmon;
# 5 And Salmon begat Booz of Rachab; and Booz begat Obed of Ruth; and Obed begat Jesse;
# 6 And Jesse begat David the king; and David the king begat Solomon of her that had been the wife of Urias;
# 7 And Solomon begat Roboam; and Roboam begat Abia; and Abia begat Asa;
# 8 And Asa begat Josaphat; and Josaphat begat Joram; and Joram begat Ozias;
# 9 And Ozias begat Joatham; and Joatham begat Achaz; and Achaz begat Ezekias;
# 10 And Ezekias begat Manasses; and Manasses begat Amon; and Amon begat Josias;
# >>> 
# >>> tekel([1,2,3,4,5,6,7,8,9,10,11,12])
# [4, 5]
# >>> tekel([1,2,3,4,5,6,7,8,9,10,11,12,13])
# [4, 5]
# >>> tekel([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
# [5]
# >>> upharsin([1,2,3,4,5,6,7,8,9,10,11,12])
# [8, 9]
# >>> upharsin([1,2,3,4,5,6,7,8,9,10,11,12,13])
# [9, 10]
# >>> upharsin([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
# [10]
# >>> 
# >>> middle([1,2,3])
# [2]
# >>> middle([1,2,3,4])
# [2, 3]
# >>> middle([])
# []
# >>> 
# >>> 
# >>> b.Ps[119].wc()
# 2423
# >>> b.Gen[1].wc()
# 797
# >>> b.Rev[1].wc()
# 592
# >>> b.Gen.wc()
# 38264
# >>> b.Ps[117].wc()
# 33
# >>> b.Ps[118].wc()
# 465
# >>> b.Ps[119].wc()
# 2423
# >>> b.Rev[22:21]
# Revelation 22:21 The grace of our Lord Jesus Christ be with you all. Amen.
# >>> b.Gen[1][1]
# Genesis 1:1 In the beginning God created the heaven and the earth.
# >>> 
# >>> b.Rev[22].wc()
# 573
# >>> len(b.Gen.words())
# 38264
# >>> 
# >>> 629-406
# 223
# >>> len((Genesis[1]-(2,3)).words())
# 864
# >>> Genesis[1].wc()
# 797
# >>> b.vc()
# 31102
# >>> 
# >>> b.wc()
# 789629
# >>> _/2
# 394814.5
# >>> b.words()[394810:394820]
# ['in', 'wait', 'for', 'my', 'soul:', 'the', 'mighty', 'are', 'gathered', 'against']
# >>> b.midword()
# ['soul:']
# >>> 
# >>> (Genesis[1:1]-(2,3))
# Genesis 1:1-2:3 (34 verses)
# >>> p(_.wc())
# 864
# >>> p(_.midword())
# ['may', 'fly']
# >>> Genesis[1:20]
# Genesis 1:20 And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl that may fly above the earth in the open firmament of heaven.
# >>> 
# >>> b['2 Corinthians']/"mighty"/"strong holds"
# 2 Corinthians 10:4 (For the weapons of our warfare are not carnal, but mighty through God to the pulling down of strong holds;)
# >>> 
# >>> 
# >>> b.doc[0]
# ('Genesis', 1, 1, 'In the beginning God created the heaven and the earth.')
# >>> b
# Genesis 1:1-Revelation 22:21 (31102 verses)
# >>> 
# >>> b.Gen
# Genesis 1:1-50:26 (1533 verses)
# >>> b.Jude
# Jude 1:1-25 (25 verses)
# >>> p(b.doc[31102//2-1:31102//2+1])
# [('Psalms', 103, 1, 'Bless the LORD, O my soul: and all that is within me, bless his holy name.'), ('Psalms', 103, 2, 'Bless the LORD, O my soul, and forget not all his benefits:')]
# >>> b.midv()
# Psalms 103:1 Bless the LORD, O my soul: and all that is within me, bless his holy name.
# Psalms 103:2 Bless the LORD, O my soul, and forget not all his benefits:
# >>> Psalm[103].bookn()
# 19
# >>> Psalm[103].chn()
# 581
# >>> Psalm[103].vn()
# 15551
# >>> Psalm[118:8].bookname()
# 'Psalms'
# >>> Psalm[1:1].bookname()
# 'Psalms'
# >>> Job[42:17].bookname()
# 'Job'
# >>> 
# >>> 
# >>> Psalm[118:8].chapter()
# 118
# >>> Psalm[118:8].verse()
# 8
# >>> Psalm[118:8].cav()
# (118, 8)
# >>> Psalm[118].ref()
# 'Psalms 118:1-29'
# >>> b.wc()
# 789629
# >>> 789629/31102
# 25.388367307568647
# >>> pf(789629)
# Counter({311: 1, 2539: 1})
# >>> 595-539
# 56
# >>> b[20].chn()
# 629
# >>> b[18][29]
# Job 29:1-25 (25 verses)
# >>> ot=Genesis-Malachi
# >>> ot.midch()
# Job 29:1-25 (25 verses)
# >>> ot.midv()
# 2 Chronicles 18:30 Now the king of Syria had commanded the captains of the chariots that were with him, saying, Fight ye not with small or great, save only with the king of Israel.
# >>> Genesis.midword()
# ['to', 'Padanaram']
# >>> sums(' '.join(_))
# (104, 518)
# >>> Genesis/'to Padanaram'
# Genesis 28:2,5-7 (4 verses)
# >>> p(_)
# Genesis 28
# 2 Arise, go to Padanaram, to the house of Bethuel thy mother's father; and take thee a wife from thence of the daughers of Laban thy mother's brother.
# 5 And Isaac sent away Jacob: and he went to Padanaram unto Laban, son of Bethuel the Syrian, the brother of Rebekah, Jacob's and Esau's mother.
# 6 When Esau saw that Isaac had blessed Jacob, and sent him away to Padanaram, to take him a wife from thence; and that as he blessed him he gave him a charge, saying, Thou shalt not take a wife of the daughers of Canaan;
# 7 And that Jacob obeyed his father and his mother, and was gone to Padanaram;
# >>> Genesis.wc()
# 38264
# >>> _//2
# 19132
# >>> Genesis.words()[19131:19140]
# ['to', 'Padanaram', 'unto', 'Laban,', 'son', 'of', 'Bethuel', 'the', 'Syrian,']
# >>> Genesis.midword()
# ['to', 'Padanaram']
# >>> 
# >>> tell('to Padanaram')
# to Padanaram
# 35+    69   =104
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 811/7
# 115.85714285714286
# >>> g1w=b.Gen[1].words()
# >>> r22w=b.Rev[22].words()
# >>> len(g1w)
# 797
# >>> len(set(g1w))
# 198
# >>> set([letters(w) for w in g1w])
# {'were', 'sea', 'void', 'created', 'seasons', 'likeness', 'gathering', 'deep', 'earth', 'that', 'winged', 'and', 'land', 'meat', 'wherein', 'blessed', 'it', 'beast', 'fourth', 'creepeth', 'fish', 'have', 'under', 'he', 'subdue', 'behold', 'thing', 'beginning', 'one', 'air', 'in', 'years', 'great', 'above', 'fruit', 'divide', 'appear', 'bring', 'grass', 'man', 'first', 'two', 'evening', 'make', 'unto', 'fill', 'from', 'which', 'signs', 'given', 'brought', 'a', 'made', 'is', 'rule', 'place', 'you', 'hath', 'heaven', 'darkness', 'image', 'i', 'divided', 'kind', 'be', 'days', 'us', 'abundantly', 'multiply', 'third', 'midst', 'all', 'yielding', 'saying', 'tree', 'saw', 'open', 'shall', 'moveth', 'second', 'without', 'fowl', 'called', 'forth', 'seed', 'firmament', 'living', 'set', 'sixth', 'every', 'moved', 'of', 'seas', 'had', 'god', 'greater', 'cattle', 'spirit', 'said', 'life', 'fruitful', 'over', 'upon', 'night', 'replenish', 'lesser', 'to', 'moving', 'their', 'give', 'also', 'may', 'very', 'bearing', 'dominion', 'together', 'whose', 'day', 'gathered', 'his', 'female', 'green', 'let', 'so', 'creeping', 'after', 'creature', 'male', 'herb', 'dry', 'morning', 'there', 'fly', 'was', 'fifth', 'light', 'good', 'the', 'waters', 'face', 'form', 'itself', 'them', 'own', 'him', 'stars', 'lights', 'whales', 'our', 'for'}
# >>> len(_)
# 150
# >>> pf(12691)
# Counter({7: 3, 37: 1})
# >>> 7**3*37
# 12691
# >>> b.verse(12691)
# Nehemiah 13:19 And it came to pass, that when the gates of Jerusalem began to be dark before the sabbath, I commanded that the gates should be shut, and charged that they should not be opened till after the sabbath: and some of my servants set I at the gates, that there should no burden be brought in on the sabbath day.
# >>> 
# >>> len([w for w in g1w if re.match(r'[bcdfghjklmnpqrstvwxyz]',w,re.I)])
# 546
# >>> len([w for w in g1w if re.match(r'[aeiou]',w,re.I)])
# 251
# >>> len(r22w)
# 573
# >>> len([w for w in r22w if re.match(r'[aeiou]',w,re.I)])
# 172
# >>> 573-172
# 401
# >>> 22*8
# 176
# >>> b.chc()
# 1189
# >>> 1*33*33+3*33+1
# 1189
# >>> base(33,1189)
# [1, 3, 1]
# >>> base(2,31)
# [1, 1, 1, 1, 1]
# >>> base(5,31)
# [1, 1, 1]
# >>> base(2, 7)
# [1, 1, 1]
# >>> base(33,15551)
# [14, 9, 8]
# >>> base(28,15551)
# [19, 23, 11]
# >>> 
# >>> 19*28*28+23*28+11
# 15551
# >>> 9*12*12*12
# 15552
# >>> 3*3*3*3*3*4*4*4
# 15552
# >>> 2**6*3**5
# 15552
# >>> [ch for ch in b.chapters() if ch.wc()==343]
# []
# >>> [ch for ch in b.chapters() if ch.wc()==311]
# [Psalms 17:1-15 (15 verses), Hosea 12:1-14 (14 verses)]
# >>> [(x.chn(),x.vn()) for x in _]
# [(495, 14105), (874, 22254)]
# >>> 
# >>> 
# >>> 
# >>> [ch for ch in b.chapters() if ch.wc()==839]
# [1 Kings 10:1-29 (29 verses)]
# >>> p(_[0])
# 1 Kings 10
# 1 And when the queen of Sheba heard of the fame of Solomon concerning the name of the LORD, she came to prove him with hard questions.
# 2 And she came to Jerusalem with a very great train, with camels that bare spices, and very much gold, and precious stones: and when she was come to Solomon, she communed with him of all that was in her heart.
# 3 And Solomon told her all her questions: there was not any thing hid from the king, which he told her not.
# 4 And when the queen of Sheba had seen all Solomon's wisdom, and the house that he had built,
# 5 And the meat of his table, and the sitting of his servants, and the attendance of his ministers, and their apparel, and his cupbearers, and his ascent by which he went up unto the house of the LORD; there was no more spirit in her.
# 6 And she said to the king, It was a true report that I heard in mine own land of thy acts and of thy wisdom.
# 7 Howbeit I believed not the words, until I came, and mine eyes had seen it: and, behold, the half was not told me: thy wisdom and prosperity exceedeth the fame which I heard.
# 8 Happy are thy men, happy are these thy servants, which stand continually before thee, and that hear thy wisdom.
# 9 Blessed be the LORD thy God, which delighted in thee, to set thee on the throne of Israel: because the LORD loved Israel for ever, therefore made he thee king, to do judgment and justice.
# 10 And she gave the king an hundred and twenty talents of gold, and of spices very great store, and precious stones: there came no more such abundance of spices as these which the queen of Sheba gave to king Solomon.
# 11 And the navy also of Hiram, that brought gold from Ophir, brought in from Ophir great plenty of almug trees, and precious stones.
# 12 And the king made of the almug trees pillars for the house of the LORD, and for the king's house, harps also and psalteries for singers: there came no such almug trees, nor were seen unto this day.
# 13 And king Solomon gave unto the queen of Sheba all her desire, whatsoever she asked, beside that which Solomon gave her of his royal bounty. So she turned and went to her own country, she and her servants.
# 14 Now the weight of gold that came to Solomon in one year was six hundred threescore and six talents of gold,
# 15 Beside that he had of the merchantmen, and of the traffick of the spice merchants, and of all the kings of Arabia, and of the governors of the country.
# 16 And king Solomon made two hundred targets of beaten gold: six hundred shekels of gold went to one target.
# 17 And he made three hundred shields of beaten gold; three pound of gold went to one shield: and the king put them in the house of the forest of Lebanon.
# 18 Moreover the king made a great throne of ivory, and overlaid it with the best gold.
# 19 The throne had six steps, and the top of the throne was round behind: and there were stays on either side on the place of the seat, and two lions stood beside the stays.
# 20 And twelve lions stood there on the one side and on the other upon the six steps: there was not the like made in any kingdom.
# 21 And all king Solomon's drinking vessels were of gold, and all the vessels of the house of the forest of Lebanon were of pure gold; none were of silver: it was nothing accounted of in the days of Solomon.
# 22 For the king had at sea a navy of Tharshish with the navy of Hiram: once in three years came the navy of Tharshish, bringing gold, and silver, ivory, and apes, and peacocks.
# 23 So king Solomon exceeded all the kings of the earth for riches and for wisdom.
# 24 And all the earth sought to Solomon, to hear his wisdom, which God had put in his heart.
# 25 And they brought every man his present, vessels of silver, and vessels of gold, and garments, and armour, and spices, horses, and mules, a rate year by year.
# 26 And Solomon gathered together chariots and horsemen: and he had a thousand and four hundred chariots, and twelve thousand horsemen, whom he bestowed in the cities for chariots, and with the king at Jerusalem.
# 27 And the king made silver to be in Jerusalem as stones, and cedars made he to be as the sycomore trees that are in the vale, for abundance.
# 28 And Solomon had horses brought out of Egypt, and linen yarn: the king's merchants received the linen yarn at a price.
# 29 And a chariot came up and went out of Egypt for six hundred shekels of silver, and an horse for an hundred and fifty: and so for all the kings of the Hittites, and for the kings of Syria, did they bring them out by their means.
# >>> 
# >>> 
# >>> import math
# >>> math.pi
# 3.141592653589793
# >>> 1/7
# 0.14285714285714285
# >>> 100/7*33*33*2
# 31114.285714285714
# >>> 1189/7
# 169.85714285714286
# >>> 15551-14*33*33-9*33-8
# 0
# >>> 66*33-7*311
# 1
# >>> 1260-33*33-33*5
# 6
# >>> 1*33*33+5*33+5+1
# 1260
# >>> b.Gen[22:2].vn()
# 550
# >>> b.Gen[22:2].chn()
# 22
# >>> b.Gen[1:31].chn()
# 1
# >>> b.Gen[1:1].chn()
# 1
# >>> b.Ecc[7:27]
# Ecclesiastes 7:27 Behold, this have I found, saith the preacher, counting one by one, to find out the account:
# >>> _.chn(),_.tell()
# Behold, this have I found, saith the preacher, counting one by one, to find out the account:
#    46  + 56 + 36 +9+  60  +  57 + 33+    74   +  103   + 34+27+ 34 +35+ 33 + 56+ 33+   77   =803
# (666, None)
# >>> 
# >>> 33*33/7
# 155.57142857142858
# >>> b.Gen
# Genesis 1:1-50:26 (1533 verses)
# >>> b.Rev
# Revelation 1:1-22:21 (404 verses)
# >>> base(6,15551)
# [1, 5, 5, 5, 5, 5]
# >>> sof(31102)
# 46656
# >>> b.Mark[1:29]-45
# Mark 1:29-45 (17 verses)
# >>> p(_)
# Mark 1
# 29 And forthwith, when they were come out of the synagogue, they entered into the house of Simon and Andrew, with James and John.
# 30 But Simon's wife's mother lay sick of a fever, and anon they tell him of her.
# 31 And he came and took her by the hand, and lifted her up; and immediately the fever left her, and she ministered unto them.
# 32 And at even, when the sun did set, they brought unto him all that were diseased, and them that were possessed with devils.
# 33 And all the city was gathered together at the door.
# 34 And he healed many that were sick of divers diseases, and cast out many devils; and suffered not the devils to speak, because they knew him.
# 35 And in the morning, rising up a great while before day, he went out, and departed into a solitary place, and there prayed.
# 36 And Simon and they that were with him followed after him.
# 37 And when they had found him, they said unto him, All men seek for thee.
# 38 And he said unto them, Let us go into the next towns, that I may preach there also: for therefore came I forth.
# 39 And he preached in their synagogues throughout all Galilee, and cast out devils.
# 40 And there came a leper to him, beseeching him, and kneeling down to him, and saying unto him, If thou wilt, thou canst make me clean.
# 41 And Jesus, moved with compassion, put forth his hand, and touched him, and saith unto him, I will; be thou clean.
# 42 And as soon as he had spoken, immediately the leprosy departed from him, and he was cleansed.
# 43 And he straitly charged him, and forthwith sent him away;
# 44 And saith unto him, See thou say nothing to any man: but go thy way, shew thyself to the priest, and offer for thy cleansing those things which Moses commanded, for a testimony unto them.
# 45 But he went out, and began to publish it much, and to blaze abroad the matter, insomuch that Jesus could no more openly enter into the city, but was without in desert places: and they came to him from every quarter.
# >>> b.Jer[33:3]
# Jeremiah 33:3 Call unto me, and I will answer thee, and shew thee great and mighty things, which thou knowest not.
# >>> b/"trusteth in him"
# Psalms 34:8 O taste and see that the LORD is good: blessed is the man that trusteth in him.
# >>> 
# >>> b/777
# Genesis 5:31 And all the days of Lamech were seven hundred seventy and seven years: and he died.
# >>> b/60
# Genesis 25:26;Leviticus 27:3,7;Numbers 7:88;Deuteronomy 3:4;Joshua 13:30;1 Kings 4:13,22;6:2;2 Kings 25:19;1 Chronicles 2:21,23;2 Chronicles 3:3;11:21;Ezra 6:3;8:13;Psalms 90:10;Song of Solomon 3:7;6:8;Jeremiah 52:25;Ezekiel 40:14;Daniel 3:1;Matthew 13:23;Mark 4:8,20;Luke 24:13;1 Timothy 5:9 (27 verses)
# >>> b/666
# 1 Kings 10:14;2 Chronicles 9:13;Ezra 2:13;Revelation 13:18 (4 verses)
# >>> b/'Here is wisdom'
# Revelation 13:18 Here is wisdom. Let him that hath understanding count the number of the beast: for it is the number of a man; and his number is Six hundred threescore and six.
# >>> 
# >>> 
# >>> b/"worshipped"/"creature"
# Romans 1:25 Who changed the truth of God into a lie, and worshipped and served the creature more than the Creator, who is blessed for ever. Amen.
# >>> b/"Gibeon"+b/"Rahab"
# Joshua 2:1,3;6:17,23,25;9:3,17;10:1-2,4-6,10,12,41;11:19;18:25;21:17;2 Samuel 2:12-13,16,24;3:30;20:8;21:1-4,9;1 Kings 3:4-5;9:2;1 Chronicles 8:29;9:35;12:4;14:16;16:39;21:29;2 Chronicles 1:3,13;Nehemiah 3:7;7:25;Psalms 87:4;89:10;Isaiah 28:21;51:9;Jeremiah 28:1;41:12,16;Hebrews 11:31;James 2:25 (51 verses)
# >>> p(_)
# Joshua 2:1 And Joshua the son of Nun sent out of Shittim two men to spy secretly, saying, Go view the land, even Jericho. And they went, and came into an harlot's house, named Rahab, and lodged there.
# Joshua 2:3 And the king of Jericho sent unto Rahab, saying, Bring forth the men that are come to thee, which are entered into thine house: for they be come to search out all the country.
# Joshua 6
# 17 And the city shall be accursed, even it, and all that are therein, to the LORD: only Rahab the harlot shall live, she and all that are with her in the house, because she hid the messengers that we sent.
# 23 And the young men that were spies went in, and brought out Rahab, and her father, and her mother, and her brethren, and all that she had; and they brought out all her kindred, and left them without the camp of Israel.
# 25 And Joshua saved Rahab the harlot alive, and her father's household, and all that she had; and she dwelleth in Israel even unto this day; because she hid the messengers, which Joshua sent to spy out Jericho.
# Joshua 9:3 And when the inhabitants of Gibeon heard what Joshua had done unto Jericho and to Ai,
# Joshua 9:17 And the children of Israel journeyed, and came unto their cities on the third day. Now their cities were Gibeon, and Chephirah, and Beeroth, and Kirjathjearim.
# Joshua 10
# 1 Now it came to pass, when Adonizedec king of Jerusalem had heard how Joshua had taken Ai, and had utterly destroyed it; as he had done to Jericho and her king, so he had done to Ai and her king; and how the inhabitants of Gibeon had made peace with Israel, and were among them;
# 2 That they feared greatly, because Gibeon was a great city, as one of the royal cities, and because it was greater than Ai, and all the men thereof were mighty.
# 4 Come up unto me, and help me, that we may smite Gibeon: for it hath made peace with Joshua and with the children of Israel.
# 5 Therefore the five kings of the Amorites, the king of Jerusalem, the king of Hebron, the king of Jarmuth, the king of Lachish, the king of Eglon, gathered themselves together, and went up, they and all their hosts, and encamped before Gibeon, and made war against it.
# 6 And the men of Gibeon sent unto Joshua to the camp to Gilgal, saying, Slack not thy hand from thy servants; come up to us quickly, and save us, and help us: for all the kings of the Amorites that dwell in the mountains are gathered together against us.
# 10 And the LORD discomfited them before Israel, and slew them with a great slaughter at Gibeon, and chased them along the way that goeth up to Bethhoron, and smote them to Azekah, and unto Makkedah.
# 12 Then spake Joshua to the LORD in the day when the LORD delivered up the Amorites before the children of Israel, and he said in the sight of Israel, Sun, stand thou still upon Gibeon; and thou, Moon, in the valley of Ajalon.
# 41 And Joshua smote them from Kadeshbarnea even unto Gaza, and all the country of Goshen, even unto Gibeon.
# Joshua 11:19 There was not a city that made peace with the children of Israel, save the Hivites the inhabitants of Gibeon: all other they took in battle.
# Joshua 18:25 Gibeon, and Ramah, and Beeroth,
# Joshua 21:17 And out of the tribe of Benjamin, Gibeon with her suburbs, Geba with her suburbs,
# 2 Samuel 2
# 12 And Abner the son of Ner, and the servants of Ishbosheth the son of Saul, went out from Mahanaim to Gibeon.
# 13 And Joab the son of Zeruiah, and the servants of David, went out, and met together by the pool of Gibeon: and they sat down, the one on the one side of the pool, and the other on the other side of the pool.
# 16 And they caught every one his fellow by the head, and thrust his sword in his fellow's side; so they fell down together: wherefore that place was called Helkathhazzurim, which is in Gibeon.
# 24 Joab also and Abishai pursued after Abner: and the sun went down when they were come to the hill of Ammah, that lieth before Giah by the way of the wilderness of Gibeon.
# 2 Samuel 3:30 So Joab, and Abishai his brother slew Abner, because he had slain their brother Asahel at Gibeon in the battle.
# 2 Samuel 20:8 When they were at the great stone which is in Gibeon, Amasa went before them. And Joab's garment that he had put on was girded unto him, and upon it a girdle with a sword fastened upon his loins in the sheath thereof; and as he went forth it fell out.
# 2 Samuel 21
# 1 Then there was a famine in the days of David three years, year after year; and David enquired of the LORD. And the LORD answered, It is for Saul, and for his bloody house, because he slew the Gibeonites.
# 2 And the king called the Gibeonites, and said unto them; (now the Gibeonites were not of the children of Israel, but of the remnant of the Amorites; and the children of Israel had sworn unto them: and Saul sought to slay them in his zeal to the children of Israel and Judah.)
# 3 Wherefore David said unto the Gibeonites, What shall I do for you? and wherewith shall I make the atonement, that ye may bless the inheritance of the LORD?
# 4 And the Gibeonites said unto him, We will have no silver nor gold of Saul, nor of his house; neither for us shalt thou kill any man in Israel. And he said, What ye shall say, that will I do for you.
# 9 And he delivered them into the hands of the Gibeonites, and they hanged them in the hill before the LORD: and they fell all seven together, and were put to death in the days of harvest, in the first days, in the beginning of barley harvest.
# 1 Kings 3:4 And the king went to Gibeon to sacrifice there; for that was the great high place: a thousand burnt offerings did Solomon offer upon that altar.
# 1 Kings 3:5 In Gibeon the LORD appeared to Solomon in a dream by night: and God said, Ask what I shall give thee.
# 1 Kings 9:2 That the LORD appeared to Solomon the second time, as he had appeared unto him at Gibeon.
# 1 Chronicles 8:29 And at Gibeon dwelt the father of Gibeon; whose wife's name was Maachah:
# 1 Chronicles 9:35 And in Gibeon dwelt the father of Gibeon, Jehiel, whose wife's name was Maachah:
# 1 Chronicles 12:4 And Ismaiah the Gibeonite, a mighty man among the thirty, and over the thirty; and Jeremiah, and Jahaziel, and Johanan, and Josabad the Gederathite,
# 1 Chronicles 14:16 David therefore did as God commanded him: and they smote the host of the Philistines from Gibeon even to Gazer.
# 1 Chronicles 16:39 And Zadok the priest, and his brethren the priests, before the tabernacle of the LORD in the high place that was at Gibeon,
# 1 Chronicles 21:29 For the tabernacle of the LORD, which Moses made in the wilderness, and the altar of the burnt offering, were at that season in the high place at Gibeon.
# 2 Chronicles 1:3 So Solomon, and all the congregation with him, went to the high place that was at Gibeon; for there was the tabernacle of the congregation of God, which Moses the servant of the LORD had made in the wilderness.
# 2 Chronicles 1:13 Then Solomon came from his journey to the high place that was at Gibeon to Jerusalem, from before the tabernacle of the congregation, and reigned over Israel.
# Nehemiah 3:7 And next unto them repaired Melatiah the Gibeonite, and Jadon the Meronothite, the men of Gibeon, and of Mizpah, unto the throne of the governor on this side the river.
# Nehemiah 7:25 The children of Gibeon, ninety and five.
# Psalms 87:4 I will make mention of Rahab and Babylon to them that know me: behold Philistia, and Tyre, with Ethiopia; this man was born there.
# Psalms 89:10 Thou hast broken Rahab in pieces, as one that is slain; thou hast scattered thine enemies with thy strong arm.
# Isaiah 28:21 For the LORD shall rise up as in mount Perazim, he shall be wroth as in the valley of Gibeon, that he may do his work, his strange work; and bring to pass his act, his strange act.
# Isaiah 51:9 Awake, awake, put on strength, O arm of the LORD; awake, as in the ancient days, in the generations of old. Art thou not it that hath cut Rahab, and wounded the dragon?
# Jeremiah 28:1 And it came to pass the same year, in the beginning of the reign of Zedekiah king of Judah, in the fourth year, and in the fifth month, that Hananiah the son of Azur the prophet, which was of Gibeon, spake unto me in the house of the LORD, in the presence of the priests and of all the people, saying,
# Jeremiah 41:12 Then they took all the men, and went to fight with Ishmael the son of Nethaniah, and found him by the great waters that are in Gibeon.
# Jeremiah 41:16 Then took Johanan the son of Kareah, and all the captains of the forces that were with him, all the remnant of the people whom he had recovered from Ishmael the son of Nethaniah, from Mizpah, after that he had slain Gedaliah the son of Ahikam, even mighty men of war, and the women, and the children, and the eunuchs, whom he had brought again from Gibeon:
# Hebrews 11:31 By faith the harlot Rahab perished not with them that believed not, when she had received the spies with peace.
# James 2:25 Likewise also was not Rahab the harlot justified by works, when she had received the messengers, and had sent them out another way?
# >>> 
# >>> base(3,31), base(3, 797)
# ([1, 0, 1, 1], [1, 0, 0, 2, 1, 1, 2])
# >>> 
# >>> cwc=[ch.wc for ch in b.chapters()]
# >>> pps=[2, 3, 5, 7, 11, 101, 131, 151, 181, 191, 313, 353, 373, 383, 727, 757, 787, 797, 919, 929, 10301, 10501, 10601, 11311, 11411, 12421, 12721, 12821, 13331, 13831, 13931, 14341, 14741, 15451, 15551]
# >>> ppc=[ch for ch in b.chapters() if ch.wc() in pps]
# >>> [ch.wc() for ch in ppc]
# [797, 919, 757, 373, 313, 101, 353, 151, 919, 727, 919, 373, 353, 353]
# >>> Sel(b.doc,[c.ix[0] for c in ppc])
# Genesis 1:1;Leviticus 15:1;2 Chronicles 31:1;Job 27:1;Psalms 86:1;128:1;136:1;142:1;Ezekiel 18:1;26:1;Matthew 10:1;1 Corinthians 2:1;Galatians 6:1;Revelation 10:1 (14 verses)
# >>> p(_)
# Genesis 1:1 In the beginning God created the heaven and the earth.
# Leviticus 15:1 And the LORD spake unto Moses and to Aaron, saying,
# 2 Chronicles 31:1 Now when all this was finished, all Israel that were present went out to the cities of Judah, and brake the images in pieces, and cut down the groves, and threw down the high places and the altars out of all Judah and Benjamin, in Ephraim also and Manasseh, until they had utterly destroyed them all. Then all the children of Israel returned, every man to his possession, into their own cities.
# Job 27:1 Moreover Job continued his parable, and said,
# Psalms 86:1 Bow down thine ear, O LORD, hear me: for I am poor and needy.
# Psalms 128:1 Blessed is every one that feareth the LORD; that walketh in his ways.
# Psalms 136:1 O give thanks unto the LORD; for he is good: for his mercy endureth for ever.
# Psalms 142:1 I cried unto the LORD with my voice; with my voice unto the LORD did I make my supplication.
# Ezekiel 18:1 The word of the LORD came unto me again, saying,
# Ezekiel 26:1 And it came to pass in the eleventh year, in the first day of the month, that the word of the LORD came unto me, saying,
# Matthew 10:1 And when he had called unto him his twelve disciples, he gave them power against unclean spirits, to cast them out, and to heal all manner of sickness and all manner of disease.
# 1 Corinthians 2:1 And I, brethren, when I came to you, came not with excellency of speech or of wisdom, declaring unto you the testimony of God.
# Galatians 6:1 Brethren, if a man be overtaken in a fault, ye which are spiritual, restore such an one in the spirit of meekness; considering thyself, lest thou also be tempted.
# Revelation 10:1 And I saw another mighty angel come down from heaven, clothed with a cloud: and a rainbow was upon his head, and his face was as it were the sun, and his feet as pillars of fire:
# >>> 
# >>> [ch for ch in b.chapters() if ch.wc() == 797]
# [Genesis 1:1-31 (31 verses)]
# >>> b.Rev[22].wc()
# 573
# >>> base(21, 573)
# [1, 6, 6]
# >>> b.Gen[1].wc()
# 797
# >>> b/r"Bless\b"
# Genesis 12:2-3;17:16;22:17;26:3,24;27:4,7,10,19,25,31,34,38;28:3;32:26;48:9,16,20;49:25;Exodus 12:32;20:24;23:25;Numbers 6:23-24,27;23:20,25;24:1;Deuteronomy 1:11;7:13;8:10;10:8;14:29;15:4,10,18;16:15;21:5;23:20;24:13,19;26:15;27:12;28:8,12;29:19;30:16;33:11;Joshua 8:33;Judges 5:9;Ruth 2:4;1 Samuel 9:13;2 Samuel 6:20;7:29;8:10;21:3;1 Kings 1:47;1 Chronicles 4:10;16:43;17:27;23:13;29:20;Nehemiah 9:5;Psalms 5:12;16:7;26:12;28:9;29:11;34:1;62:4;63:4;66:8;67:1,6-7;68:26;96:2;100:4;103:1-2,20-104:1,35;109:28;115:12-13,18;128:5;129:8;132:15;134:1-3;135:19-20;145:1-2,10,21;Proverbs 30:11;Isaiah 19:25;65:16;Jeremiah 4:2;31:23;Haggai 2:19;Matthew 5:44;Luke 6:28;Acts 3:26;Romans 12:14;1 Corinthians 4:12;10:16;14:16;Hebrews 6:14;James 3:9 (117 verses)
# >>> b/'O my soul'
# Genesis 49:6;Judges 5:21;Psalms 16:2;42:5,11;43:5;103:1-2,22-104:1,35;116:7;146:1;Jeremiah 4:19 (14 verses)
# >>> 
# >>> 
# >>> len(_)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# TypeError: object of type 'Sel' has no len()
# >>> 
# >>> b/'abraham'/'ewe'
# Genesis 21:28 And Abraham set seven ewe lambs of the flock by themselves.
# Genesis 21:29 And Abimelech said unto Abraham, What mean these seven ewe lambs which thou hast set by themselves?
# >>> 
# >>> b.Gen[1:1].wc()+b.Gen[1:31].wc()
# 35
# >>> b.Rev[22:1].wc(),b.Rev[22:21].wc()
# (25, 12)
# >>> p(b/"any thing too hard")
# Genesis 18:14 Is any thing too hard for the LORD? At the time appointed I will return unto thee, according to the time of life, and Sarah shall have a son.
# Jeremiah 32:27 Behold, I am the LORD, the God of all flesh: is there any thing too hard for me?
# >>> Sel(b.doc,[x-1 for x in [10301,10501,10601,11311,11411,12421,12721,12821,13331,13831,13931,14341,14741,15451,15551]])
# 1 Chronicles 1:48;6:46;8:25;2 Chronicles 6:28;10:15;Nehemiah 6:19;Esther 1:18;8:3;Job 20:4;38:37;42:8;Psalms 31:9;55:8;94:19;103:1 (15 verses)
# >>> p(_)
# 1 Chronicles 1:48 And when Samlah was dead, Shaul of Rehoboth by the river reigned in his stead.
# 1 Chronicles 6:46 The son of Amzi, the son of Bani, the son of Shamer,
# 1 Chronicles 8:25 And Iphedeiah, and Penuel, the sons of Shashak;
# 2 Chronicles 6:28 If there be dearth in the land, if there be pestilence, if there be blasting, or mildew, locusts, or caterpillers; if their enemies besiege them in the cities of their land; whatsoever sore or whatsoever sickness there be:
# 2 Chronicles 10:15 So the king hearkened not unto the people: for the cause was of God, that the LORD might perform his word, which he spake by the hand of Ahijah the Shilonite to Jeroboam the son of Nebat.
# Nehemiah 6:19 Also they reported his good deeds before me, and uttered my words to him. And Tobiah sent letters to put me in fear.
# Esther 1:18 Likewise shall the ladies of Persia and Media say this day unto all the king's princes, which have heard of the deed of the queen. Thus shall there arise too much contempt and wrath.
# Esther 8:3 And Esther spake yet again before the king, and fell down at his feet, and besought him with tears to put away the mischief of Haman the Agagite, and his device that he had devised against the Jews.
# Job 20:4 Knowest thou not this of old, since man was placed upon earth,
# Job 38:37 Who can number the clouds in wisdom? or who can stay the bottles of heaven,
# Job 42:8 Therefore take unto you now seven bullocks and seven rams, and go to my servant Job, and offer up for yourselves a burnt offering; and my servant Job shall pray for you: for him will I accept: lest I deal with you after your folly, in that ye have not spoken of me the thing which is right, like my servant Job.
# Psalms 31:9 Have mercy upon me, O LORD, for I am in trouble: mine eye is consumed with grief, yea, my soul and my belly.
# Psalms 55:8 I would hasten my escape from the windy storm and tempest.
# Psalms 94:19 In the multitude of my thoughts within me thy comforts delight my soul.
# Psalms 103:1 Bless the LORD, O my soul: and all that is within me, bless his holy name.
# >>> p(b.Pro[8:12]-36)
# Proverbs 8
# 12 I wisdom dwell with prudence, and find out knowledge of witty inventions.
# 13 The fear of the LORD is to hate evil: pride, and arrogancy, and the evil way, and the froward mouth, do I hate.
# 14 Counsel is mine, and sound wisdom: I am understanding; I have strength.
# 15 By me kings reign, and princes decree justice.
# 16 By me princes rule, and nobles, even all the judges of the earth.
# 17 I love them that love me; and those that seek me early shall find me.
# 18 Riches and honour are with me; yea, durable riches and righteousness.
# 19 My fruit is better than gold, yea, than fine gold; and my revenue than choice silver.
# 20 I lead in the way of righteousness, in the midst of the paths of judgment:
# 21 That I may cause those that love me to inherit substance; and I will fill their treasures.
# 22 The LORD possessed me in the beginning of his way, before his works of old.
# 23 I was set up from everlasting, from the beginning, or ever the earth was.
# 24 When there were no depths, I was brought forth; when there were no fountains abounding with water.
# 25 Before the mountains were settled, before the hills was I brought forth:
# 26 While as yet he had not made the earth, nor the fields, nor the highest part of the dust of the world.
# 27 When he prepared the heavens, I was there: when he set a compass upon the face of the depth:
# 28 When he established the clouds above: when he strengthened the fountains of the deep:
# 29 When he gave to the sea his decree, that the waters should not pass his commandment: when he appointed the foundations of the earth:
# 30 Then I was by him, as one brought up with him: and I was daily his delight, rejoicing always before him;
# 31 Rejoicing in the habitable part of his earth; and my delights were with the sons of men.
# 32 Now therefore hearken unto me, O ye children: for blessed are they that keep my ways.
# 33 Hear instruction, and be wise, and refuse it not.
# 34 Blessed is the man that heareth me, watching daily at my gates, waiting at the posts of my doors.
# 35 For whoso findeth me findeth life, and shall obtain favour of the LORD.
# 36 But he that sinneth against me wrongeth his own soul: all they that hate me love death.
# >>> p(b/"Babylon"*b/"fall")
# Isaiah 21:9 And, behold, here cometh a chariot of men, with a couple of horsemen. And he answered and said, Babylon is fallen, is fallen; and all the graven images of her gods he hath broken unto the ground.
# Jeremiah 20:4 For thus saith the LORD, Behold, I will make thee a terror to thyself, and to all thy friends: and they shall fall by the sword of their enemies, and thine eyes shall behold it: and I will give all Judah into the hand of the king of Babylon, and he shall carry them captive into Babylon, and shall slay them with the sword.
# Jeremiah 51
# 8 Babylon is suddenly fallen and destroyed: howl for her; take balm for her pain, if so be she may be healed.
# 44 And I will punish Bel in Babylon, and I will bring forth out of his mouth that which he hath swallowed up: and the nations shall not flow together any more unto him: yea, the wall of Babylon shall fall.
# 47 Therefore, behold, the days come, that I will do judgment upon the graven images of Babylon: and her whole land shall be confounded, and all her slain shall fall in the midst of her.
# 49 As Babylon hath caused the slain of Israel to fall, so at Babylon shall fall the slain of all the earth.
# Ezekiel 30:25 But I will strengthen the arms of the king of Babylon, and the arms of Pharaoh shall fall down; and they shall know that I am the LORD, when I shall put my sword into the hand of the king of Babylon, and he shall stretch it out upon the land of Egypt.
# Revelation 14:8 And there followed another angel, saying, Babylon is fallen, is fallen, that great city, because she made all nations drink of the wine of the wrath of her fornication.
# Revelation 18:2 And he cried mightily with a strong voice, saying, Babylon the great is fallen, is fallen, and is become the habitation of devils, and the hold of every foul spirit, and a cage of every unclean and hateful bird.
# >>> b.vi(1)+b.vi(31102)
# Genesis 1:1 In the beginning God created the heaven and the earth.
# Revelation 22:21 The grace of our Lord Jesus Christ be with you all. Amen.
# >>> _.tell()
# In the beginning God created the heaven and the earth.
# 23+ 33+    81   + 26+   56  + 33+  55  + 19+ 33+  52  =411
# The grace of our Lord Jesus Christ be with you all. Amen.
#  33+  34 +21+ 54+ 49 +  74 +  77  +7 + 60 + 61+ 25 +  33 =528
# >>> bible.midv().tell()
# Bless the LORD, O  my soul: and all that is within me, bless his holy name.
#   57 + 33+  49 +15+38+  67 + 19+ 25+ 49 +28+  83  + 18+  57 + 36+ 60 +  33 =667
# Bless the LORD, O  my soul, and forget not all his benefits:
#   57 + 33+  49 +15+38+  67 + 19+  71  + 49+ 25+ 36+    80   =539
# >>> 667+539
# 1206
