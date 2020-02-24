from bible import *
c=299792458
mc=c/1000 # speed of light in km/s
chron=[
248956422,
242193529,
198295559,
190214555,
181538259,
170805979,
159345973,
145138636,
138394717,
133797422,
135086622,
133275309,
114364328,
107043718,
101991189,
90338345,
83257441,
80373285,
58617616,
64444167,
46709983,
50818468,
16569,
156040895,
57227415]
A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y = chron
AV=sum(chron[:22])
# W=chron[23-1]
# X=chron[24-1]
# Y=chron[25-1]
AW=AV+W
AX=AV+W+X
AY=AX+Y

def bp(i):
    if type(i) is int:
        return chron[i-1]
    if type(i) is str:
        return sum([bp(osum(c)) for c in i])

# >>> from dna import *
# >>> from bible import *
# >>> 
# >>> tell('Lord Jesus Christ')
# Lord Jesus Christ
#  49 +  74 +  77  =200
# >>> tell('Jesus')
# J  e s  u  s
# 10+5+19+21+19=74
# >>> factors(c)
# [2, 7, 73, 293339]
# >>> [bp/293339 for bp in chron]
# [848.698679684597, 825.6438080173451, 675.9945285147901, 648.446183426002, 618.8684729954081, 582.2818616004009, 543.2144140397288, 494.78124627137885, 471.79105744548116, 456.1187636147938, 460.5136787130249, 454.33886731733594, 389.8708593129451, 364.91471642025095, 347.6905184786203, 307.9656813447922, 283.82670221143457, 273.99454215089025, 199.828921486744, 219.69177981788988, 159.23550226870617, 173.2414305632732, 0.056484136101916216, 531.9473203358572, 195.08969144914246]
# >>> bpomc=[bp/mc for bp in chron]
# >>> bpomc
# [830.4292364819931, 807.870653637324, 661.4427871964677, 634.4874593209413, 605.5464510718278, 569.7474183956956, 531.5209530721417, 484.13037795633943, 461.6350855630931, 446.30016009275323, 450.60046840804785, 444.55857858839136, 381.47833592264686, 357.05940941316146, 340.2059867696872, 301.33628311623505, 277.7169297567853, 268.0964208912821, 195.52732043712723, 214.9626025615361, 155.80773216116066, 169.51216297776244, 0.055268234933381816, 520.4963995458485, 190.89010905004156]
# >>> sum(bpomc)
# 10301.414590623226
# >>> math.pi
# 3.141592653589793
# >>> math.sqrt(2)
# 1.4142135623730951
# >>> pp(21)
# 10301
# >>> pp(35)
# 15551
# >>> _*2
# 31102
# >>> pp(46)
# 19991
# >>> pp(45)
# 19891
# >>> sum(bpomc+bpomc[:22])
# 19891.387404415625
# >>> 
# >>> 
# >>> (AV+W+X+Y)/mc
# 10301.414590623224
# >>> npp(10301)
# 21
# >>> prime(21)
# 73
# >>> 
# >>> Isaiah[41:4]
# Isaiah 41:4 Who hath wrought and done it, calling the generations from the beginning? I the LORD, the first, and with the last; I am he.
# >>> _.tell(lsum, osum, ssum)
# Who hath wrought and done it, calling the generations from the beginning? I the LORD, the first, and with the last; I am he.
#  3 + 4  +   7   + 3 + 4  + 2 +   7   + 3 +     11    + 4  + 3 +    9     +1+ 3 +  4  + 3 +  5   + 3 + 4  + 3 +  4  +1+2 + 2 = 95
#  46+ 37 +  112  + 19+ 38 + 29+   58  + 33+    127    + 52 + 33+    81    +9+ 33+  49 + 33+  72  + 19+ 60 + 33+  52 +9+14+ 13=1061
# 568+217 +  1165 + 55+119 +209+  130  +213+    577    +196 +213+   189    +9+213+ 184 +213+ 405  + 55+717 +213+ 331 +9+41+ 13=6254
# >>> is414="מִי -פָעַל וְעָשָׂה, קֹרֵא הַדֹּרוֹת מֵרֹאשׁ:  אֲנִי יְהוָה רִאשׁוֹן, וְאֶת -אַחֲרֹנִים אֲנִי -הוּא"
# >>> tell(lsum,osum,ssum,is414)
# מִי -פָעַל וְעָשָׂה, קֹרֵא הַדֹּרוֹת מֵרֹאשׁ: אֲנִי יְהוָה רִאשׁוֹן, וְאֶת -אַחֲרֹנִים אֲנִי -הוּא
# 2 + 3  +  4  + 3 +  5  +  4  + 3 + 4  +  5   + 3 +   6   + 3 + 3  = 48
# 23+ 45 +  48 + 40+  57 +  55 + 25+ 26 +  62  + 29+   66  + 25+ 12 =513
# 50+180 + 381 +301+ 615 + 541 + 61+ 26 + 557  +407+  309  + 61+ 12 =3501
# >>> tell('אֲנִי הוּא',lsum,osum,ssum)
# אֲנִי הוּא
#  3 + 3 =6
#  25+ 12=37
#  61+ 12=73
# >>> 
# >>> 
# >>> tell('In the beginning')
# In the beginning
# 23+ 33+    81   =137
# >>> tell('Who')
# W  h o
# 23+8+15=46
# >>> tell('it')
# i t
# 9+20=29
# >>> tell('rib')
# r  i b
# 18+9+2=29
# >>> tell('the first')
# the first
#  33+  72 =105
# >>> (AV*2+X+Y)/mc
# 19891.332136180692
# >>> npp(19891)
# 45
# >>> (AV+W+X+Y)/293339
# 10528.045711616935
# >>> _/25.4
# 414.48998864633603
# >>> 41449*254*293339
# 3088286485594
# >>> sum(chron)
# 3088286401
# >>> _/c
# 10.301414590623224
# >>> _*1000
# 10301.414590623224
# >>> 
# >>> fs(41459)
# [11, 3769]
# >>> (AV+AV+X+X)/c*1000
# 20220.938426676497
# >>> (AV+AV+X+X+W)/c*1000
# 20220.99369491143
# >>> 
# >>> (AV*2+X+Y)/c
# 19.89133213618069
# >>> _*1000
# 19891.33213618069
# >>> 
# >>> sbp=sorted(chron)
# >>> sbp
# [16569, 46709983, 50818468, 57227415, 58617616, 64444167, 80373285, 83257441, 90338345, 101991189, 107043718, 114364328, 133275309, 133797422, 135086622, 138394717, 145138636, 156040895, 159345973, 170805979, 181538259, 190214555, 198295559, 242193529, 248956422]
# >>> sbp[23]/999
# 242435.96496496495
# >>> [x/y for x,y in zip(sbp[:-1],sbp[1:])]
# [0.00035472074567014937, 0.9191537021541066, 0.8880091473640737, 0.9762835629480394, 0.9095876124832213, 0.8018107882488565, 0.9653585797814757, 0.9216179574686696, 0.8857465618917336, 0.9527993880033203, 0.9359886939570877, 0.8581058926676358, 0.9960977349772853, 0.9904564939080348, 0.9760966670425721, 0.9535346398046624, 0.9301320400655225, 0.9792584780288109, 0.9329062948083334, 0.9408814425173043, 0.9543867923251194, 0.9592476803779554, 0.8187483778726392, 0.9728350329520722]
# >>> pp(43)
# 18481
# >>> pp(44)
# 19391
# >>> pp(45)
# 19891
# >>> 939/989
# 0.9494438827098078
# >>> sbp[0]/sbp[1]
# 0.00035472074567014937
# >>> 6/131
# 0.04580152671755725
# >>> _**3
# 9.6081519831715e-05
# >>> 
# >>> ppab=[pp(i) for i in range(21,47)]
# >>> ppab
# [10301, 10501, 10601, 11311, 11411, 12421, 12721, 12821, 13331, 13831, 13931, 14341, 14741, 15451, 15551, 16061, 16361, 16561, 16661, 17471, 17971, 18181, 18481, 19391, 19891, 19991]
# >>> pp(47)
# 30103
# >>> 
# >>> tell('adenine cytosine thymine and guanine')
# adenine cytosine thymine and guanine
#    52  +  110   +   94  + 19+   71  =346
# >>> tell('the Father the Word the Holy Ghost')
# the Father the Word the Holy Ghost
#  33+  58  + 33+ 60 + 33+ 60 +  69 =346
# >>> ssum('God')
# 71
# >>> 
# >>> tell('ACT of God')
# ACT of God
#  24+21+ 26=71
# >>> tell('one')
# o  n  e
# 15+14+5=34
# >>> 
# >>> tell('adenine cytosine thymine and guanine',ssum)
# adenine cytosine thymine and guanine
#   124  +  1127  +  1012 + 55+  422  =2740
# >>> sums('DNA')
# (19, 55)
# >>> 
# >>> pf(2740)
# Counter({2: 2, 5: 1, 137: 1})
# >>> np(137)
# 33
# >>> Genesis[1:1].tell(ssum)
# In the beginning God created the heaven and the earth.
# 59+213+   189   + 71+  308  +213+ 469  + 55+213+ 304  =2094
# >>> Genesis[1:1:2].tell(ssum)
# In the beginning God created the heaven and the earth.
# 59+213+   189   + 71+  308  +213+ 469  + 55+213+ 304  =2094
# And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.
#  55+213+ 304 +601+  1277 + 196 + 55+ 473 + 55+  370   +601+480 +213+ 15 +66+213+  84 + 55+213+ 478  +66+ 71+ 509 +480 +213+ 15 +66+213+  896  =8546
# >>> 
# >>> (Genesis[2:22]-3).tell()
# And the rib, which the LORD God had taken from man, made he a woman, and brought her unto the man.
#  19+ 33+ 29 +  51 + 33+ 49 + 26+ 13+  51 + 52 + 28 + 23 +13+1+  66  + 19+   91  + 31+ 70 + 33+ 28 =759
# And Adam said, This is now bone of my bones, and flesh of my flesh: she shall be called Woman, because she was taken out of Man.
#  19+ 19 +  33 + 56 +28+ 52+ 36 +21+38+  55  + 19+  50 +21+38+  50  + 32+  52 +7 +  37  +  66  +   56  + 32+ 43+  51 + 56+21+ 28 =1016
# Therefore shall a man leave his father and his mother, and shall cleave unto his wife: and they shall be one flesh.
#    100   +  52 +1+ 28+  45 + 36+  58  + 19+ 36+   79  + 19+  52 +  48  + 70 + 36+  43 + 19+ 58 +  52 +7 + 34+  50  =942
# And they were both naked, the man and his wife, and were not ashamed.
#  19+ 58 + 51 + 45 +  35  + 33+ 28+ 19+ 36+  43 + 19+ 51 + 49+   51   =537
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> Genesis[1:1]+Genesis[2:3]
# Genesis 1:1 In the beginning God created the heaven and the earth.
# Genesis 2:3 And God blessed the seventh day, and sanctified it: because that in it he had rested from all his work which God created and made.
# >>> _.lcs()
# [44, 103]
# >>> sum(_)
# 147
# >>> (Genesis[1:1]-Genesis[2:3])
# Genesis 1:1-2:3 (34 verses)
# >>> _.lcs()
# [44, 110, 41, 66, 91, 87, 116, 72, 98, 95, 136, 136, 41, 128, 79, 100, 61, 90, 42, 127, 158, 97, 41, 122, 134, 194, 81, 188, 152, 145, 95, 56, 101, 103]
# >>> tale(_)
# [44, 154, 195, 261, 352, 439, 555, 627, 725, 820, 956, 1092, 1133, 1261, 1340, 1440, 1501, 1591, 1633, 1760, 1918, 2015, 2056, 2178, 2312, 2506, 2587, 2775, 2927, 3072, 3167, 3223, 3324, 3427]
# >>> p(bisect_right(_,3427/2))
# 19
# >>> 3428/2
# 1714.0
# >>> (Genesis[1:1]-19).lc()
# 1633
# >>> 1714-1633
# 81
# >>> base(22,3427)
# [7, 1, 17]
# >>> base(22,3167)
# [6, 11, 21]
# >>> 789629/math.pi
# 251346.71711742046
# >>> 
# >>> Genesis[1:20]
# Genesis 1:20 And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl that may fly above the earth in the open firmament of heaven.
# >>> Genesis[1:20].letters()[:81]
# 'andgodsaidletthewatersbringforthabundantlythemovingcreaturethathathlifeandfowltha'
# >>> Genesis[1:20].lc()
# 127
# >>> np(127)
# 31
# >>> 
# >>> 17+9
# 26
# >>> 5**26
# 1490116119384765625
# >>> exp(89)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'exp' is not defined
# >>> 2**128.0
# 3.402823669209385e+38
# >>> sums('π')
# (17, 80)
# >>> sums('God')
# (26, 71)
# >>> 2**6,4**3
# (64, 64)
# >>> sums('ACTG')
# (31, 211)
# >>> 
# >>> exp(17)/pi
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'exp' is not defined
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> b/"divid"/"light"
# Genesis 1:4,14,18;Job 38:25;Jeremiah 31:35 (5 verses)
# >>> p(_)
# Genesis 1
# 4 And God saw the light, that it was good: and God divided the light from the darkness.
# 14 And God said, Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days, and years:
# 18 And to rule over the day and over the night, and to divide the light from the darkness: and God saw that it was good.
# Job 38:25 Who hath divided a watercourse for the overflowing of waters, or a way for the lightning of thunder;
# Jeremiah 31:35 Thus saith the LORD, which giveth the sun for a light by day, and the ordinances of the moon and of the stars for a light by night, which divideth the sea when the waves thereof roar; The LORD of hosts is his name:
# >>> sums('the light')
# (89, 467)
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> b.chapter(328)
# 2 Kings 15:1-38 (38 verses)
# >>> p(_)
# 2 Kings 15
# 1 In the twenty and seventh year of Jeroboam king of Israel began Azariah son of Amaziah king of Judah to reign.
# 2 Sixteen years old was he when he began to reign, and he reigned two and fifty years in Jerusalem. And his mother's name was Jecholiah of Jerusalem.
# 3 And he did that which was right in the sight of the LORD, according to all that his father Amaziah had done;
# 4 Save that the high places were not removed: the people sacrificed and burnt incense still on the high places.
# 5 And the LORD smote the king, so that he was a leper unto the day of his death, and dwelt in a several house. And Jotham the king's son was over the house, judging the people of the land.
# 6 And the rest of the acts of Azariah, and all that he did, are they not written in the book of the chronicles of the kings of Judah?
# 7 So Azariah slept with his fathers; and they buried him with his fathers in the city of David: and Jotham his son reigned in his stead.
# 8 In the thirty and eighth year of Azariah king of Judah did Zachariah the son of Jeroboam reign over Israel in Samaria six months.
# 9 And he did that which was evil in the sight of the LORD, as his fathers had done: he departed not from the sins of Jeroboam the son of Nebat, who made Israel to sin.
# 10 And Shallum the son of Jabesh conspired against him, and smote him before the people, and slew him, and reigned in his stead.
# 11 And the rest of the acts of Zachariah, behold, they are written in the book of the chronicles of the kings of Israel.
# 12 This was the word of the LORD which he spake unto Jehu, saying, Thy sons shall sit on the throne of Israel unto the fourth generation. And so it came to pass.
# 13 Shallum the son of Jabesh began to reign in the nine and thirtieth year of Uzziah king of Judah; and he reigned a full month in Samaria.
# 14 For Menahem the son of Gadi went up from Tirzah, and came to Samaria, and smote Shallum the son of Jabesh in Samaria, and slew him, and reigned in his stead.
# 15 And the rest of the acts of Shallum, and his conspiracy which he made, behold, they are written in the book of the chronicles of the kings of Israel.
# 16 Then Menahem smote Tiphsah, and all that were therein, and the coasts thereof from Tirzah: because they opened not to him, therefore he smote it; and all the women therein that were with child he ripped up.
# 17 In the nine and thirtieth year of Azariah king of Judah began Menahem the son of Gadi to reign over Israel, and reigned ten years in Samaria.
# 18 And he did that which was evil in the sight of the LORD: he departed not all his days from the sins of Jeroboam the son of Nebat, who made Israel to sin.
# 19 And Pul the king of Assyria came against the land: and Menahem gave Pul a thousand talents of silver, that his hand might be with him to confirm the kingdom in his hand.
# 20 And Menahem exacted the money of Israel, even of all the mighty men of wealth, of each man fifty shekels of silver, to give to the king of Assyria. So the king of Assyria turned back, and stayed not there in the land.
# 21 And the rest of the acts of Menahem, and all that he did, are they not written in the book of the chronicles of the kings of Israel?
# 22 And Menahem slept with his fathers; and Pekahiah his son reigned in his stead.
# 23 In the fiftieth year of Azariah king of Judah Pekahiah the son of Menahem began to reign over Israel in Samaria, and reigned two years.
# 24 And he did that which was evil in the sight of the LORD: he departed not from the sins of Jeroboam the son of Nebat, who made Israel to sin.
# 25 But Pekah the son of Remaliah, a captain of his, conspired against him, and smote him in Samaria, in the palace of the king's house, with Argob and Arieh, and with him fifty men of the Gileadites: and he killed him, and reigned in his room.
# 26 And the rest of the acts of Pekahiah, and all that he did, behold, they are written in the book of the chronicles of the kings of Israel.
# 27 In the two and fiftieth year of Azariah king of Judah Pekah the son of Remaliah began to reign over Israel in Samaria, and reigned twenty years.
# 28 And he did that which was evil in the sight of the LORD: he departed not from the sins of Jeroboam the son of Nebat, who made Israel to sin.
# 29 In the days of Pekah king of Israel came Tiglathpileser king of Assyria, and took Ijon, and Abelbethmaachah, and Janoah, and Kedesh, and Hazor, and Gilead, and Galilee, all the land of Naphtali, and carried them captive to Assyria.
# 30 And Hoshea the son of Elah made a conspiracy against Pekah the son of Remaliah, and smote him, and slew him, and reigned in his stead, in the twentieth year of Jotham the son of Uzziah.
# 31 And the rest of the acts of Pekah, and all that he did, behold, they are written in the book of the chronicles of the kings of Israel.
# 32 In the second year of Pekah the son of Remaliah king of Israel began Jotham the son of Uzziah king of Judah to reign.
# 33 Five and twenty years old was he when he began to reign, and he reigned sixteen years in Jerusalem. And his mother's name was Jerusha, the daughter of Zadok.
# 34 And he did that which was right in the sight of the LORD: he did according to all that his father Uzziah had done.
# 35 Howbeit the high places were not removed: the people sacrificed and burned incense still in the high places. He built the higher gate of the house of the LORD.
# 36 Now the rest of the acts of Jotham, and all that he did, are they not written in the book of the chronicles of the kings of Judah?
# 37 In those days the LORD began to send against Judah Rezin the king of Syria, and Pekah the son of Remaliah.
# 38 And Jotham slept with his fathers, and was buried with his fathers in the city of David his father: and Ahaz his son reigned in his stead.
# >>> IIKings[16:]
# 2 Kings 16:1-20 (20 verses)
# >>> 
# >>> 
# >>> 
# >>> Psalm[99:]
# Psalms 99:1-9 (9 verses)
# >>> Psalm[99:4]-5
# Psalms 99:4 The king's strength also loveth judgment; thou dost establish equity, thou executest judgment and righteousness in Jacob.
# Psalms 99:5 Exalt ye the LORD our God, and worship at his footstool; for he is holy.
# >>> 
# >>> 
# >>> sum(chron)
# 3088286401
# >>> _/c*1000
# 10301.414590623224
# >>> b.chapter(414)
# Nehemiah 1:1-11 (11 verses)
# >>> Isaiah[41:4]
# Isaiah 41:4 Who hath wrought and done it, calling the generations from the beginning? I the LORD, the first, and with the last; I am he.
# >>> _.tell()
# Who hath wrought and done it, calling the generations from the beginning? I the LORD, the first, and with the last; I am he.
#  46+ 37 +  112  + 19+ 38 + 29+   58  + 33+    127    + 52 + 33+    81    +9+ 33+  49 + 33+  72  + 19+ 60 + 33+  52 +9+14+ 13=1061
# >>> tell('In the beginning')
# In the beginning
# 23+ 33+    81   =137
# >>> tell('the first and with the last')
# the first and with the last
#  33+  72 + 19+ 60 + 33+ 52 =269
# >>> (Genesis[1:1]-(2,3)).count("And God")
# 29
# >>> Genesis[1:30]
# Genesis 1:30 And to every beast of the earth, and to every fowl of the air, and to every thing that creepeth upon the earth, wherein there is life, I have given every green herb for meat: and it was so.
# >>> Genesis[1:29]
# Genesis 1:29 And God said, Behold, I have given you every herb bearing seed, which is upon the face of all the earth, and every tree, in the which is the fruit of a tree yielding seed; to you it shall be for meat.
# >>> Genesis[1:25].lc()
# 134
# >>> 134/2
# 67.0
# >>> 39*2
# 78
# >>> week=Genesis[1:1]-(2,3)
# >>> sums('week')
# (44, 530)
# >>> week/'And God'
# Genesis 1:3-12,14,16-18,20-22,24-26,28-29,31;2:3 (24 verses)
# >>> week.count('And God')
# 29
# >>> sums('rib')
# (29, 101)
# >>> sums('cannine')
# (60, 168)
# >>> sums('kennel')
# (61, 160)
# >>> sums('Cainan')
# (42, 114)
# >>> sums('Cainanite')
# (76, 328)
# >>> week.lcs()
# [44, 110, 41, 66, 91, 87, 116, 72, 98, 95, 136, 136, 41, 128, 79, 100, 61, 90, 42, 127, 158, 97, 41, 122, 134, 194, 81, 188, 152, 145, 95, 56, 101, 103]
# >>> tale(_)
# [44, 154, 195, 261, 352, 439, 555, 627, 725, 820, 956, 1092, 1133, 1261, 1340, 1440, 1501, 1591, 1633, 1760, 1918, 2015, 2056, 2178, 2312, 2506, 2587, 2775, 2927, 3072, 3167, 3223, 3324, 3427]
# >>> 
# >>> 
# >>> 
# >>> 
# >>> pp(12)
# 353
# >>> npp(797)
# 18
# >>> pp(35)
# 15551
# >>> npp(10301)
# 21
# >>> pp(12)
# 353
# >>> np(10301)
# 1263
# >>> base(23,10301)
# [19, 10, 20]
# >>> sum(base(23,3088286401))
# 123
# >>> sum(base(22,3088286401))
# 46
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> mc
# 299792.458
# >>> AV/c
# 9.5899728137924
# >>> W/c
# 5.526823493338181e-05
# >>> X/c
# 0.5204963995458485
# >>> Y/c
# 0.19089010905004156
# >>> (AV*2+X+X)/mc
# 20220.938426676497
# >>> (AV*2+X+Y)/mc
# 19891.332136180692
# >>> (AV+X+Y)/mc
# 10301.35932238829
# >>> (AV+W+X+Y)/mc
# 10301.414590623224
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> b.chapter(1)
# Genesis 1:1-31 (31 verses)
# >>> b.midch()
# Psalms 117:1 O praise the LORD, all ye nations: praise him, all ye people.
# Psalms 117:2 For his merciful kindness is great toward us: and the truth of the LORD endureth for ever. Praise ye the LORD.
# >>> b.book(1)
# Genesis 1:1-50:26 (1533 verses)
# >>> b.book(66)
# Revelation 1:1-22:21 (404 verses)
# >>> b.book(range(1,66+1))
# [Genesis 1:1-50:26 (1533 verses), Exodus 1:1-40:38 (1213 verses), Leviticus 1:1-27:34 (859 verses), Numbers 1:1-36:13 (1288 verses), Deuteronomy 1:1-34:12 (959 verses), Joshua 1:1-24:33 (658 verses), Judges 1:1-21:25 (618 verses), Ruth 1:1-4:22 (85 verses), 1 Samuel 1:1-31:13 (810 verses), 2 Samuel 1:1-24:25 (695 verses), 1 Kings 1:1-22:53 (816 verses), 2 Kings 1:1-25:30 (719 verses), 1 Chronicles 1:1-29:30 (942 verses), 2 Chronicles 1:1-36:23 (822 verses), Ezra 1:1-10:44 (280 verses), Nehemiah 1:1-13:31 (406 verses), Esther 1:1-10:3 (167 verses), Job 1:1-42:17 (1070 verses), Psalms 1:1-150:6 (2461 verses), Proverbs 1:1-31:31 (915 verses), Ecclesiastes 1:1-12:14 (222 verses), Song of Solomon 1:1-8:14 (117 verses), Isaiah 1:1-66:24 (1292 verses), Jeremiah 1:1-52:34 (1364 verses), Lamentations 1:1-5:22 (154 verses), Ezekiel 1:1-48:35 (1273 verses), Daniel 1:1-12:13 (357 verses), Hosea 1:1-14:9 (197 verses), Joel 1:1-3:21 (73 verses), Amos 1:1-9:15 (146 verses), Obadiah 1:1-21 (21 verses), Jonah 1:1-4:11 (48 verses), Micah 1:1-7:20 (105 verses), Nahum 1:1-3:19 (47 verses), Habakkuk 1:1-3:19 (56 verses), Zephaniah 1:1-3:20 (53 verses), Haggai 1:1-2:23 (38 verses), Zechariah 1:1-14:21 (211 verses), Malachi 1:1-4:6 (55 verses), Matthew 1:1-28:20 (1071 verses), Mark 1:1-16:20 (678 verses), Luke 1:1-24:53 (1151 verses), John 1:1-21:25 (879 verses), Acts 1:1-28:31 (1007 verses), Romans 1:1-16:27 (433 verses), 1 Corinthians 1:1-16:24 (437 verses), 2 Corinthians 1:1-13:14 (257 verses), Galatians 1:1-6:18 (149 verses), Ephesians 1:1-6:24 (155 verses), Philippians 1:1-4:23 (104 verses), Colossians 1:1-4:18 (95 verses), 1 Thessalonians 1:1-5:28 (89 verses), 2 Thessalonians 1:1-3:18 (47 verses), 1 Timothy 1:1-6:21 (113 verses), 2 Timothy 1:1-4:22 (83 verses), Titus 1:1-3:15 (46 verses), Philemon 1:1-25 (25 verses), Hebrews 1:1-13:25 (303 verses), James 1:1-5:20 (108 verses), 1 Peter 1:1-5:14 (105 verses), 2 Peter 1:1-3:18 (61 verses), 1 John 1:1-5:21 (105 verses), 2 John 1:1-13 (13 verses), 3 John 1:1-14 (14 verses), Jude 1:1-25 (25 verses), Revelation 1:1-22:21 (404 verses)]
# >>> [b.vc() for b in b.book(range(1,67))]
# [1533, 1213, 859, 1288, 959, 658, 618, 85, 810, 695, 816, 719, 942, 822, 280, 406, 167, 1070, 2461, 915, 222, 117, 1292, 1364, 154, 1273, 357, 197, 73, 146, 21, 48, 105, 47, 56, 53, 38, 211, 55, 1071, 678, 1151, 879, 1007, 433, 437, 257, 149, 155, 104, 95, 89, 47, 113, 83, 46, 25, 303, 108, 105, 61, 105, 13, 14, 25, 404]
# >>> b.book(15)
# Ezra 1:1-10:44 (280 verses)
# >>> b.bookix
# [0, 1533, 2746, 3605, 4893, 5852, 6510, 7128, 7213, 8023, 8718, 9534, 10253, 11195, 12017, 12297, 12703, 12870, 13940, 16401, 17316, 17538, 17655, 18947, 20311, 20465, 21738, 22095, 22292, 22365, 22511, 22532, 22580, 22685, 22732, 22788, 22841, 22879, 23090, 23145, 24216, 24894, 26045, 26924, 27931, 28364, 28801, 29058, 29207, 29362, 29466, 29561, 29650, 29697, 29810, 29893, 29939, 29964, 30267, 30375, 30480, 30541, 30646, 30659, 30673, 30698, 31102]
# >>> b.book(22)
# Song of Solomon 1:1-8:14 (117 verses)
# >>> b.book(23)
# Isaiah 1:1-66:24 (1292 verses)
# >>> b.chapter(830)
# Ezekiel 28:1-26 (26 verses)
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> chae=b.Genesis[1:1]-(2,3)
# >>> chae
# Genesis 1:1-2:3 (34 verses)
# >>> chae.count('and')
# 104
# >>> chae.count(r'\band\b')
# 104
# >>> chae.count('God')
# 35
# >>> chae.count('And God')
# 29
# >>> chae.count('And God said')
# 10
# >>> chae.count('And God said, let')
# 8
# >>> Genesis.count('And God said.*let')
# 9
# >>> Genesis[2:4]-(50,26)
# Genesis 2:4-50:26 (1499 verses)
# >>> _/('And God said.*let')
# Genesis 21:12 And God said unto Abraham, Let it not be grievous in thy sight because of the lad, and because of thy bondwoman; in all that Sarah hath said unto thee, hearken unto her voice; for in Isaac shall thy seed be called.
# >>> tell('And God said unto Abraham')
# And God said unto Abraham
#  19+ 26+ 33 + 70 +   44  =192
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> Genesis.count('And God said')
# 21
# >>> b.count('And God said')
# 30
# >>> b.Genesis[1:1].vs()[::-1]
# '.htrae eht dna nevaeh eht detaerc doG gninnigeb eht nI'
# >>> 
# >>> Genesis.count('And God')
# 66
# >>> b.count("And God")
# 137
# >>> tell('In the beginning')
# In the beginning
# 23+ 33+    81   =137
# >>> tell('In the beginning God')
# In the beginning God
# 23+ 33+    81   + 26=163
# >>> Genesis[1:1].tell(ssum)
# In the beginning God created the heaven and the earth.
# 59+213+   189   + 71+  308  +213+ 469  + 55+213+ 304  =2094
# >>> sums('eve')
# (32, 410)
# >>> sums('even')
# (46, 460)
# >>> b/"even I"
# Genesis 6:17;42:28;Leviticus 13:18;23:5;26:28;Numbers 8:16;9:5;Deuteronomy 4:30;32:39;Joshua 5:10;6:17;Judges 5:3,15;8:27;1 Samuel 17:40;28:3;1 Kings 12:33;15:28;18:22;19:10,14;2 Kings 3:24;18:10;25:23;1 Chronicles 21:17;2 Chronicles 8:13;28:27;Ezra 7:21;Psalms 18:6;Proverbs 14:13;Isaiah 18:2;43:11,25;46:4;48:15;51:12;Jeremiah 7:11;15:13;21:5;22:25;23:39;29:23;31:2;33:10;40:8;Ezekiel 5:8;6:3;12:4,7;17:19;34:11,20;44:19;Daniel 8:15;9:25;11:1;Hosea 5:14;Joel 1:2;Zephaniah 3:20;Zechariah 7:1;12:6;Mark 14:30,54;Romans 10:8;Galatians 5:14;Ephesians 1:10;Philippians 4:16;1 Thessalonians 2:18;1 John 5:20;Revelation 2:13;3:4 (71 verses)
# >>> chae.wc()
# 864
# >>> factors(864)
# [2, 2, 2, 2, 2, 3, 3, 3]
# >>> sof(864)
# 2520
# >>> 7*360
# 2520
# >>> 
# >>> 
# >>> tell('God')
# G o  d
# 7+15+4=26
# >>> 26*2*2
# 104
# >>> tell("DNA")
# D N  A
# 4+14+1=19
# >>> tell("and")
# a n  d
# 1+14+4=19
# >>> tell("And God")
# And God
#  19+ 26=45
# >>> 
# >>> 26
# 26
# >>> chae.wc()
# 864
# >>> factors(864)
# [2, 2, 2, 2, 2, 3, 3, 3]
# >>> chae.midv()
# Genesis 1:17 And God set them in the firmament of the heaven to give light upon the earth,
# Genesis 1:18 And to rule over the day and over the night, and to divide the light from the darkness: and God saw that it was good.
# >>> tell(chae.midv().v(1))
# And God set them in the firmament of the heaven to give light upon the earth,
#  19+ 26+ 44+ 46 +23+ 33+    99   +21+ 33+  55  +35+ 43 +  56 + 66 + 33+  52  =684
# >>> tell(chae.midv().v(2))
# And to rule over the day and over the night, and to divide the light from the darkness: and God saw that it was good.
#  19+35+ 56 + 60 + 33+ 30+ 19+ 60 + 33+  58  + 19+35+  53  + 33+  56 + 52 + 33+    91   + 19+ 26+ 43+ 49 +29+ 43+  41 =1025
# >>> chae.midv().wcs()
# [16, 25]
# >>> sum(_)
# 41
# >>> tell('good')
# g o  o  d
# 7+15+15+4=41
# >>> tell('sol sun son')
# sol sun son
#  46+ 54+ 48=148
# >>> tell('sol om on')
# sol om on
#  46+28+29=103
# >>> tell('Who man rib')
# Who man rib
#  46+ 28+ 29=103
# >>> tell('In ... made.')
# In ... made.
# 23+ 0 +  23 =46
# >>> tell(' '.join([chae.words()[0],chae.words()[-1]]))
# In made.
# 23+  23 =46
# >>> tell('made he him')
# made he him
#  23 +13+ 30=66
# >>> tell('lord XY')
# lord XY
#  49 +49=98
# >>> tell('woman')
# w  o  m  a n
# 23+15+13+1+14=66
# >>> tell('dna dna man')
# dna dna man
#  19+ 19+ 28=66
# >>> 
# >>> chae.wc()
# 864
# >>> pf(_)
# Counter({2: 5, 3: 3})
# >>> 
# >>> chae.midword()
# ['may', 'fly']
# >>> chae/"may"
# Genesis 1:20 And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl that may fly above the earth in the open firmament of heaven.
# >>> _.wc()
# 29
# >>> 
# >>> 
# >>> adam=b.Genesis[1:]-b.Genesis[4:]
# >>> adam
# Genesis 1:1-4:26 (106 verses)
# >>> adam.midv()
# Genesis 2:22 And the rib, which the LORD God had taken from man, made he a woman, and brought her unto the man.
# Genesis 2:23 And Adam said, This is now bone of my bones, and flesh of my flesh: she shall be called Woman, because she was taken out of Man.
# >>> tell(adam.midv().v(1))
# And the rib, which the LORD God had taken from man, made he a woman, and brought her unto the man.
#  19+ 33+ 29 +  51 + 33+ 49 + 26+ 13+  51 + 52 + 28 + 23 +13+1+  66  + 19+   91  + 31+ 70 + 33+ 28 =759
# >>> tell(adam.midv().v(2))
# And Adam said, This is now bone of my bones, and flesh of my flesh: she shall be called Woman, because she was taken out of Man.
#  19+ 19 +  33 + 56 +28+ 52+ 36 +21+38+  55  + 19+  50 +21+38+  50  + 32+  52 +7 +  37  +  66  +   56  + 32+ 43+  51 + 56+21+ 28 =1016
# >>> tell('wo man')
# wo man
# 38+ 28=66
# >>> 66-19
# 47
# >>> tell('son'),tell('rib dna')
# s  o  n
# 19+15+14=48
# rib dna
#  29+ 19=48
# (None, None)
# >>> tell('blood')
# b l  o  o  d
# 2+12+15+15+4=48
# >>> 38//2
# 19
# >>> tell('saith')
# s  a i t  h
# 19+1+9+20+8=57
# >>> b.Genesis[1:]-b.Genesis[4:]
# Genesis 1:1-4:26 (106 verses)
# >>> 4*26
# 104
# >>> tell('DNA')
# D N  A
# 4+14+1=19
# >>> tell('deoxyribonucleic acid')
# deoxyribonucleic acid
#       184       + 17 =201
# >>> tell('ribo nucleic')
# ribo nucleic
#  44 +   67  =111
# >>> tell('ribosome')
# r  i b o  s  o  m  e
# 18+9+2+15+19+15+13+5=96
# >>> 
# >>> tell('deoxy acid')
# deoxy acid
#   73 + 17 =90
# >>> adam.count("God")
# 60
# >>> adam.count(r"\band\b")
# 273
# >>> factors(273)
# [3, 7, 13]
# >>> 27*3
# 81
# >>> osum('dog')*3
# 78
# >>> sums('dog')
# (26, 71)
# >>> sums('LORD God')
# (75, 255)
# >>> 
# >>> 
# >>> tell('Genes is')
# Genes is
#   50 +28=78
# >>> tell('genes man')
# genes man
#   50 + 28=78
# >>> sums('adam')
# (19, 46)
# >>> tell('ge ne s is')
# ge ne s  is
# 12+19+19+28=78
# >>> (b['1 John'][5:7]-8).tell()
# For there are three that bear record in heaven, the Father, the Word, and the Holy Ghost: and these three are one.
#  39+  56 + 24+  56 + 49 + 26 +  63  +23+   55  + 33+   58  + 33+  60 + 19+ 33+ 60 +  69  + 19+  57 +  56 + 24+ 34 =946
# And there are three that bear witness in earth, the Spirit, and the water, and the blood: and these three agree in one.
#  19+  56 + 24+  56 + 49 + 26 +  109  +23+  52  + 33+   91  + 19+ 33+  67  + 19+ 33+  48  + 19+  57 +  56 +  36 +23+ 34 =982
# >>> 
# >>> osum('dna')*104
# 1976
# >>> b.Gen.count(r'\band\b')
# 3678
# >>> pf(3678)
# Counter({2: 1, 3: 1, 613: 1})
# >>> b.count(r'dog')
# 41
# >>> 
# >>> b.count(r'\bCai?n')
# 746
# >>> pf(746)
# Counter({2: 1, 373: 1})
# >>> np(41)
# 13
# >>> pp(13)
# 373
# >>> Genesis[1:25]
# Genesis 1:25 And God made the beast of the earth after his kind, and cattle after their kind, and every thing that creepeth upon the earth after his kind: and God saw that it was good.
# >>> _.wc()
# 34
# >>> sums('the beginning')
# (114, 402)
# >>> 
# >>> tell('And God made the beast of')
# And God made the beast of
#  19+ 26+ 23 + 33+  47 +21=169
# >>> pn(39)
# 167
# >>> 2445000000/pi
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'pi' is not defined
# >>> 78/pi
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'pi' is not defined
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> tell('what why when where who')
# what why when where who
#  52 + 56+ 50 +  59 + 46=263
# >>> tell('how')
# h o  w
# 8+15+23=46
# >>> sums('eden')
# (28, 64)
# >>> sums('live')
# (48, 444)
# >>> sums('lord')
# (49, 184)
# >>> 
# >>> b
# Genesis 1:1-Revelation 22:21 (31102 verses)
# >>> b.midv
# <bound method Sel.midv of Genesis 1:1-Revelation 22:21 (31102 verses)>
# >>> 
# >>> tell('dog dna')
# dog dna
#  26+ 19=45
# >>> tell('and god')
# and god
#  19+ 26=45
# >>> 2445/c
# 8.155642127594817e-06
# >>> b.verse(8155)
# 2 Samuel 5:22 And the Philistines came up yet again, and spread themselves in the valley of Rephaim.
# >>> b/"am I a dog"
# 1 Samuel 17:43 And the Philistine said unto David, Am I a dog, that thou comest to me with staves? And the Philistine cursed David by his gods.
# 2 Samuel 3:8 Then was Abner very wroth for the words of Ishbosheth, and said, Am I a dog's head, which against Judah do shew kindness this day unto the house of Saul thy father, to his brethren, and to his friends, and have not delivered thee into the hand of David, that thou chargest me to day with a fault concerning this woman?
# >>> _.wcs(),_.tell()
# And the Philistine said unto David, Am I a dog, that thou comest to me with staves? And the Philistine cursed David by his gods.
#  19+ 33+   121    + 33 + 70 +  40  +14+9+1+ 26 + 49 + 64 +  75  +35+18+ 60 +   86  + 19+ 33+   121    +  70  +  40 +27+ 36+  45 =1144
# Then was Abner very wroth for the words of Ishbosheth, and said, Am I a dog's head, which against Judah do shew kindness this day unto the house of Saul thy father, to his brethren, and to his friends, and have not delivered thee into the hand of David, that thou chargest me to day with a fault concerning this woman?
#  47 + 43+  40 + 70 +  84 + 39+ 33+  79 +21+    113    + 19+  33 +14+9+1+  45 +  18 +  51 +   71  +  44 +19+ 55 +   95   + 56 + 30+ 70 + 33+  68 +21+ 53 + 53+   58  +35+ 36+    90   + 19+35+ 36+   75   + 19+ 36 + 49+    84   + 38 + 58 + 33+ 27 +21+  40  + 49 + 64 +   81   +18+35+ 30+ 60 +1+  60 +   102    + 56 +  66  =2838
# ([25, 61], None)
# >>> b/"dog"
# Exodus 11:7;22:31;Deuteronomy 23:18;Judges 7:5;1 Samuel 17:43;24:14;2 Samuel 3:8;9:8;16:9;1 Kings 14:11;16:4;21:19,23-24;22:38;2 Kings 8:13;9:10,36;Job 30:1;Psalms 22:16,20;59:6,14;68:23;Proverbs 26:11,17;Ecclesiastes 9:4;Isaiah 56:10-11;66:3;Jeremiah 15:3;Matthew 7:6;15:26-27;Mark 7:27-28;Luke 16:21;Philippians 3:2;2 Peter 2:22;Revelation 22:15 (40 verses)
# >>> _.vi(1).wc()
# 36
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 8090*pi
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'pi' is not defined
# >>> 
# >>> 
# >>> p(Genesis[1:])
# Genesis 1
# 1 In the beginning God created the heaven and the earth.
# 2 And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters.
# 3 And God said, Let there be light: and there was light.
# 4 And God saw the light, that it was good: and God divided the light from the darkness.
# 5 And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day.
# 6 And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters.
# 7 And God made the firmament, and divided the waters which were under the firmament from the waters which were above the firmament: and it was so.
# 8 And God called the firmament Heaven. And the evening and the morning were the second day.
# 9 And God said, Let the waters under the heaven be gathered together unto one place, and let the dry land appear: and it was so.
# 10 And God called the dry land Earth; and the gathering together of the waters called he Seas: and God saw that it was good.
# 11 And God said, Let the earth bring forth grass, the herb yielding seed, and the fruit tree yielding fruit after his kind, whose seed is in itself, upon the earth: and it was so.
# 12 And the earth brought forth grass, and herb yielding seed after his kind, and the tree yielding fruit, whose seed was in itself, after his kind: and God saw that it was good.
# 13 And the evening and the morning were the third day.
# 14 And God said, Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days, and years:
# 15 And let them be for lights in the firmament of the heaven to give light upon the earth: and it was so.
# 16 And God made two great lights; the greater light to rule the day, and the lesser light to rule the night: he made the stars also.
# 17 And God set them in the firmament of the heaven to give light upon the earth,
# 18 And to rule over the day and over the night, and to divide the light from the darkness: and God saw that it was good.
# 19 And the evening and the morning were the fourth day.
# 20 And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl that may fly above the earth in the open firmament of heaven.
# 21 And God created great whales, and every living creature that moveth, which the waters brought forth abundantly, after their kind, and every winged fowl after his kind: and God saw that it was good.
# 22 And God blessed them, saying, Be fruitful, and multiply, and fill the waters in the seas, and let fowl multiply in the earth.
# 23 And the evening and the morning were the fifth day.
# 24 And God said, Let the earth bring forth the living creature after his kind, cattle, and creeping thing, and beast of the earth after his kind: and it was so.
# 25 And God made the beast of the earth after his kind, and cattle after their kind, and every thing that creepeth upon the earth after his kind: and God saw that it was good.
# 26 And God said, Let us make man in our image, after our likeness: and let them have dominion over the fish of the sea, and over the fowl of the air, and over the cattle, and over all the earth, and over every creeping thing that creepeth upon the earth.
# 27 So God created man in his own image, in the image of God created he him; male and female created he them.
# 28 And God blessed them, and God said unto them, Be fruitful, and multiply, and replenish the earth, and subdue it: and have dominion over the fish of the sea, and over the fowl of the air, and over every living thing that moveth upon the earth.
# 29 And God said, Behold, I have given you every herb bearing seed, which is upon the face of all the earth, and every tree, in the which is the fruit of a tree yielding seed; to you it shall be for meat.
# 30 And to every beast of the earth, and to every fowl of the air, and to every thing that creepeth upon the earth, wherein there is life, I have given every green herb for meat: and it was so.
# 31 And God saw every thing that he had made, and, behold, it was very good. And the evening and the morning were the sixth day.
# >>> 
# >>> tell('And God made the beast')
# And God made the beast
#  19+ 26+ 23 + 33+  47 =148
# >>> 39*2
# 78
# >>> Genesis[1:].wcs()
# [10, 29, 11, 17, 22, 23, 26, 16, 25, 24, 34, 33, 10, 34, 22, 26, 16, 25, 10, 29, 34, 23, 10, 30, 34, 50, 22, 46, 42, 39, 25]
# >>> Genesis[1:26].tell()
# And God said, Let us make man in our image, after our likeness: and let them have dominion over the fish of the sea, and over the fowl of the air, and over the cattle, and over all the earth, and over every creeping thing that creepeth upon the earth.
#  19+ 26+  33 + 37+40+ 30 + 28+23+ 54+  35  +  50 + 54+    94   + 19+ 37+ 46 + 36 +   93   + 60 + 33+ 42 +21+ 33+ 25 + 19+ 60 + 33+ 56 +21+ 33+ 28 + 19+ 60 + 33+   61  + 19+ 60 + 25+ 33+  52  + 19+ 60 +  75 +   77   +  58 + 49 +   80   + 66 + 33+  52  =2149
# >>> sof(28)
# 56
# >>> tell('genesis')
# g e n  e s  i s
# 7+5+14+5+19+9+19=78
# >>> tell('genesis',ssum)
# g e n  e  s  i  s
# 7+5+50+5+100+9+100=276
# >>> pf(276)
# Counter({2: 2, 3: 1, 23: 1})
# >>> sums('genes')
# (50, 167)
# >>> sums('dna')
# (19, 55)
# >>> sums('')
# (0, 0)
# >>> 
# >>> 
# >>> bin(3088286401)
# '0b10111000000100111000001011000001'
# >>> (23<<27)+(39<<15)+(11<<6)+1
# 3088286401
# >>> len('0d=d:IFdVDUd:a=POINT(32*POS,31-VPOS<<5):RETURNELSEMODE9:GCOL-9:CLG:O FF:d=9:REPEATVDU30:REPEATGOSUBFALSE:IFPOS=28VDUPOS,15,VPOS,24;11,26:IF0E LSEIFa=0PRINT:UNTIL0ELSEUNTILVPOS=25:v=ABSRNDMOD7:i=0:VDU4895;3:REPEATm= 9-INKEY6MOD3:FORr=TRUETO1:t=rANDSGNt:IFt=rCOLOURv-15:VDUrEORm:i+=m=7AND9 -6*r:IF0ELSEFORn=0TO11:d=n/3OR2EORd:GOSUBFALSE:IF1<<(n+i)MOD12AND975AND& C2590EC/8^vVDU2080*ABSr;:t+=a:IF0ELSENEXT,:VDU20:UNTILt*LOGm:UNTILVPOS=3')
# 433
# >>> bin(433)
# '0b110110001'
# >>> 433>>4
# 27
# >>> 
# >>> b.book(59)
# James 1:1-5:20 (108 verses)
# >>> tell('isaiah')
# i s  a i a h
# 9+19+1+9+1+8=47
# >>> sums('king')
# (41, 86)
# >>> sums('אלהימ')
# (41, 86)
# >>> Isaiah[41:4]
# Isaiah 41:4 Who hath wrought and done it, calling the generations from the beginning? I the LORD, the first, and with the last; I am he.
# >>> _.tell()
# Who hath wrought and done it, calling the generations from the beginning? I the LORD, the first, and with the last; I am he.
#  46+ 37 +  112  + 19+ 38 + 29+   58  + 33+    127    + 52 + 33+    81    +9+ 33+  49 + 33+  72  + 19+ 60 + 33+  52 +9+14+ 13=1061
# >>> base(22,3088286401)
# [1, 5, 5, 5, 8, 9, 0, 13]
# >>> sum(_)
# 46
# >>> sum(base(10,3088286401))
# 40
# >>> AV+X+Y+AV+W+W
# 5963304492
# >>> 
# >>> math.sqrt(_)
# 77222.4351597384
# >>> AV+W+X
# 3031058986
# >>> a=math.sqrt(_);a
# 55055.054136745704
# >>> b=math.sqrt(AV+X);b
# 55054.903659892094
# >>> (a-b)
# 0.15047685361059848
# >>> math.sqrt(AV+AV+X+X)
# 77859.39143096354
# >>> math.sqrt(AV+AV+X+Y)
# 77222.22059744204
# >>> 
# >>> math.sqrt(AV+AV+W+X+X)
# 77859.49783423985
# >>> math.sqrt(AV+AV+W+X+Y)
# 77222.32787866473

# >>> w=math.sqrt(AV+W+X);w
# 55055.054136745704
# >>> tell(ssum,osum,lsum,'Authorised Version')
# Authorised Version
#    777    +  714  =1491
#    120    +  102  =222
#     10    +   7   = 17
# >>> Genesis/'let there be light'
# Genesis 1:3 And God said, Let there be light: and there was light.
# Genesis 1:14 And God said, Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days, and years:
# >>> _.v(1)[::-1]
# '.thgil saw ereht dna :thgil eb ereht teL ,dias doG dnA'
# >>> tell('dias dog dna')
# dias dog dna
#  33 + 26+ 19=78
# >>> bible/'science'
# Daniel 1:4 Children in whom was no blemish, but well favoured, and skilful in all wisdom, and cunning in knowledge, and understanding science, and such as had ability in them to stand in the king's palace, and whom they might teach the learning and the tongue of the Chaldeans.
# 1 Timothy 6:20 O Timothy, keep that which is committed to thy trust, avoiding profane and vain babblings, and oppositions of science falsely so called:
# >>> bible/'God of forces'
# Daniel 11:38 But in his estate shall he honour the God of forces: and a god whom his fathers knew not shall he honour with gold, and silver, and with precious stones, and pleasant things.
# >>> bible/'net'
# Exodus 19:17;27:4-5;38:4;Numbers 1:8;2:5;7:18,23;10:15;Deuteronomy 24:6;Joshua 15:19;16:3;18:13;Judges 1:15;2 Samuel 23:28-29;1 Kings 6:6;7:17-18,20,41-42;9:17;2 Kings 25:23,25;1 Chronicles 2:14,54;7:24;9:2,16;11:30;15:24;24:6;25:2,12;26:4;27:13,15;2 Chronicles 8:5;17:7-8;35:9;Ezra 2:22,43,58,70;7:7,24;8:17,20;10:22;Nehemiah 3:26,31;7:26,46,60,73;10:28;11:3,21;12:21,28,36;Job 18:8;19:6;30:7;41:24;Psalms 9:15;10:9;25:15;31:4;35:7-8;57:6;66:11;140:5;141:10;Proverbs 1:17;12:12;24:31;29:5;Ecclesiastes 7:26;9:12;Isaiah 19:8-9;34:13;51:20;Jeremiah 36:14;40:8,14-15;41:1-2,6-7,9-12,15-16,18;52:22-23;Lamentations 1:13;Ezekiel 12:13;17:20;19:8;26:5,14;31:14,16,18;32:3,18,24;47:10;Hosea 5:1;7:12;9:6;Micah 7:2;Habakkuk 1:15-17;Zephaniah 2:9;Matthew 4:18,20-21;13:47;Mark 1:16,18-19;Luke 5:2,4-6;John 21:6,8,11 (139 verses)
# >>> 
# >>> AY**(1/3)
# 1456.260902161315
# >>> 6e-23**(1/3)
# 3.9148676411688676e-08
# >>> AX+AW+Y
# 5963304492
# >>> _/2
# 2981652246.0
# >>> tell('km / s')
# km / s
# 24+0+19=43
# >>> 24/19
# 1.263157894736842
# >>> 106*19
# 2014
# >>> (Genesis[1:1]-(2,3)).count('and')
# 104
# >>> 104*19
# 1976
# >>> 2001-1952
# 49
# >>> 
