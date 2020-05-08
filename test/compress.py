from auto import *
from collections import Counter
from func import pairs, method, aslist
from operator import itemgetter as li

def notf(f): return (lambda x: not x)

def alpha(s): return ''.join((c for c in s if c.isalpha()))

def nonalpha(s): return ''.join((c for c in s if not c.isalpha()))

def sortu(l): return sorted(set(l))

def sortus(s): return ''.join(sortu(s))

def punc(s): return ''.join(map(nof(isalpha),sortus(s)))

def textgroups(text):
    return re.findall(r'( |\n|\w+(?:[^\w \n]*\w+)*|\W)',text)

def shorten(text, wordlist=None):
    words=textgroups(text)
    if wordlist is None:
        wset=set(words)
        wordlist=sorted(wset)
    windex={w:256+i for i,w in enumerate(wordlist)}
    windex.update({chr(i):i for i in range(256)})
    nums=[windex[w] for w in words]
    compressed=''.join([chr(x) for x in nums])
    # compwordlist=compshortwordlist(shortenwordlist(wordlist))
    return wordlist,compressed

def commonlength(s,t):
    return len(list(itertools.takewhile((lambda x: x[0]==x[1]),zip(s,t))))

@aslist
def shortenwordlist(ws):
    assert list(ws) == sorted(ws)
    for w,v in pairs(['']+ws):
        k=commonlength(w,v)
        yield str(k)+v[k:]

@aslist
def unshortenwordlist(wl):
    w=''
    for v in wl:
        ks=(''.join(itertools.takewhile(method.isdigit,v)))
        k=int(ks)
        w=w[:k]+v[len(ks):]
        yield w

def compshortwordlist(swl):
    return ''.join(swl)

def uncompwordlist(swl):
    return re.findall(r'[0-9]+[^0-9]+', swl)

def unshorten(shortwordlist,compressed):
    # shortwordlist=uncompwordlist(compwordlist)
    # assert(len(''.join(shortwordlist))==len(compwordlist))
    wordlist=[chr(i) for i in range(256)]+unshortenwordlist(shortwordlist)
    return ''.join([wordlist[ord(c)] for c in compressed])


# >>> from bible import *
# >>> from compress import *
# >>> text=Genesis.text()
# >>> 
# >>> t=shorten(text)
# >>> wl, st=t
# >>> 
# >>> wl[:10],st[:10]
# (['\n', ' ', '!', "'", '(', ')', ',', '.', ':', ';'], 'Ȫ \u0a46 Х ǯ ԇ ')
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> len(text),len(wl),len(st), len(st.replace(' ',''))
# (196806, 2676, 82978, 46247)
# >>> 
# >>> st.__sizeof__()
# 165994
# >>> st[:3]
# 'Ȫ \u0a46'
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> unt=unshorten(*t)
# <27>:1: ValueError: invalid literal for int() with base 10: ''
# /home/pi/python/bible/test/compress.py:61: ValueError: invalid literal for int() with base 10: ''
#   unshorten(
#     shortwordlist=['\n', ' ', '!', "'", '(', ')', ',', '.', ':', ';',...
#     compressed=Ȫ ੆ Х ǯ ԇ ੆ ۂ ϋ ੆ ֒.
#     ĳ ੆ ֒ ૨ ି ذ, ϋ ૗; ϋ Ԡ ૨ ઺ ੆ ׍ ࠷ ੆ Բ. ...
#   )
# /home/pi/python/parle/func.py:12: ValueError: invalid literal for int() with base 10: ''
#   __call__(
#     self=Func(functools.partial(<function aslist.<locals>.tolist at 0...
#   )
#     args=(['\n', ' ', '!', "'", '(', ')', ',', '.', ':', ';', '?', 'A...
#     kwargs={}
# /home/pi/python/parle/func.py:296: ValueError: invalid literal for int() with base 10: ''
#   tolist(f=<function unshortenwordlist at 0xb5803468>)
#     args=(['\n', ' ', '!', "'", '(', ')', ',', '.', ':', ';', '?', 'A...
# /home/pi/python/bible/test/compress.py:48: ValueError: invalid literal for int() with base 10: ''
#   unshortenwordlist(
#     wl=['\n', ' ', '!', "'", '(', ')', ',', '.', ':', ';', '?', 'A', ...
#   )
#     w=
#     v=
#     
#     ks=
# >>> 
# >>> unt==text
# <29>:1: NameError: name 'unt' is not defined
# >>> [''.join(g) for x,g in itertools.groupby('a,b,c.sdfhjsfh--x',key=method.isalpha)]
# ['a', ',', 'b', ',', 'c', '.', 'sdfhjsfh', '--', 'x']
# >>> wl=sortu(Genesis[1].words())
# >>> cwl=compshortwordlist(shortenwordlist(wl))
# >>> swl=uncompwordlist(cwl)
# >>> 
# >>> uwl=unshortenwordlist(swl)
# >>> wl==uwl
# True
# >>> 
# >>> 
# >>> words=b.words()
# >>> text=b.text()
# >>> len(text)
# 4137733
# >>> wset=set(words)
# >>> len(wset)
# 28870
# >>> 0x2028
# 8232
# >>> p(chr(_))
#  # 
# >>> 0x2029
# 8233
# >>> p(chr(_))
#  # 
# >>> 0x202a
# 8234
# >>> p(chr(_))
# ‪
# >>> ''.join(set('abcdef'))
# 'dcbafe'
# >>> pp=pprint.pprint
# >>> 

# >>> sws=sorted(wset)
# >>> nonalpha('abc.')
# '.'
# >>> punc=[nonalpha(w) for w in sws]
# >>> set(punc)
# {'', ';)', '-:', ',', '.', "'.", '!)', '),', "',", "':", ')', '.)', "';", '?)', ':', "'", '-', "'?", '(,', ').', "':)", '!', ':)', '(', '--;', '-.', '?', ',)', ';', '-,'}
# >>> puncchrs=''.join(sorted(''.join(set(''.join(_)))))
# >>> puncchrs
# ' .Tacehmnost'
# >>> t=text
# >>> 
# >>> for c in puncchrs: t=f' {c} '.join(t.split(c))
# ... 
# >>> 

## >>> 
## >>> [w for w in sws if w.endswith("'s:)")]
## ["Joseph's:)"]
## >>> len(nonalpha(text))
## 915328
## >>> _-789000
## 126328
## >>> len(re.findall("'s",text))
## 1789
## >>> len(re.findall("'S",text))
## 0

# >>> Counter=collections.Counter
# >>> wcounter=Counter(words)
# >>> len(wcounter)
# 28870
# >>> wcounter.most_common(52)
# [('the', 62060), ('and', 38576), ('of', 34391), ('to', 13369), ('And', 12735), ('that', 12451), ('in', 12167), ('shall', 9760), ('he', 9508), ('unto', 8932), ('I', 8708), ('his', 8362), ('a', 7943), ('for', 7141), ('they', 6893), ('be', 6718), ('is', 6696), ('with', 5951), ('not', 5840), ('all', 5238), ('thou', 4629), ('it', 4461), ('thy', 4451), ('was', 4447), ('which', 4268), ('my', 4135), ('LORD', 3930), ('their', 3873), ('have', 3821), ('will', 3751), ('from', 3578), ('ye', 3566), ('them', 3503), ('as', 3256), ('him', 3157), ('are', 2884), ('upon', 2716), ('were', 2711), ('by', 2493), ('when', 2483), ('out', 2459), ('but', 2410), ('said', 2281), ('this', 2271), ('God', 2229), ('hath', 2217), ('him,', 2033), ('into', 2011), ('had', 1992), ('came', 1989), ('man', 1970), ('on', 1925)]
# >>> 128-44
# 84
# >>> 
# >>> tc=(tale(wcounter.values()))
# >>> li(25,51,83,-1)(tc)
# (169918, 226376, 248325, 789629)
# >>> _[2]-_[1]
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# TypeError: unsupported operand type(s) for -: 'str' and 'str'
# >>> [w for w in sws if w.find('-')!=-1]
# ['Ben-hadad', 'God-ward', 'God-ward,', 'God-ward:', 'brick-kiln:', 'fellow-prisoners,', 'joint-heirs', 'sin--;', 'standard-bearer', 'stumbling-block', 'thee-ward', 'two-edged', 'us-ward', 'us-ward,', 'us-ward:', 'well-beloved', 'you-ward', 'you-ward.', 'you-ward:']
# >>> 
# >>> dir('')
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# >>> help(''.find)
# Help on built-in function find:
# 
# find(...) method of builtins.str instance
#     S.find(sub[, start[, end]]) -> int
#     
#     Return the lowest index in S where substring sub is found,
#     such that sub is contained within S[start:end].  Optional
#     arguments start and end are interpreted as in slice notation.
#     
#     Return -1 on failure.
# 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 

# >>> 
# >>> 
# >>> ''.join(map(chr,range(32,127)))
# ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
# >>> 

# >>> 
# >>> help(Counter)
# Help on class Counter in module collections:
# 
# class Counter(builtins.dict)
#  |  Counter(*args, **kwds)
#  |  
#  |  Dict subclass for counting hashable items.  Sometimes called a bag
#  |  or multiset.  Elements are stored as dictionary keys and their counts
#  |  are stored as dictionary values.
#  |  
#  |  >>> c = Counter('abcdeabcdabcaba')  # count elements from a string
#  |  
#  |  >>> c.most_common(3)                # three most common elements
#  |  [('a', 5), ('b', 4), ('c', 3)]
#  |  >>> sorted(c)                       # list all unique elements
#  |  ['a', 'b', 'c', 'd', 'e']
#  |  >>> ''.join(sorted(c.elements()))   # list elements with repetitions
#  |  'aaaaabbbbcccdde'
#  |  >>> sum(c.values())                 # total of all counts
#  |  15
#  |  
#  |  >>> c['a']                          # count of letter 'a'
#  |  5
#  |  >>> for elem in 'shazam':           # update counts from an iterable
#  |  ...     c[elem] += 1                # by adding 1 to each element's count
#  |  >>> c['a']                          # now there are seven 'a'
#  |  7
#  |  >>> del c['b']                      # remove all 'b'
#  |  >>> c['b']                          # now there are zero 'b'
#  |  0
#  |  
#  |  >>> d = Counter('simsalabim')       # make another counter
#  |  >>> c.update(d)                     # add in the second counter
#  |  >>> c['a']                          # now there are nine 'a'
#  |  9
#  |  
#  |  >>> c.clear()                       # empty the counter
#  |  >>> c
#  |  Counter()
#  |  
#  |  Note:  If a count is set to zero or reduced to zero, it will remain
#  |  in the counter until the entry is deleted or the counter is cleared:
#  |  
#  |  >>> c = Counter('aaabbc')
#  |  >>> c['b'] -= 2                     # reduce the count of 'b' by two
#  |  >>> c.most_common()                 # 'b' is still in, but its count is zero
#  |  [('a', 3), ('c', 1), ('b', 0)]
#  |  
#  |  Method resolution order:
#  |      Counter
#  |      builtins.dict
#  |      builtins.object
#  |  
#  |  Methods defined here:
#  |  
#  |  __add__(self, other)
#  |      Add counts from two counters.
#  |      
#  |      >>> Counter('abbb') + Counter('bcc')
#  |      Counter({'b': 4, 'c': 2, 'a': 1})
#  |  
#  |  __and__(self, other)
#  |      Intersection is the minimum of corresponding counts.
#  |      
#  |      >>> Counter('abbb') & Counter('bcc')
#  |      Counter({'b': 1})
#  |  
#  |  __delitem__(self, elem)
#  |      Like dict.__delitem__() but does not raise KeyError for missing values.
#  |  
#  |  __iadd__(self, other)
#  |      Inplace add from another counter, keeping only positive counts.
#  |      
#  |      >>> c = Counter('abbb')
#  |      >>> c += Counter('bcc')
#  |      >>> c
#  |      Counter({'b': 4, 'c': 2, 'a': 1})
#  |  
#  |  __iand__(self, other)
#  |      Inplace intersection is the minimum of corresponding counts.
#  |      
#  |      >>> c = Counter('abbb')
#  |      >>> c &= Counter('bcc')
#  |      >>> c
#  |      Counter({'b': 1})
#  |  
#  |  __init__(*args, **kwds)
#  |      Create a new, empty Counter object.  And if given, count elements
#  |      from an input iterable.  Or, initialize the count from another mapping
#  |      of elements to their counts.
#  |      
#  |      >>> c = Counter()                           # a new, empty counter
#  |      >>> c = Counter('gallahad')                 # a new counter from an iterable
#  |      >>> c = Counter({'a': 4, 'b': 2})           # a new counter from a mapping
#  |      >>> c = Counter(a=4, b=2)                   # a new counter from keyword args
#  |  
#  |  __ior__(self, other)
#  |      Inplace union is the maximum of value from either counter.
#  |      
#  |      >>> c = Counter('abbb')
#  |      >>> c |= Counter('bcc')
#  |      >>> c
#  |      Counter({'b': 3, 'c': 2, 'a': 1})
#  |  
#  |  __isub__(self, other)
#  |      Inplace subtract counter, but keep only results with positive counts.
#  |      
#  |      >>> c = Counter('abbbc')
#  |      >>> c -= Counter('bccd')
#  |      >>> c
#  |      Counter({'b': 2, 'a': 1})
#  |  
#  |  __missing__(self, key)
#  |      The count of elements not in the Counter is zero.
#  |  
#  |  __neg__(self)
#  |      Subtracts from an empty counter.  Strips positive and zero counts,
#  |      and flips the sign on negative counts.
#  |  
#  |  __or__(self, other)
#  |      Union is the maximum of value in either of the input counters.
#  |      
#  |      >>> Counter('abbb') | Counter('bcc')
#  |      Counter({'b': 3, 'c': 2, 'a': 1})
#  |  
#  |  __pos__(self)
#  |      Adds an empty counter, effectively stripping negative and zero counts
#  |  
#  |  __reduce__(self)
#  |      Helper for pickle.
#  |  
#  |  __repr__(self)
#  |      Return repr(self).
#  |  
#  |  __sub__(self, other)
#  |      Subtract count, but keep only results with positive counts.
#  |      
#  |      >>> Counter('abbbc') - Counter('bccd')
#  |      Counter({'b': 2, 'a': 1})
#  |  
#  |  copy(self)
#  |      Return a shallow copy.
#  |  
#  |  elements(self)
#  |      Iterator over elements repeating each as many times as its count.
#  |      
#  |      >>> c = Counter('ABCABC')
#  |      >>> sorted(c.elements())
#  |      ['A', 'A', 'B', 'B', 'C', 'C']
#  |      
#  |      # Knuth's example for prime factors of 1836:  2**2 * 3**3 * 17**1
#  |      >>> prime_factors = Counter({2: 2, 3: 3, 17: 1})
#  |      >>> product = 1
#  |      >>> for factor in prime_factors.elements():     # loop over factors
#  |      ...     product *= factor                       # and multiply them
#  |      >>> product
#  |      1836
#  |      
#  |      Note, if an element's count has been set to zero or is a negative
#  |      number, elements() will ignore it.
#  |  
#  |  most_common(self, n=None)
#  |      List the n most common elements and their counts from the most
#  |      common to the least.  If n is None, then list all element counts.
#  |      
#  |      >>> Counter('abcdeabcdabcaba').most_common(3)
#  |      [('a', 5), ('b', 4), ('c', 3)]
#  |  
#  |  subtract(*args, **kwds)
#  |      Like dict.update() but subtracts counts instead of replacing them.
#  |      Counts can be reduced below zero.  Both the inputs and outputs are
#  |      allowed to contain zero and negative counts.
#  |      
#  |      Source can be an iterable, a dictionary, or another Counter instance.
#  |      
#  |      >>> c = Counter('which')
#  |      >>> c.subtract('witch')             # subtract elements from another iterable
#  |      >>> c.subtract(Counter('watch'))    # subtract elements from another counter
#  |      >>> c['h']                          # 2 in which, minus 1 in witch, minus 1 in watch
#  |      0
#  |      >>> c['w']                          # 1 in which, minus 1 in witch, minus 1 in watch
#  |      -1
#  |  
#  |  update(*args, **kwds)
#  |      Like dict.update() but add counts instead of replacing them.
#  |      
#  |      Source can be an iterable, a dictionary, or another Counter instance.
#  |      
#  |      >>> c = Counter('which')
#  |      >>> c.update('witch')           # add elements from another iterable
#  |      >>> d = Counter('watch')
#  |      >>> c.update(d)                 # add elements from another counter
#  |      >>> c['h']                      # four 'h' in which, witch, and watch
#  |      4
#  |  
#  |  ----------------------------------------------------------------------
#  |  Class methods defined here:
#  |  
#  |  fromkeys(iterable, v=None) from builtins.type
#  |      Create a new dictionary with keys from iterable and values set to value.
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |  
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |  
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |  
#  |  ----------------------------------------------------------------------
#  |  Methods inherited from builtins.dict:
#  |  
#  |  __contains__(self, key, /)
#  |      True if the dictionary has the specified key, else False.
#  |  
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |  
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |  
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |  
#  |  __getitem__(...)
#  |      x.__getitem__(y) <==> x[y]
#  |  
#  |  __gt__(self, value, /)
#  |      Return self>value.
#  |  
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |  
#  |  __le__(self, value, /)
#  |      Return self<=value.
#  |  
#  |  __len__(self, /)
#  |      Return len(self).
#  |  
#  |  __lt__(self, value, /)
#  |      Return self<value.
#  |  
#  |  __ne__(self, value, /)
#  |      Return self!=value.
#  |  
#  |  __setitem__(self, key, value, /)
#  |      Set self[key] to value.
#  |  
#  |  __sizeof__(...)
#  |      D.__sizeof__() -> size of D in memory, in bytes
#  |  
#  |  clear(...)
#  |      D.clear() -> None.  Remove all items from D.
#  |  
#  |  get(self, key, default=None, /)
#  |      Return the value for key if key is in the dictionary, else default.
#  |  
#  |  items(...)
#  |      D.items() -> a set-like object providing a view on D's items
#  |  
#  |  keys(...)
#  |      D.keys() -> a set-like object providing a view on D's keys
#  |  
#  |  pop(...)
#  |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
#  |      If key is not found, d is returned if given, otherwise KeyError is raised
#  |  
#  |  popitem(...)
#  |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
#  |      2-tuple; but raise KeyError if D is empty.
#  |  
#  |  setdefault(self, key, default=None, /)
#  |      Insert key with a value of default if key is not in the dictionary.
#  |      
#  |      Return the value for key if key is in the dictionary, else default.
#  |  
#  |  values(...)
#  |      D.values() -> an object providing a view on D's values
#  |  
#  |  ----------------------------------------------------------------------
#  |  Static methods inherited from builtins.dict:
#  |  
#  |  __new__(*args, **kwargs) from builtins.type
#  |      Create and return a new object.  See help(type) for accurate signature.
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes inherited from builtins.dict:
#  |  
#  |  __hash__ = None
# 
# >>> 
# >>> 2**15
# 32768
# >>> 
# >>> 
# >>> 
# >>> 
