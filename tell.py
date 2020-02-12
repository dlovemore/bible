# >>> from bible import *
# >>> b/'counting'
# Ecclesiastes 7:27 Behold, this have I found, saith the preacher, counting one by one, to find out the account:
# >>> _.chn()
# 666
# >>> Revelation/'here is wisdom'
# Revelation 13:18 Here is wisdom. Let him that hath understanding count the number of the beast: for it is the number of a man; and his number is Six hundred threescore and six.
# >>> 
# >>> tell('counting')
# c  o  u  n  t i  n g
# 3+15+21+14+20+9+14+7 = 103
# >>> tell('Solomon')
#  S  o  l  o  m  o  n
# 19+15+12+15+13+15+14 = 103
# >>> b.midv()
# Psalms 103:1 Bless the LORD, O my soul: and all that is within me, bless his holy name.
# Psalms 103:2 Bless the LORD, O my soul, and forget not all his benefits:
# >>> b.vc()
# 31102
# >>> 
# >>> tell('Solomon',ssum)
#   S  o  l  o  m  o  n
# 100+60+30+60+40+60+50 = 400
# >>> IKings/'half'/'told'
# 1 Kings 10:7 Howbeit I believed not the words, until I came, and mine eyes had seen it: and, behold, the half was not told me: thy wisdom and prosperity exceedeth the fame which I heard.
# >>> 400//2
# 200
# >>> tell('Lord Jesus Christ')
# Lord Jesus Christ
#   49+   74+    77 = 200
# >>> tell('the water, and the blood')
# the water, and the blood
#  33+    67+ 19+ 33+   48 = 200
# >>> tell('the water'),tell('and the blood')
# the water
#  33+   67 = 100
# and the blood
#  19+ 33+   48 = 100
# (None, None)
# >>> tell('the Spirit, and the water, and the blood')
# the Spirit, and the water, and the blood
#  33+     91+ 19+ 33+    67+ 19+ 33+   48 = 343
# >>> 7*7*7
# 343
# >>> tell('the Father, the Word, the Holy Ghost')
# the Father, the Word, the Holy Ghost
#  33+     58+ 33+   60+ 33+  60+   69 = 346
# >>> 343+3
# 346
# >>> IJohn[5:7]-8
# 1 John 5:7 For there are three that bear record in heaven, the Father, the Word, and the Holy Ghost: and these three are one.
# 1 John 5:8 And there are three that bear witness in earth, the Spirit, and the water, and the blood: and these three agree in one.
# >>> tell('the Father, the Word and the Holy Ghost',lsum)
# the Father, the Word and the Holy Ghost
#   3+      6+  3+   4+  3+  3+   4+    5 = 31
# >>> tell('the Spirit, and the water, and the blood',lsum)
# the Spirit, and the water, and the blood
#   3+      6+  3+  3+     5+  3+  3+    5 = 31
# >>> tell('the Father, the Word and the Holy Ghost')
# the Father, the Word and the Holy Ghost
#  33+     58+ 33+  60+ 19+ 33+  60+   69 = 365
# >>> tell('the Father, the Word + the Holy Ghost')
# the Father, the Word + the Holy Ghost
#  33+     58+ 33+  60+0+ 33+  60+   69 = 346
# >>> tell('the Spirit, and the water, and the blood')
# the Spirit, and the water, and the blood
#  33+     91+ 19+ 33+    67+ 19+ 33+   48 = 343
# >>> tell('the Spirit,and the-water, and-the-blood')
# the Spirit,and the-water, and-the-blood
#  33+       110+       100+          100 = 343
# >>> 7*7*7
# 343
# >>> _+3
# 346
# >>> tell('Lord')
#  L  o  r d
# 12+15+18+4 = 49
# >>> 7*7
# 49
# >>> tell('Christ')
# C h  r i  s  t
# 3+8+18+9+19+20 = 77
# >>> 
# >>> 
# >>> 
# >>> tell('the Father, the Word and the Holy Ghost',ssum)
# the Father, the Word and the Holy Ghost
# 213+    310+213+ 654+ 55+213+ 798+  375 = 2831
# >>> tell('the Spirit, and the water, and the blood',ssum)
# the Spirit, and the water, and the blood
# 213+    478+ 55+213+   796+ 55+213+  156 = 2179
# >>> 2831+3
# 2834
# >>> pf(2831+3)
# Counter({2: 1, 13: 1, 109: 1})
# >>> 26*109
# 2834
# >>> osum('bear')*osum('witness')
# 2834
# >>> osum('witness')*osum('God')
# 2834
# >>> osum('man'),osum('one')
# (28, 34)
# >>> pn(osum('witness')*3)
# 2179
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> (IJohn[5:7]-8).tell(ssum)
# 5:7 For there are three that bear record in heaven, the Father, the Word, and the Holy Ghost: and these three are one.
#   0+156+  308+ 96+  308+ 409+  98+   252+59+    469+213+    310+213+  654+ 55+213+ 798+   375+ 55+  318+  308+ 96+ 115 = 5878
# 5:8 And there are three that bear witness in earth, the Spirit, and the water, and the blood: and these three agree in one.
#   0+ 55+  308+ 96+  308+ 409+  98+    964+59+   304+213+    478+ 55+213+   796+ 55+213+   156+ 55+  318+  308+  108+59+ 115 = 5743
# >>> 5878-5743
# 135
# >>> 
# >>> 
# >>> tells=b/'tell'
# >>> tells.vi(1)
# Genesis 12:18 And Pharaoh called Abram and said, What is this that thou hast done unto me? why didst thou not tell me that she was thy wife?
# >>> tell('me')
#  m e
# 13+5 = 18
# >>> tell('me that she was thy wife')
# me that she was thy wife
# 18+  49+ 32+ 43+ 53+  43 = 238
# >>> tells.vi(2)
# Genesis 15:5 And he brought him forth abroad, and said, Look now toward heaven, and tell the stars, if thou be able to number them: and he said unto him, So shall thy seed be.
# >>> tell('the stars')
# the stars
#  33+   77 = 110
# >>> tell('Christ')
# C h  r i  s  t
# 3+8+18+9+19+20 = 77
# >>> Luke[3:].count('son of')
# 77
# >>> tell('Jesus',ssum)
#  J e   s   u   s
# 10+5+100+300+100 = 515
# >>> 
# >>> tells.vi(3)
# Genesis 21:26 And Abimelech said, I wot not who hath done this thing; neither didst thou tell me, neither yet heard I of it, but to day.
# >>> _.tell()
# 21:26 And Abimelech said, I wot not who hath done this thing; neither didst thou tell me, neither yet heard I of it, but to day.
#     0+ 19+       58+   33+9+ 58+ 49+ 46+  37+  38+  56+    58+     79+   56+  64+  49+ 18+     79+ 50+   36+9+21+ 29+ 43+35+  30 = 1059
# >>> 
# >>> tells.vi(4)
# Genesis 22:2 And he said, Take now thy son, thine only son Isaac, whom thou lovest, and get thee into the land of Moriah; and offer him there for a burnt offering upon one of the mountains which I will tell thee of.
# >>> _.tell()
# 22:2 And he said, Take now thy son, thine only son Isaac, whom thou lovest, and get thee into the land of Moriah; and offer him there for a burnt offering upon one of the mountains which I will tell thee of.
#    0+ 19+13+   33+  37+ 52+ 53+  48+   56+  66+ 48+    33+  59+  64+     93+ 19+ 32+  38+  58+ 33+  31+21+     64+ 19+   50+ 30+   56+ 39+1+   75+      80+  66+ 34+21+ 33+      126+   51+9+  56+  49+  38+ 21 = 1824
# >>> 
# >>> tells.vi(5)
# Genesis 24:23 And said, Whose daughter art thou? tell me, I pray thee: is there room in thy father's house for us to lodge in?
# >>> tell('me I pray thee')
# me I pray thee
# 18+9+  60+  38 = 125
# >>> 5*5*5
# 125
# >>> tell('Bethlehem Ephratah')
# Bethlehem Ephratah
#        78+      77 = 155
# >>> 
# >>> tells.vi(6)
# Genesis 24:49 And now if ye will deal kindly and truly with my master, tell me: and if not, tell me; that I may turn to the right hand, or to the left.
# >>> 
# >>> tells.vi(7)
# Genesis 26:2 And the LORD appeared unto him, and said, Go not down into Egypt; dwell in the land which I shall tell thee of:
# >>> tell('thee of')
# thee of
#   38+21 = 59
# >>> 
# >>> tells.vi(8)
# Genesis 29:15 And Laban said unto Jacob, Because thou art my brother, shouldest thou therefore serve me for nought? tell me, what shall thy wages be?
# >>> tell('what shall thy wages be?')
# what shall thy wages be?
#   52+   52+ 53+   55+  7 = 219
# >>> 
# >>> tells.vi(9)
# Genesis 31:27 Wherefore didst thou flee away secretly, and steal away from me; and didst not tell me, that I might have sent thee away with mirth, and with songs, with tabret, and with harp?
# >>> tells.vi(10)
# Genesis 32:5 And I have oxen, and asses, flocks, and menservants, and womenservants: and I have sent to tell my lord, that I may find grace in thy sight.
# >>> tell('my lord')
# my lord
# 38+  49 = 87
# >>> tells.vi(11)
# Genesis 32:29 And Jacob asked him, and said, Tell me, I pray thee, thy name. And he said, Wherefore is it that thou dost ask after my name? And he blessed him there.
# >>> tell('me, I-pray-thee, thy name')
# me, I-pray-thee, thy name
#  18+         107+ 53+  33 = 211
# >>> tell('thy name',ssum)
# thy name
# 908+  96 = 1004
# >>> tells.vi(12)
# Genesis 37:16 And he said, I seek my brethren: tell me, I pray thee, where they feed their flocks.
# >>> tell('me I pray thee')
# me I pray thee
# 18+9+  60+  38 = 125
# >>> tells.vi(13)
# Genesis 40:8 And they said unto him, We have dreamed a dream, and there is no interpreter of it. And Joseph said unto them, Do not interpretations belong to God? tell me them, I pray you.
# >>> tell('me them, I pray you')
# me them, I pray you
# 18+   46+9+  60+ 61 = 194
# >>> tells.vi(14)
# Genesis 43:6 And Israel said, Wherefore dealt ye so ill with me, as to tell the man whether ye had yet a brother?
# >>> tell('the man')
# the man
#  33+ 28 = 61
# >>> tell('whether ye had yet a brother')
# whether ye had yet a brother
#      87+30+ 13+ 50+1+     86 = 267
# >>> 61+267
# 328
# >>> 
# >>> tells.vi(15)
# Genesis 43:22 And other money have we brought down in our hands to buy food: we cannot tell who put our money in our sacks.
# >>> tell('who put our money in our sacks')
# who put our money in our sacks
#  46+ 57+ 54+   72+23+ 54+   53 = 359
# >>> tell('In the beginning God created the heaven and the')
# In the beginning God created the heaven and the
# 23+ 33+       81+ 26+     56+ 33+    55+ 19+ 33 = 359
# >>> np(359)
# 72
# >>> tells.vi(16).tell()
# 45:13 And ye shall tell my father of all my glory in Egypt, and of all that ye have seen; and ye shall haste and bring down my father hither.
#     0+ 19+30+   52+  49+38+    58+21+ 25+38+   77+23+    73+ 19+21+ 25+  49+30+  36+   43+ 19+30+   52+   53+ 19+   50+  56+38+    58+     68 = 1169
# >>> tell('my-father of-all')
# my-father of-all
#        96+    46 = 142
# >>> tells.vi(17)
# Genesis 49:1 And Jacob called unto his sons, and said, Gather yourselves together, that I may tell you that which shall befall you in the last days.
# >>> _.tell()
# 49:1 And Jacob called unto his sons, and said, Gather yourselves together, that I may tell you that which shall befall you in the last days.
#    0+ 19+   31+    37+  70+ 36+   67+ 19+   33+    59+       161+       98+  49+9+ 39+  49+ 61+  49+   51+   52+    38+ 61+23+ 33+  52+   49 = 1245
# >>> tell('you that which shall befall you in the last days')
# you that which shall befall you in the last days
#  61+  49+   51+   52+    38+ 61+23+ 33+  52+  49 = 469
# >>> tell('you that')
# you that
#  61+  49 = 110
# >>> tell('that which')
# that which
#   49+   51 = 100
# >>> tell('shall befall')
# shall befall
#    52+    38 = 90
# >>> tell('you in the')
# you in the
#  61+23+ 33 = 117
# >>> tell('last-days')
#  l a  s  t - d a  y  s
# 12+1+19+20+0+4+1+25+19 = 101
# >>> tells.verse(18)
# Exodus 9:1 Then the LORD said unto Moses, Go in unto Pharaoh, and tell him, Thus saith the LORD God of the Hebrews, Let my people go, that they may serve me.
# >>> _.tell()
# 9:1 Then the LORD said unto Moses, Go in unto Pharaoh, and tell him, Thus saith the LORD God of the Hebrews, Let my people go, that they may serve me.
#   0+  47+ 33+  49+  33+  70+    71+22+23+  70+      67+ 19+  49+  30+  68+   57+ 33+  49+ 26+21+ 33+      80+ 37+38+    69+ 22+  49+  58+ 39+   69+ 18 = 1349
# >>> tells.verse(19).tell()
# 10:2 And that thou mayest tell in the ears of thy son, and of thy son's son, what things I have wrought in Egypt, and my signs which I have done among them; that ye may know how that I am the LORD.
#    0+ 19+  49+  64+    83+  49+23+ 33+  43+21+ 53+  48+ 19+21+ 53+   67+  48+  52+    77+9+  36+    112+23+    73+ 19+38+   68+   51+9+  36+  38+   50+   46+  49+30+ 39+  63+ 46+  49+9+14+ 33+   49 = 1811
# >>> tell("in the ears of thy son, & of thy son's son")
# in the ears of thy son, & of thy son's son
# 23+ 33+  43+21+ 53+  48+0+21+ 53+   67+ 48 = 410
# >>> tell('Christ',ssum)
# C h  r i   s   t
# 3+8+90+9+100+200 = 410
# >>> 
# >>> tells.verse(20)
# Exodus 14:12 Is not this the word that we did tell thee in Egypt, saying, Let us alone, that we may serve the Egyptians? For it had been better for us to serve the Egyptians, than that we should die in the wilderness.
# >>> tell('thee in Egypt')
# thee in Egypt
#   38+23+   73 = 134
# >>> tells.verse(21)
# Exodus 19:3 And Moses went up unto God, and the LORD called unto him out of the mountain, saying, Thus shalt thou say to the house of Jacob, and tell the children of Israel;
# >>> tell('the children of Israel')
# the children of Israel
#  33+      73+21+    64 = 191
# >>> tells.verse(22)
# Leviticus 14:35 And he that owneth the house shall come and tell the priest, saying, It seemeth to me there is as it were a plague in the house:
# >>> tells.verse(23)
# Numbers 14:14 And they will tell it to the inhabitants of this land: for they have heard that thou LORD art among this people, that thou LORD art seen face to face, and that thy cloud standeth over them, and that thou goest before them, by day time in a pillar of a cloud, and in a pillar of fire by night.
# >>> tell('it')
# i  t
# 9+20 = 29
# >>> tells.verse(24)
# Numbers 21:1 And when king Arad the Canaanite, which dwelt in the south, heard tell that Israel came by the way of the spies; then he fought against Israel, and took some of them prisoners.
# >>> tell('that')
#  t h a  t
# 20+8+1+20 = 49
# >>> tell('Lord')
#  L  o  r d
# 12+15+18+4 = 49
# >>> sof(119)
# 144
# >>> sof(150)
# 372
# >>> factors(_)
# [2, 2, 3, 31]
# >>> tells.verse(25)
# Numbers 23:3 And Balaam said unto Balak, Stand by thy burnt offering, and I will go: peradventure the LORD will come to meet me: and whatsoever he sheweth me I will tell thee. And he went to an high place.
# >>> tell('thee')
#  t h e e
# 20+8+5+5 = 38
# >>> _.tell()
# 23:3 And Balaam said unto Balak, Stand by thy burnt offering, and I will go: peradventure the LORD will come to meet me: and whatsoever he sheweth me I will tell thee. And he went to an high place.
#    0+ 19+    30+  33+  70+    27+   58+27+ 53+   75+       80+ 19+9+  56+ 22+         149+ 33+  49+  56+  36+35+  43+ 18+ 19+       136+13+     88+18+9+  56+  49+   38+ 19+13+  62+35+15+  32+    37 = 1636
# >>> tells.verse(26)
# Deuteronomy 17:11 According to the sentence of the law which they shall teach thee, and according to the judgment which they shall tell thee, thou shalt do: thou shalt not decline from the sentence which they shall shew thee, to the right hand, nor to the left.
# >>> tell('sentence')
#  s e  n  t e  n c e
# 19+5+14+20+5+14+3+5 = 85
# >>> tells.verse(27)
# Deuteronomy 32:7 Remember the days of old, consider the years of many generations: ask thy father, and he will shew thee; thy elders, and they will tell thee.
# >>> tells.verse(28)
# Joshua 7:19 And Joshua said unto Achan, My son, give, I pray thee, glory to the LORD God of Israel, and make confession unto him; and tell me now what thou hast done; hide it not from me.
# >>> tell('me now what thou hast done')
# me now what thou hast done
# 18+ 52+  52+  64+  48+  38 = 272
# >>> tells.verse(29)
# Judges 7:15 And it was so, when Gideon heard the telling of the dream, and the interpretation thereof, that he worshipped, and returned into the host of Israel, and said, Arise; for the LORD hath delivered into your hand the host of Midian.
# >>> tell('of the dream')
# of the dream
# 21+ 33+   41 = 95
# >>> tell('I AM  THAT I AM')
# I AM THAT I AM
# 9+14+  49+9+14 = 95
# >>> tells.verse(28)
# Joshua 7:19 And Joshua said unto Achan, My son, give, I pray thee, glory to the LORD God of Israel, and make confession unto him; and tell me now what thou hast done; hide it not from me.
# >>> tell('me now what thou hast done')
# me now what thou hast done
# 18+ 52+  52+  64+  48+  38 = 272
# >>> tells.verse(29)
# Judges 7:15 And it was so, when Gideon heard the telling of the dream, and the interpretation thereof, that he worshipped, and returned into the host of Israel, and said, Arise; for the LORD hath delivered into your hand the host of Midian.
# >>> tell('of the dream')
# of the dream
# 21+ 33+   41 = 95
# >>> tells.verse(30)
# Judges 14:16 And Samson's wife wept before him, and said, Thou dost but hate me, and lovest me not: thou hast put forth a riddle unto the children of my people, and hast not told it me. And he said unto her, Behold, I have not told it my father nor my mother, and shall I tell it thee?
# >>> tell('Samson')
#  S a  m  s  o  n
# 19+1+13+19+15+14 = 81
# >>> tell('beginning')
# b e g i  n  n i  n g
# 2+5+7+9+14+14+9+14+7 = 81
# >>> tell('it thee')
# it thee
# 29+  38 = 67
# >>> tells.verse(31)
# Judges 16:6 And Delilah said to Samson, Tell me, I pray thee, wherein thy great strength lieth, and wherewith thou mightest be bound to afflict thee.
# >>> tells.verse(32)
# Judges 16:10 And Delilah said unto Samson, Behold, thou hast mocked me, and told me lies: now tell me, I pray thee, wherewith thou mightest be bound.
# >>> tells.verse(33)
# Judges 16:13 And Delilah said unto Samson, Hitherto thou hast mocked me, and told me lies: tell me wherewith thou mightest be bound. And he said unto her, If thou weavest the seven locks of my head with the web.
# >>> tells.verse(34)
# Judges 20:3 (Now the children of Benjamin heard that the children of Israel were gone up to Mizpeh.) Then said the children of Israel, Tell us, how was this wickedness?
# >>> tell('us')
#  u  s
# 21+19 = 40
# >>> tells.verse(35)
# Ruth 3:4 And it shall be, when he lieth down, that thou shalt mark the place where he shall lie, and thou shalt go in, and uncover his feet, and lay thee down; and he will tell thee what thou shalt do.
# >>> tells.verse(36)
# Ruth 4:4 And I thought to advertise thee, saying, Buy it before the inhabitants, and before the elders of my people. If thou wilt redeem it, redeem it: but if thou wilt not redeem it, then tell me, that I may know: for there is none to redeem it beside thee; and I am after thee. And he said, I will redeem it.
# >>> tell('me that I may know')
# me that I may know
# 18+  49+9+ 39+  63 = 178
# >>> 
# >>> tells.verse(37)
# 1 Samuel 6:2 And the Philistines called for the priests and the diviners, saying, What shall we do to the ark of the LORD? tell us wherewith we shall send it to his place.
# >>> tells.verse(38)
# 1 Samuel 9:8 And the servant answered Saul again, and said, Behold, I have here at hand the fourth part of a shekel of silver: that will I give to the man of God, to tell us our way.
# >>> tell('us our way')
# us our way
# 40+ 54+ 49 = 143
# >>> tell('way truth life')
# way truth life
#  49+   87+  32 = 168
# >>> tells.verse(39)
# 1 Samuel 9:18 Then Saul drew near to Samuel in the gate, and said, Tell me, I pray thee, where the seer's house is.
# >>> tells.verse(40)
# 1 Samuel 9:19 And Samuel answered Saul, and said, I am the seer: go up before me unto the high place; for ye shall eat with me to day, and to morrow I will let thee go, and will tell thee all that is in thine heart.
# >>> tell('all that is in thine heart')
# all that is in thine heart
#  25+  49+28+23+   56+   52 = 233
# >>> tells.verse(41)
# 1 Samuel 10:15 And Saul's uncle said, Tell me, I pray thee, what Samuel said unto you.
# >>> tells.verse(42)
# 1 Samuel 14:43 Then Saul said to Jonathan, Tell me what thou hast done. And Jonathan told him, and said, I did but taste a little honey with the end of the rod that was in mine hand, and, lo, I must die.
# >>> tells.verse(43)
# 1 Samuel 15:16 Then Samuel said unto Saul, Stay, and I will tell thee what the LORD hath said to me this night. And he said unto him, Say on.
# >>> tells.verse(44)
# 1 Samuel 17:55 And when Saul saw David go forth against the Philistine, he said unto Abner, the captain of the host, Abner, whose son is this youth? And Abner said, As thy soul liveth, O king, I cannot tell.
# >>> tells.verse(45)
# 1 Samuel 19:3 And I will go out and stand beside my father in the field where thou art, and I will commune with my father of thee; and what I see, that I will tell thee.
# >>> tells.verse(46)
# 1 Samuel 20:9 And Jonathan said, Far be it from thee: for if I knew certainly that evil were determined by my father to come upon thee, then would not I tell it thee?
# >>> tells.verse(47)
# 1 Samuel 20:10 Then said David to Jonathan, Who shall tell me? or what if thy father answer thee roughly?
# >>> tells.verse(48)
# 1 Samuel 22:22 And David said unto Abiathar, I knew it that day, when Doeg the Edomite was there, that he would surely tell Saul: I have occasioned the death of all the persons of thy father's house.
# >>> tells.verse(49)
# 1 Samuel 23:11 Will the men of Keilah deliver me up into his hand? will Saul come down, as thy servant hath heard? O LORD God of Israel, I beseech thee, tell thy servant. And the LORD said, He will come down.
# >>> tells.verse(50)
# 1 Samuel 27:11 And David saved neither man nor woman alive, to bring tidings to Gath, saying, Lest they should tell on us, saying, So did David, and so will be his manner all the while he dwelleth in the country of the Philistines.
# >>> tell('on us')
# on us
# 29+40 = 69
# >>> tells.verse(51)
# 2 Samuel 1:4 And David said unto him, How went the matter? I pray thee, tell me. And he answered, That the people are fled from the battle, and many of the people also are fallen and dead; and Saul and Jonathan his son are dead also.
# >>> tells.verse(52)
# 2 Samuel 1:20 Tell it not in Gath, publish it not in the streets of Askelon; lest the daughters of the Philistines rejoice, lest the daughters of the uncircumcised triumph.
# >>> tells.verse(53)
# 2 Samuel 7:5 Go and tell my servant David, Thus saith the LORD, Shalt thou build me an house for me to dwell in?
# >>> tells.verse(54)
# 2 Samuel 7:11 And as since the time that I commanded judges to be over my people Israel, and have caused thee to rest from all thine enemies. Also the LORD telleth thee that he will make thee an house.
# >>> tells.verse(55)
# 2 Samuel 11:19 And charged the messenger, saying, When thou hast made an end of telling the matters of the war unto the king,
# >>> tell('the matters of the war')
# the matters of the war
#  33+     96+21+ 33+ 42 = 225
# >>> fs(225)
# [3, 3, 5, 5]
# >>> tells.verse(56)
# 2 Samuel 12:18 And it came to pass on the seventh day, that the child died. And the servants of David feared to tell him that the child was dead: for they said, Behold, while the child was yet alive, we spake unto him, and he would not hearken unto our voice: how will he then vex himself, if we tell him that the child is dead?
# >>> tells.verse(57)
# 2 Samuel 12:22 And he said, While the child was yet alive, I fasted and wept: for I said, Who can tell whether GOD will be gracious to me, that the child may live?
# >>> tells.verse(58)
# 2 Samuel 13:4 And he said unto him, Why art thou, being the king's son, lean from day to day? wilt thou not tell me? And Amnon said unto him, I love Tamar, my brother Absalom's sister.
# >>> tells.verse(59)
# 2 Samuel 15:35 And hast thou not there with thee Zadok and Abiathar the priests? therefore it shall be, that what thing soever thou shalt hear out of the king's house, thou shalt tell it to Zadok and Abiathar the priests.
# >>> tell('Zadok Abiathar')
# Zadok Abiathar
#    57+      60 = 117
# >>> tell('Zadok Abiathar',ssum)
# Zadok Abiathar
#   885+     312 = 1197
# >>> b/'Abel'/'Zacharias'
# Matthew 23:35 That upon you may come all the righteous blood shed upon the earth, from the blood of righteous Abel unto the blood of Zacharias son of Barachias, whom ye slew between the temple and the altar.
# Luke 11:51 From the blood of Abel unto the blood of Zacharias which perished between the altar and the temple: verily I say unto you, It shall be required of this generation.
# >>> _.vns()
# [23954, 25457]
# >>> [x-23145 for x in _]
# [809, 2312]
# >>> Matthew-Luke[11:51]
# Matthew 1:1-Luke 11:51 (2312 verses)
# >>> 
# >>> 
# >>> 
# >>> tell('Abel Zecharias')
# Abel Zecharias
#   20+       90 = 110
# >>> tell('the blood')
# the blood
#  33+   48 = 81
# >>> tell('Abel Zecharias',ssum)
# Abel Zecharias
#   38+     1017 = 1055
# >>> tells.verse(60)
# 2 Samuel 17:16 Now therefore send quickly, and tell David, saying, Lodge not this night in the plains of the wilderness, but speedily pass over; lest the king be swallowed up, and all the people that are with him.
# >>> sums('David')
# (40, 418)
# >>> tells.verse(61)
# 2 Samuel 18:21 Then said Joab to Cushi, Go tell the king what thou hast seen. And Cushi bowed himself unto Joab, and ran.
# >>> tell('the king')
# the king
#  33+  41 = 74
# >>> tell('Jesus')
#  J e  s  u  s
# 10+5+19+21+19 = 74
# >>> tell('the king',ssum)
# the king
# 213+  86 = 299
# >>> sums('elohim')
# (62, 152)
# >>> sums('אלהימ')
# (41, 86)
# >>> sums('James')
# (48, 156)
# >>> sums('Jacob')
# (31, 76)
# >>> 
