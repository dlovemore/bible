# >>> from bible import *
# >>> g11="א בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ"
# >>> g12="וְהָאָרֶץ, הָיְתָה תֹהוּ וָבֹהוּ, וְחֹשֶׁךְ, עַל-פְּנֵי תְהוֹם; וְרוּחַ אֱלֹהִים, מְרַחֶפֶת עַל-פְּנֵי הַמָּיִם."
# >>> g11tl="aleph bereshiyt bara elohim eth hashamim v'eth haarets"
# >>> g11t="1 In-beginning created God - the-heaven and the-earth"
# >>> from htmldraw import *
# >>> tell(lsum,osum,ssum,g11[2:])
# בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת  הַשָּׁמַיִם וְאֵת הָאָרֶץ
#   6   + 3 +  5  + 2 +  5  + 3 + 4  = 28
#   76  + 23+  41 + 23+  62 + 29+ 44 =298
#  913  +203+  86 +401+ 395 +407+296 =2701
# >>> tell(lsum,osum,ssum,g12)
# וְהָאָרֶץ, הָיְתָה תֹהוּ וָבֹהוּ, וְחֹשֶׁךְ, עַל-פְּנֵי תְהוֹם; וְרוּחַ אֱלֹהִים, מְרַחֶפֶת עַל-פְּנֵי הַמָּיִם.
#   5   + 4  + 3 +  4  +  4  +  5   +  4  + 4  +  5   +  5  +  5   +  4  = 52
#   50  + 42 + 33+  19 +  46 +  69  +  46 + 40 +  41  +  80 +  69  +  41 =576
#  302  +420 +411+  19 + 334 + 240  + 451 +220 +  86  + 728 + 240  +  95 =3546
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
## >>> draw(th(table(zip(g11.split(),g11tl.split(),g11t.split()))))
# >>> 
# >>> from search import *
# >>> tell(g11[1:],lsum,osum,ssum)
# בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת  הַשָּׁמַיִם וְאֵת הָאָרֶץ
#   6   + 3 +  5  + 2 +  5  + 3 + 4  = 28
#   76  + 23+  41 + 23+  62 + 29+ 44 =298
#  913  +203+  86 +401+ 395 +407+296 =2701
# >>> 
# >>> fs(2701)
# [37, 73]
# >>> Genesis[1:1].tell(lsum,osum,ssum)
# In the beginning God created the heaven and the earth.
# 2 + 3 +    9    + 3 +   7   + 3 +  6   + 3 + 3 +  5   = 44
# 23+ 33+    81   + 26+   56  + 33+  55  + 19+ 33+  52  =411
# 59+213+   189   + 71+  308  +213+ 469  + 55+213+ 304  =2094
# >>> Genesis[1:2].tell(lsum,osum,ssum)
# And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.
#  3 + 3 +  5  + 3 +   7   +  4  + 3 +  4  + 3 +   8    + 3 + 4  + 3 + 4  +2 + 3 +  4  + 3 + 3 +  6   +2 + 3 +  5  + 4  + 3 + 4  +2 + 3 +   6   =110
#  19+ 33+  52 + 43+  116  +  52 + 19+  50 + 19+   91   + 43+ 66 + 33+ 15 +21+ 33+  30 + 19+ 33+  91  +21+ 26+  59 + 66 + 33+ 15 +21+ 33+   86  =1238
#  55+213+ 304 +601+  1277 + 196 + 55+ 473 + 55+  370   +601+480 +213+ 15 +66+213+  84 + 55+213+ 478  +66+ 71+ 509 +480 +213+ 15 +66+213+  896  =8546
# >>> Genesis[1:3:5].tell(lsum,osum,ssum)
# And God said, Let there be light: and there was light.
#  3 + 3 +  4  + 3 +  5  +2 +  5   + 3 +  5  + 3 +  5   = 41
#  19+ 26+  33 + 37+  56 +7 +  56  + 19+  56 + 43+  56  =408
#  55+ 71+ 114 +235+ 308 +7 + 254  + 55+ 308 +601+ 254  =2262
# And God saw the light, that  it was good: and God divided the light from the darkness.
#  3 + 3 + 3 + 3 +  5   + 4  + 2 + 3 +  4  + 3 + 3 +   7   + 3 +  5  + 4  + 3 +    8    = 66
#  19+ 26+ 43+ 33+  56  + 49 + 29+ 43+  41 + 19+ 26+   57  + 33+  56 + 52 + 33+    91   =706
#  55+ 71+601+213+ 254  +409 +209+601+ 131 + 55+ 71+  435  +213+ 254 +196 +213+   370   =4351
# And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day.
#  3 + 3 +  6   + 3 +  5  + 3  + 3 + 3 +   8    +2 +  6   +  5   + 3 + 3 +   7   + 3 + 3 +   7   + 4  + 3 +  5  + 3  = 91
#  19+ 26+  37  + 33+  56 + 30 + 19+ 33+   91   +13+  37  +  58  + 19+ 33+   76  + 19+ 33+   90  + 51 + 33+  72 + 30 =908
#  55+ 71+  73  +213+ 254 +705 + 55+213+  370   +13+  73  + 274  + 55+213+  526  + 55+213+  306  +600 +213+ 405 +705 =5660
# >>> Genesis[2:22:23].tell(lsum,osum,ssum)
# And the rib, which the LORD God had taken from man, made he a woman, and brought her unto the man.
#  3 + 3 + 3  +  5  + 3 + 4  + 3 + 3 +  5  + 4  + 3  + 4  +2 +1+  5   + 3 +   7   + 3 + 4  + 3 + 3  = 74
#  19+ 33+ 29 +  51 + 33+ 49 + 26+ 13+  51 + 52 + 28 + 23 +13+1+  66  + 19+   91  + 31+ 70 + 33+ 28 =759
#  55+213+101 + 528 +213+184 + 71+ 13+ 276 +196 + 91 + 50 +13+1+ 651  + 55+  667  +103+610 +213+ 91 =4395
# And Adam said, This  is now bone of  my bones, and flesh of  my flesh: she shall be called Woman, because she was taken out of Man.
#  3 + 4  +  4  + 4  + 2 + 3 + 4  +2 + 2 +  5   + 3 +  5  +2 + 2 +  5   + 3 +  5  +2 +  6   +  5   +   7   + 3 + 3 +  5  + 3 +2 + 3  = 97
#  19+ 19 +  33 + 56 + 28+ 52+ 36 +21+ 38+  55  + 19+  50 +21+ 38+  50  + 32+  52 +7 +  37  +  66  +   56  + 32+ 43+  51 + 56+21+ 28 =1016
#  55+ 46 + 114 +317 +109+610+117 +66+740+ 217  + 55+ 149 +66+740+ 149  +113+ 169 +7 +  73  + 651  +  416  +113+601+ 276 +560+66+ 91 =6686
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
# In the beginning God created the heaven and the earth.
# 2 + 3 +    9    + 3 +   7   + 3 +  6   + 3 + 3 +  5   =44
# >>> Genesis[1:1].tell(ssum)
# In the beginning God created the heaven and the earth.
# 59+213+   189   + 71+  308  +213+ 469  + 55+213+ 304  =2094
# >>> (Genesis[1:1]-2).tell(ssum)
# In the beginning God created the heaven and the earth.
# 59+213+   189   + 71+  308  +213+ 469  + 55+213+ 304  =2094
# And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.
#  55+213+ 304 +601+  1277 + 196 + 55+ 473 + 55+  370   +601+480 +213+ 15 +66+213+  84 + 55+213+ 478  +66+ 71+ 509 +480 +213+ 15 +66+213+  896  =8546
# >>> (Genesis[1:1]-5).tell()
# In the beginning God created the heaven and the earth.
# 23+ 33+    81   + 26+   56  + 33+  55  + 19+ 33+  52  =411
# And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.
#  19+ 33+  52 + 43+  116  +  52 + 19+  50 + 19+   91   + 43+ 66 + 33+ 15 +21+ 33+  30 + 19+ 33+  91  +21+ 26+  59 + 66 + 33+ 15 +21+ 33+   86  =1238
# And God said, Let there be light: and there was light.
#  19+ 26+  33 + 37+  56 +7 +  56  + 19+  56 + 43+  56  =408
# And God saw the light, that it was good: and God divided the light from the darkness.
#  19+ 26+ 43+ 33+  56  + 49 +29+ 43+  41 + 19+ 26+   57  + 33+  56 + 52 + 33+    91   =706
# And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day.
#  19+ 26+  37  + 33+  56 + 30 + 19+ 33+   91   +13+  37  +  58  + 19+ 33+   76  + 19+ 33+   90  + 51 + 33+  72 + 30 =908
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
# יְהֹוָה אֱלֹהִים
#  26 +  41 =67
