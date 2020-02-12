>>> from bible import *
>>> c='Who sends a message in the number of characters in a book?'
>>> tell(lsum,c)
Who sends a message in the number of characters in a book?
 3 +  5  +1+   7   +2 + 3 +  6   +2 +    10    +2 +1+  4  =46
>>> tell(lsum,"1:1 In the beginning God created the heaven and the earth.")
1:1 In the beginning God created the heaven and the earth.
 0 +2 + 3 +    9    + 3 +   7   + 3 +  6   + 3 + 3 +  5   =44
>>> tell(lsum,osum,Isaiah[41:26].text())
Who hath declared from the beginning, that we may know? and beforetime, that we may say, He is righteous? yea, there is none that sheweth, yea, there is none that declareth, yea, there is none that heareth your words.
 3 + 4  +   8    + 4  + 3 +    9     + 4  +2 + 3 +  4  + 3 +     10    + 4  +2 + 3 + 3  +2 +2 +    9     + 3  +  5  +2 + 4  + 4  +   7    + 3  +  5  +2 + 4  + 4  +    9     + 3  +  5  +2 + 4  + 4  +   7   + 4  +  5   =168
 46+ 37 +   52   + 52 + 33+    81    + 49 +28+ 39+  63 + 19+     98    + 49 +28+ 39+ 45 +13+28+   122    + 31 +  56 +28+ 48 + 49 +   88   + 31 +  56 +28+ 48 + 49 +    76    + 31 +  56 +28+ 48 + 49 +   65  + 79 +  79  =1944
>>> tell(lsum,osum,Isaiah[46:10].text())
Declaring the end from the beginning, and from ancient times the things that are not yet done, saying, My counsel shall stand, and I will do all my pleasure:
    9    + 3 + 3 + 4  + 3 +    9     + 3 + 4  +   7   +  5  + 3 +  6   + 4  + 3 + 3 + 3 +  4  +   6   +2 +   7   +  5  +  5   + 3 +1+ 4  +2 + 3 +2 +    8    =124
    73   + 33+ 23+ 52 + 33+    81    + 19+ 52 +   66  +  66 + 33+  77  + 49 + 24+ 49+ 50+  38 +   75  +38+   89  +  52 +  58  + 19+9+ 56 +19+ 25+38+    97   =1393
>>> tell(lsum,osum,Isaiah[48:3].text())
I have declared the former things from the beginning; and they went forth out of my mouth, and I shewed them; I did them suddenly, and they came to pass.
1+ 4  +   8    + 3 +  6   +  6   + 4  + 3 +    9     + 3 + 4  + 4  +  5  + 3 +2 +2 +  5   + 3 +1+  6   +  4  +1+ 3 + 4  +    8    + 3 + 4  + 4  +2 +  4  =119
9+ 36 +   52   + 33+  75  +  77  + 52 + 33+    81    + 19+ 58 + 62 +  67 + 56+21+38+  77  + 19+9+  64  +  46 +9+ 17+ 46 +   104   + 19+ 58 + 22 +35+  55 =1349
>>> tell(lsum,osum,Isaiah[48:5].text())
I have even from the beginning declared it to thee; before it came to pass I shewed it thee: lest thou shouldest say, Mine idol hath done them, and my graven image, and my molten image, hath commanded them.
1+ 4  + 4  + 4  + 3 +    9    +   8    +2 +2 +  4  +  6   +2 + 4  +2 + 4  +1+  6   +2 +  4  + 4  + 4  +    9    + 3  + 4  + 4  + 4  + 4  +  4  + 3 +2 +  6   +  5   + 3 +2 +  6   +  5   + 4  +    9    +  4  =161
9+ 36 + 46 + 52 + 33+    81   +   52   +29+35+  38 +  51  +29+ 22 +35+ 55 +9+  64  +29+  38 + 56 + 64 +   123   + 45 + 41 + 40 + 37 + 38 +  46 + 19+38+  67  +  35  + 19+38+  79  +  35  + 37 +    72   +  46 =1718
>>> Isaiah[41:26]|Isaiah[48:5]
Isaiah 41:26 Who hath declared from the beginning, that we may know? and beforetime, that we may say, He is righteous? yea, there is none that sheweth, yea, there is none that declareth, yea, there is none that heareth your words.
Isaiah 48:5 I have even from the beginning declared it to thee; before it came to pass I shewed it thee: lest thou shouldest say, Mine idol hath done them, and my graven image, and my molten image, hath commanded them.
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> lsum(Genesis[1:1])
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/pi/bible/mene.py", line 47, in lsum
    def lsum(s): return sum((l.isalpha() for l in letters(s)))
TypeError: unhashable type: 'Sel'
>>> 
>>> base(22,103)
[4, 15]
>>> tell(lsum,osum,ssum,'Or in the base of the code in the book?')
 Or in the base of the code in the book?
 2 +2 + 3 + 4  +2 + 3 + 4  +2 + 3 +  4  = 29
 33+23+ 33+ 27 +21+ 33+ 27 +23+ 33+  43 =296
150+59+213+108 +66+213+ 72 +59+213+ 142 =1295
>>> tell(lsum,'The contents of the book are the message.')
The contents of the book are the message.
 3 +   8    +2 + 3 + 4  + 3 + 3 +   7    =33
>>> base(33,1189)
[1, 3, 1]
>>> IJohn[5:7:8]
1 John 5:7 For there are three that bear record in heaven, the Father, the Word, and the Holy Ghost: and these three are one.
1 John 5:8 And there are three that bear witness in earth, the Spirit, and the water, and the blood: and these three agree in one.
>>> tell(lsum,'the Father, the Word, and the Holy Ghost')
the Father, the Word, and the Holy Ghost
 3 +   6   + 3 +  4  + 3 + 3 + 4  +  5  =31
>>> tell(lsum,'the Spirit, and the water, and the blood')
the Spirit, and the water, and the blood
 3 +   6   + 3 + 3 +  5   + 3 + 3 +  5  =31
>>> base(22,3088286401)
[1, 5, 5, 5, 8, 9, 0, 13]
>>> base(23,3088286401)
[20, 19, 18, 19, 18, 11, 18]
>>> sum(_)
123
>>> tell('rib')
r  i b
18+9+2=29
>>> tell('Lord Jesus')
Lord Jesus
 49 +  74 =123
>>> base(33,1189)
[1, 3, 1]
>>> int('1555890d',base=22)
3088286401
>>> chr(55)
'7'
>>> 
>>> bible.vi(15558)
Psalms 103:8 The LORD is merciful and gracious, slow to anger, and plenteous in mercy.
>>> 3088286401/3
1029428800.3333334
>>> int(_)
1029428800
>>> p(base(22,_))
[9, 1, 16, 10, 3, 0, 4]
>>> p(base(23,_))
[6, 21, 21, 14, 6, 3, 21]
>>> int('6JJD63J',23)
1015984263
>>> int('KJIJIBI',23)
3088286401
>>> int('1555890d',22) 
3088286401
>>> int('15558',22) 
290034
>>> p(Psalm[103])
Psalms 103
1 Bless the LORD, O my soul: and all that is within me, bless his holy name.
2 Bless the LORD, O my soul, and forget not all his benefits:
3 Who forgiveth all thine iniquities; who healeth all thy diseases;
4 Who redeemeth thy life from destruction; who crowneth thee with lovingkindness and tender mercies;
5 Who satisfieth thy mouth with good things; so that thy youth is renewed like the eagle's.
6 The LORD executeth righteousness and judgment for all that are oppressed.
7 He made known his ways unto Moses, his acts unto the children of Israel.
8 The LORD is merciful and gracious, slow to anger, and plenteous in mercy.
9 He will not always chide: neither will he keep his anger for ever.
10 He hath not dealt with us after our sins; nor rewarded us according to our iniquities.
11 For as the heaven is high above the earth, so great is his mercy toward them that fear him.
12 As far as the east is from the west, so far hath he removed our transgressions from us.
13 Like as a father pitieth his children, so the LORD pitieth them that fear him.
14 For he knoweth our frame; he remembereth that we are dust.
15 As for man, his days are as grass: as a flower of the field, so he flourisheth.
16 For the wind passeth over it, and it is gone; and the place thereof shall know it no more.
17 But the mercy of the LORD is from everlasting to everlasting upon them that fear him, and his righteousness unto children's children;
18 To such as keep his covenant, and to those that remember his commandments to do them.
19 The LORD hath prepared his throne in the heavens; and his kingdom ruleth over all.
20 Bless the LORD, ye his angels, that excel in strength, that do his commandments, hearkening unto the voice of his word.
21 Bless ye the LORD, all ye his hosts; ye ministers of his, that do his pleasure.
22 Bless the LORD, all his works in all places of his dominion: bless the LORD, O my soul.
>>> tell(lsum,osum,ssum,'Bless bless who who who the he the he he for as like for as for but to the bless bless bless')
Bless bless who who who the he the he he for  as like for  as for but  to the bless bless bless
  5  +  5  + 3 + 3 + 3 + 3 +2 + 3 +2 +2 + 3 + 2 + 4  + 3 + 2 + 3 + 3 + 2 + 3 +  5  +  5  +  5  = 71
  57 +  57 + 46+ 46+ 46+ 33+13+ 33+13+13+ 39+ 20+ 37 + 39+ 20+ 39+ 43+ 35+ 33+  57 +  57 +  57 =833
 237 + 237 +568+568+568+213+13+213+13+13+156+101+ 64 +156+101+156+502+260+213+ 237 + 237 + 237 =5063
>>> b.v(15558)
'The LORD is merciful and gracious, slow to anger, and plenteous in mercy.'
>>> 
>>> int('15551189',22)
3088208165
>>> pf(15558)
Counter({2: 1, 3: 1, 2593: 1})
>>> int('15558',22)
290034
>>> pf(_)
Counter({3: 3, 2: 1, 41: 1, 131: 1})
>>> pf(3088286401)
Counter({6619: 1, 466579: 1})
>>> pf(_)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/pi/python/parle/primes.py", line 82, in pf
    return collections.Counter(factors(n))
  File "/home/pi/python/parle/primes.py", line 69, in factors
    for p in (prime(j) for j in range(1,n)):
TypeError: 'Counter' object cannot be interpreted as an integer
>>> [b.name() for b in b.books()]
['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 'Ruth', '1 Samuel', '2 Samuel', '1 Kings', '2 Kings', '1 Chronicles', '2 Chronicles', 'Ezra', 'Nehemiah', 'Esther', 'Job', 'Psalms', 'Proverbs', 'Ecclesiastes', 'Song of Solomon', 'Isaiah', 'Jeremiah', 'Lamentations', 'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos', 'Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah', 'Malachi', 'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1 Corinthians', '2 Corinthians', 'Galatians', 'Ephesians', 'Philippians', 'Colossians', '1 Thessalonians', '2 Thessalonians', '1 Timothy', '2 Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1 Peter', '2 Peter', '1 John', '2 John', '3 John', 'Jude', 'Revelation']
>>> ' '.join(_)
'Genesis Exodus Leviticus Numbers Deuteronomy Joshua Judges Ruth 1 Samuel 2 Samuel 1 Kings 2 Kings 1 Chronicles 2 Chronicles Ezra Nehemiah Esther Job Psalms Proverbs Ecclesiastes Song of Solomon Isaiah Jeremiah Lamentations Ezekiel Daniel Hosea Joel Amos Obadiah Jonah Micah Nahum Habakkuk Zephaniah Haggai Zechariah Malachi Matthew Mark Luke John Acts Romans 1 Corinthians 2 Corinthians Galatians Ephesians Philippians Colossians 1 Thessalonians 2 Thessalonians 1 Timothy 2 Timothy Titus Philemon Hebrews James 1 Peter 2 Peter 1 John 2 John 3 John Jude Revelation'
>>> tell(lsum,_)
Genesis Exodus Leviticus Numbers Deuteronomy Joshua Judges Ruth 1 Samuel 2 Samuel 1 Kings 2 Kings 1 Chronicles 2 Chronicles Ezra Nehemiah Esther Job Psalms Proverbs Ecclesiastes Song of Solomon Isaiah Jeremiah Lamentations Ezekiel Daniel Hosea Joel Amos Obadiah Jonah Micah Nahum Habakkuk Zephaniah Haggai Zechariah Malachi Matthew Mark Luke John Acts Romans 1 Corinthians 2 Corinthians Galatians Ephesians Philippians Colossians 1 Thessalonians 2 Thessalonians 1 Timothy 2 Timothy Titus Philemon Hebrews James 1 Peter 2 Peter 1 John 2 John 3 John Jude Revelation
   7   +  6   +    9    +   7   +     11    +  6   +  6   + 4  +0+  6   +0+  6   +0+  5  +0+  5  +0+    10    +0+    10    + 4  +   8    +  6   + 3 +  6   +   8    +     12     + 4  +2 +   7   +  6   +   8    +     12     +   7   +  6   +  5  + 4  + 4  +   7   +  5  +  5  +  5  +   8    +    9    +  6   +    9    +   7   +   7   + 4  + 4  + 4  + 4  +  6   +0+     11    +0+     11    +    9    +    9    +     11    +    10    +0+      13     +0+      13     +0+   7   +0+   7   +  5  +   8    +   7   +  5  +0+  5  +0+  5  +0+ 4  +0+ 4  +0+ 4  + 4  +    10    =462
>>> nF(51)
(9, 34, -17, 51, 4, 55, 10)
>>> nF(55)
10
>>> nF(15)
(7, 13, -2, 15, 6, 21, 8)
>>> nF(1)
2
>>> nF(5)
5
>>> nF(55)
10
>>> nF(89)
11
>>> int('90d',base=22)
4369
>>> 
>>> int('90d',base=17)
2614
>>> nF(_)
(18, 2584, -30, 2614, 1567, 4181, 19)
>>> [int('90d',b) for b in span(14,33)]
[1777, 2038, 2317, 2614, 2929, 3262, 3613, 3982, 4369, 4774, 5197, 5638, 6097, 6574, 7069, 7582, 8113, 8662, 9229, 9814]
>>> hex(2317)
'0x90d'
>>> chr(2317)
'ऍ'
>>> 
>>> 3088286401/299792.458
10301.414590623224
>>> math.sqrt(_)
101.49588459944188
>>> 588+599
1187
>>> b.chapter(588)
Psalms 110:1-7 (7 verses)
>>> b.chapter(599)
Psalms 121:1-8 (8 verses)
>>> sof(3088)
6014
>>> sof(3088286401)
3088759600
>>> p(bin(_))
0b10111000000110101011101100110000
>>> p(base(22,_))
[1, 5, 5, 7, 8, 18, 15, 14]
>>> p(base(23,_))
[20, 19, 20, 12, 16, 0, 15]
>>> pf(_)
Counter({2: 4, 5: 2, 41: 1, 331: 1, 569: 1})
>>> pf(3088)
Counter({2: 4, 193: 1})
>>> math.sqrt(3088)
55.569775957799216
>>> 6**3
216
>>> math.sqrt(3088286401)
55572.35284743665
>>> 
>>> 
>>> from dna import *
>>> AV,W,X,Y
(2875001522, 16569, 156040895, 57227415)
>>> AV+W+X
3031058986
>>> math.sqrt(_)
55055.054136745704
>>> _,_*math.sqrt(2)
(55055.054136745704, 77859.60423737075)
>>> AV+W+X+Y
3088286401
>>> math.sqrt(_), _/299792.458
(55572.35284743665, 10301.414590623224)
>>> Deuteronomy[5].vn()
5055
>>> b.vi(30882)
Revelation 11:9 And they of the people and kindreds and tongues and nations shall see their dead bodies three days and an half, and shall not suffer their dead bodies to be put in graves.
>>> 
>>> pf(55055)
Counter({11: 2, 5: 1, 7: 1, 13: 1})
>>> factors(55055)
[5, 7, 11, 11, 13]
>>> sof(55055)
89376
>>> 55055
55055
>>> b.book(55)
2 Timothy 1:1-4:22 (83 verses)
>>> b.book(15)
Ezra 1:1-10:44 (280 verses)
>>> b.book(51)
Colossians 1:1-4:18 (95 verses)
>>> tell('the spirit')
the spirit
 33+  91  =124
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
