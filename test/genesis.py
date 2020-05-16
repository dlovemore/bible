# >>> from bible import *
# >>> g11="בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ"
# >>> g12="וְהָאָרֶץ, הָיְתָה תֹהוּ וָבֹהוּ, וְחֹשֶׁךְ, עַל-פְּנֵי תְהוֹם; וְרוּחַ אֱלֹהִים, מְרַחֶפֶת עַל-פְּנֵי הַמָּיִם."
# >>> g11tl="aleph bereshiyt bara elohim eth hashamim v'eth haarets"
# >>> g11t="1 In-beginning created God - the-heaven and the-earth"
# >>> from htmldraw import *
# >>> tells(g11)
# בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת  הַשָּׁמַיִם וְאֵת הָאָרֶץ  =
#   6     3    5    2    5    3   4    28
#   76    23   41   23   62   29  44  298
#  913   203   86  401  395  407 296  2701
# >>> tells(g12)
# וְהָאָרֶץ, הָיְתָה תֹהוּ וָבֹהוּ, וְחֹשֶׁךְ, עַל-פְּנֵי תְהוֹם; וְרוּחַ אֱלֹהִים, מְרַחֶפֶת עַל-פְּנֵי הַמָּיִם.  =
#   5     4    3    4     4     5      4    4     5      5     5      4    52
#   50    42   33   19    46    69     46   40    41     80    69     41  576
#  302   420  411   19   334   240    451  220    86    728   240     95  3546
# >>> tells('In the begin ning God cre ate d the hea ven and the ear th.')
# In the begin ning God cre ate d the hea ven and the ear th.  =
# 2   3    5    4    3   3   3  1  3   3   3   3   3   3   2   44
# 23  33   37   44   26  26  26 4  33  14  41  19  33  24  28 411
# 59 213   73  116   71  98 206 4 213  14 455  55 213  96 208 2094
# >>> Genesis[1:1].tell(lsum,osum,ssum)
# In the beginning God created the heaven and the earth.  =
# 2   3      9      3     7     3    6     3   3    5     44
# 23  33     81     26    56    33   55    19  33   52   411
# 59 213    189     71   308   213  469    55 213  304   2094
# >>> divmod(2094,411)
# (5, 39)
# >>> divmod(2094,49)
# (42, 36)
# >>> pf(2094)
# >>> Genesis[1:1].tell(lsum,osum,ssum)
# Counter({2: 1, 3: 1, 349: 1})
# >>> 44+411+2094
# 2549
# >>> np(_)
# 373
# >>> npp(373)
# 13
# >>> np(373)
# 74
# >>> pn(pn(osum('Jesus')))
# 2549
# >>> osum(g11)
# 298
# >>> pf(_)
# Counter({2: 1, 149: 1})
# >>> 3*19
# 57
# >>> 
# >>> b/86
# Genesis 16:16 And Abram was fourscore and six years old, when Hagar bare Ishmael to Abram.
# >>> 
# >>> tell('In the beginning',lsum,osum,ssum)
# In the beginning  =
# 2   3      9      14
# 23  33     81    137
# 59 213    189    461
# >>> 411*5+39
# 2094
# >>> 
# >>> np(137)
# 33
# >>> np(461)
# 89
# >>> 
# >>> 
# >>> tell(lsum,osum,ssum,"בְּרֵא שִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם-וְ אֵת הָאָרֶץ")
# בְּרֵא שִׁית בָּרָא אֱלֹהִים אֵת  הַשָּׁמַיִם-וְ אֵת  הָאָרֶץ  =
#  3   3   3    5    2     6     2   4    28
#  23  53  23   41   23    68    23  44  298
# 203 710 203   86  401   401   401 296  2701
# >>> tell(lsum,osum,ssum,"בְּרֵא שִׁית בָּרָא אֱלֹהִ ים אֵת הַשָּׁמַ יִם וְ אֵת הָ אָרֶץ")
# בְּרֵא שִׁית בָּרָא אֱלֹהִ ים אֵת  הַשָּׁמַ יִם וְ אֵת  הָ אָרֶץ  =
#  3   3   3   3  2   2   3  2  1  2  1  3   28
#  23  53  23  18 23  23  39 23 6  23 5  39 298
# 203 710 203  36 50 401 345 50 6 401 5 291 2701
# >>> 8*37
# 296
# >>> p(Row(span(20))@Fibonacci)
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> tell(lsum,osum,ssum,g11)
# בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת  הַשָּׁמַיִם וְאֵת הָאָרֶץ  =
#   6     3    5    2    5    3   4    28
#   76    23   41   23   62   29  44  298
#  913   203   86  401  395  407 296  2701
# >>> tell(lsum,osum,ssum,g12)
# וְהָאָרֶץ, הָיְתָה תֹהוּ וָבֹהוּ, וְחֹשֶׁךְ, עַל-פְּנֵי תְהוֹם; וְרוּחַ אֱלֹהִים, מְרַחֶפֶת עַל-פְּנֵי הַמָּיִם.  =
#   5     4    3    4     4     5      4    4     5      5     5      4    52
#   50    42   33   19    46    69     46   40    41     80    69     41  576
#  302   420  411   19   334   240    451  220    86    728   240     95  3546
# >>> npf(302)
# {2: 1, 151: 36}
# >>> 73*37
# 2701
# >>> isperfect(28)
# True
## >>> [i for i in range(10000) if isperfect(i)]
# [0, 6, 28, 496, 8128]
# >>> (Genesis-Isaiah).chaptercount()
# 745
# >>> b.verse(496+1)
# Genesis 20:1 And Abraham journeyed from thence toward the south country, and dwelled between Kadesh and Shur, and sojourned in Gerar.
# >>> 
# >>> 
# >>> 
## >>> draw(th(table(zip(['א']+g11.split(),g11tl.split(),g11t.split()))))
# >>> 
# >>> from search import *
# >>> tell(g11[1:],lsum,osum,ssum)
# ְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת  הַשָּׁמַיִם וְאֵת הָאָרֶץ  =
#   5    3    5    2    5    3   4    27
#   74   23   41   23   62   29  44  296
#  911  203   86  401  395  407 296  2699
# >>> 
# >>> fs(2701)
# [37, 73]
# >>> Genesis[1:1].tell(lsum,osum,ssum)
# In the beginning God created the heaven and the earth.  =
# 2   3      9      3     7     3    6     3   3    5     44
# 23  33     81     26    56    33   55    19  33   52   411
# 59 213    189     71   308   213  469    55 213  304   2094
# >>> Genesis[1:2].tell(lsum,osum,ssum)
# And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.  =
#  3   3    5    3     7      4    3    4    3     8      3   4    3   4   2   3    4    3   3    6    2   3    5    4    3   4   2   3     6    110
#  19  33   52   43   116     52   19   50   19    91     43  66   33  15  21  33   30   19  33   91   21  26   59   66   33  15  21  33    86   1238
#  55 213  304  601   1277   196   55  473   55   370    601 480  213  15  66 213   84   55 213  478   66  71  509  480  213  15  66 213   896   8546
# >>> tell('Genes is',osum,ssum)
# Genes  is  =
#   50   28  78
#  167  109 276
# >>> sof(44)
# 84
# >>> 
# >>> sums('Jesus')
# (5, 74, 515)
# >>> Genesis[1:2].tell(lsum,osum,ssum)
# And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.  =
#  3   3    5    3     7      4    3    4    3     8      3   4    3   4   2   3    4    3   3    6    2   3    5    4    3   4   2   3     6    110
#  19  33   52   43   116     52   19   50   19    91     43  66   33  15  21  33   30   19  33   91   21  26   59   66   33  15  21  33    86   1238
#  55 213  304  601   1277   196   55  473   55   370    601 480  213  15  66 213   84   55 213  478   66  71  509  480  213  15  66 213   896   8546
# >>> Genesis[1:3:5].tell(lsum,osum,ssum)
# And God said, Let there be light: and there was light.  =
#  3   3    4    3    5   2    5     3    5    3    5     41
#  19  26   33   37   56  7    56    19   56   43   56   408
#  55  71  114  235  308  7   254    55  308  601  254   2262
# And God saw the light, that  it was good: and God divided the light from the darkness.  =
#  3   3   3   3    5     4    2   3    4    3   3     7     3    5    4    3      8      66
#  19  26  43  33   56    49   29  43   41   19  26    57    33   56   52   33     91    706
#  55  71 601 213  254   409  209 601  131   55  71   435   213  254  196  213    370    4351
# And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day.  =
#  3   3    6     3    5    3    3   3     8     2    6      5     3   3     7     3   3     7     4    3    5    3    91
#  19  26   37    33   56   30   19  33    91    13   37     58    19  33    76    19  33    90    51   33   72   30  908
#  55  71   73   213  254  705   55 213   370    13   73    274    55 213   526    55 213   306   600  213  405  705  5660
# >>> Genesis[2:22:23].tell(lsum,osum,ssum)
# And the rib, which the LORD God had taken from man, made he a woman, and brought her unto the man.  =
#  3   3   3     5    3   4    3   3    5    4    3    4   2  1   5     3     7     3   4    3   3    74
#  19  33  29    51   33  49   26  13   51   52   28   23  13 1   66    19    91    31  70   33  28  759
#  55 213 101   528  213 184   71  13  276  196   91   50  13 1  651    55   667   103 610  213  91  4395
# And Adam said, This  is now bone of  my bones, and flesh of  my flesh: she shall be called Woman, because she was taken out of Man.  =
#  3   4     4    4    2   3   4   2   2    5     3    5   2   2    5     3    5   2    6      5       7     3   3    5    3  2   3    97
#  19  19    33   56   28  52  36  21  38   55    19   50  21  38   50    32   52  7    37     66      56    32  43   51   56 21  28  1016
#  55  46   114  317  109 610 117  66 740  217    55  149  66 740  149   113  169  7    73    651     416   113 601  276  560 66  91  6686
# >>> 
# >>> fs(502411)
# [7, 13, 5521]
# >>> fs(411)
# [3, 137]
# >>> npf(411)
# {3: 2, 137: 33}
# >>> 3*prime(33)
# 411
# >>> Genesis[1:1].tell(lsum)
# In the beginning God created the heaven and the earth. =
# 2   3      9      3     7     3    6     3   3    5    44
# >>> Genesis[1:1].tell(ssum)
# In the beginning God created the heaven and the earth.  =
# 59 213    189     71   308   213  469    55 213  304   2094
# >>> (Genesis[1:1]-2).tell(ssum)
# In the beginning God created the heaven and the earth.  =
# 59 213    189     71   308   213  469    55 213  304   2094
# And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.  =
#  55 213  304  601   1277   196   55  473   55   370    601 480  213  15  66 213   84   55 213  478   66  71  509  480  213  15  66 213   896   8546
# >>> (Genesis[1:1]-5).tell()
# In the beginning God created the heaven and the earth.  =
# 23  33     81     26    56    33   55    19  33   52   411
# And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.  =
#  19  33   52   43   116     52   19   50   19    91     43  66   33  15  21  33   30   19  33   91   21  26   59   66   33  15  21  33    86   1238
# And God said, Let there be light: and there was light.  =
#  19  26   33   37   56  7    56    19   56   43   56   408
# And God saw the light, that it was good: and God divided the light from the darkness.  =
#  19  26  43  33   56    49  29  43   41   19  26    57    33   56   52   33     91    706
# And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day.  =
#  19  26   37    33   56   30   19  33    91    13   37     58    19  33    76    19  33    90    51   33   72   30  908
# >>> Genesis[1:1].count()
# 411
# >>> Genesis[1:1].count(ssum)
# 2094
# >>> pf(2094)
# Counter({2: 1, 3: 1, 349: 1})
# >>> npf(2094)
# {2: 1, 3: 2, 349: 70}
# >>> 
# >>> Genesis[1:1:5].count()
# 3671
# >>> p(pf(_))
# Counter({3671: 1})
# >>> np(_)
# 512
# >>> prime(2**9)
# 3671
# >>> 
# >>> (Genesis[1:1]-(2,3)).count()
# 37120
# >>> pf(_)
# Counter({2: 8, 5: 1, 29: 1})
# >>> 128*290
# 37120
# >>> (Genesis[1:1]-(2,3)).count(lsum)
# 3427
# >>> (Genesis[1:1]-(2,3)).count(ssum)
# 250798
# >>> pf(250798)
# Counter({2: 1, 125399: 1})
# >>> np(125399)
# 11769
# >>> npf(_)
# {3: 2, 3923: 544}
# >>> npf(544)
# {2: 1, 17: 7}
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> tell('יְהֹוָה אֱלֹהִים')
# יְהֹוָה אֱלֹהִים =
#  26    41  67
# >>> 2702*ns
# [2, 7, 193] [1, 4, 44]
# >>> 2*pn(4)*pn(44)
# 2702
# >>> b.vi(2701)
# Exodus 39:36 The table, and all the vessels thereof, and the shewbread,
# >>> b.vi(2702)
# Exodus 39:37 The pure candlestick, with the lamps thereof, even with the lamps to be set in order, and all the vessels thereof, and the oil for light,
# >>> Exodus/'table'/'breadth'
# Exodus 25:23 Thou shalt also make a table of shittim wood: two cubits shall be the length thereof, and a cubit the breadth thereof, and a cubit and a half the height thereof.
# Exodus 37:10 And he made the table of shittim wood: two cubits was the length thereof, and a cubit the breadth thereof, and a cubit and a half the height thereof:
# >>> 2*1.5
# 3.0
# >>> 7*7*7*3
# 1029
# >>> 17.75**3
# 5592.359375
# >>> 17.75**3*3
# 16777.078125
# >>> b.vi(16777)
# Proverbs 14:4 Where no oxen are, the crib is clean: but much increase is by the strength of the ox.
# >>> Proverbs/'strength'
# Proverbs 8:14,28;10:29;14:4;20:29;21:22;24:5,10;31:3,17,25 (11 verses)
# >>> p(_)
# Proverbs 8:14 Counsel is mine, and sound wisdom: I am understanding; I have strength.
# Proverbs 8:28 When he established the clouds above: when he strengthened the fountains of the deep:
# Proverbs 10:29 The way of the LORD is strength to the upright: but destruction shall be to the workers of iniquity.
# Proverbs 14:4 Where no oxen are, the crib is clean: but much increase is by the strength of the ox.
# Proverbs 20:29 The glory of young men is their strength: and the beauty of old men is the grey head.
# Proverbs 21:22 A wise man scaleth the city of the mighty, and casteth down the strength of the confidence thereof.
# Proverbs 24:5 A wise man is strong; yea, a man of knowledge increaseth strength.
# Proverbs 24:10 If thou faint in the day of adversity, thy strength is small.
# Proverbs 31
# 3 Give not thy strength unto women, nor thy ways to that which destroyeth kings.
# 17 She girdeth her loins with strength, and strengtheneth her arms.
# 25 Strength and honour are her clothing; and she shall rejoice in time to come.
# >>> 17.75**2
# 315.0625
# >>> _*2
# 630.125
# >>> Proverbs[2].chn()
# 630
# >>> Deuteronomy.vi(630)
# Deuteronomy 23:22 But if thou shalt forbear to vow, it shall be no sin in thee.
# >>> 315*1.5*2
# 945.0
# >>> 630.125*3
# 1890.375
# >>> 5**.5*17.75
# 39.690206600621266
# >>> 81*49
# 3969
# >>> 18*5**.5
# 40.24922359499622
# >>> 360
# 360
# >>> jc=5**.5*17.75*100
# >>> divmod(jc,1)
# (3969.0, 0.020660062126808043)
# >>> p(_[1]*360,_[1]*365,_[1]*365.25)
# 7.4376223656508955 7.540922676284936 7.546087691816638
# >>> 
# >>> 
# >>> _[1]*365
# 7.540922676284936
# >>> (jc/100)**2+(17.75*1.5)**2
# 2284.203125
# >>> _**.5
# 47.793337663318724
# >>> b[:79]
# Numbers 7:79;1 Chronicles 6:79;Psalms 119:79;Luke 1:79 (4 verses)
# >>> b[4][7][79]
# Numbers 7:79 His offering was one silver charger, the weight whereof was an hundred and thirty shekels, one silver bowl of seventy shekels, after the shekel of the sanctuary; both of them full of fine flour mingled with oil for a meat offering:
# >>> _.tell(lsum,osum,ssum)
# His offering was one silver charger, the weight whereof was an hundred and thirty shekels, one silver bowl of seventy shekels, after the shekel of the sanctuary; both of them full of fine flour mingled with oil for a meat offering:   =
#  3     8      3   3    6       7      3    6       7     3  2     7     3    6       7      3    6     4   2     7       7       5    3    6    2   3      9       4   2   4    4   2   4     5      7     4    3   3  1  4       8      186
#  36    80     43  34   85      60     33   72      80    43 15    74    19  100      79     34   85    52  21   110      79      50   33   60   21  33    122      45  21  46   51  21  34    72     64    60   36  39 1  39      80     2162
# 117   233    601 115  634     204    213  729     674   601 51   461    55  1207    268    115  634   592  66   1460    268     302  213  168   66 213    1445    270  66 253  366  66  70   486    145   717   99 156 1 246     233    14879
# >>> b[33][3:7]
# Micah 3:7 Then shall the seers be ashamed, and the diviners confounded: yea, they shall all cover their lips; for there is no answer of God.
# >>> _.tell()
# Then shall the seers be ashamed, and the diviners confounded: yea, they shall all cover their lips; for there is no answer of God.  =
#  47    52   33   66  7     51     19  33   100        101      31   58    52   25   63    60    56   39   56  28 29   80   21  26  1133
# >>> Numbers[7].vn()
# 3852
# >>> Numbers[7].chn()
# 124
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> base(12,411)
# [2, 10, 3]
# >>> 411-298
# 113
# >>> base(12,113)
# [9, 5]
