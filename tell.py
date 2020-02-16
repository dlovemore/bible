# >>> from bible import *
# >>> b/'counting'
# Ecclesiastes 7:27 Behold, this have I found, saith the preacher, counting one by one, to find out the account:
# >>> _.chn()
# 666
# >>> Revelation/'here is wisdom'
# Revelation 13:18 Here is wisdom. Let him that hath understanding count the number of the beast: for it is the number of a man; and his number is Six hundred threescore and six.
# >>> 
# >>> tell('counting')
# c o  u  n  t  i n  g
# 3+15+21+14+20+9+14+7=103
# >>> tell('Solomon')
# S  o  l  o  m  o  n
# 19+15+12+15+13+15+14=103
# >>> b.midv()
# Psalms 103:1 Bless the LORD, O my soul: and all that is within me, bless his holy name.
# Psalms 103:2 Bless the LORD, O my soul, and forget not all his benefits:
# >>> b.vc()
# 31102
# >>> 
# >>> tell('Solomon',ssum)
#  S  o  l  o  m  o  n
# 100+60+30+60+40+60+50=400
# >>> IKings/'half'/'told'
# 1 Kings 10:7 Howbeit I believed not the words, until I came, and mine eyes had seen it: and, behold, the half was not told me: thy wisdom and prosperity exceedeth the fame which I heard.
# >>> 400//2
# 200
# >>> tell('Lord Jesus Christ')
# Lord Jesus Christ
#  49 +  74 +  77  =200
# >>> tell('the water, and the blood')
# the water, and the blood
#  33+  67  + 19+ 33+  48 =200
# >>> tell('the water'),tell('and the blood')
# the water
#  33+  67 =100
# and the blood
#  19+ 33+  48 =100
# (None, None)
# >>> tell('the Spirit, and the water, and the blood')
# the Spirit, and the water, and the blood
#  33+   91  + 19+ 33+  67  + 19+ 33+  48 =343
# >>> 7*7*7
# 343
# >>> tell('the Father, the Word, the Holy Ghost')
# the Father, the Word, the Holy Ghost
#  33+   58  + 33+  60 + 33+ 60 +  69 =346
# >>> 343+3
# 346
# >>> IJohn[5:7]-8
# 1 John 5:7 For there are three that bear record in heaven, the Father, the Word, and the Holy Ghost: and these three are one.
# 1 John 5:8 And there are three that bear witness in earth, the Spirit, and the water, and the blood: and these three agree in one.
# >>> tell('the Father, the Word and the Holy Ghost',lsum)
# the Father, the Word and the Holy Ghost
#  3 +   6   + 3 + 4  + 3 + 3 + 4  +  5  =31
# >>> tell('the Spirit, and the water, and the blood',lsum)
# the Spirit, and the water, and the blood
#  3 +   6   + 3 + 3 +  5   + 3 + 3 +  5  =31
# >>> tell('the Father, the Word and the Holy Ghost')
# the Father, the Word and the Holy Ghost
#  33+   58  + 33+ 60 + 19+ 33+ 60 +  69 =365
# >>> tell('the Father, the Word + the Holy Ghost')
# the Father, the Word + the Holy Ghost
#  33+   58  + 33+ 60 +0+ 33+ 60 +  69 =346
# >>> tell('the Spirit, and the water, and the blood')
# the Spirit, and the water, and the blood
#  33+   91  + 19+ 33+  67  + 19+ 33+  48 =343
# >>> tell('the Spirit,and the-water, and-the-blood')
# the Spirit,and the-water, and-the-blood
#  33+   110    +   100    +     100     =343
# >>> 7*7*7
# 343
# >>> _+3
# 346
# >>> tell('Lord')
# L  o  r  d
# 12+15+18+4=49
# >>> 7*7
# 49
# >>> tell('Christ')
# C h r  i s  t
# 3+8+18+9+19+20=77
# >>> 
# >>> 
# >>> 
# >>> tell('the Father, the Word and the Holy Ghost',ssum)
# the Father, the Word and the Holy Ghost
# 213+  310  +213+654 + 55+213+798 + 375 =2831
# >>> 13+456+897+573
# 1939
# >>> 
# >>> tell('the Spirit, and the water, and the blood',ssum)
# the Spirit, and the water, and the blood
# 213+  478  + 55+213+ 796  + 55+213+ 156 =2179
# >>> 874+697+651
# 2222
# >>> 
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
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> (IJohn[5:7]-8).tell(ssum)
# For there are three that bear record in heaven, the Father, the Word, and the Holy Ghost: and these three are one.
# 156+ 308 + 96+ 308 +409 + 98 + 252  +59+  469  +213+  310  +213+ 654 + 55+213+798 + 375  + 55+ 318 + 308 + 96+115 =5878
# And there are three that bear witness in earth, the Spirit, and the water, and the blood: and these three agree in one.
#  55+ 308 + 96+ 308 +409 + 98 +  964  +59+ 304  +213+  478  + 55+213+ 796  + 55+213+ 156  + 55+ 318 + 308 + 108 +59+115 =5743
# >>> 5878-5743
# 135
# >>> 
# >>> 
# >>> tells=b/'tell'
# >>> tells.vi(1)
# Genesis 12:18 And Pharaoh called Abram and said, What is this that thou hast done unto me? why didst thou not tell me that she was thy wife?
# >>> tell('me')
# m  e
# 13+5=18
# >>> tell('me that she was thy wife')
# me that she was thy wife
# 18+ 49 + 32+ 43+ 53+ 43 =238
# >>> tells.vi(2)
# Genesis 15:5 And he brought him forth abroad, and said, Look now toward heaven, and tell the stars, if thou be able to number them: and he said unto him, So shall thy seed be.
# >>> tell('the stars')
# the stars
#  33+  77 =110
# >>> tell('Christ')
# C h r  i s  t
# 3+8+18+9+19+20=77
# >>> Luke[3:].count('son of')
# 77
# >>> tell('Jesus',ssum)
# J  e  s   u   s
# 10+5+100+300+100=515
# >>> 
# >>> tells.vi(3)
# Genesis 21:26 And Abimelech said, I wot not who hath done this thing; neither didst thou tell me, neither yet heard I of it, but to day.
# >>> _.tell()
# And Abimelech said, I wot not who hath done this thing; neither didst thou tell me, neither yet heard I of it, but to day.
#  19+    58   +  33 +9+ 58+ 49+ 46+ 37 + 38 + 56 +  58  +   79  +  56 + 64 + 49 + 18+   79  + 50+  36 +9+21+ 29+ 43+35+ 30 =1059
# >>> 
# >>> tells.vi(4)
# Genesis 22:2 And he said, Take now thy son, thine only son Isaac, whom thou lovest, and get thee into the land of Moriah; and offer him there for a burnt offering upon one of the mountains which I will tell thee of.
# >>> _.tell()
# And he said, Take now thy son, thine only son Isaac, whom thou lovest, and get thee into the land of Moriah; and offer him there for a burnt offering upon one of the mountains which I will tell thee of.
#  19+13+  33 + 37 + 52+ 53+ 48 +  56 + 66 + 48+  33  + 59 + 64 +   93  + 19+ 32+ 38 + 58 + 33+ 31 +21+   64  + 19+  50 + 30+  56 + 39+1+  75 +   80   + 66 + 34+21+ 33+   126   +  51 +9+ 56 + 49 + 38 + 21=1824
# >>> 
# >>> tells.vi(5)
# Genesis 24:23 And said, Whose daughter art thou? tell me, I pray thee: is there room in thy father's house for us to lodge in?
# >>> tell('me I pray thee')
# me I pray thee
# 18+9+ 60 + 38 =125
# >>> 5*5*5
# 125
# >>> tell('Bethlehem Ephratah')
# Bethlehem Ephratah
#     78   +   77   =155
# >>> 
# >>> tells.vi(6).tell()
# And now if ye will deal kindly and truly with my master, tell me: and if not, tell me; that I may turn to the right hand, or to the left.
#  19+ 52+15+30+ 56 + 22 +  75  + 19+  96 + 60 +38+   76  + 49 + 18+ 19+15+ 49 + 49 + 18+ 49 +9+ 39+ 73 +35+ 33+  62 +  27 +33+35+ 33+  43 =1246
# >>> 
# >>> 
# >>> tells.vi(7)
# Genesis 26:2 And the LORD appeared unto him, and said, Go not down into Egypt; dwell in the land which I shall tell thee of:
# >>> tell('thee of',osum,ssum)
# thee of
#  38 +21= 59
# 218 +66=284
# >>> 
# >>> tells.vi(8)
# Genesis 29:15 And Laban said unto Jacob, Because thou art my brother, shouldest thou therefore serve me for nought? tell me, what shall thy wages be?
# >>> tell('what shall thy wages be?')
# what shall thy wages be?
#  52 +  52 + 53+  55 + 7 =219
# >>> 
# >>> tells.vi(9)
# Genesis 31:27 Wherefore didst thou flee away secretly, and steal away from me; and didst not tell me, that I might have sent thee away with mirth, and with songs, with tabret, and with harp?
# >>> tells.vi(10)
# Genesis 32:5 And I have oxen, and asses, flocks, and menservants, and womenservants: and I have sent to tell my lord, that I may find grace in thy sight.
# >>> tell('my lord')
# my lord
# 38+ 49 =87
# >>> tells.vi(11)
# Genesis 32:29 And Jacob asked him, and said, Tell me, I pray thee, thy name. And he said, Wherefore is it that thou dost ask after my name? And he blessed him there.
# >>> tell('me, I-pray-thee, thy name')
# me, I-pray-thee, thy name
#  18+    107     + 53+ 33 =211
# >>> tell('thy name',ssum)
# thy name
# 908+ 96 =1004
# >>> tells.vi(12)
# Genesis 37:16 And he said, I seek my brethren: tell me, I pray thee, where they feed their flocks.
# >>> tell('me I pray thee')
# me I pray thee
# 18+9+ 60 + 38 =125
# >>> tells.vi(13)
# Genesis 40:8 And they said unto him, We have dreamed a dream, and there is no interpreter of it. And Joseph said unto them, Do not interpretations belong to God? tell me them, I pray you.
# >>> tell('me them, I pray you')
# me them, I pray you
# 18+  46 +9+ 60 + 61=194
# >>> tells.vi(14)
# Genesis 43:6 And Israel said, Wherefore dealt ye so ill with me, as to tell the man whether ye had yet a brother?
# >>> tell('the man')
# the man
#  33+ 28=61
# >>> tell('whether ye had yet a brother')
# whether ye had yet a brother
#    87  +30+ 13+ 50+1+   86  =267
# >>> 61+267
# 328
# >>> 
# >>> tells.vi(15)
# Genesis 43:22 And other money have we brought down in our hands to buy food: we cannot tell who put our money in our sacks.
# >>> tell('who put our money in our sacks')
# who put our money in our sacks
#  46+ 57+ 54+  72 +23+ 54+  53 =359
# >>> tell('In the beginning God created the heaven and the')
# In the beginning God created the heaven and the
# 23+ 33+    81   + 26+   56  + 33+  55  + 19+ 33=359
# >>> np(359)
# 72
# >>> tells.vi(16).tell()
# And ye shall tell my father of all my glory in Egypt, and of all that ye have seen; and ye shall haste and bring down my father hither.
#  19+30+  52 + 49 +38+  58  +21+ 25+38+  77 +23+  73  + 19+21+ 25+ 49 +30+ 36 +  43 + 19+30+  52 +  53 + 19+  50 + 56 +38+  58  +   68  =1169
# >>> tell('my-father of-all')
# my-father of-all
#     96   +  46  =142
# >>> tells.vi(17)
# Genesis 49:1 And Jacob called unto his sons, and said, Gather yourselves together, that I may tell you that which shall befall you in the last days.
# >>> _.tell()
# And Jacob called unto his sons, and said, Gather yourselves together, that I may tell you that which shall befall you in the last days.
#  19+  31 +  37  + 70 + 36+  67 + 19+  33 +  59  +   161    +    98   + 49 +9+ 39+ 49 + 61+ 49 +  51 +  52 +  38  + 61+23+ 33+ 52 +  49 =1245
# >>> tell('you that which shall befall you in the last days')
# you that which shall befall you in the last days
#  61+ 49 +  51 +  52 +  38  + 61+23+ 33+ 52 + 49 =469
# >>> tell('you that')
# you that
#  61+ 49 =110
# >>> tell('that which')
# that which
#  49 +  51 =100
# >>> tell('shall befall')
# shall befall
#   52 +  38  =90
# >>> tell('you in the')
# you in the
#  61+23+ 33=117
# >>> tell('last-days')
# l  a s  t- d a y  s
# 12+1+19+20+4+1+25+19=101
# >>> tells.verse(18)
# Exodus 9:1 Then the LORD said unto Moses, Go in unto Pharaoh, and tell him, Thus saith the LORD God of the Hebrews, Let my people go, that they may serve me.
# >>> _.tell()
# Then the LORD said unto Moses, Go in unto Pharaoh, and tell him, Thus saith the LORD God of the Hebrews, Let my people go, that they may serve me.
#  47 + 33+ 49 + 33 + 70 +  71  +22+23+ 70 +   67   + 19+ 49 + 30 + 68 +  57 + 33+ 49 + 26+21+ 33+   80   + 37+38+  69  + 22+ 49 + 58 + 39+  69 + 18=1349
# >>> tells.verse(19).tell()
# And that thou mayest tell in the ears of thy son, and of thy son's son, what things I have wrought in Egypt, and my signs which I have done among them; that ye may know how that I am the LORD.
#  19+ 49 + 64 +  83  + 49 +23+ 33+ 43 +21+ 53+ 48 + 19+21+ 53+  67 + 48 + 52 +  77  +9+ 36 +  112  +23+  73  + 19+38+  68 +  51 +9+ 36 + 38 +  50 +  46 + 49 +30+ 39+ 63 + 46+ 49 +9+14+ 33+  49 =1811
# >>> tell("in the ears of thy son, & of thy son's son")
# in the ears of thy son, & of thy son's son
# 23+ 33+ 43 +21+ 53+ 48 +0+21+ 53+  67 + 48=410
# >>> tell('Christ',ssum)
# C h r  i  s   t
# 3+8+90+9+100+200=410
# >>> 
# >>> tells.verse(20)
# Exodus 14:12 Is not this the word that we did tell thee in Egypt, saying, Let us alone, that we may serve the Egyptians? For it had been better for us to serve the Egyptians, than that we should die in the wilderness.
# >>> tell('thee in Egypt')
# thee in Egypt
#  38 +23+  73 =134
# >>> tells.verse(21)
# Exodus 19:3 And Moses went up unto God, and the LORD called unto him out of the mountain, saying, Thus shalt thou say to the house of Jacob, and tell the children of Israel;
# >>> tell('the children of Israel')
# the children of Israel
#  33+   73   +21+  64  =191
# >>> tells.verse(22)
# Leviticus 14:35 And he that owneth the house shall come and tell the priest, saying, It seemeth to me there is as it were a plague in the house:
# >>> tells.verse(23)
# Numbers 14:14 And they will tell it to the inhabitants of this land: for they have heard that thou LORD art among this people, that thou LORD art seen face to face, and that thy cloud standeth over them, and that thou goest before them, by day time in a pillar of a cloud, and in a pillar of fire by night.
# >>> tell('it')
# i t
# 9+20=29
# >>> tells.verse(24)
# Numbers 21:1 And when king Arad the Canaanite, which dwelt in the south, heard tell that Israel came by the way of the spies; then he fought against Israel, and took some of them prisoners.
# >>> tell('that')
# t  h a t
# 20+8+1+20=49
# >>> tell('Lord')
# L  o  r  d
# 12+15+18+4=49
# >>> sof(119)
# 144
# >>> sof(150)
# 372
# >>> factors(_)
# [2, 2, 3, 31]
# >>> tells.verse(25)
# Numbers 23:3 And Balaam said unto Balak, Stand by thy burnt offering, and I will go: peradventure the LORD will come to meet me: and whatsoever he sheweth me I will tell thee. And he went to an high place.
# >>> tell('thee')
# t  h e e
# 20+8+5+5=38
# >>> _.tell()
# And Balaam said unto Balak, Stand by thy burnt offering, and I will go: peradventure the LORD will come to meet me: and whatsoever he sheweth me I will tell thee. And he went to an high place.
#  19+  30  + 33 + 70 +  27  +  58 +27+ 53+  75 +    80   + 19+9+ 56 + 22+    149     + 33+ 49 + 56 + 36 +35+ 43 + 18+ 19+   136    +13+   88  +18+9+ 56 + 49 +  38 + 19+13+ 62 +35+15+ 32 +  37  =1636
# >>> tells.verse(26)
# Deuteronomy 17:11 According to the sentence of the law which they shall teach thee, and according to the judgment which they shall tell thee, thou shalt do: thou shalt not decline from the sentence which they shall shew thee, to the right hand, nor to the left.
# >>> tell('sentence')
# s  e n  t  e n  c e
# 19+5+14+20+5+14+3+5=85
# >>> tells.verse(27)
# Deuteronomy 32:7 Remember the days of old, consider the years of many generations: ask thy father, and he will shew thee; thy elders, and they will tell thee.
# >>> tells.verse(28)
# Joshua 7:19 And Joshua said unto Achan, My son, give, I pray thee, glory to the LORD God of Israel, and make confession unto him; and tell me now what thou hast done; hide it not from me.
# >>> tell('me now what thou hast done')
# me now what thou hast done
# 18+ 52+ 52 + 64 + 48 + 38 =272
# >>> tells.verse(29)
# Judges 7:15 And it was so, when Gideon heard the telling of the dream, and the interpretation thereof, that he worshipped, and returned into the host of Israel, and said, Arise; for the LORD hath delivered into your hand the host of Midian.
# >>> tell('of the dream')
# of the dream
# 21+ 33+  41 =95
# >>> tell('I AM  THAT I AM')
# I AM THAT I AM
# 9+14+ 49 +9+14=95
# >>> tells.verse(28)
# Joshua 7:19 And Joshua said unto Achan, My son, give, I pray thee, glory to the LORD God of Israel, and make confession unto him; and tell me now what thou hast done; hide it not from me.
# >>> tell('me now what thou hast done')
# me now what thou hast done
# 18+ 52+ 52 + 64 + 48 + 38 =272
# >>> tells.verse(29)
# Judges 7:15 And it was so, when Gideon heard the telling of the dream, and the interpretation thereof, that he worshipped, and returned into the host of Israel, and said, Arise; for the LORD hath delivered into your hand the host of Midian.
# >>> tell('of the dream')
# of the dream
# 21+ 33+  41 =95
# >>> tells.verse(30)
# Judges 14:16 And Samson's wife wept before him, and said, Thou dost but hate me, and lovest me not: thou hast put forth a riddle unto the children of my people, and hast not told it me. And he said unto her, Behold, I have not told it my father nor my mother, and shall I tell it thee?
# >>> tell('Samson')
# S  a m  s  o  n
# 19+1+13+19+15+14=81
# >>> tell('beginning')
# b e g i n  n  i n  g
# 2+5+7+9+14+14+9+14+7=81
# >>> tell('it thee')
# it thee
# 29+ 38 =67
# >>> tells.verse(31)
# Judges 16:6 And Delilah said to Samson, Tell me, I pray thee, wherein thy great strength lieth, and wherewith thou mightest be bound to afflict thee.
# >>> tells.verse(32)
# Judges 16:10 And Delilah said unto Samson, Behold, thou hast mocked me, and told me lies: now tell me, I pray thee, wherewith thou mightest be bound.
# >>> tells.verse(33)
# Judges 16:13 And Delilah said unto Samson, Hitherto thou hast mocked me, and told me lies: tell me wherewith thou mightest be bound. And he said unto her, If thou weavest the seven locks of my head with the web.
# >>> tells.verse(34)
# Judges 20:3 (Now the children of Benjamin heard that the children of Israel were gone up to Mizpeh.) Then said the children of Israel, Tell us, how was this wickedness?
# >>> tell('us')
# u  s
# 21+19=40
# >>> tells.verse(35)
# Ruth 3:4 And it shall be, when he lieth down, that thou shalt mark the place where he shall lie, and thou shalt go in, and uncover his feet, and lay thee down; and he will tell thee what thou shalt do.
# >>> tells.verse(36)
# Ruth 4:4 And I thought to advertise thee, saying, Buy it before the inhabitants, and before the elders of my people. If thou wilt redeem it, redeem it: but if thou wilt not redeem it, then tell me, that I may know: for there is none to redeem it beside thee; and I am after thee. And he said, I will redeem it.
# >>> tell('me that I may know')
# me that I may know
# 18+ 49 +9+ 39+ 63 =178
# >>> 
# >>> tells.verse(37)
# 1 Samuel 6:2 And the Philistines called for the priests and the diviners, saying, What shall we do to the ark of the LORD? tell us wherewith we shall send it to his place.
# >>> tells.verse(38)
# 1 Samuel 9:8 And the servant answered Saul again, and said, Behold, I have here at hand the fourth part of a shekel of silver: that will I give to the man of God, to tell us our way.
# >>> tell('us our way')
# us our way
# 40+ 54+ 49=143
# >>> tell('way truth life')
# way truth life
#  49+  87 + 32 =168
# >>> tells.verse(39)
# 1 Samuel 9:18 Then Saul drew near to Samuel in the gate, and said, Tell me, I pray thee, where the seer's house is.
# >>> tells.verse(40)
# 1 Samuel 9:19 And Samuel answered Saul, and said, I am the seer: go up before me unto the high place; for ye shall eat with me to day, and to morrow I will let thee go, and will tell thee all that is in thine heart.
# >>> tell('all that is in thine heart')
# all that is in thine heart
#  25+ 49 +28+23+  56 +  52 =233
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
# 29+40=69
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
#  33+   96  +21+ 33+ 42=225
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
#   57 +   60   =117
# >>> tell('Zadok Abiathar',ssum)
# Zadok Abiathar
#  885 +  312   =1197
# >>> b/'Abel'/'Zacharias'
# Matthew 23:35 That upon you may come all the righteous blood shed upon the earth, from the blood of righteous Abel unto the blood of Zacharias son of Barachias, whom ye slew between the temple and the altar.
# Luke 11:51 From the blood of Abel unto the blood of Zacharias which perished between the altar and the temple: verily I say unto you, It shall be required of this generation.
# >>> tells.tell()
# And Pharaoh called Abram and said, What is this that thou hast done unto me? why didst thou not tell me that she was thy wife?
#  19+   67  +  37  +  35 + 19+  33 + 52 +28+ 56 + 49 + 64 + 48 + 38 + 70 + 18+ 56+  56 + 64 + 49+ 49 +18+ 49 + 32+ 43+ 53+  43 =1145
# And he brought him forth abroad, and said, Look now toward heaven, and tell the stars, if thou be able to number them: and he said unto him, So shall thy seed be.
#  19+13+   91  + 30+  67 +   41  + 19+  33 + 53 + 52+  81  +   55  + 19+ 49 + 33+  77  +15+ 64 +7 + 20 +35+  73  +  46 + 19+13+ 33 + 70 + 30 +34+  52 + 53+ 33 + 7 =1336
# And Abimelech said, I wot not who hath done this thing; neither didst thou tell me, neither yet heard I of it, but to day.
#  19+    58   +  33 +9+ 58+ 49+ 46+ 37 + 38 + 56 +  58  +   79  +  56 + 64 + 49 + 18+   79  + 50+  36 +9+21+ 29+ 43+35+ 30 =1059
# And he said, Take now thy son, thine only son Isaac, whom thou lovest, and get thee into the land of Moriah; and offer him there for a burnt offering upon one of the mountains which I will tell thee of.
#  19+13+  33 + 37 + 52+ 53+ 48 +  56 + 66 + 48+  33  + 59 + 64 +   93  + 19+ 32+ 38 + 58 + 33+ 31 +21+   64  + 19+  50 + 30+  56 + 39+1+  75 +   80   + 66 + 34+21+ 33+   126   +  51 +9+ 56 + 49 + 38 + 21=1824
# And said, Whose daughter art thou? tell me, I pray thee: is there room in thy father's house for us to lodge in?
#  19+  33 +  70 +   84   + 39+  64 + 49 + 18+9+ 60 +  38 +28+  56 + 61 +23+ 53+   77   +  68 + 39+40+35+  43 + 23=1029
# And now if ye will deal kindly and truly with my master, tell me: and if not, tell me; that I may turn to the right hand, or to the left.
#  19+ 52+15+30+ 56 + 22 +  75  + 19+  96 + 60 +38+   76  + 49 + 18+ 19+15+ 49 + 49 + 18+ 49 +9+ 39+ 73 +35+ 33+  62 +  27 +33+35+ 33+  43 =1246
# And the LORD appeared unto him, and said, Go not down into Egypt; dwell in the land which I shall tell thee of:
#  19+ 33+ 49 +   66   + 70 + 30 + 19+  33 +22+ 49+ 56 + 58 +  73  +  56 +23+ 33+ 31 +  51 +9+  52 + 49 + 38 + 21=940
# And Laban said unto Jacob, Because thou art my brother, shouldest thou therefore serve me for nought? tell me, what shall thy wages be?
#  19+  30 + 33 + 70 +  31  +   56  + 64 + 39+38+   86   +   123   + 64 +   100   +  69 +18+ 39+   85  + 49 + 18+ 52 +  52 + 53+  55 + 7 =1250
# Wherefore didst thou flee away secretly, and steal away from me; and didst not tell me, that I might have sent thee away with mirth, and with songs, with tabret, and with harp?
#    103   +  56 + 64 + 28 + 50 +   107   + 19+  57 + 50 + 52 + 18+ 19+  56 + 49+ 49 + 18+ 49 +9+  57 + 36 + 58 + 38 + 50 + 60 +  68  + 19+ 60 +  74  + 60 +   66  + 19+ 60 +  43 =1621
# And I have oxen, and asses, flocks, and menservants, and womenservants: and I have sent to tell my lord, that I may find grace in thy sight.
#  19+9+ 36 +  58 + 19+  63  +   66  + 19+    150     + 19+     188      + 19+9+ 36 + 58 +35+ 49 +38+  49 + 49 +9+ 39+ 33 +  34 +23+ 53+  63  =1242
# And Jacob asked him, and said, Tell me, I pray thee, thy name. And he said, Wherefore is it that thou dost ask after my name? And he blessed him there.
#  19+  31 +  40 + 30 + 19+  33 + 49 + 18+9+ 60 +  38 + 53+  33 + 19+13+  33 +   103   +28+29+ 49 + 64 + 58 + 31+  50 +38+  33 + 19+13+   66  + 30+  56  =1164
# And he said, I seek my brethren: tell me, I pray thee, where they feed their flocks.
#  19+13+  33 +9+ 40 +38+    90   + 49 + 18+9+ 60 +  38 +  59 + 58 + 20 +  60 +   66  =679
# And they said unto him, We have dreamed a dream, and there is no interpreter of it. And Joseph said unto them, Do not interpretations belong to God? tell me them, I pray you.
#  19+ 58 + 33 + 70 + 30 +28+ 36 +   50  +1+  41  + 19+  56 +28+29+    148    +21+ 29+ 19+  73  + 33 + 70 +  46 +19+ 49+      203      +  55  +35+ 26 + 49 +18+  46 +9+ 60 + 61 =1567
# And Israel said, Wherefore dealt ye so ill with me, as to tell the man whether ye had yet a brother?
#  19+  64  +  33 +   103   +  42 +30+34+ 33+ 60 + 18+20+35+ 49 + 33+ 28+   87  +30+ 13+ 50+1+   86   =868
# And other money have we brought down in our hands to buy food: we cannot tell who put our money in our sacks.
#  19+  66 +  72 + 36 +28+   91  + 56 +23+ 54+  46 +35+ 48+  40 +28+  67  + 49 + 46+ 57+ 54+  72 +23+ 54+  53  =1117
# And ye shall tell my father of all my glory in Egypt, and of all that ye have seen; and ye shall haste and bring down my father hither.
#  19+30+  52 + 49 +38+  58  +21+ 25+38+  77 +23+  73  + 19+21+ 25+ 49 +30+ 36 +  43 + 19+30+  52 +  53 + 19+  50 + 56 +38+  58  +   68  =1169
# And Jacob called unto his sons, and said, Gather yourselves together, that I may tell you that which shall befall you in the last days.
#  19+  31 +  37  + 70 + 36+  67 + 19+  33 +  59  +   161    +    98   + 49 +9+ 39+ 49 + 61+ 49 +  51 +  52 +  38  + 61+23+ 33+ 52 +  49 =1245
# Then the LORD said unto Moses, Go in unto Pharaoh, and tell him, Thus saith the LORD God of the Hebrews, Let my people go, that they may serve me.
#  47 + 33+ 49 + 33 + 70 +  71  +22+23+ 70 +   67   + 19+ 49 + 30 + 68 +  57 + 33+ 49 + 26+21+ 33+   80   + 37+38+  69  + 22+ 49 + 58 + 39+  69 + 18=1349
# And that thou mayest tell in the ears of thy son, and of thy son's son, what things I have wrought in Egypt, and my signs which I have done among them; that ye may know how that I am the LORD.
#  19+ 49 + 64 +  83  + 49 +23+ 33+ 43 +21+ 53+ 48 + 19+21+ 53+  67 + 48 + 52 +  77  +9+ 36 +  112  +23+  73  + 19+38+  68 +  51 +9+ 36 + 38 +  50 +  46 + 49 +30+ 39+ 63 + 46+ 49 +9+14+ 33+  49 =1811
# Is not this the word that we did tell thee in Egypt, saying, Let us alone, that we may serve the Egyptians? For it had been better for us to serve the Egyptians, than that we should die in the wilderness.
# 28+ 49+ 56 + 33+ 60 + 49 +28+ 17+ 49 + 38 +23+  73  +   75  + 37+40+  47  + 49 +28+ 39+  69 + 33+   116    + 39+29+ 13+ 26 +  70  + 39+40+35+  69 + 33+   116    + 43 + 49 +28+  79  + 18+23+ 33+    128    =1946
# And Moses went up unto God, and the LORD called unto him out of the mountain, saying, Thus shalt thou say to the house of Jacob, and tell the children of Israel;
#  19+  71 + 62 +37+ 70 + 26 + 19+ 33+ 49 +  37  + 70 + 30+ 56+21+ 33+   107   +   75  + 68 +  60 + 64 + 45+35+ 33+  68 +21+  31  + 19+ 49 + 33+   73   +21+   64  =1499
# And he that owneth the house shall come and tell the priest, saying, It seemeth to me there is as it were a plague in the house:
#  19+13+ 49 +  85  + 33+  68 +  52 + 36 + 19+ 49 + 33+   87  +   75  +29+   75  +35+18+  56 +28+20+29+ 51 +1+  62  +23+ 33+  68  =1146
# And they will tell it to the inhabitants of this land: for they have heard that thou LORD art among this people, that thou LORD art seen face to face, and that thy cloud standeth over them, and that thou goest before them, by day time in a pillar of a cloud, and in a pillar of fire by night.
#  19+ 58 + 56 + 49 +29+35+ 33+    117    +21+ 56 +  31 + 39+ 58 + 36 +  36 + 49 + 64 + 49 + 39+  50 + 56 +   69  + 49 + 64 + 49 + 39+ 43 + 15 +35+  15 + 19+ 49 + 53+  55 +   91   + 60 +  46 + 19+ 49 + 64 +  66 +  51  +  46 +27+ 30+ 47 +23+1+  68  +21+1+  55  + 19+23+1+  68  +21+ 38 +27+  58  =2554
# And when king Arad the Canaanite, which dwelt in the south, heard tell that Israel came by the way of the spies; then he fought against Israel, and took some of them prisoners.
#  19+ 50 + 41 + 24 + 33+    68    +  51 +  64 +23+ 33+  83  +  36 + 49 + 49 +  64  + 22 +27+ 33+ 49+21+ 33+  68  + 47 +13+  77  +   71  +   64  + 19+ 61 + 52 +21+ 46 +   133    =1544
# And Balaam said unto Balak, Stand by thy burnt offering, and I will go: peradventure the LORD will come to meet me: and whatsoever he sheweth me I will tell thee. And he went to an high place.
#  19+  30  + 33 + 70 +  27  +  58 +27+ 53+  75 +    80   + 19+9+ 56 + 22+    149     + 33+ 49 + 56 + 36 +35+ 43 + 18+ 19+   136    +13+   88  +18+9+ 56 + 49 +  38 + 19+13+ 62 +35+15+ 32 +  37  =1636
# According to the sentence of the law which they shall teach thee, and according to the judgment which they shall tell thee, thou shalt do: thou shalt not decline from the sentence which they shall shew thee, to the right hand, nor to the left.
#     74   +35+ 33+   85   +21+ 33+ 36+  51 + 58 +  52 +  37 +  38 + 19+    74   +35+ 33+   94   +  51 + 58 +  52 + 49 +  38 + 64 +  60 + 19+ 64 +  60 + 49+   52  + 52 + 33+   85   +  51 + 58 +  52 + 55 +  38 +35+ 33+  62 +  27 + 47+35+ 33+  43 =2163
# Remember the days of old, consider the years of many generations: ask thy father, and he will shew thee; thy elders, and they will tell thee.
#    79   + 33+ 49 +21+ 31 +   87   + 33+  68 +21+ 53 +    127     + 31+ 53+   58  + 19+13+ 56 + 55 +  38 + 53+   63  + 19+ 58 + 56 + 49 +  38 =1261
# And Joshua said unto Achan, My son, give, I pray thee, glory to the LORD God of Israel, and make confession unto him; and tell me now what thou hast done; hide it not from me.
#  19+  74  + 33 + 70 +  27  +38+ 48 +  43 +9+ 60 +  38 +  77 +35+ 33+ 49 + 26+21+   64  + 19+ 30 +   119    + 70 + 30 + 19+ 49 +18+ 52+ 52 + 64 + 48 +  38 + 26 +29+ 49+ 52 + 18=1546
# And it was so, when Gideon heard the telling of the dream, and the interpretation thereof, that he worshipped, and returned into the host of Israel, and said, Arise; for the LORD hath delivered into your hand the host of Midian.
#  19+29+ 43+ 34+ 50 +  54  +  36 + 33+   79  +21+ 33+  41  + 19+ 33+     184      +   77   + 49 +13+    133    + 19+  105   + 58 + 33+ 62 +21+   64  + 19+  33 +  52  + 39+ 33+ 49 + 37 +    84   + 58 + 79 + 27 + 33+ 62 +21+   50  =2018
# And Samson's wife wept before him, and said, Thou dost but hate me, and lovest me not: thou hast put forth a riddle unto the children of my people, and hast not told it me. And he said unto her, Behold, I have not told it my father nor my mother, and shall I tell it thee?
#  19+  100   + 43 + 64 +  51  + 30 + 19+  33 + 64 + 58 + 43+ 34 + 18+ 19+  93  +18+ 49 + 64 + 48 + 57+  67 +1+  52  + 70 + 33+   73   +21+38+   69  + 19+ 48 + 49+ 51 +29+ 18+ 19+13+ 33 + 70 + 31 +   46  +9+ 36 + 49+ 51 +29+38+  58  + 47+38+   79  + 19+  52 +9+ 49 +29+  38 =2404
# And Delilah said to Samson, Tell me, I pray thee, wherein thy great strength lieth, and wherewith thou mightest be bound to afflict thee.
#  19+   51  + 33 +35+   81  + 49 + 18+9+ 60 +  38 +   82  + 53+  51 +  111   +  54  + 19+   119   + 64 +  101   +7 +  56 +35+   57  +  38 =1240
# And Delilah said unto Samson, Behold, thou hast mocked me, and told me lies: now tell me, I pray thee, wherewith thou mightest be bound.
#  19+   51  + 33 + 70 +   81  +   46  + 64 + 48 +  51  + 18+ 19+ 51 +18+  45 + 52+ 49 + 18+9+ 60 +  38 +   119   + 64 +  101   +7 +  56  =1187
# And Delilah said unto Samson, Hitherto thou hast mocked me, and told me lies: tell me wherewith thou mightest be bound. And he said unto her, If thou weavest the seven locks of my head with the web.
#  19+   51  + 33 + 70 +   81  +  103   + 64 + 48 +  51  + 18+ 19+ 51 +18+  45 + 49 +18+   119   + 64 +  101   +7 +  56  + 19+13+ 33 + 70 + 31 +15+ 64 +   95  + 33+  65 +  60 +21+38+ 18 + 60 + 33+ 30 =1783
# (Now the children of Benjamin heard that the children of Israel were gone up to Mizpeh.) Then said the children of Israel, Tell us, how was this wickedness?
#  52 + 33+   73   +21+   68   +  36 + 49 + 33+   73   +21+  64  + 51 + 41 +37+35+   77   + 47 + 33 + 33+   73   +21+   64  + 49 + 40+ 46+ 43+ 56 +    112    =1381
# And it shall be, when he lieth down, that thou shalt mark the place where he shall lie, and thou shalt go in, and uncover his feet, and lay thee down; and he will tell thee what thou shalt do.
#  19+29+  52 + 7 + 50 +13+  54 +  56 + 49 + 64 +  60 + 43 + 33+  37 +  59 +13+  52 + 26 + 19+ 64 +  60 +22+ 23+ 19+   98  + 36+  36 + 19+ 38+ 38 +  56 + 19+13+ 56 + 49 + 38 + 52 + 64 +  60 + 19=1614
# And I thought to advertise thee, saying, Buy it before the inhabitants, and before the elders of my people. If thou wilt redeem it, redeem it: but if thou wilt not redeem it, then tell me, that I may know: for there is none to redeem it beside thee; and I am after thee. And he said, I will redeem it.
#  19+9+   99  +35+   103   +  38 +   75  + 48+29+  51  + 33+    117     + 19+  51  + 33+  63  +21+38+   69  +15+ 64 + 64 +  50  + 29+  50  + 29+ 43+15+ 64 + 64 + 49+  50  + 29+ 47 + 49 + 18+ 49 +9+ 39+  63 + 39+  56 +28+ 48 +35+  50  +29+  44  +  38 + 19+9+14+  50 +  38 + 19+13+  33 +9+ 56 +  50  + 29=2545
# And the Philistines called for the priests and the diviners, saying, What shall we do to the ark of the LORD? tell us wherewith we shall send it to his place.
#  19+ 33+    140    +  37  + 39+ 33+  106  + 19+ 33+   100   +   75  + 52 +  52 +28+19+35+ 33+ 30+21+ 33+  49 + 49 +40+   119   +28+  52 + 42 +29+35+ 36+  37  =1453
# And the servant answered Saul again, and said, Behold, I have here at hand the fourth part of a shekel of silver: that will I give to the man of God, to tell us our way.
#  19+ 33+   99  +   89   + 53 +  32  + 19+  33 +   46  +9+ 36 + 36 +21+ 27 + 33+  88  + 55 +21+1+  60  +21+   85  + 49 + 56 +9+ 43 +35+ 33+ 28+21+ 26 +35+ 49 +40+ 54+ 49 =1443
# Then Saul drew near to Samuel in the gate, and said, Tell me, I pray thee, where the seer's house is.
#  47 + 53 + 50 + 38 +35+  71  +23+ 33+  33 + 19+  33 + 49 + 18+9+ 60 +  38 +  59 + 33+  66  +  68 + 28=863
# And Samuel answered Saul, and said, I am the seer: go up before me unto the high place; for ye shall eat with me to day, and to morrow I will let thee go, and will tell thee all that is in thine heart.
#  19+  71  +   89   +  53 + 19+  33 +9+14+ 33+  47 +22+37+  51  +18+ 70 + 33+ 32 +  37  + 39+30+  52 + 26+ 60 +18+35+ 30 + 19+35+ 102  +9+ 56 + 37+ 38 + 22+ 19+ 56 + 49 + 38 + 25+ 49 +28+23+  56 +  52  =1690
# And Saul's uncle said, Tell me, I pray thee, what Samuel said unto you.
#  19+  72  +  55 +  33 + 49 + 18+9+ 60 +  38 + 52 +  71  + 33 + 70 + 61 =640
# Then Saul said to Jonathan, Tell me what thou hast done. And Jonathan told him, and said, I did but taste a little honey with the end of the rod that was in mine hand, and, lo, I must die.
#  47 + 53 + 33 +35+    83   + 49 +18+ 52 + 64 + 48 +  38 + 19+   83   + 51 + 30 + 19+  33 +9+ 17+ 43+  65 +1+  78  +  67 + 60 + 33+ 23+21+ 33+ 37+ 49 + 43+23+ 41 +  27 + 19 + 27+9+ 73 + 18 =1571
# Then Samuel said unto Saul, Stay, and I will tell thee what the LORD hath said to me this night. And he said unto him, Say on.
#  47 +  71  + 33 + 70 +  53 +  65 + 19+9+ 56 + 49 + 38 + 52 + 33+ 49 + 37 + 33 +35+18+ 56 +  58  + 19+13+ 33 + 70 + 30 + 45+ 29=1120
# And when Saul saw David go forth against the Philistine, he said unto Abner, the captain of the host, Abner, whose son is this youth? And Abner said, As thy soul liveth, O  king, I cannot tell.
#  19+ 50 + 53 + 43+  40 +22+  67 +   71  + 33+    121    +13+ 33 + 70 +  40  + 33+   64  +21+ 33+  62 +  40  +  70 + 48+28+ 56 +  89  + 19+  40 +  33 +20+ 53+ 67 +   76  +15+  41 +9+  67  +  49 =1708
# And I will go out and stand beside my father in the field where thou art, and I will commune with my father of thee; and what I see, that I will tell thee.
#  19+9+ 56 +22+ 56+ 19+  58 +  44  +38+  58  +23+ 33+  36 +  59 + 64 + 39 + 19+9+ 56 +   84  + 60 +38+  58  +21+  38 + 19+ 52 +9+ 29 + 49 +9+ 56 + 49 +  38 =1326
# And Jonathan said, Far be it from thee: for if I knew certainly that evil were determined by my father to come upon thee, then would not I tell it thee?
#  19+   83   +  33 + 25+7 +29+ 52 +  38 + 39+15+9+ 53 +   107   + 49 + 48 + 51 +    97    +27+38+  58  +35+ 36 + 66 +  38 + 47 +  75 + 49+9+ 49 +29+  38 =1348
# Then said David to Jonathan, Who shall tell me? or what if thy father answer thee roughly?
#  47 + 33 +  40 +35+    83   + 46+  52 + 49 + 18+33+ 52 +15+ 53+  58  +  80  + 38 +  106   =838
# And David said unto Abiathar, I knew it that day, when Doeg the Edomite was there, that he would surely tell Saul: I have occasioned the death of all the persons of thy father's house.
#  19+  40 + 33 + 70 +    60   +9+ 53 +29+ 49 + 30 + 50 + 31 + 33+   71  + 43+  56  + 49 +13+  75 + 100  + 49 +  53 +9+ 36 +    88    + 33+  38 +21+ 25+ 33+  106  +21+ 53+   77   +  68  =1623
# Will the men of Keilah deliver me up into his hand? will Saul come down, as thy servant hath heard? O  LORD God of Israel, I beseech thee, tell thy servant. And the LORD said, He will come down.
#  56 + 33+ 32+21+  46  +   75  +18+37+ 58 + 36+  27 + 56 + 53 + 36 +  56 +20+ 53+   99  + 37 +  36  +15+ 49 + 26+21+   64  +9+   47  +  38 + 49 + 53+   99   + 19+ 33+ 49 +  33 +13+ 56 + 36 +  56 =1650
# And David saved neither man nor woman alive, to bring tidings to Gath, saying, Lest they should tell on us, saying, So did David, and so will be his manner all the while he dwelleth in the country of the Philistines.
#  19+  40 +  51 +   79  + 28+ 47+  66 +  49  +35+  50 +   82  +35+  36 +   75  + 56 + 58 +  79  + 49 +29+ 40+   75  +34+ 17+  40  + 19+34+ 56 +7 + 36+  65  + 25+ 33+  57 +13+   89   +23+ 33+  116  +21+ 33+    140     =1969
# And David said unto him, How went the matter? I pray thee, tell me. And he answered, That the people are fled from the battle, and many of the people also are fallen and dead; and Saul and Jonathan his son are dead also.
#  19+  40 + 33 + 70 + 30 + 46+ 62 + 33+   77  +9+ 60 +  38 + 49 + 18+ 19+13+    89   + 49 + 33+  69  + 24+ 27 + 52 + 33+   60  + 19+ 53 +21+ 33+  69  + 47 + 24+  50  + 19+  14 + 19+ 53 + 19+   83   + 36+ 48+ 24+ 14 +  47 =1744
# Tell it not in Gath, publish it not in the streets of Askelon; lest the daughters of the Philistines rejoice, lest the daughters of the uncircumcised triumph.
#  49 +29+ 49+23+  36 +   87  +29+ 49+23+ 33+  106  +21+   77   + 56 + 33+   103   +21+ 33+    140    +   65   + 56 + 33+   103   +21+ 33+     142     +  105   =1555
# Go and tell my servant David, Thus saith the LORD, Shalt thou build me an house for me to dwell in?
# 22+ 19+ 49 +38+   99  +  40  + 68 +  57 + 33+  49 +  60 + 64 +  48 +18+15+  68 + 39+18+35+  56 + 23=918
# And as since the time that I commanded judges to be over my people Israel, and have caused thee to rest from all thine enemies. Also the LORD telleth thee that he will make thee an house.
#  19+20+  50 + 33+ 47 + 49 +9+    72   +  66  +35+7 + 60 +38+  69  +   64  + 19+ 36 +  53  + 38 +35+ 62 + 52 + 25+  56 +   70   + 47 + 33+ 49 +   82  + 38 + 49 +13+ 56 + 30 + 38 +15+  68  =1602
# And charged the messenger, saying, When thou hast made an end of telling the matters of the war unto the king,
#  19+   46  + 33+   105    +   75  + 50 + 64 + 48 + 23 +15+ 23+21+   79  + 33+   96  +21+ 33+ 42+ 70 + 33+  41 =970
# And it came to pass on the seventh day, that the child died. And the servants of David feared to tell him that the child was dead: for they said, Behold, while the child was yet alive, we spake unto him, and he would not hearken unto our voice: how will he then vex himself, if we tell him that the child is dead?
#  19+29+ 22 +35+ 55 +29+ 33+   93  + 30 + 49 + 33+  36 +  22 + 19+ 33+  118   +21+  40 +  39  +35+ 49 + 30+ 49 + 33+  36 + 43+  14 + 39+ 58 +  33 +   46  +  57 + 33+  36 + 43+ 50+  49  +28+  52 + 70 + 30 + 19+13+  75 + 49+   62  + 70 + 54+  54  + 46+ 56 +13+ 47 + 51+   72   +15+28+ 49 + 30+ 49 + 33+  36 +28+  14 =2631
# And he said, While the child was yet alive, I fasted and wept: for I said, Who can tell whether GOD will be gracious to me, that the child may live?
#  19+13+  33 +  57 + 33+  36 + 43+ 50+  49  +9+  55  + 19+  64 + 39+9+  33 + 46+ 18+ 49 +   87  + 26+ 56 +7 +   93   +35+ 18+ 49 + 33+  36 + 39+  48 =1201
# And he said unto him, Why art thou, being the king's son, lean from day to day? wilt thou not tell me? And Amnon said unto him, I love Tamar, my brother Absalom's sister.
#  19+13+ 33 + 70 + 30 + 56+ 39+  64 +  37 + 33+  60  + 48 + 32 + 52 + 30+35+ 30 + 64 + 64 + 49+ 49 + 18+ 19+  57 + 33 + 70 + 30 +9+ 54 +  53  +38+   86  +    82   +   90  =1546
# And hast thou not there with thee Zadok and Abiathar the priests? therefore it shall be, that what thing soever thou shalt hear out of the king's house, thou shalt tell it to Zadok and Abiathar the priests.
#  19+ 48 + 64 + 49+  56 + 60 + 38 +  57 + 19+   60   + 33+  106   +   100   +29+  52 + 7 + 49 + 52 +  58 +  84  + 64 +  60 + 32 + 56+21+ 33+  60  +  68  + 64 +  60 + 49 +29+35+  57 + 19+   60   + 33+  106   =1946
# Now therefore send quickly, and tell David, saying, Lodge not this night in the plains of the wilderness, but speedily pass over; lest the king be swallowed up, and all the people that are with him.
#  52+   100   + 42 +   98   + 19+ 49 +  40  +   75  +  43 + 49+ 56 +  58 +23+ 33+  71  +21+ 33+    128    + 43+   95   + 55 +  60 + 56 + 33+ 41 +7 +   114   + 37+ 19+ 25+ 33+  69  + 49 + 24+ 60 + 30 =1840
# Then said Joab to Cushi, Go tell the king what thou hast seen. And Cushi bowed himself unto Joab, and ran.
#  47 + 33 + 28 +35+  60  +22+ 49 + 33+ 41 + 52 + 64 + 48 +  43 + 19+  60 +  49 +   72  + 70 +  28 + 19+ 33 =905
# And thou, my lord, O  king, the eyes of all Israel are upon thee, that thou shouldest tell them who shall sit on the throne of my lord the king after him.
#  19+  64 +38+  49 +15+  41 + 33+ 54 +21+ 25+  64  + 24+ 66 +  38 + 49 + 64 +   123   + 49 + 46 + 46+  52 + 48+29+ 33+  80  +21+38+ 49 + 33+ 41 +  50 + 30 =1432
# And take with thee ten loaves, and cracknels, and a cruse of honey, and go to him: he shall tell thee what shall become of the child.
#  19+ 37 + 60 + 38 + 39+   74  + 19+    86    + 19+1+  66 +21+  67  + 19+22+35+ 30 +13+  52 + 49 + 38 + 52 +  52 +  43  +21+ 33+  36  =1041
# Go, tell Jeroboam, Thus saith the LORD God of Israel, Forasmuch as I exalted thee from among the people, and made thee prince over my people Israel,
#  22+ 49 +    79   + 68 +  57 + 33+ 49 + 26+21+   64  +   104   +20+9+   71  + 38 + 52 +  50 + 33+   69  + 19+ 23 + 38 +  65  + 60 +38+  69  +   64  =1290
# And he answered him, I am: go, tell thy lord, Behold, Elijah is here.
#  19+13+   89   + 30 +9+ 14+ 22+ 49 + 53+  49 +   46  +  45  +28+  36 =502
# And now thou sayest, Go, tell thy lord, Behold, Elijah is here.
#  19+ 52+ 64 +   89  + 22+ 49 + 53+  49 +   46  +  45  +28+  36 =552
# And it shall come to pass, as soon as I am gone from thee, that the Spirit of the LORD shall carry thee whither I know not; and so when I come and tell Ahab, and he cannot find thee, he shall slay me: but I thy servant fear the LORD from my youth.
#  19+29+  52 + 36 +35+  55 +20+ 63 +20+9+14+ 41 + 52 +  38 + 49 + 33+  91  +21+ 33+ 49 +  52 +  65 + 38 +   91  +9+ 63 + 49 + 19+34+ 50 +9+ 36 + 19+ 49 +  12 + 19+13+  67  + 33 +  38 +13+  52 + 57 + 18+ 43+9+ 53+   99  + 30 + 33+ 49 + 52 +38+  89  =2159
# And now thou sayest, Go, tell thy lord, Behold, Elijah is here: and he shall slay me.
#  19+ 52+ 64 +   89  + 22+ 49 + 53+  49 +   46  +  45  +28+  36 + 19+13+  52 + 57 + 18=711
# Wherefore he said unto the messengers of Benhadad, Tell my lord the king, All that thou didst send for to thy servant at the first I will do: but this thing I may not do. And the messengers departed, and brought him word again.
#    103   +13+ 33 + 70 + 33+   124    +21+    39   + 49 +38+ 49 + 33+  41 + 25+ 49 + 64 +  56 + 42 + 39+35+ 53+   99  +21+ 33+  72 +9+ 56 + 19+ 43+ 56 +  58 +9+ 39+ 49+ 19+ 19+ 33+   124    +    73   + 19+   91  + 30+ 60 +  32  =2072
# And the king of Israel answered and said, Tell him, Let not him that girdeth on his harness boast himself as he that putteth it off.
#  19+ 33+ 41 +21+  64  +   89   + 19+  33 + 49 + 30 + 37+ 49+ 30+ 49 +   71  +29+ 36+   84  +  57 +   72  +20+13+ 49 +  110  +29+ 27 =1160
# And the king said unto him, How many times shall I adjure thee that thou tell me nothing but that which is true in the name of the LORD?
#  19+ 33+ 41 + 33 + 70 + 30 + 46+ 53 +  66 +  52 +9+  59  + 38 + 49 + 64 + 49 +18+   87  + 43+ 49 +  51 +28+ 64 +23+ 33+ 33 +21+ 33+  49 =1243
# And the king of Israel said unto Jehoshaphat, Did I not tell thee that he would prophesy no good concerning me, but evil?
#  19+ 33+ 41 +21+  64  + 33 + 70 +    111     + 17+9+ 49+ 49 + 38 + 49 +13+  75 +  122   +29+ 41 +   102    + 18+ 43+  48 =1094
# And Elisha said unto her, What shall I do for thee? tell me, what hast thou in the house? And she said, Thine handmaid hath not any thing in the house, save a pot of oil.
#  19+  54  + 33 + 70 + 31 + 52 +  52 +9+19+ 39+  38 + 49 + 18+ 52 + 48 + 64 +23+ 33+  68  + 19+ 32+  33 +  56 +   54   + 37 + 49+ 40+  58 +23+ 33+  68  + 47 +1+ 51+21+ 36 =1429
# And one of his servants said, None, my lord, O  king: but Elisha, the prophet that is in Israel, telleth the king of Israel the words that thou speakest in thy bedchamber.
#  19+ 34+21+ 36+  118   +  33 +  48 +38+  49 +15+  41 + 43+   54  + 33+   98  + 49 +28+23+   64  +   82  + 33+ 41 +21+  64  + 33+  79 + 49 + 64 +   96   +23+ 53+     61    =1543
# Then they said one to another, We do not well: this day is a day of good tidings, and we hold our peace: if we tarry till the morning light, some mischief will come upon us: now therefore come, that we may go and tell the king's household.
#  47 + 58 + 33 + 34+35+   81   +28+19+ 49+  52 + 56 + 30+28+1+ 30+21+ 41 +   82   + 19+28+ 39 + 54+  30  +15+28+  82 + 53 + 33+   90  +  56  + 52 +   72   + 56 + 36 + 66 + 40+ 52+   100   +  36 + 49 +28+ 39+22+ 19+ 49 + 33+  60  +   107    =2168
# And the king talked with Gehazi the servant of the man of God, saying, Tell me, I pray thee, all the great things that Elisha hath done.
#  19+ 33+ 41 +  53  + 60 +  56  + 33+   99  +21+ 33+ 28+21+ 26 +   75  + 49 + 18+9+ 60 +  38 + 25+ 33+  51 +  77  + 49 +  54  + 37 +  38 =1136
# And it came to pass, as he was telling the king how he had restored a dead body to life, that, behold, the woman, whose son he had restored to life, cried to the king for her house and for her land. And Gehazi said, My lord, O  king, this is the woman, and this is her son, whom Elisha restored to life.
#  19+29+ 22 +35+  55 +20+13+ 43+   79  + 33+ 41 + 46+13+ 13+  104   +1+ 14 + 46 +35+  32 +  49 +   46  + 33+  66  +  70 + 48+13+ 13+  104   +35+  32 +  39 +35+ 33+ 41 + 39+ 31+  68 + 19+ 39+ 31+  31 + 19+  56  +  33 +38+  49 +15+  41 + 56 +28+ 33+  66  + 19+ 56 +28+ 31+ 48 + 59 +  54  +  104   +35+  32 =2508
# And they said, It is false; tell us now. And he said, Thus and thus spake he to me, saying, Thus saith the LORD, I have anointed thee king over Israel.
#  19+ 58 +  33 +29+28+  43  + 49 +40+ 52 + 19+13+  33 + 68 + 19+ 68 +  52 +13+35+ 18+   75  + 68 +  57 + 33+  49 +9+ 36 +   82   + 38 + 41 + 60 +   64  =1301
# But king Joram was returned to be healed in Jezreel of the wounds which the Syrians had given him, when he fought with Hazael king of Syria.) And Jehu said, If it be your minds, then let none go forth nor escape out of the city to go to tell it in Jezreel.
#  43+ 41 +  57 + 43+  105   +35+7 +  35  +23+   81  +21+ 33+  96  +  51 + 33+  105  + 13+  57 + 30 + 50 +13+  77  + 60 +  53  + 41 +21+   72  + 19+ 44 +  33 +15+29+7 + 79 +  59  + 47 + 37+ 48 +22+  67 + 47+  49  + 56+21+ 33+ 57 +35+22+35+ 49 +29+23+   81   =2339
# Turn again, and tell Hezekiah the captain of my people, Thus saith the LORD, the God of David thy father, I have heard thy prayer, I have seen thy tears: behold, I will heal thee: on the third day thou shalt go up unto the house of the LORD.
#  73 +  32  + 19+ 49 +   73   + 33+   64  +21+38+   69  + 68 +  57 + 33+  49 + 33+ 26+21+  40 + 53+   58  +9+ 36 +  36 + 53+   83  +9+ 36 + 43 + 53+  63  +   46  +9+ 56 + 26 +  38 +29+ 33+  59 + 30+ 64 +  60 +22+37+ 70 + 33+  68 +21+ 33+  49 =2113
# And she said unto them, Thus saith the LORD God of Israel, Tell the man that sent you to me,
#  19+ 32+ 33 + 70 +  46 + 68 +  57 + 33+ 49 + 26+21+   64  + 49 + 33+ 28+ 49 + 58 + 61+35+ 18=849
# Go and tell David my servant, Thus saith the LORD, Thou shalt not build me an house to dwell in:
# 22+ 19+ 49 +  40 +38+   99   + 68 +  57 + 33+  49 + 64 +  60 + 49+  48 +18+15+  68 +35+  56 + 23=910
# And since the time that I commanded judges to be over my people Israel. Moreover I will subdue all thine enemies. Furthermore I tell thee that the LORD will build thee an house.
#  19+  50 + 33+ 47 + 49 +9+    72   +  66  +35+7 + 60 +38+  69  +   64  +  111   +9+ 56 +  72  + 25+  56 +   70   +    147    +9+ 49 + 38 + 49 + 33+ 49 + 56 +  48 + 38 +15+  68  =1616
# Go and tell David, saying, Thus saith the LORD, I offer thee three things: choose thee one of them, that I may do it unto thee.
# 22+ 19+ 49 +  40  +   75  + 68 +  57 + 33+  49 +9+  50 + 38 +  56 +   77  +  65  + 38 + 34+21+  46 + 49 +9+ 39+19+29+ 70 +  38 =1099
# And the king of Israel said to Jehoshaphat, Did I not tell thee that he would not prophesy good unto me, but evil?
#  19+ 33+ 41 +21+  64  + 33 +35+    111     + 17+9+ 49+ 49 + 38 + 49 +13+  75 + 49+  122   + 41 + 70 + 18+ 43+  48 =1047
# And she answered them, Thus saith the LORD God of Israel, Tell ye the man that sent you to me,
#  19+ 32+   89   +  46 + 68 +  57 + 33+ 49 + 26+21+   64  + 49 +30+ 33+ 28+ 49 + 58 + 61+35+ 18=865
# And the Sabeans fell upon them, and took them away; yea, they have slain the servants with the edge of the sword; and I only am escaped alone to tell thee.
#  19+ 33+   61  + 35 + 66 +  46 + 19+ 61 + 46 +  50 + 31 + 58 + 36 +  55 + 33+  118   + 60 + 33+ 21 +21+ 33+  79  + 19+9+ 66 +14+   53  +  47 +35+ 49 +  38 =1344
# While he was yet speaking, there came also another, and said, The fire of God is fallen from heaven, and hath burned up the sheep, and the servants, and consumed them; and I only am escaped alone to tell thee.
#   57 +13+ 43+ 50+    82   +  56 + 22 + 47 +   81   + 19+  33 + 33+ 38 +21+ 26+28+  50  + 52 +   55  + 19+ 37 +  64  +37+ 33+  53  + 19+ 33+   118   + 19+   94   +  46 + 19+9+ 66 +14+   53  +  47 +35+ 49 +  38 =1708
# While he was yet speaking, there came also another, and said, The Chaldeans made out three bands, and fell upon the camels, and have carried them away, yea, and slain the servants with the edge of the sword; and I only am escaped alone to tell thee.
#   57 +13+ 43+ 50+    82   +  56 + 22 + 47 +   81   + 19+  33 + 33+    67   + 23 + 56+  56 +  40  + 19+ 35 + 66 + 33+   53  + 19+ 36 +   58  + 46 +  50 + 31 + 19+  55 + 33+  118   + 60 + 33+ 21 +21+ 33+  79  + 19+9+ 66 +14+   53  +  47 +35+ 49 +  38 =2026
# And, behold, there came a great wind from the wilderness, and smote the four corners of the house, and it fell upon the young men, and they are dead; and I only am escaped alone to tell thee.
#  19 +   46  +  56 + 22 +1+  51 + 50 + 52 + 33+    128    + 19+  72 + 33+ 60 +   92  +21+ 33+  68  + 19+29+ 35 + 66 + 33+  82 + 32 + 19+ 58 + 24+  14 + 19+9+ 66 +14+   53  +  47 +35+ 49 +  38 =1597
# Shall not they teach thee, and tell thee, and utter words out of their heart?
#   52 + 49+ 58 +  37 +  38 + 19+ 49 +  38 + 19+  84 +  79 + 56+21+  60 +  52  =711
# But ask now the beasts, and they shall teach thee; and the fowls of the air, and they shall tell thee:
#  43+ 31+ 52+ 33+   66  + 19+ 58 +  52 +  37 +  38 + 19+ 33+  75 +21+ 33+ 28 + 19+ 58 +  52 + 49 +  38 =854
# Let men of understanding tell me, and let a wise man hearken unto me.
#  37+ 32+21+     150     + 49 + 18+ 19+ 37+1+ 56 + 28+   62  + 70 + 18=598
# I may tell all my bones: they look and stare upon me.
# 9+ 39+ 49 + 25+38+  55  + 58 + 53 + 19+  63 + 66 + 18=492
# That I may publish with the voice of thanksgiving, and tell of all thy wondrous works.
#  49 +9+ 39+   87  + 60 + 33+  54 +21+     141     + 19+ 49 +21+ 25+ 53+  129   +  86  =875
# And if he come to see me, he speaketh vanity: his heart gathereth iniquity to itself; when he goeth abroad, he telleth it.
#  19+15+13+ 36 +35+ 29+ 18+13+   85   +   91  + 36+  52 +    92   +  124   +35+   71  + 50 +13+  55 +   41  +13+   82  + 29=1047
# Walk about Zion, and go round about her: tell the towers thereof.
#  47 +  59 +  64 + 19+22+  72 +  59 + 31 + 49 + 33+ 100  +   77   =632
# Mark ye well her bulwarks, consider her palaces; that ye may tell it to the generation following.
#  43 +30+ 52 + 31+   107   +   87   + 31+   57   + 49 +30+ 39+ 49 +29+35+ 33+   108    +   113    =923
# If I were hungry, I would not tell thee: for the world is mine, and the fulness thereof.
# 15+9+ 51 +   93  +9+  75 + 49+ 49 +  38 + 39+ 33+  72 +28+  41 + 19+ 33+   96  +   77   =826
# Thou tellest my wanderings: put thou my tears into thy bottle: are they not in thy book?
#  64 +   93  +38+    114    + 57+ 64 +38+  63 + 58 + 53+   74  + 24+ 58 + 49+23+ 53+  43 =966
# He that worketh deceit shall not dwell within my house: he that telleth lies shall not tarry in my sight.
# 13+ 49 +  100  +  46  +  52 + 49+  56 +  83  +38+  68  +13+ 49 +   82  + 45 +  52 + 49+  82 +23+38+  63  =1050
# He telleth the number of the stars; he calleth them all by their names.
# 13+   82  + 33+  73  +21+ 33+  77  +13+   61  + 46 + 25+27+  60 +  52  =616
# Who hath ascended up into heaven, or descended? who hath gathered the wind in his fists? who hath bound the waters in a garment? who hath established all the ends of the earth? what is his name, and what is his son's name, if thou canst tell?
#  46+ 37 +   55   +37+ 58 +   55  +33+    63    + 46+ 37 +   68   + 33+ 50 +23+ 36+  73  + 46+ 37 +  56 + 33+  86  +23+1+   78   + 46+ 37 +    104    + 25+ 33+ 42 +21+ 33+  52  + 52 +28+ 36+  33 + 19+ 52 +28+ 36+  67 +  33 +15+ 64 +  57 +  49 =2072
# For who knoweth what is good for man in this life, all the days of his vain life which he spendeth as a shadow? for who can tell a man what shall be after him under the sun?
#  39+ 46+   96  + 52 +28+ 41 + 39+ 28+23+ 56 +  32 + 25+ 33+ 49 +21+ 36+ 46 + 32 +  51 +13+   91   +20+1+   70  + 39+ 46+ 18+ 49 +1+ 28+ 52 +  52 +7 +  50 + 30+  62 + 33+ 54 =1489
# For he knoweth not that which shall be: for who can tell him when it shall be?
#  39+13+   96  + 49+ 49 +  51 +  52 + 7 + 39+ 46+ 18+ 49 + 30+ 50 +29+  52 + 7 =676
# A fool also is full of words: a man cannot tell what shall be; and what shall be after him, who can tell him?
# 1+ 48 + 47 +28+ 51 +21+  79  +1+ 28+  67  + 49 + 52 +  52 + 7 + 19+ 52 +  52 +7 +  50 + 30 + 46+ 18+ 49 + 30 =884
# Curse not the king, no not in thy thought; and curse not the rich in thy bedchamber: for a bird of the air shall carry the voice, and that which hath wings shall tell the matter.
#   66 + 49+ 33+  41 +29+ 49+23+ 53+   99   + 19+  66 + 49+ 33+ 38 +23+ 53+     61    + 39+1+ 33 +21+ 33+ 28+  52 +  65 + 33+  54  + 19+ 49 +  51 + 37 +  72 +  52 + 49 + 33+   77  =1582
# Tell me, O  thou whom my soul loveth, where thou feedest, where thou makest thy flock to rest at noon: for why should I be as one that turneth aside by the flocks of thy companions?
#  49 + 18+15+ 64 + 59 +38+ 67 +   82  +  59 + 64 +   64   +  59 + 64 +  69  + 53+  47 +35+ 62 +21+  58 + 39+ 56+  79  +9+7 +20+ 34+ 49 +  106  +  38 +27+ 33+  66  +21+ 53+    119    =1803
# I charge you, O  daughters of Jerusalem, if ye find my beloved, that ye tell him, that I am sick of love.
# 9+  42  + 61 +15+   103   +21+   104    +15+30+ 33 +38+   65   + 49 +30+ 49 + 30 + 49 +9+14+ 42 +21+  54 =883
# And now go to; I will tell you what I will do to my vineyard: I will take away the hedge thereof, and it shall be eaten up; and break down the wall thereof, and it shall be trodden down:
#  19+ 52+22+ 35+9+ 56 + 49 + 61+ 52 +9+ 56 +19+35+38+    98   +9+ 56 + 37 + 50 + 33+  29 +   77   + 19+29+  52 +7 +  45 + 37+ 19+  37 + 56 + 33+ 48 +   77   + 19+29+  52 +7 +   80  +  56 =1603
# And he said, Go, and tell this people, Hear ye indeed, but understand not; and see ye indeed, but perceive not.
#  19+13+  33 + 22+ 19+ 49 + 56 +   69  + 32 +30+   41  + 43+   120    + 49 + 19+ 29+30+   41  + 43+   83   + 49 =889
# Where are they? where are thy wise men? and let them tell thee now, and let them know what the LORD of hosts hath purposed upon Egypt.
#   59 + 24+  58 +  59 + 24+ 53+ 56 + 32 + 19+ 37+ 46 + 49 + 38 + 52 + 19+ 37+ 46 + 63 + 52 + 33+ 49 +21+  81 + 37 +  114   + 66 +  73  =1297
# Behold, the former things are come to pass, and new things do I declare: before they spring forth I tell you of them.
#    46  + 33+  75  +  77  + 24+ 36 +35+  55 + 19+ 42+  77  +19+9+   48   +  51  + 58 +  83  +  67 +9+ 49 + 61+21+  46 =1040
# Tell ye, and bring them near; yea, let them take counsel together: who hath declared this from ancient time? who hath told it from that time? have not I the LORD? and there is no God else beside me; a just God and a Saviour; there is none beside me.
#  49 + 30+ 19+  50 + 46 +  38 + 31 + 37+ 46 + 37 +   89  +    98   + 46+ 37 +   52   + 56 + 52 +   66  +  47 + 46+ 37 + 51 +29+ 52 + 49 +  47 + 36 + 49+9+ 33+  49 + 19+  56 +28+29+ 26+ 41 +  44  + 18+1+ 70 + 26+ 19+1+  105   +  56 +28+ 48 +  44  + 18=2090
# Go ye forth of Babylon, flee ye from the Chaldeans, with a voice of singing declare ye, tell this, utter it even to the end of the earth; say ye, The LORD hath redeemed his servant Jacob.
# 22+30+  67 +21+   71   + 28 +30+ 52 + 33+    67    + 60 +1+  54 +21+   79  +   48  + 30+ 49 +  56 +  84 +29+ 46 +35+ 33+ 23+21+ 33+  52  + 45+ 30+ 33+ 49 + 37 +   59   + 36+   99  +  31  =1594
# And it shall come to pass, if they say unto thee, Whither shall we go forth? then thou shalt tell them, Thus saith the LORD; Such as are for death, to death; and such as are for the sword, to the sword; and such as are for the famine, to the famine; and such as are for the captivity, to the captivity.
#  19+29+  52 + 36 +35+  55 +15+ 58 + 45+ 70 +  38 +   91  +  52 +28+22+  67  + 47 + 64 +  60 + 49 +  46 + 68 +  57 + 33+  49 + 51 +20+ 24+ 39+  38  +35+  38  + 19+ 51 +20+ 24+ 39+ 33+  79  +35+ 33+  79  + 19+ 51 +20+ 24+ 39+ 33+   48  +35+ 33+   48  + 19+ 51 +20+ 24+ 39+ 33+   125    +35+ 33+   125    =2696
# And go forth unto the valley of the son of Hinnom, which is by the entry of the east gate, and proclaim there the words that I shall tell thee,
#  19+22+  67 + 70 + 33+  77  +21+ 33+ 48+21+   73  +  51 +28+27+ 33+  82 +21+ 33+ 45 +  33 + 19+   87   +  56 + 33+  79 + 49 +9+  52 + 49 +  38 =1308
# Which think to cause my people to forget my name by their dreams which they tell every man to his neighbour, as their fathers have forgotten my name for Baal.
#   51 +  62 +35+  49 +38+  69  +35+  71  +38+ 33 +27+  60 +  60  +  51 + 58 + 49 +  75 + 28+35+ 36+    99    +20+  60 +   77  + 36 +   120   +38+ 33 + 39+  16 =1498
# The prophet that hath a dream, let him tell a dream; and he that hath my word, let him speak my word faithfully. What is the chaff to the wheat? saith the LORD.
#  33+   98  + 49 + 37 +1+  41  + 37+ 30+ 49 +1+  41  + 19+13+ 49 + 37 +38+  60 + 37+ 30+  52 +38+ 60 +    120    + 52 +28+ 33+  24 +35+ 33+  57  +  57 + 33+  49 =1371
# Behold, I am against them that prophesy false dreams, saith the LORD, and do tell them, and cause my people to err by their lies, and by their lightness; yet I sent them not, nor commanded them: therefore they shall not profit this people at all, saith the LORD.
#    46  +9+14+   71  + 46 + 49 +  122   +  43 +   60  +  57 + 33+  49 + 19+19+ 49 +  46 + 19+  49 +38+  69  +35+ 41+27+  60 +  45 + 19+27+  60 +   113    + 50+9+ 58 + 46 + 49 + 47+    72   +  46 +   100   + 58 +  52 + 49+  84  + 56 +  69  +21+ 25 +  57 + 33+  49 =2364
# Go and tell Hananiah, saying, Thus saith the LORD; Thou hast broken the yokes of wood; but thou shalt make for them yokes of iron.
# 22+ 19+ 49 +    56   +   75  + 68 +  57 + 33+  49 + 64 + 48 +  65  + 33+  75 +21+  57 + 43+ 64 +  60 + 30 + 39+ 46 +  75 +21+  56 =1225
# In the cities of the mountains, in the cities of the vale, and in the cities of the south, and in the land of Benjamin, and in the places about Jerusalem, and in the cities of Judah, shall the flocks pass again under the hands of him that telleth them, saith the LORD.
# 23+ 33+  65  +21+ 33+   126    +23+ 33+  65  +21+ 33+  40 + 19+23+ 33+  65  +21+ 33+  83  + 19+23+ 33+ 31 +21+    68   + 19+23+ 33+  56  +  59 +   104    + 19+23+ 33+  65  +21+  44  +  52 + 33+  66  + 55 +  32 +  62 + 33+  46 +21+ 30+ 49 +   82  +  46 +  57 + 33+  49 =2233
# Thus saith the LORD, the God of Israel; Go and speak to Zedekiah king of Judah, and tell him, Thus saith the LORD; Behold, I will give this city into the hand of the king of Babylon, and he shall burn it with fire:
#  68 +  57 + 33+  49 + 33+ 26+21+   64  +22+ 19+  52 +35+   69   + 41 +21+  44  + 19+ 49 + 30 + 68 +  57 + 33+  49 +   46  +9+ 56 + 43 + 56 + 57 + 58 + 33+ 27 +21+ 33+ 41 +21+   71   + 19+13+  52 + 55 +29+ 60 +  38 =1797
# Thus saith the LORD of hosts, the God of Israel; Go and tell the men of Judah and the inhabitants of Jerusalem, Will ye not receive instruction to hearken to my words? saith the LORD.
#  68 +  57 + 33+ 49 +21+  81  + 33+ 26+21+   64  +22+ 19+ 49 + 33+ 32+21+  44 + 19+ 33+    117    +21+   104    + 56 +30+ 49+   67  +    162    +35+   62  +35+38+  79  +  57 + 33+  49 =1719
# Now it came to pass, when they had heard all the words, they were afraid both one and other, and said unto Baruch, We will surely tell the king of all these words.
#  52+29+ 22 +35+  55 + 50 + 58 + 13+  36 + 25+ 33+  79  + 58 + 51 +  39  + 45 + 34+ 19+  66  + 19+ 33 + 70 +   53  +28+ 56 + 100  + 49 + 33+ 41 +21+ 25+  57 +  79  =1463
# And they asked Baruch, saying, Tell us now, How didst thou write all these words at his mouth?
#  19+ 58 +  40 +   53  +   75  + 49 +40+ 52 + 46+  56 + 64 +  75 + 25+  57 +  79 +21+ 36+  77  =922
# Moab is confounded; for it is broken down: howl and cry; tell ye it in Arnon, that Moab is spoiled,
#  31 +28+    101    + 39+29+28+  65  +  56 + 58 + 19+ 46 + 49 +30+29+23+  62  + 49 + 31 +28+   80   =881
# And go, get thee to them of the captivity, unto the children of thy people, and speak unto them, and tell them, Thus saith the Lord GOD; whether they will hear, or whether they will forbear.
#  19+ 22+ 32+ 38 +35+ 46 +21+ 33+   125    + 70 + 33+   73   +21+ 53+   69  + 19+  52 + 70 +  46 + 19+ 49 +  46 + 68 +  57 + 33+ 49 + 26 +   87  + 58 + 56 +  32 +33+   87  + 58 + 56 +   65   =1756
# Tell them therefore, Thus saith the Lord GOD; I will make this proverb to cease, and they shall no more use it as a proverb in Israel; but say unto them, The days are at hand, and the effect of every vision.
#  49 + 46 +   100    + 68 +  57 + 33+ 49 + 26 +9+ 56 + 30 + 56 +   96  +35+  33  + 19+ 58 +  52 +29+ 51 + 45+29+20+1+   96  +23+   64  + 43+ 45+ 70 +  46 + 33+ 49 + 24+21+  27 + 19+ 33+  45  +21+  75 +   88  =1869
# Say now to the rebellious house, Know ye not what these things mean? tell them, Behold, the king of Babylon is come to Jerusalem, and hath taken the king thereof, and the princes thereof, and led them with him to Babylon;
#  45+ 52+35+ 33+   118    +  68  + 63 +30+ 49+ 52 +  57 +  77  +  33 + 49 +  46 +   46  + 33+ 41 +21+   71  +28+ 36 +35+   104    + 19+ 37 +  51 + 33+ 41 +   77   + 19+ 33+   84  +   77   + 19+ 21+ 46 + 60 + 30+35+   71   =1975
# And the people said unto me, Wilt thou not tell us what these things are to us, that thou doest so?
#  19+ 33+  69  + 33 + 70 + 18+ 64 + 64 + 49+ 49 +40+ 52 +  57 +  77  + 24+35+ 40+ 49 + 64 +  63 + 34=1003
# Then spake the Chaldeans to the king in Syriack, O  king, live for ever: tell thy servants the dream, and we will shew the interpretation.
#  47 +  52 + 33+    67   +35+ 33+ 41 +23+   86   +15+  41 + 48 + 39+  50 + 49 + 53+  118   + 33+  41  + 19+28+ 56 + 55 + 33+      184      =1279
# They answered again and said, Let the king tell his servants the dream, and we will shew the interpretation of it.
#  58 +   89   +  32 + 19+  33 + 37+ 33+ 41 + 49 + 36+  118   + 33+  41  + 19+28+ 56 + 55 + 33+     184      +21+ 29=1044
# But if ye will not make known unto me the dream, there is but one decree for you: for ye have prepared lying and corrupt words to speak before me, till the time be changed: therefore tell me the dream, and I shall know that ye can shew me the interpretation thereof.
#  43+15+30+ 56 + 49+ 30 +  77 + 70 +18+ 33+  41  +  56 +28+ 43+ 34+  40  + 39+ 61 + 39+30+ 36 +   83   +  67 + 19+  111  +  79 +35+  52 +  51  + 18+ 53 + 33+ 47 +7 +   42   +   100   + 49 +18+ 33+  41  + 19+9+  52 + 63 + 49 +30+ 18+ 55 +18+ 33+     184      +   77   =2413
# This is the dream; and we will tell the interpretation thereof before the king.
#  56 +28+ 33+  41  + 19+28+ 56 + 49 + 33+     184      +   77  +  51  + 33+  41 =729
# O  Belteshazzar, master of the magicians, because I know that the spirit of the holy gods is in thee, and no secret troubleth thee, tell me the visions of my dream that I have seen, and the interpretation thereof.
# 15+     143     +  76  +21+ 33+    76    +   56  +9+ 63 + 49 + 33+  91  +21+ 33+ 60 + 45 +28+23+  38 + 19+29+  70  +   121   +  38 + 49 +18+ 33+  107  +21+38+  41 + 49 +9+ 36 +  43 + 19+ 33+     184      +   77   =1947
# Tell ye your children of it, and let your children tell their children, and their children another generation.
#  49 +30+ 79 +   73   +21+ 29+ 19+ 37+ 79 +   73   + 49 +  60 +    73   + 19+  60 +   73   +   81  +    108    =1012
# Then said they unto him, Tell us, we pray thee, for whose cause this evil is upon us; What is thine occupation? and whence comest thou? what is thy country? and of what people art thou?
#  47 + 33 + 58 + 70 + 30 + 49 + 40+28+ 60 +  38 + 39+  70 +  49 + 56 + 48 +28+ 66 + 40+ 52 +28+  56 +    117    + 19+  58  +  75  +  64 + 52 +28+ 53+  116   + 19+21+ 52 +  69  + 39+  64 =1831
# Who can tell if God will turn and repent, and turn away from his fierce anger, that we perish not?
#  46+ 18+ 49 +15+ 26+ 56 + 73 + 19+   78  + 19+ 73 + 50 + 52 + 36+  46  +  45  + 49 +28+  75  + 49 =902
# And Jesus saith unto him, See thou tell no man; but go thy way, shew thyself to the priest, and offer the gift that Moses commanded, for a testimony unto them.
#  19+  74 +  57 + 70 + 30 + 29+ 64 + 49 +29+ 28 + 43+22+ 53+ 49 + 55 +   95  +35+ 33+   87  + 19+  50 + 33+ 42 + 49 +  71 +    72    + 39+1+   140   + 70 +  46 =1553
# What I tell you in darkness, that speak ye in light: and what ye hear in the ear, that preach ye upon the housetops.
#  52 +9+ 49 + 61+23+    91   + 49 +  52 +30+23+  56  + 19+ 52 +30+ 32 +23+ 33+ 24 + 49 +  51  +30+ 66 + 33+   138    =1075
# Then charged he his disciples that they should tell no man that he was Jesus the Christ.
#  47 +   46  +13+ 36+    96   + 49 + 58 +  79  + 49 +29+ 28+ 49 +13+ 43+  74 + 33+   77  =819
# And as they came down from the mountain, Jesus charged them, saying, Tell the vision to no man, until the Son of man be risen again from the dead.
#  19+20+ 58 + 22 + 56 + 52 + 33+   107   +  74 +   46  +  46 +   75  + 49 + 33+  88  +35+29+ 28 +  76 + 33+ 48+21+ 28+7 +  65 +  32 + 52 + 33+  14 =1279
# Moreover if thy brother shall trespass against thee, go and tell him his fault between thee and him alone: if he shall hear thee, thou hast gained thy brother.
#   111   +15+ 53+   86  +  52 +  117   +   71  +  38 +22+ 19+ 49 + 30+ 36+  60 +   74  + 38 + 19+ 30+  47  +15+13+  52 + 32 +  38 + 64 + 48 +  40  + 53+   86   =1408
# And if he shall neglect to hear them, tell it unto the church: but if he neglect to hear the church, let him be unto thee as an heathen man and a publican.
#  19+15+13+  52 +   66  +35+ 32 +  46 + 49 +29+ 70 + 33+   61  + 43+15+13+   66  +35+ 32 + 33+   61  + 37+ 30+7 + 70 + 38 +20+15+   61  + 28+ 19+1+    78   =1222
# Tell ye the daughter of Sion, Behold, thy King cometh unto thee, meek, and sitting upon an ass, and a colt the foal of an ass.
#  49 +30+ 33+   84   +21+  57 +   46  + 53+ 41 +  64  + 70 +  38 +  34 + 19+   98  + 66 +15+ 39 + 19+1+ 50 + 33+ 34 +21+15+ 39 =1069
# And Jesus answered and said unto them, I also will ask you one thing, which if ye tell me, I in like wise will tell you by what authority I do these things.
#  19+  74 +   89   + 19+ 33 + 70 +  46 +9+ 47 + 56 + 31+ 61+ 34+  58  +  51 +15+30+ 49 + 18+9+23+ 37 + 56 + 56 + 49 + 61+27+ 52 +   137   +9+19+  57 +   77  =1478
# And they answered Jesus, and said, We cannot tell. And he said unto them, Neither tell I you by what authority I do these things.
#  19+ 58 +   89   +  74  + 19+  33 +28+  67  +  49 + 19+13+ 33 + 70 +  46 +   79  + 49 +9+ 61+27+ 52 +   137   +9+19+  57 +   77  =1193
# Again, he sent forth other servants, saying, Tell them which are bidden, Behold, I have prepared my dinner: my oxen and my fatlings are killed, and all things are ready: come unto the marriage.
#   32  +13+ 58 +  67 +  66 +   118   +   75  + 49 + 46 +  51 + 24+   38  +   46  +9+ 36 +   83   +38+   64  +38+ 58 + 19+38+   88   + 24+   53  + 19+ 25+  77  + 24+  53  + 36 + 70 + 33+    72   =1640
# Tell us therefore, What thinkest thou? Is it lawful to give tribute unto Caesar, or not?
#  49 +40+   100    + 52 +  106   +  64 +28+29+  75  +35+ 43 +   95  + 70 +   47  +33+ 49 =915
# And as he sat upon the mount of Olives, the disciples came unto him privately, saying, Tell us, when shall these things be? and what shall be the sign of thy coming, and of the end of the world?
#  19+20+13+ 40+ 66 + 33+  83 +21+   82  + 33+    96   + 22 + 70 + 30+   128    +   75  + 49 + 40+ 50 +  52 +  57 +  77  + 7 + 19+ 52 +  52 +7 + 33+ 49 +21+ 53+   61  + 19+21+ 33+ 23+21+ 33+  72  =1732
# But Jesus held his peace, And the high priest answered and said unto him, I adjure thee by the living God, that thou tell us whether thou be the Christ, the Son of God.
#  43+  74 + 29 + 36+  30  + 19+ 33+ 32 +  87  +   89   + 19+ 33 + 70 + 30 +9+  59  + 38 +27+ 33+  73  + 26 + 49 + 64 + 49 +40+   87  + 64 +7 + 33+   77  + 33+ 48+21+ 26 =1487
# And go quickly, and tell his disciples that he is risen from the dead; and, behold, he goeth before you into Galilee; there shall ye see him: lo, I have told you.
#  19+22+   98   + 19+ 49 + 36+    96   + 49 +13+28+  65 + 52 + 33+  14 + 19 +   46  +13+  55 +  51  + 61+ 58 +   51   +  56 +  52 +30+ 29+ 30 + 27+9+ 36 + 51 + 61 =1328
# And as they went to tell his disciples, behold, Jesus met them, saying, All hail. And they came and held him by the feet, and worshipped him.
#  19+20+ 58 + 62 +35+ 49 + 36+    96    +   46  +  74 + 38+  46 +   75  + 25+  30 + 19+ 58 + 22 + 19+ 29 + 30+27+ 33+  36 + 19+   133    + 30 =1164
# Then said Jesus unto them, Be not afraid: go tell my brethren that they go into Galilee, and there shall they see me.
#  47 + 33 +  74 + 70 +  46 +7 + 49+   39  +22+ 49 +38+   90   + 49 + 58 +22+ 58 +   51   + 19+  56 +  52 + 58 + 29+ 18=1034
# But Simon's wife's mother lay sick of a fever, and anon they tell him of her.
#  43+   89  +  62  +  79  + 38+ 42 +21+1+  56  + 19+ 44 + 58 + 49 + 30+21+ 31 =683
# Howbeit Jesus suffered him not, but saith unto him, Go home to thy friends, and tell them how great things the Lord hath done for thee, and hath had compassion on thee.
#    82  +  74 +   84   + 30+ 49 + 43+  57 + 70 + 30 +22+ 41 +35+ 53+   75   + 19+ 49 + 46 + 46+  51 +  77  + 33+ 49 + 37 + 38 + 39+  38 + 19+ 37 + 13+   124    +29+  38 =1527
# And he charged them that they should tell no man: but the more he charged them, so much the more a great deal they published it;
#  19+13+   46  + 46 + 49 + 58 +  79  + 49 +29+ 28 + 43+ 33+ 51 +13+   46  +  46 +34+ 45 + 33+ 51 +1+  51 + 22 + 58 +    96   + 29=1068
# And he sent him away to his house, saying, Neither go into the town, nor tell it to any in the town.
#  19+13+ 58 + 30+ 50 +35+ 36+  68  +   75  +   79  +22+ 58 + 33+  72 + 47+ 49 +29+35+ 40+23+ 33+  72 =976
# And he charged them that they should tell no man of him.
#  19+13+   46  + 46 + 49 + 58 +  79  + 49 +29+ 28+21+ 30 =467
# And as they came down from the mountain, he charged them that they should tell no man what things they had seen, till the Son of man were risen from the dead.
#  19+20+ 58 + 22 + 56 + 52 + 33+   107   +13+   46  + 46 + 49 + 58 +  79  + 49 +29+ 28+ 52 +  77  + 58 + 13+  43 + 53 + 33+ 48+21+ 28+ 51 +  65 + 52 + 33+  14 =1405
# And they were in the way going up to Jerusalem; and Jesus went before them: and they were amazed; and as they followed, they were afraid. And he took again the twelve, and began to tell them what things should happen unto him,
#  19+ 58 + 51 +23+ 33+ 49+  52 +37+35+   104    + 19+  74 + 62 +  51  +  46 + 19+ 58 + 51 +   50  + 19+20+ 58 +    92   + 58 + 51 +   39  + 19+13+ 61 +  32 + 33+   87  + 19+  29 +35+ 49 + 46 + 52 +  77  +  79  +  60  + 70 + 30 =2019
# And Jesus answered and said unto them, I will also ask of you one question, and answer me, and I will tell you by what authority I do these things.
#  19+  74 +   89   + 19+ 33 + 70 +  46 +9+ 56 + 47 + 31+21+ 61+ 34+   120   + 19+  80  + 18+ 19+9+ 56 + 49 + 61+27+ 52 +   137   +9+19+  57 +   77  =1418
# And they answered and said unto Jesus, We cannot tell. And Jesus answering saith unto them, Neither do I tell you by what authority I do these things.
#  19+ 58 +   89   + 19+ 33 + 70 +  74  +28+  67  +  49 + 19+  74 +   110   +  57 + 70 +  46 +   79  +19+9+ 49 + 61+27+ 52 +   137   +9+19+  57 +   77  =1477
# Tell us, when shall these things be? and what shall be the sign when all these things shall be fulfilled?
#  49 + 40+ 50 +  52 +  57 +  77  + 7 + 19+ 52 +  52 +7 + 33+ 49 + 50 + 25+  57 +  77  +  52 +7 +    87    =899
# But go your way, tell his disciples and Peter that he goeth before you into Galilee: there shall ye see him, as he said unto you.
#  43+22+ 79 + 49 + 49 + 36+    96   + 19+  64 + 49 +13+  55 +  51  + 61+ 58 +   51   +  56 +  52 +30+ 29+ 30 +20+13+ 33 + 70 + 61 =1189
# But I tell you of a truth, many widows were in Israel in the days of Elias, when the heaven was shut up three years and six months, when great famine was throughout all the land;
#  43+9+ 49 + 61+21+1+  87  + 53 +  93  + 51 +23+  64  +23+ 33+ 49 +21+  46  + 50 + 33+  55  + 43+ 68 +37+  56 +  68 + 19+ 52+   89  + 50 +  51 +  48  + 43+   153    + 25+ 33+  31 =1731
# And he charged him to tell no man: but go, and shew thyself to the priest, and offer for thy cleansing, according as Moses commanded, for a testimony unto them.
#  19+13+   46  + 30+35+ 49 +29+ 28 + 43+ 22+ 19+ 55 +   95  +35+ 33+   87  + 19+  50 + 39+ 53+    84    +    74   +20+  71 +    72    + 39+1+   140   + 70 +  46 =1416
# Then Jesus answering said unto them, Go your way, and tell John what things ye have seen and heard; how that the blind see, the lame walk, the lepers are cleansed, the deaf hear, the dead are raised, to the poor the gospel is preached.
#  47 +  74 +   110   + 33 + 70 +  46 +22+ 79 + 49 + 19+ 49 + 47 + 52 +  77  +30+ 36 + 43 + 19+  36  + 46+ 49 + 33+  41 + 29 + 33+ 31 +  47 + 33+  75  + 24+    63   + 33+ 16 +  32 + 33+ 14 + 24+   56  +35+ 33+ 64 + 33+  74  +28+    60   =1977
# And when they had nothing to pay, he frankly forgave them both. Tell me therefore, which of them will love him most?
#  19+ 50 + 58 + 13+   87  +35+ 42 +13+   87  +   74  + 46 +  45 + 49 +18+   100    +  51 +21+ 46 + 56 + 54 + 30+  67 =1061
# And her parents were astonished: but he charged them that they should tell no man what was done.
#  19+ 31+   93  + 51 +    114    + 43+13+   46  + 46 + 49 + 58 +  79  + 49 +29+ 28+ 52 + 43+  38 =881
# And he straitly charged them, and commanded them to tell no man that thing;
#  19+13+  124   +   46  +  46 + 19+    72   + 46 +35+ 49 +29+ 28+ 49 +  58  =633
# But I tell you of a truth, there be some standing here, which shall not taste of death, till they see the kingdom of God.
#  43+9+ 49 + 61+21+1+  87  +  56 +7 + 52 +   88   +  36 +  51 +  52 + 49+  65 +21+  38  + 53 + 58 + 29+ 33+   73  +21+ 26 =1079
# For I tell you, that many prophets and kings have desired to see those things which ye see, and have not seen them; and to hear those things which ye hear, and have not heard them.
#  39+9+ 49 + 61 + 49 + 53 +  117   + 19+  60 + 36 +   64  +35+ 29+  67 +  77  +  51 +30+ 29 + 19+ 36 + 49+ 43 +  46 + 19+35+ 32 +  67 +  77  +  51 +30+  32 + 19+ 36 + 49+  36 +  46 =1596
# Suppose ye that I am come to give peace on earth? I tell you, Nay; but rather division:
#   111  +30+ 49 +9+14+ 36 +35+ 43 +  30 +29+  52  +9+ 49 + 61 + 40 + 43+  70  +   101   =811
# I tell thee, thou shalt not depart thence, till thou hast paid the very last mite.
# 9+ 49 +  38 + 64 +  60 + 49+  64  +   55  + 53 + 64 + 48 + 30 + 33+ 70 + 52 +  47 =785
# I tell you, Nay: but, except ye repent, ye shall all likewise perish.
# 9+ 49 + 61 + 40 + 43 +  73  +30+   78  +30+  52 + 25+   93   +   75  =658
# I tell you, Nay: but, except ye repent, ye shall all likewise perish.
# 9+ 49 + 61 + 40 + 43 +  73  +30+   78  +30+  52 + 25+   93   +   75  =658
# But he shall say, I tell you, I know you not whence ye are; depart from me, all ye workers of iniquity.
#  43+13+  52 + 45 +9+ 49 + 61 +9+ 63 + 61+ 49+  58  +30+ 24 +  64  + 52 + 18+ 25+30+  109  +21+   124   =1009
# And he said unto them, Go ye, and tell that fox, Behold, I cast out devils, and I do cures to day and to morrow, and the third day I shall be perfected.
#  19+13+ 33 + 70 +  46 +22+ 30+ 19+ 49 + 49 + 45 +   46  +9+ 43 + 56+   71  + 19+9+19+  66 +35+ 30+ 19+35+  102  + 19+ 33+  59 + 30+9+  52 +7 +    82    =1245
# I tell you, in that night there shall be two men in one bed; the one shall be taken, and the other shall be left.
# 9+ 49 + 61 +23+ 49 +  58 +  56 +  52 +7 + 58+ 32+23+ 34+ 11 + 33+ 34+  52 +7 +  51  + 19+ 33+  66 +  52 +7 +  43 =919
# I tell you that he will avenge them speedily. Nevertheless when the Son of man cometh, shall he find faith on the earth?
# 9+ 49 + 61+ 49 +13+ 56 +  54  + 46 +    95   +    152     + 50 + 33+ 48+21+ 28+   64  +  52 +13+ 33 +  44 +29+ 33+  52  =1084
# I tell you, this man went down to his house justified rather than the other: for every one that exalteth himself shall be abased; and he that humbleth himself shall be exalted.
# 9+ 49 + 61 + 56 + 28+ 62 + 56 +35+ 36+  68 +   103   +  70  + 43 + 33+  66  + 39+  75 + 34+ 49 +   95   +   72  +  52 +7 +   32  + 19+13+ 49 +   89   +   72  +  52 +7 +   71   =1602
# And he answered and said unto them, I tell you that, if these should hold their peace, the stones would immediately cry out.
#  19+13+   89   + 19+ 33 + 70 +  46 +9+ 49 + 61+  49 +15+  57 +  79  + 39 +  60 +  30  + 33+  92  +  75 +    116    + 46+ 56 =1155
# And spake unto him, saying, Tell us, by what authority doest thou these things? or who is he that gave thee this authority?
#  19+  52 + 70 + 30 +   75  + 49 + 40+27+ 52 +   137   +  63 + 64 +  57 +   77  +33+ 46+28+13+ 49 + 35 + 38 + 56 +   137    =1247
# And they answered, that they could not tell whence it was.
#  19+ 58 +    89   + 49 + 58 +  55 + 49+ 49 +  58  +29+ 43 =556
# And Jesus said unto them, Neither tell I you by what authority I do these things.
#  19+  74 + 33 + 70 +  46 +   79  + 49 +9+ 61+27+ 52 +   137   +9+19+  57 +   77  =818
# And he said, I tell thee, Peter, the cock shall not crow this day, before that thou shalt thrice deny that thou knowest me.
#  19+13+  33 +9+ 49 +  38 +  64  + 33+ 32 +  52 + 49+ 59 + 56 + 30 +  51  + 49 + 64 +  60 +  63  + 48 + 49 + 64 +  107  + 18=1109
# Art thou the Christ? tell us. And he said unto them, If I tell you, ye will not believe:
#  39+ 64 + 33+   77  + 49 + 40+ 19+13+ 33 + 70 +  46 +15+9+ 49 + 61 +30+ 56 + 49+   60   =812
# The wind bloweth where it listeth, and thou hearest the sound thereof, but canst not tell whence it cometh, and whither it goeth: so is every one that is born of the Spirit.
#  33+ 50 +   85  +  59 +29+   93   + 19+ 64 +   76  + 33+  73 +   77   + 43+  57 + 49+ 49 +  58  +29+   64  + 19+   91  +29+  55  +34+28+  75 + 34+ 49 +28+ 49 +21+ 33+   91  =1676
# If I have told you earthly things, and ye believe not, how shall ye believe, if I tell you of heavenly things?
# 15+9+ 36 + 51 + 61+   89  +   77  + 19+30+   60  + 49 + 46+  52 +30+   60   +15+9+ 49 + 61+21+   92   +   77  =1008
# The woman saith unto him, I know that Messias cometh, which is called Christ: when he is come, he will tell us all things.
#  33+  66 +  57 + 70 + 30 +9+ 63 + 49 +   85  +   64  +  51 +28+  37  +   77  + 50 +13+28+  36 +13+ 56 + 49 +40+ 25+   77  =1106
# Jesus answered and said unto them, Though I bear record of myself, yet my record is true: for I know whence I came, and whither I go; but ye cannot tell whence I come, and whither I go.
#   74 +   89   + 19+ 33 + 70 +  46 +  79  +9+ 26 +  63  +21+   80  + 50+38+  63  +28+  64 + 39+9+ 63 +  58  +9+  22 + 19+   91  +9+ 22+ 43+30+  67  + 49 +  58  +9+  36 + 19+   91  +9+ 22=1626
# And because I tell you the truth, ye believe me not.
#  19+   56  +9+ 49 + 61+ 33+  87  +30+   60  +18+ 49 =471
# Then came the Jews round about him, and said unto him, How long dost thou make us to doubt? If thou be the Christ, tell us plainly.
#  47 + 22 + 33+ 57 +  72 +  59 + 30 + 19+ 33 + 70 + 30 + 46+ 48 + 58 + 64 + 30 +40+35+  62  +15+ 64 +7 + 33+   77  + 49 +40+   89   =1229
# Philip cometh and telleth Andrew: and again Andrew and Philip tell Jesus.
#   70  +  64  + 19+   82  +   65  + 19+  32 +  65  + 19+  70  + 49 +  74  =628
# Now I tell you before it come, that, when it is come to pass, ye may believe that I am he.
#  52+9+ 49 + 61+  51  +29+  36 +  49 + 50 +29+28+ 36 +35+  55 +30+ 39+   60  + 49 +9+14+ 13=783
# Nevertheless I tell you the truth; It is expedient for you that I go away: for if I go not away, the Comforter will not come unto you; but if I depart, I will send him unto you.
#     152     +9+ 49 + 61+ 33+  87  +29+28+   102   + 39+ 61+ 49 +9+22+  50 + 39+15+9+22+ 49+  50 + 33+   113   + 56 + 49+ 36 + 70 + 61 + 43+15+9+   64  +9+ 56 + 42 + 30+ 70 + 61 =1781
# They said therefore, What is this that he saith, A little while? we cannot tell what he saith.
#  58 + 33 +   100    + 52 +28+ 56 + 49 +13+  57  +1+  78  +  57  +28+  67  + 49 + 52 +13+  57  =848
# Jesus answered him, Sayest thou this thing of thyself, or did others tell it thee of me?
#   74 +   89   + 30 +  89  + 64 + 56 +  58 +21+   95   +33+ 17+  85  + 49 +29+ 38 +21+ 18=866
# Jesus saith unto her, Woman, why weepest thou? whom seekest thou? She, supposing him to be the gardener, saith unto him, Sir, if thou have borne him hence, tell me where thou hast laid him, and I will take him away.
#   74 +  57 + 70 + 31 +  66  + 56+   93  +  64 + 59 +   84  +  64 + 32 +   136   + 30+35+7 + 33+    72   +  57 + 70 + 30 + 46 +15+ 64 + 36 +  54 + 30+  35  + 49 +18+  59 + 64 + 48 + 26 + 30 + 19+9+ 56 + 37 + 30+  50 =1995
# And Peter answered unto her, Tell me whether ye sold the land for so much? And she said, Yea, for so much.
#  19+  64 +   89   + 70 + 31 + 49 +18+   87  +30+ 50 + 33+ 31 + 39+34+  45 + 19+ 32+  33 + 31 + 39+34+  45 =922
# He lodgeth with one Simon a tanner, whose house is by the sea side: he shall tell thee what thou oughtest to do.
# 13+   71  + 60 + 34+  70 +1+   72  +  70 +  68 +28+27+ 33+ 25+  37 +13+  52 + 49 + 38 + 52 + 64 +  115   +35+ 19=1046
# Who shall tell thee words, whereby thou and all thy house shall be saved.
#  46+  52 + 49 + 38 +  79  +   86  + 64 + 19+ 25+ 53+  68 +  52 +7 +  51  =689
# We have sent therefore Judas and Silas, who shall also tell you the same things by mouth.
# 28+ 36 + 58 +   100   +  55 + 19+  60  + 46+  52 + 47 + 49 + 61+ 33+ 38 +  77  +27+  77  =863
# (For all the Athenians and strangers which were there spent their time in nothing else, but either to tell, or to hear some new thing.)
#  39 + 25+ 33+    91   + 19+   121   +  51 + 51 +  56 +  74 +  60 + 47 +23+   87  +  41 + 43+  65  +35+  49 +33+35+ 32 + 52 + 42+   58  =1262
# Then the chief captain came, and said unto him, Tell me, art thou a Roman? He said, Yea.
#  47 + 33+  31 +   64  +  22 + 19+ 33 + 70 + 30 + 49 + 18+ 39+ 64 +1+  61  +13+  33 + 31 =658
# Then Paul called one of the centurions unto him, and said, Bring this young man unto the chief captain: for he hath a certain thing to tell him.
#  47 + 50 +  37  + 34+21+ 33+   138    + 70 + 30 + 19+  33 +  50 + 56 +  82 + 28+ 70 + 33+  31 +   64   + 39+13+ 37 +1+   70  +  58 +35+ 49 + 30 =1258
# Then the chief captain took him by the hand, and went with him aside privately, and asked him, What is that thou hast to tell me?
#  47 + 33+  31 +   64  + 61 + 30+27+ 33+  27 + 19+ 62 + 60 + 30+  38 +   128    + 19+  40 + 30 + 52 +28+ 49 + 64 + 48 +35+ 49 + 18=1122
# So the chief captain then let the young man depart, and charged him, See thou tell no man that thou hast shewed these things to me.
# 34+ 33+  31 +   64  + 47 + 37+ 33+  82 + 28+   64  + 19+   46  + 30 + 29+ 64 + 49 +29+ 28+ 49 + 64 + 48 +  64  +  57 +  77  +35+ 18=1159
# I knew a man in Christ above fourteen years ago, (whether in the body, I cannot tell; or whether out of the body, I cannot tell: God knoweth;) such an one caught up to the third heaven.
# 9+ 53 +1+ 28+23+  77  +  45 +  104   +  68 + 23 +   87   +23+ 33+  46 +9+  67  +  49 +33+   87  + 56+21+ 33+  46 +9+  67  +  49 + 26+    96   + 51 +15+ 34+  60  +37+35+ 33+  59 +   55  =1647
# And I knew such a man, (whether in the body, or out of the body, I cannot tell: God knoweth;)
#  19+9+ 53 + 51 +1+ 28 +   87   +23+ 33+  46 +33+ 56+21+ 33+  46 +9+  67  +  49 + 26+    96   =786
# Am I therefore become your enemy, because I tell you the truth?
# 14+9+   100   +  43  + 79 +  62  +   56  +9+ 49 + 61+ 33+  87  =602
# Tell me, ye that desire to be under the law, do ye not hear the law?
#  49 + 18+30+ 49 +  60  +35+7 +  62 + 33+ 36 +19+30+ 49+ 32 + 33+ 36 =578
# Envyings, murders, drunkenness, revellings, and such like: of the which I tell you before, as I have also told you in time past, that they which do such things shall not inherit the kingdom of God.
#    115   +   98   +    144     +    123    + 19+ 51 +  37 +21+ 33+  51 +9+ 49 + 61+   51  +20+9+ 36 + 47 + 51 + 61+23+ 47 +  56 + 49 + 58 +  51 +19+ 51 +  77  +  52 + 49+   83  + 33+   73  +21+ 26 =1854
# (For many walk, of whom I have told you often, and now tell you even weeping, that they are the enemies of the cross of Christ:
#  39 + 53 +  47 +21+ 59 +9+ 36 + 51 + 61+  60  + 19+ 52+ 49 + 61+ 46 +   79   + 49 + 58 + 24+ 33+   70  +21+ 33+  74 +21+   77  =1202
# And what shall I more say? for the time would fail me to tell of Gedeon, and of Barak, and of Samson, and of Jephthae; of David also, and Samuel, and of the prophets:
#  19+ 52 +  52 +9+ 51 + 45 + 39+ 33+ 47 +  75 + 28 +18+35+ 49 +21+   50  + 19+21+  33  + 19+21+   81  + 19+21+    73   +21+  40 +  47 + 19+   71  + 19+21+ 33+   117   =1318
# And the angel said unto me, Wherefore didst thou marvel? I will tell thee the mystery of the woman, and of the beast that carrieth her, which hath the seven heads and ten horns.
#  19+ 33+  39 + 33 + 70 + 18+   103   +  56 + 64 +   71  +9+ 56 + 49 + 38 + 33+  125  +21+ 33+  66  + 19+21+ 33+  47 + 49 +   82   + 31 +  51 + 37 + 33+  65 +  37 + 19+ 39+  74  =1573
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
