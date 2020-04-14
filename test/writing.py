    >>> from bible import *
    >>> b/'MENE'
    Daniel 5:25 And this is the writing that was written, MENE, MENE, TEKEL, UPHARSIN.
    Daniel 5:26 This is the interpretation of the thing: MENE; God hath numbered thy kingdom, and finished it.
    >>> Daniel[5:25]-31
    Daniel 5:25-31 (7 verses)
    >>> p(_)
    Daniel 5
    25 And this is the writing that was written, MENE, MENE, TEKEL, UPHARSIN.
    26 This is the interpretation of the thing: MENE; God hath numbered thy kingdom, and finished it.
    27 TEKEL; Thou art weighed in the balances, and art found wanting.
    28 PERES; Thy kingdom is divided, and given to the Medes and Persians.
    29 Then commanded Belshazzar, and they clothed Daniel with scarlet, and put a chain of gold about his neck, and made a proclamation concerning him, that he should be the third ruler in the kingdom.
    30 In that night was Belshazzar the king of the Chaldeans slain.
    31 And Darius the Median took the kingdom, being about threescore and two years old.
    >>> tell(lsum,osum,ssum,'MENE MENE TEKEL UPHARSIN')
    MENE MENE TEKEL UPHARSIN
     4  + 4  +  5  +   8    = 21
     37 + 37 +  53 +  106   =233
    100 +100 + 260 +  628   =1088
    >>> tell(lsum,osum,ssum,'PERES')
    P  E R  E  S
    1 +1+1 +1+ 1 = 5
    16+5+18+5+ 19= 63
    70+5+90+5+100=270
    >>> 
    >>> show('37 + 37')
    37 + 37 = 74
    >>> tell('Jesus')
     J e  s  u  s
    10+5+19+21+19 = 74
    >>> b.verse(1)-b.verse(106)
    Genesis 1:1-4:26 (106 verses)
    >>> _.midv()
    Genesis 2:22 And the rib, which the LORD God had taken from man, made he a woman, and brought her unto the man.
    Genesis 2:23 And Adam said, This is now bone of my bones, and flesh of my flesh: she shall be called Woman, because she was taken out of Man.
    >>> 
    >>> 
    >>> 
