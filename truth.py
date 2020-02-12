    >>> from bible import *
    >>> showalphas()
    a b c d e f g h i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

    >>> b/"Here is wisdom"
    Revelation 13:18 Here is wisdom. Let him that hath understanding count the number of the beast: for it is the number of a man; and his number is Six hundred threescore and six.

This suggests there is sme way of numbering a man, perhaps by name.

    >>> Ecclesiastes[7:27]
    Ecclesiastes 7:27 Behold, this have I found, saith the preacher, counting one by one, to find out the account:

    >>> _.tell()
    7:27 Behold, this have I found, saith the preacher, counting one by one, to find out the account:
       0+     46+  56+  36+9+    60+   57+ 33+       74+     103+ 34+27+  34+35+  33+ 56+ 33+      77 = 803

    >>> tell('Solomon')
     S  o  l  o  m  o  n
    19+15+12+15+13+15+14 = 103

'counting' and 'Solomon' have the same sum: 103

    >>> 
Various sums:

    >>> for w in 'Lord Jesus Christ the water and the blood the spirit'.split(): tell(w)
    ... 
     L  o  r d
    12+15+18+4 = 49
     J e  s  u  s
    10+5+19+21+19 = 74
    C h  r i  s  t
    3+8+18+9+19+20 = 77
     t h e
    20+8+5 = 33
     w a  t e  r
    23+1+20+5+18 = 67
    a  n d
    1+14+4 = 19
     t h e
    20+8+5 = 33
    b  l  o  o d
    2+12+15+15+4 = 48
     t h e
    20+8+5 = 33
     s  p i  r i  t
    19+16+9+18+9+20 = 91

     L  o  r d
    12+15+18+4 = 49
     J e  s  u  s
    10+5+19+21+19 = 74
    C h  r i  s  t
    3+8+18+9+19+20 = 77
     t h e
    20+8+5 = 33
     w a  t e  r
    23+1+20+5+18 = 67
    a  n d
    1+14+4 = 19
     t h e
    20+8+5 = 33
    b  l  o  o d
    2+12+15+15+4 = 48
     t h e
    20+8+5 = 33
     s  p i  r i  t
    19+16+9+18+9+20 = 91
    >>> tell('Lord Jesus Christ')
    Lord Jesus Christ
      49+   74+    77 = 200

    >>> IJohn[5:7]-8
    1 John 5:7 For there are three that bear record in heaven, the Father, the Word, and the Holy Ghost: and these three are one.
    1 John 5:8 And there are three that bear witness in earth, the Spirit, and the water, and the blood: and these three agree in one.

Now we could take these as alphabetic sums. There are questions about whether we add the 3, and do we include the 'and's and the 'the's well there are a few possibilities an we look to see if it could work:

    >>> tell('the Father, the Word, + the Holy Ghost')
    the Father, the Word, + the Holy Ghost
     33+     58+ 33+   60+0+ 33+  60+   69 = 346
    >>> 
    >>> tell('the spirit+and the+water and+the+blood')
    the spirit+and the+water and+the+blood
     33+       110+      100+          100 = 343
    >>> show('343+3')
    343+3 = 346
    >>> show('7*7*7')
    7*7*7 = 343

Letter counts also work:

    >>> tell('the Father, the Word, and the Holy Ghost',lsum)
    the Father, the Word, and the Holy Ghost
      3+      6+  3+    4+  3+  3+   4+    5 = 31
    >>> tell('the spirit and the water and the blood',lsum)
    the spirit and the water and the blood
      3+     6+  3+  3+    5+  3+  3+    5 = 31

31 is a pun on the three are one.

The middle chapter of the bible is:

    >>> bible.midchapter()
    Psalms 117:1 O praise the LORD, all ye nations: praise him, all ye people.
    Psalms 117:2 For his merciful kindness is great toward us: and the truth of the LORD endureth for ever. Praise ye the LORD.

The middle verses are:

    >>> bible.midverse()
    Psalms 103:1 Bless the LORD, O my soul: and all that is within me, bless his holy name.
    Psalms 103:2 Bless the LORD, O my soul, and forget not all his benefits:

Here's this number 103 again.

The total number of verses in the bible is:

    >>> b.vc()
    31102

This is an anagram of 103:1-2, the middle verses.

And as I say, the factors of 31102 are:

    >>> allfactors(31102)
    [1, 2, 15551, 31102]

which add to:

    >>> sum(_)
    46656
    >>> show('6**6')
    6**6 = 46656


