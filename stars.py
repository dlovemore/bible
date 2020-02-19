    >>> from bible import *
    >>> b/'number'/'seed'|b/'seed'/'stars'/'heaven'
    Genesis 13:16;15:5;16:10;22:17;26:4;32:12;Exodus 32:13;Jeremiah 33:22 (8 verses)
    >>> p(_)
    Genesis 13:16 And I will make thy seed as the dust of the earth: so that if a man can number the dust of the earth, then shall thy seed also be numbered.
    Genesis 15:5 And he brought him forth abroad, and said, Look now toward heaven, and tell the stars, if thou be able to number them: and he said unto him, So shall thy seed be.
    Genesis 16:10 And the angel of the LORD said unto her, I will multiply thy seed exceedingly, that it shall not be numbered for multitude.
    Genesis 22:17 That in blessing I will bless thee, and in multiplying I will multiply thy seed as the stars of the heaven, and as the sand which is upon the sea shore; and thy seed shall possess the gate of his enemies;
    Genesis 26:4 And I will make thy seed to multiply as the stars of heaven, and will give unto thy seed all these countries; and in thy seed shall all the nations of the earth be blessed;
    Genesis 32:12 And thou saidst, I will surely do thee good, and make thy seed as the sand of the sea, which cannot be numbered for multitude.
    Exodus 32:13 Remember Abraham, Isaac, and Israel, thy servants, to whom thou swarest by thine own self, and saidst unto them, I will multiply your seed as the stars of heaven, and all this land that I have spoken of will I give unto your seed, and they shall inherit it for ever.
    Jeremiah 33:22 As the host of heaven cannot be numbered, neither the sand of the sea measured: so will I multiply the seed of David my servant, and the Levites that minister unto me.
    >>> _.tell()
    And I will make thy seed as the dust of the earth: so that if a man can number the dust of the earth, then shall thy seed also be numbered.
     19+9+ 56 + 30 + 53+ 33 +20+ 33+ 64 +21+ 33+  52  +34+ 49 +15+1+ 28+ 18+  73  + 33+ 64 +21+ 33+  52  + 47 +  52 + 53+ 33 + 47 +7 +    82   =1165
    And he brought him forth abroad, and said, Look now toward heaven, and tell the stars, if thou be able to number them: and he said unto him, So shall thy seed be.
     19+13+   91  + 30+  67 +   41  + 19+  33 + 53 + 52+  81  +   55  + 19+ 49 + 33+  77  +15+ 64 +7 + 20 +35+  73  +  46 + 19+13+ 33 + 70 + 30 +34+  52 + 53+ 33 + 7 =1336
    And the angel of the LORD said unto her, I will multiply thy seed exceedingly, that it shall not be numbered for multitude.
     19+ 33+  39 +21+ 33+ 49 + 33 + 70 + 31 +9+ 56 +  128   + 53+ 33 +    113     + 49 +29+  52 + 49+7 +   82   + 39+   125    =1152
    That in blessing I will bless thee, and in multiplying I will multiply thy seed as the stars of the heaven, and as the sand which is upon the sea shore; and thy seed shall possess the gate of his enemies;
     49 +23+   87   +9+ 56 +  57 +  38 + 19+23+    158    +9+ 56 +  128   + 53+ 33 +20+ 33+  77 +21+ 33+   55  + 19+20+ 33+ 38 +  51 +28+ 66 + 33+ 25+  65  + 19+ 53+ 33 +  52 +  112  + 33+ 33 +21+ 36+   70   =1877
    And I will make thy seed to multiply as the stars of heaven, and will give unto thy seed all these countries; and in thy seed shall all the nations of the earth be blessed;
     19+9+ 56 + 30 + 53+ 33 +35+  128   +20+ 33+  77 +21+   55  + 19+ 56 + 43 + 70 + 53+ 33 + 25+  57 +   124    + 19+23+ 53+ 33 +  52 + 25+ 33+   92  +21+ 33+  52 +7 +   66   =1558
    And thou saidst, I will surely do thee good, and make thy seed as the sand of the sea, which cannot be numbered for multitude.
     19+ 64 +   72  +9+ 56 + 100  +19+ 38 +  41 + 19+ 30 + 53+ 33 +20+ 33+ 38 +21+ 33+ 25 +  51 +  67  +7 +   82   + 39+   125    =1094
    Remember Abraham, Isaac, and Israel, thy servants, to whom thou swarest by thine own self, and saidst unto them, I will multiply your seed as the stars of heaven, and all this land that I have spoken of will I give unto your seed, and they shall inherit it for ever.
       79   +   44   +  33  + 19+   64  + 53+   118   +35+ 59 + 64 +  105  +27+  56 + 52+  42 + 19+  72  + 70 +  46 +9+ 56 +  128   + 79 + 33 +20+ 33+  77 +21+   55  + 19+ 25+ 56 + 31 + 49 +9+ 36 +  80  +21+ 56 +9+ 43 + 70 + 79 +  33 + 19+ 58 +  52 +   83  +29+ 39+  50 =2514
    As the host of heaven cannot be numbered, neither the sand of the sea measured: so will I multiply the seed of David my servant, and the Levites that minister unto me.
    20+ 33+ 62 +21+  55  +  67  +7 +    82   +   79  + 33+ 38 +21+ 33+ 25+    86   +34+ 56 +9+  128   + 33+ 33 +21+  40 +38+   99   + 19+ 33+   92  + 49 +  107   + 70 + 18=1541
    >>> 
    >>> tell(lsum,osum,ssum,'the dust')
    the dust
     3 + 4  = 7
     33+ 64 = 97
    213+604 =817
    >>> tell(lsum,osum,ssum,'the stars')
    the stars
     3 +  5  = 8
     33+  77 =110
    213+ 491 =704
    >>> 
    >>> 
    >>> tell(lsum,osum,ssum,'thy seed')
    thy seed
     3 + 4  = 7
     53+ 33 = 86
    908+114 =1022
    >>> tell(lsum,osum,ssum,'dust of the earth')
    dust of the earth
     4  +2 + 3 +  5  = 14
     64 +21+ 33+  52 =170
    604 +66+213+ 304 =1187
    >>> b.chapter(1187)
    Revelation 20:1-15 (15 verses)
    >>> tell(lsum,osum,ssum,'stars of heaven')
    stars of heaven
      5  +2 +  6   = 13
      77 +21+  55  =153
     491 +66+ 469  =1026
    >>> Deuteronomy.chc()
    34
    >>> tell('זַרְעֶֽךָ׃')
    זַ  רְ עֶֽ  ךָ׃
    7+20+16+11=54
    >>> tell('צְדָקָה')
     צְ דָ  קָ ה
    18+4+19+5=46
    >>> np(53)
    16
    >>> sof(53)
    54
    >>> nsof(144)
    [66, 70, 94, 115, 119]
    >>> sof(70)
    144
    >>> Job/'Arcturus'
    Job 9:9 Which maketh Arcturus, Orion, and Pleiades, and the chambers of the south.
    Job 38:32 Canst thou bring forth Mazzaroth in his season? or canst thou guide Arcturus with his sons?
    >>> Job[38:31:32].tell(osum,ssum)
    Canst thou bind the sweet influences of Pleiades,  or loose the bands of Orion?
      57 + 64 + 29 + 33+  72 +   108    +21+    71   + 33+  66 + 33+  40 +21+  71  =719
     354 +568 + 65 +213+ 810 +   558    +66+   224   +150+ 255 +213+ 157 +66+ 269  =3968
    Canst thou bring forth Mazzaroth in his season?  or canst thou guide Arcturus with his sons?
      57 + 64 +  50 +  67 +   128   +23+ 36+   73  + 33+  57 + 64 +  46 +  121   + 60 + 36+  67 =982
     354 +568 + 158 + 364 +   2000  +59+117+  316  +150+ 354 +568 + 325 +  1084  +717 +117+ 310 =7561
    >>> tell('his sons')
    his sons
     36+ 67 =103
    >>> 789629/math.pi
    251346.71711742046
    >>> sums('the sweet influences')
    (213, 1581)
    >>> sums('sweet influences')
    (180, 1368)
    >>> tell(osum,ssum,'loose the bands')
    loose the bands
      66 + 33+  40 =139
     255 +213+ 157 =625
    >>> tell('his sons')
    his sons
     36+ 67 =103
    >>> tell('thou guide')
    thou guide
     64 +  46 =110
    >>> sums('sheep')
    (53, 188)
    >>> sums('the stars')
    (110, 704)
    >>> sums('stars')
    (77, 491)
    >>> sums('star')
    (58, 391)
