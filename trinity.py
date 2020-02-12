# >>> from bible import *
# >>> b/"counting"-29
# Ecclesiastes 7:27-29 (3 verses)
# >>> p(_)
# Ecclesiastes 7
# 27 Behold, this have I found, saith the preacher, counting one by one, to find out the account:
# 28 Which yet my soul seeketh, but I find not: one man among a thousand have I found; but a woman among all those have I not found.
# 29 Lo, this only have I found, that God hath made man upright; but they have sought out many inventions.
# >>> _.tell()
# Behold, this have I found, saith the preacher, counting one by one, to find out the account:
#    46  + 56 + 36 +9+  60  +  57 + 33+    74   +  103   + 34+27+ 34 +35+ 33 + 56+ 33+   77   =803
# Which yet my soul seeketh, but I find not: one man among a thousand have I found; but a woman among all those have I not found.
#   51 + 50+38+ 67 +   73   + 43+9+ 33 + 49 + 34+ 28+  50 +1+  102   + 36 +9+  60  + 43+1+  66 +  50 + 25+  67 + 36 +9+ 49+  60  =1139
# Lo, this only have I found, that God hath made man upright; but they have sought out many inventions.
#  27+ 56 + 66 + 36 +9+  60  + 49 + 26+ 37 + 23 + 28+   99   + 43+ 58 + 36 +  90  + 56+ 53 +    141    =993
# >>> tell('Solomon')
# S  o  l  o  m  o  n
# 19+15+12+15+13+15+14=103
# >>> 
# >>> b/"tale"/"bricks"
# Exodus 5:8 And the tale of the bricks, which they did make heretofore, ye shall lay upon them; ye shall not diminish ought thereof: for they be idle; therefore they cry, saying, Let us go and sacrifice to our God.
# Exodus 5:18 Go therefore now, and work; for there shall no straw be given you, yet shall ye deliver the tale of bricks.
# >>> b/"tale that is told"
# Psalms 90:9 For all our days are passed away in thy wrath: we spend our years as a tale that is told.
# >>> b/"profitable"/"instruction"-18
# 2 Timothy 3:16 All scripture is given by inspiration of God, and is profitable for doctrine, for reproof, for correction, for instruction in righteousness:
# 2 Timothy 3:17 That the man of God may be perfect, throughly furnished unto all good works.
# >>> 
# >>> b/"told"/"half"
# 1 Kings 10:7 Howbeit I believed not the words, until I came, and mine eyes had seen it: and, behold, the half was not told me: thy wisdom and prosperity exceedeth the fame which I heard.
# 2 Chronicles 9:6 Howbeit I believed not their words, until I came, and mine eyes had seen it: and, behold, the one half of the greatness of thy wisdom was not told me: for thou exceedest the fame that I heard.
# >>> sums('Solomon')
# (103, 400)
# >>> osum('Solomon')/2,ssum('Solomon')//2
# (51.5, 200)
# >>> ssum('Jesus')
# 515
# >>> 
# >>> 
# >>> tell('Lord Jesus Christ')
# Lord Jesus Christ
#  49 +  74 +  77  =200
# >>> tell('the water and the blood')
# the water and the blood
#  33+  67 + 19+ 33+  48 =200
# >>> b['1 John'][5:7]-8
# 1 John 5:7 For there are three that bear record in heaven, the Father, the Word, and the Holy Ghost: and these three are one.
# 1 John 5:8 And there are three that bear witness in earth, the Spirit, and the water, and the blood: and these three agree in one.
# >>> _.tell()
# For there are three that bear record in heaven, the Father, the Word, and the Holy Ghost: and these three are one.
#  39+  56 + 24+  56 + 49 + 26 +  63  +23+   55  + 33+   58  + 33+  60 + 19+ 33+ 60 +  69  + 19+  57 +  56 + 24+ 34 =946
# And there are three that bear witness in earth, the Spirit, and the water, and the blood: and these three agree in one.
#  19+  56 + 24+  56 + 49 + 26 +  109  +23+  52  + 33+   91  + 19+ 33+  67  + 19+ 33+  48  + 19+  57 +  56 +  36 +23+ 34 =982
# >>> _.tell(ssum)
# For there are three that bear record in heaven, the Father, the Word, and the Holy Ghost: and these three are one.
# 156+ 308 + 96+ 308 +409 + 98 + 252  +59+  469  +213+  310  +213+ 654 + 55+213+798 + 375  + 55+ 318 + 308 + 96+115 =5878
# And there are three that bear witness in earth, the Spirit, and the water, and the blood: and these three agree in one.
#  55+ 308 + 96+ 308 +409 + 98 +  964  +59+ 304  +213+  478  + 55+213+ 796  + 55+213+ 156  + 55+ 318 + 308 + 108 +59+115 =5743
# >>> tell('the son', ssum)
# the son
# 213+210 = 423
# >>> tell('Lord Jesus Christ',ssum)
# Lord Jesus Christ
#  184+  515+   410 = 1109
# >>> np(41)
# 13
# >>> prime(1)*prime(3)*prime(13)
# 410
# >>> pf(184)
# Counter({2: 3, 23: 1})
# >>> 2**3*23
# 184
# >>> tell('agree')
# a g  r e e
# 1+7+18+5+5 = 36
# >>> tell('these')
#  t h e  s e
# 20+8+5+19+5 = 57
# >>> 
# >>> 
# >>> tell('the Father the Word the Holy Ghost')
# the Father the Word the Holy Ghost
#  33+    58+ 33+  60+ 33+  60+   69 = 346
# >>> tell('the Spirit and the water and the blood')
# the Spirit and the water and the blood
#  33+    91+ 19+ 33+   67+ 19+ 33+   48 = 343
# >>> 
# >>> 343+3
# 346
# >>> 3,psum('Adam')
# (3, 46)
# >>> 2*prime(40)
# 346
# >>> factors(343)
# [7, 7, 7]
# >>> tell("Lord Jesus Christ")
# Lord Jesus Christ
#   49+   74+    77 = 200
# >>> 
# >>> tell('people')
#  p e  o  p  l e
# 16+5+15+16+12+5 = 69
# >>> tell('ghost')
# g h  o  s  t
# 7+8+15+19+20 = 69
# >>> tell('JeHOVAH')
#  J e H  O  V A H
# 10+5+8+15+22+1+8 = 69
# >>> osum('I am')*3
# 69
# >>> tell('holy')
# h  o  l  y
# 8+15+12+25 = 60
# >>> tell('spirit')
#  s  p i  r i  t
# 19+16+9+18+9+20 = 91
# >>> 
# >>> tell('Holy Ghost')
# Holy Ghost
#   60+   69 = 129
# >>> factors(343)
# [7, 7, 7]
# >>> 
# >>> tell('the Father the Word the Holy Ghost',ssum)
# the Father the Word the Holy Ghost
# 213+   310+213+ 654+213+ 798+  375 = 2776
# >>> tell('the Spirit and the water and the blood',ssum)
# the Spirit and the water and the blood
# 213+   478+ 55+213+  796+ 55+213+  156 = 2179
# >>> 2776-2179
# 597
# >>> factors(_)
# [3, 199]
# >>> tell('F W H G',ssum)
# F   W H G
# 6+500+8+7 = 521
# >>> tell('S',ssum)
#   S
# 100 = 100
# >>> tell('FWHG')
# F  W H G
# 6+23+8+7 = 44
# >>> tell('S')
#  S
# 19 = 19
# >>> 
# >>> 
# >>> tell('the Father the Word the Holy Ghost',lsum)
# the Father the Word the Holy Ghost
#   3+     6+  3+   4+  3+   4+    5 = 28
# >>> tell('the Spirit and the water and the blood',lsum)
# the Spirit and the water and the blood
#   3+     6+  3+  3+    5+  3+  3+    5 = 31
# >>> sums('and')
# (19, 55)
# >>> IJohn[5:7].tell(ssum)
# 5:7 For there are three that bear record in heaven, the Father, the Word, and the Holy Ghost: and these three are one.
#   0+156+  308+ 96+  308+ 409+  98+   252+59+    469+213+    310+213+  654+ 55+213+ 798+   375+ 55+  318+  308+ 96+ 115 = 5878
# >>> IJohn[5:8].tell(ssum)
# 5:8 And there are three that bear witness in earth, the Spirit, and the water, and the blood: and these three agree in one.
#   0+ 55+  308+ 96+  308+ 409+  98+    964+59+   304+213+    478+ 55+213+   796+ 55+213+   156+ 55+  318+  308+  108+59+ 115 = 5743
# >>> 
# >>> 
# >>> 213*3-597
# 42
# >>> 
