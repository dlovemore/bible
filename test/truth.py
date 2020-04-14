    >>> from bible import *

    >>> b/"Here is wisdom"
    Revelation 13:18 Here is wisdom. Let him that hath understanding count the number of the beast: for it is the number of a man; and his number is Six hundred threescore and six.

This suggests there is some way of numbering a man, perhaps by name.

    >>> Ecclesiastes[7:27]
    Ecclesiastes 7:27 Behold, this have I found, saith the preacher, counting one by one, to find out the account:

The traditional hebrew counting system which is used for example to number verses uses the values:
    >>> showalphas(אב,ssum)
    א ב ג ד ה ו ז ח ט י  כ  ל  מ  נ  ס  ע  פ  צ   ק   ר   ש   ת 
    1 2 3 4 5 6 7 8 9 10 20 30 40 50 60 70 80 90 100 200 300 400
    >>> 
What does counting one by one mean? We could count the letters, or letter position, or with tens and hundreds as above.

This gives us three numbering systems to try.
    >>> showalphas(ab,lsum)
    a b c d e f g h i j k l m n o p q r s t u v w x y z
    1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    >>> showalphas(ab,osum)
    a b c d e f g h i j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z 
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
    >>> showalphas(ab,ssum)
    a b c d e f g h i j  k  l  m  n  o  p  q  r   s   t   u   v   w   x   y   z 
    1 2 3 4 5 6 7 8 9 10 20 30 40 50 60 70 80 90 100 200 300 400 500 600 700 800
    >>> 

    >>> _.tell()
    Behold, this have I found, saith the preacher, counting one by one, to find out the account:
       46  + 56 + 36 +9+  60  +  57 + 33+    74   +  103   + 34+27+ 34 +35+ 33 + 56+ 33+   77   =803

Ecclesiates was written by Solomon.

    >>> tell('Solomon')
    S  o  l  o  m  o  n
    19+15+12+15+13+15+14=103

'counting' and 'Solomon' have the same sum: 103

Also Ecclesiastes 7, is the 666th book.

    >>> 
Various sums:

    >>> for w in 'God Lord Jesus Christ '.split()+['LORD JEHOVAH']: tell(w,osum,ssum)
    ... 
    G o  d
    7+15+4=26
    7+60+4=71
    L  o  r  d
    12+15+18+4= 49
    30+60+90+4=184
    J  e  s   u   s
    10+5+ 19+ 21+ 19= 74
    10+5+100+300+100=515
    C h r  i  s   t
    3+8+18+9+ 19+ 20= 77
    3+8+90+9+100+200=410
    LORD JEHOVAH
     49 +   69  =118
    184 +  492  =676
    >>> 
    >>> tell('Lord Jesus Christ')
    Lord Jesus Christ
     49 +  74 +  77  =200

    >>> IJohn[5:7]-8
    1 John 5:7 For there are three that bear record in heaven, the Father, the Word, and the Holy Ghost: and these three are one.
    1 John 5:8 And there are three that bear witness in earth, the Spirit, and the water, and the blood: and these three agree in one.

Now we could take these as alphabetic sums. There are questions about whether we add the 3, and do we include the 'and's and the 'the's well there are a few possibilities an we look to see if it could work:

    >>> tell('the Father, the Word, + the Holy Ghost')
    the Father, the Word, + the Holy Ghost
     33+   58  + 33+  60 +0+ 33+ 60 +  69 =346
    >>> 
    >>> tell('the spirit and the water and the blood')
    the spirit and the water and the blood
     33+  91  + 19+ 33+  67 + 19+ 33+  48 =343
    >>> tell('the spirit+and the+water and+the+blood')
    the spirit+and the+water and+the+blood
     33+   110    +   100   +     100     =343
    >>> show('343+3')
    343+3 = 346
    >>> show('7*7*7')
    7*7*7 = 343

Letter counts also work:

    >>> tell('the Father, the Word, and the Holy Ghost',lsum)
    the Father, the Word, and the Holy Ghost
     3 +   6   + 3 +  4  + 3 + 3 + 4  +  5  =31
    >>> tell('the spirit and the water and the blood',lsum)
    the spirit and the water and the blood
     3 +  6   + 3 + 3 +  5  + 3 + 3 +  5  =31

31 is a pun on the three are one.

Now actually, we see this pattern in Genesis and the chapters of the bible.

There are 1189 books in the bible
    >>> tell([b.name() for b in bible.books()],(lambda x:(b[x].chc())))
    Genesis Exodus Leviticus Numbers Deuteronomy Joshua Judges Ruth 1 Samuel 2 Samuel 1 Kings 2 Kings 1 Chronicles 2 Chronicles Ezra Nehemiah Esther Job Psalms Proverbs Ecclesiastes Song of Solomon Isaiah Jeremiah Lamentations Ezekiel Daniel Hosea Joel Amos Obadiah Jonah Micah Nahum Habakkuk Zephaniah Haggai Zechariah Malachi Matthew Mark Luke John Acts Romans 1 Corinthians 2 Corinthians Galatians Ephesians Philippians Colossians 1 Thessalonians 2 Thessalonians 1 Timothy 2 Timothy Titus Philemon Hebrews James 1 Peter 2 Peter 1 John 2 John 3 John Jude Revelation
       50  +  40  +    27   +   36  +     34    +  24  +  21  + 4  +   31   +   24   +   22  +   25  +     29     +     36     + 10 +   13   +  10  + 42+ 150  +   31   +     12     +       8       +  66  +   52   +     5      +   48  +  12  +  14 + 3  + 9  +   1   +  4  +  7  +  3  +   3    +    3    +  2   +    14   +   4   +   28  + 16 + 24 + 21 + 28 +  16  +      16     +      13     +    6    +    6    +     4     +    4     +       5       +       3       +    6    +    4    +  3  +   1    +   13  +  5  +   5   +   3   +  5   +  1   +  1   + 1  +    22    =1189
    >>> 
    >>> 
    >>> 

The middle chapter of the bible is:

    >>> bible.midchapter()
    Psalms 117:1 O praise the LORD, all ye nations: praise him, all ye people.
    Psalms 117:2 For his merciful kindness is great toward us: and the truth of the LORD endureth for ever. Praise ye the LORD.

Now this is marked out in that it is also the shortest. And in Psalms, the lengths of the Psalms are 

    >>> 

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

    >>> tell(allfactors(31102), I)
    1 2 15551 31102
    1+2+15551+31102=46656
    >>> 

    >>> show('6**6')
    6**6 = 46656


