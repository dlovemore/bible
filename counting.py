    >>> from bible import *
    >>> b/"counting"
    Ecclesiastes 7:27 Behold, this have I found, saith the preacher, counting one by one, to find out the account:
    >>> _.tell()
    Behold, this have I found, saith the preacher, counting one by one, to find out the account:
       46  + 56 + 36 +9+  60  +  57 + 33+    74   +  103   + 34+27+ 34 +35+ 33 + 56+ 33+   77   =803
    >>> _.tell(lsum)
    Behold, this have I found, saith the preacher, counting one by one, to find out the account:
       6   + 4  + 4  +1+  5   +  5  + 3 +    8    +   8    + 3 +2 + 3  +2 + 4  + 3 + 3 +   7    =71
    >>> 
    >>> tell('God',ssum)
    G o  d
    7+60+4=71
    >>> 7*27
    189
    >>> tell('Solomon')
    S  o  l  o  m  o  n
    19+15+12+15+13+15+14=103
    >>> tell('counting')
    c o  u  n  t  i n  g
    3+15+21+14+20+9+14+7=103
    >>> tell('account')
    a c c o  u  n  t
    1+3+3+15+21+14+20=77
    >>> 
    >>> 
    >>> count('one')*count('one')
    1156
    >>> b.chaptercount()
    1189
    >>> 1189-1156
    33

Expecting one x one to be the number of books in the biblical account, we find it is out 33 or out by the count of "the".

    >>> tell('the')
    t  h e
    20+8+5=33

Another way to look at this is that we should find out "the" account. This is marked by 33. There are 33 words in Psalm 117.
This is also the middle chapter of the 1189 chapters and the shortest chapter.

    >>> Psalm[117]
    Psalms 117:1 O praise the LORD, all ye nations: praise him, all ye people.
    Psalms 117:2 For his merciful kindness is great toward us: and the truth of the LORD endureth for ever. Praise ye the LORD.

    >>> show('Psalm[117].wordcount()')
    Psalm[117].wordcount() = 33
    >>> l=[(c.wc(),c) for c in bible.chapters()]
    >>> sorted(l)[:7]
    [(33, Psalms 117:1 O praise the LORD, all ye nations: praise him, all ye people.
    Psalms 117:2 For his merciful kindness is great toward us: and the truth of the LORD endureth for ever. Praise ye the LORD.), (44, Psalms 134:1-3 (3 verses)), (60, Psalms 131:1-3 (3 verses)), (69, Psalms 133:1-3 (3 verses)), (85, Psalms 150:1-6 (6 verses)), (86, Psalms 100:1-5 (5 verses)), (88, Psalms 120:1-7 (7 verses))]
    >>> sorted(l)[-7:]
    [(1820, Ezekiel 16:1-63 (63 verses)), (1853, Jeremiah 51:1-64 (64 verses)), (1857, Leviticus 13:1-59 (59 verses)), (1939, Numbers 7:1-89 (89 verses)), (2075, Deuteronomy 28:1-68 (68 verses)), (2139, 1 Kings 8:1-66 (66 verses)), (2423, Psalms 119:1-176 (176 verses))]
    >>> 
    >>> l=[(c.vc(),c) for c in bible.chapters()]
    >>> l.sort()
    >>> l[-7:]
    [(72, Mark 14:1-72 (72 verses)), (73, Nehemiah 7:1-73 (73 verses)), (75, Matthew 26:1-75 (75 verses)), (80, Luke 1:1-80 (80 verses)), (81, 1 Chronicles 6:1-81 (81 verses)), (89, Numbers 7:1-89 (89 verses)), (176, Psalms 119:1-176 (176 verses))]
    >>> 
    >>> 
    >>> 
    >>> 
    >>> 
    >>> 

    >>> b.chapter(666)
    Ecclesiastes 7:1-29 (29 verses)
    >>> b/"here is wisdom"
    Revelation 13:18 Here is wisdom. Let him that hath understanding count the number of the beast: for it is the number of a man; and his number is Six hundred threescore and six.
    >>> _.tell()
    Here is wisdom. Let him that hath understanding count the number of the beast: for it is the number of a man; and his number is Six hundred threescore and six.
     36 +28+   83  + 37+ 30+ 49 + 37 +     150     +  73 + 33+  73  +21+ 33+  47  + 39+29+28+ 33+  73  +21+1+ 28 + 19+ 36+  73  +28+ 52+   74  +   116    + 19+ 52 =1451
    >>> 52+74+116+47
    289
    >>> _+19
    308
    >>> b/"rightly dividing"
    2 Timothy 2:15 Study to shew thyself approved unto God, a workman that needeth not to be ashamed, rightly dividing the word of truth.
    >>> tell("Solomon")
    S  o  l  o  m  o  n
    19+15+12+15+13+15+14=103
    >>> tell("counting")
    c o  u  n  t  i n  g
    3+15+21+14+20+9+14+7=103
    >>> b.midv()
    Psalms 103:1 Bless the LORD, O my soul: and all that is within me, bless his holy name.
    Psalms 103:2 Bless the LORD, O my soul, and forget not all his benefits:
    >>> b/"MENE"
    Daniel 5:25 And this is the writing that was written, MENE, MENE, TEKEL, UPHARSIN.
    Daniel 5:26 This is the interpretation of the thing: MENE; God hath numbered thy kingdom, and finished it.
    >>> tell("MENE MENE")
    MENE MENE
     37 + 37 =74
    >>> tell("Jesus")
    J  e s  u  s
    10+5+19+21+19=74
    >>> 37+37
    74
    >>> tell("TEKEL UPHARSIN")
    TEKEL UPHARSIN
      53 +  106   =159
    >>> tell("mene mene tekel upharsin",ssum)
    mene mene tekel upharsin
    100 +100 + 260 +  628   =1088
    >>> tell('upharsin',ssum)
     u  p  h a r   s  i n
    300+70+8+1+90+100+9+50=628
    >>> sums('peres')
    (63, 270)
    >>> b.bookix[25]
    20465
    >>> b.v(20466)
    'Now it came to pass in the thirtieth year, in the fourth month, in the fifth day of the month, as I was among the captives by the river of Chebar, that the heavens were opened, and I saw visions of God.'
    >>> b.chapter(855)
    Daniel 5:1-31 (31 verses)
    >>> Daniel[5:]
    Daniel 5:1-31 (31 verses)
    >>> p(_)
    Daniel 5
    1 Belshazzar the king made a great feast to a thousand of his lords, and drank wine before the thousand.
    2 Belshazzar, whiles he tasted the wine, commanded to bring the golden and silver vessels which his father Nebuchadnezzar had taken out of the temple which was in Jerusalem; that the king, and his princes, his wives, and his concubines, might drink therein.
    3 Then they brought the golden vessels that were taken out of the temple of the house of God which was at Jerusalem; and the king, and his princes, his wives, and his concubines, drank in them.
    4 They drank wine, and praised the gods of gold, and of silver, of brass, of iron, of wood, and of stone.
    5 In the same hour came forth fingers of a man's hand, and wrote over against the candlestick upon the plaister of the wall of the king's palace: and the king saw the part of the hand that wrote.
    6 Then the king's countenance was changed, and his thoughts troubled him, so that the joints of his loins were loosed, and his knees smote one against another.
    7 The king cried aloud to bring in the astrologers, the Chaldeans, and the soothsayers. And the king spake, and said to the wise men of Babylon, Whosoever shall read this writing, and shew me the interpretation thereof, shall be clothed with scarlet, and have a chain of gold about his neck, and shall be the third ruler in the kingdom.
    8 Then came in all the king's wise men: but they could not read the writing, nor make known to the king the interpretation thereof.
    9 Then was king Belshazzar greatly troubled, and his countenance was changed in him, and his lords were astonied.
    10 Now the queen by reason of the words of the king and his lords came into the banquet house: and the queen spake and said, O king, live for ever: let not thy thoughts trouble thee, nor let thy countenance be changed:
    11 There is a man in thy kingdom, in whom is the spirit of the holy gods; and in the days of thy father light and understanding and wisdom, like the wisdom of the gods, was found in him; whom the king Nebuchadnezzar thy father, the king, I say, thy father, made master of the magicians, astrologers, Chaldeans, and soothsayers;
    12 Forasmuch as an excellent spirit, and knowledge, and understanding, interpreting of dreams, and shewing of hard sentences, and dissolving of doubts, were found in the same Daniel, whom the king named Belteshazzar: now let Daniel be called, and he will shew the interpretation.
    13 Then was Daniel brought in before the king. And the king spake and said unto Daniel, Art thou that Daniel, which art of the children of the captivity of Judah, whom the king my father brought out of Jewry?
    14 I have even heard of thee, that the spirit of the gods is in thee, and that light and understanding and excellent wisdom is found in thee.
    15 And now the wise men, the astrologers, have been brought in before me, that they should read this writing, and make known unto me the interpretation thereof: but they could not shew the interpretation of the thing:
    16 And I have heard of thee, that thou canst make interpretations, and dissolve doubts: now if thou canst read the writing, and make known to me the interpretation thereof, thou shalt be clothed with scarlet, and have a chain of gold about thy neck, and shalt be the third ruler in the kingdom.
    17 Then Daniel answered and said before the king, Let thy gifts be to thyself, and give thy rewards to another; yet I will read the writing unto the king, and make known to him the interpretation.
    18 O thou king, the most high God gave Nebuchadnezzar thy father a kingdom, and majesty, and glory, and honour:
    19 And for the majesty that he gave him, all people, nations, and languages, trembled and feared before him: whom he would he slew; and whom he would he kept alive; and whom he would he set up; and whom he would he put down.
    20 But when his heart was lifted up, and his mind hardened in pride, he was deposed from his kingly throne, and they took his glory from him:
    21 And he was driven from the sons of men; and his heart was made like the beasts, and his dwelling was with the wild asses: they fed him with grass like oxen, and his body was wet with the dew of heaven; till he knew that the most high God ruled in the kingdom of men, and that he appointeth over it whomsoever he will.
    22 And thou his son, O Belshazzar, hast not humbled thine heart, though thou knewest all this;
    23 But hast lifted up thyself against the Lord of heaven; and they have brought the vessels of his house before thee, and thou, and thy lords, thy wives, and thy concubines, have drunk wine in them; and thou hast praised the gods of silver, and gold, of brass, iron, wood, and stone, which see not, nor hear, nor know: and the God in whose hand thy breath is, and whose are all thy ways, hast thou not glorified:
    24 Then was the part of the hand sent from him; and this writing was written.
    25 And this is the writing that was written, MENE, MENE, TEKEL, UPHARSIN.
    26 This is the interpretation of the thing: MENE; God hath numbered thy kingdom, and finished it.
    27 TEKEL; Thou art weighed in the balances, and art found wanting.
    28 PERES; Thy kingdom is divided, and given to the Medes and Persians.
    29 Then commanded Belshazzar, and they clothed Daniel with scarlet, and put a chain of gold about his neck, and made a proclamation concerning him, that he should be the third ruler in the kingdom.
    30 In that night was Belshazzar the king of the Chaldeans slain.
    31 And Darius the Median took the kingdom, being about threescore and two years old.
    >>> 
    >>> 
    >>> 
    >>> Genesis
    Genesis 1:1-50:26 (1533 verses)
    >>> b.v(1533), b.v(1534)
    ('So Joseph died, being an hundred and ten years old: and they embalmed him, and he was put in a coffin in Egypt.', 'Now these are the names of the children of Israel, which came into Egypt; every man and his household came with Jacob.')
    >>> b.bookix
    [0, 1533, 2746, 3605, 4893, 5852, 6510, 7128, 7213, 8023, 8718, 9534, 10253, 11195, 12017, 12297, 12703, 12870, 13940, 16401, 17316, 17538, 17655, 18947, 20311, 20465, 21738, 22095, 22292, 22365, 22511, 22532, 22580, 22685, 22732, 22788, 22841, 22879, 23090, 23145, 24216, 24894, 26045, 26924, 27931, 28364, 28801, 29058, 29207, 29362, 29466, 29561, 29650, 29697, 29810, 29893, 29939, 29964, 30267, 30375, 30480, 30541, 30646, 30659, 30673, 30698, 31102]
    >>> Daniel[5:25].tell()
    And this is the writing that was written, MENE, MENE, TEKEL, UPHARSIN.
     19+ 56 +28+ 33+  100  + 49 + 43+  109   +  37 +  37 +  53  +   106   =670
    >>> Daniel[5:].wc()
    995
    >>> pf(995)
    Counter({5: 1, 199: 1})
    >>> np(137)
    33
    >>> np(103)
    27
    >>> pn(count('az'))
    103
    >>> pn(39)
    167
    >>> np(929)
    158
    >>> npp(929)
    20
    >>> 
    >>> 
    >>> 
    >>> 
    >>> 
    >>> 
    >>> 
    >>> 
    >>> 
    >>> b.book([33,34])
    [Micah 1:1-7:20 (105 verses), Nahum 1:1-3:19 (47 verses)]
    >>> nt=b.Matthew-b.Revelation
    >>> nt
    Matthew 1:1-Revelation 22:21 (7957 verses)
    >>> nt.midch()
    Romans 13:1-14:23 (37 verses)
    >>> b.Romans[13:]
    Romans 13:1-14 (14 verses)
    >>> 
    >>> b/"the first"/"the last"
    Nehemiah 8:18...Revelation 22:13 (15 verses)
    >>> p(_)
    Nehemiah 8:18 Also day by day, from the first day unto the last day, he read in the book of the law of God. And they kept the feast seven days; and on the eighth day was a solemn assembly, according unto the manner.
    Isaiah 41:4 Who hath wrought and done it, calling the generations from the beginning? I the LORD, the first, and with the last; I am he.
    Isaiah 44:6 Thus saith the LORD the King of Israel, and his redeemer the LORD of hosts; I am the first, and I am the last; and beside me there is no God.
    Isaiah 48:12 Hearken unto me, O Jacob and Israel, my called; I am he; I am the first, I also am the last.
    Matthew 12:45 Then goeth he, and taketh with himself seven other spirits more wicked than himself, and they enter in and dwell there: and the last state of that man is worse than the first. Even so shall it be also unto this wicked generation.
    Matthew 20:8 So when even was come, the lord of the vineyard saith unto his steward, Call the labourers, and give them their hire, beginning from the last unto the first.
    Matthew 20:16 So the last shall be first, and the first last: for many be called, but few chosen.
    Matthew 27:64 Command therefore that the sepulchre be made sure until the third day, lest his disciples come by night, and steal him away, and say unto the people, He is risen from the dead: so the last error shall be worse than the first.
    Luke 11:26 Then goeth he, and taketh to him seven other spirits more wicked than himself; and they enter in, and dwell there: and the last state of that man is worse than the first.
    1 Corinthians 15:45 And so it is written, The first man Adam was made a living soul; the last Adam was made a quickening spirit.
    Revelation 1:11 Saying, I am Alpha and Omega, the first and the last: and, What thou seest, write in a book, and send it unto the seven churches which are in Asia; unto Ephesus, and unto Smyrna, and unto Pergamos, and unto Thyatira, and unto Sardis, and unto Philadelphia, and unto Laodicea.
    Revelation 1:17 And when I saw him, I fell at his feet as dead. And he laid his right hand upon me, saying unto me, Fear not; I am the first and the last:
    Revelation 2:8 And unto the angel of the church in Smyrna write; These things saith the first and the last, which was dead, and is alive;
    Revelation 2:19 I know thy works, and charity, and service, and faith, and thy patience, and thy works; and the last to be more than the first.
    Revelation 22:13 I am Alpha and Omega, the beginning and the end, the first and the last.
    >>> b/'MOTHER OF HARLOTS'
    Revelation 17:5 And upon her forehead was a name written, MYSTERY, BABYLON THE GREAT, THE MOTHER OF HARLOTS AND ABOMINATIONS OF THE EARTH.
    >>> 'MYSTERY, BABYLON THE GREAT, THE MOTHER OF HARLOTS AND ABOMINATIONS OF THE EARTH.'
    'MYSTERY, BABYLON THE GREAT, THE MOTHER OF HARLOTS AND ABOMINATIONS OF THE EARTH.'
    >>> tell(_)
    MYSTERY, BABYLON THE GREAT, THE MOTHER OF HARLOTS AND ABOMINATIONS OF THE EARTH.
      125   +   71  + 33+  51  + 33+  79  +21+   93  + 19+    132     +21+ 33+  52  =763
    >>> tell(_,ascsum)
    MYSTERY, BABYLON THE GREAT, THE MOTHER  OF HARLOTS AND ABOMINATIONS  OF THE EARTH.
      573   +  519  +225+ 371  +225+ 463  +149+  541  +211+    900     +149+225+ 372  =4923
    >>> tell('λατεινος',ssum)
    λ  α  τ  ε ι  ν  ο   ς
    30+1+300+5+10+50+70+200=666
    >>> tell('רומיית',ssum)
     ר  ו מ  י  י   ת
    200+6+40+10+10+400=666
    >>> 
