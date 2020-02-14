# >>> from bible import *
# >>> from math import *
# >>> from primes import *
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# ModuleNotFoundError: No module named 'primes'
# >>> b.Gen[5:].wc()
# 505
# >>> b.Gen[5:].wcs()
# [24, 21, 25, 20, 16, 11, 17, 15, 8, 17, 15, 8, 17, 15, 10, 17, 16, 13, 15, 16, 10, 17, 13, 13, 12, 18, 16, 13, 29, 18, 16, 14]
# >>> 59*8
# 472
# >>> 456/8
# 57.0
# >>> 57*8
# 456
# >>> 57*8
# 456
# >>> b.chapter(797)
# Jeremiah 52:1-34 (34 verses)
# >>> b.chapter(789)
# Jeremiah 44:1-30 (30 verses)
# >>> Genesis[1:1].lc()
# 44
# >>> 
# >>> b.chapter(629)
# Proverbs 1:1-33 (33 verses)
# >>> Psalms-Revelation
# Psalms 1:1-Revelation 22:21 (17162 verses)
# >>> _.chc()
# 711
# >>> 
# >>> b[33]
# Micah 1:1-7:20 (105 verses)
# >>> Micah[7].chn()
# 900
# >>> 
# >>> ot=Genesis-Malachi
# >>> ot
# Genesis 1:1-Malachi 4:6 (23145 verses)
# >>> ot.chaptercount()
# 929
# >>> 789629/pi
# 251346.71711742046
# >>> 6**6
# 46656
# >>> 25+13
# 38
# >>> factors(251)
# [251]
# >>> np(251)
# 54
# >>> factors(_)
# [2, 3, 3, 3]
# >>> 
# >>> 
# >>> tell('wo')
# w  o
# 23+15=38
# >>> ssum('adam')
# 46
# >>> 
# >>> b.chapter(251)
# 1 Samuel 15:1-35 (35 verses)
# >>> 
# >>> 
# >>> Genesis.wordcount()
# 38264
# >>> Genesis
# Genesis 1:1-50:26 (1533 verses)
# >>> 
# >>> 3*7*73
# 1533
# >>> Genesis[1].wc()
# 797
# >>> Psalms[59:1]-5
# Psalms 59:1-5 (5 verses)
# >>> p(_.words().index('mighty')+1)
# 41
# >>> _.wcs()
# [17, 13, 25, 14, 25]
# >>> sum(_)
# 94
# >>> 94-41
# 53
# >>> 94+53
# 147
# >>> Psalm[59].words()[147-3:147+3]
# ['derision.', 'Because', 'of', 'his', 'strength', 'will']
# >>> 
# >>> 94*2
# 188
# >>> Psalm[59].words()[188-1:190]
# ['thy', 'power;', 'and']
# >>> print(Psalm[59])
# Psalms 59
# 1 Deliver me from mine enemies, O my God: defend me from them that rise up against me.
# 2 Deliver me from the workers of iniquity, and save me from bloody men.
# 3 For, lo, they lie in wait for my soul: the mighty are gathered against me; not for my transgression, nor for my sin, O LORD.
# 4 They run and prepare themselves without my fault: awake to help me, and behold.
# 5 Thou therefore, O LORD God of hosts, the God of Israel, awake to visit all the heathen: be not merciful to any wicked transgressors. Selah.
# 6 They return at evening: they make a noise like a dog, and go round about the city.
# 7 Behold, they belch out with their mouth: swords are in their lips: for who, say they, doth hear?
# 8 But thou, O LORD, shalt laugh at them; thou shalt have all the heathen in derision.
# 9 Because of his strength will I wait upon thee: for God is my defence.
# 10 The God of my mercy shall prevent me: God shall let me see my desire upon mine enemies.
# 11 Slay them not, lest my people forget: scatter them by thy power; and bring them down, O Lord our shield.
# 12 For the sin of their mouth and the words of their lips let them even be taken in their pride: and for cursing and lying which they speak.
# 13 Consume them in wrath, consume them, that they may not be: and let them know that God ruleth in Jacob unto the ends of the earth. Selah.
# 14 And at evening let them return; and let them make a noise like a dog, and go round about the city.
# 15 Let them wander up and down for meat, and grudge if they be not satisfied.
# 16 But I will sing of thy power; yea, I will sing aloud of thy mercy in the morning: for thou hast been my defence and refuge in the day of my trouble.
# 17 Unto thee, O my strength, will I sing: for God is my defence, and the God of my mercy.
# >>> 59*3
# 177
# >>> np(59)
# 17
# >>> 
# >>> _*11
# 187
# >>> 595
# 595
# >>> 
# >>> 
# >>> b.count('Selah')
# 76
# >>> factors(_)
# [2, 2, 19]
# >>> tell('selah')
# s  e l  a h
# 19+5+12+1+8=45
# >>> 
# >>> 
# >>> 17+11
# 28
# >>> 94-28
# 66
# >>> chi.index(659)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'chi' is not defined
# >>> sqrt(15551)
# 124.70364870363657
# >>> sqrt(31102)
# 176.35759127409287
# >>> base(16,31102)
# [7, 9, 7, 14]
# >>> exp(3.1102)
# 22.425529058077274
# >>> exp(1.5551)
# 4.735560057488161
# >>> 3.1103**2
# 9.67396609
# >>> 31103*31103
# 967396609
# >>> sqrt(10)
# 3.1622776601683795
# >>> log(10)
# 2.302585092994046
# >>> factors(502411)
# [7, 13, 5521]
# >>> factors(1223502411)
# [3, 23, 23, 59, 73, 179]
# >>> factors(3166)
# [2, 1583]
# >>> factors(3167)
# [3167]
# >>> 
# >>> 
# >>> b.Pro[1:1].ix[0]+1
# 16402
# >>> b.Job[42:17].ix[0]+1
# 13940
# >>> factors(13940)
# [2, 2, 5, 17, 41]
# >>> factors(16402)
# [2, 59, 139]
# >>> factors(13941)
# [3, 3, 1549]
# >>> factors(16403)
# [47, 349]
# >>> chi
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'chi' is not defined
# >>> James.chn()
# 1147
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 789629/pi
# 251346.71711742046
# >>> b/"five thousand"
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> b.Mark[6:].ix
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'b' is not defined
# >>> 24450/50
# 489.0
# >>> 111*56
# 6216
# >>> 24463/6216
# 3.9354890604890604
# >>> 24463/110/55
# 4.043471074380165
# >>> 4*111*55
# 24420
# >>> Sel(b.doc,[24420-1])
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'Sel' is not defined
# >>> b.Matt[1:1].ix[0]+1
# 23146
# >>> 24409-23145
# 1264
# >>> 
# >>> 24463-23145
# 1318
# >>> 
# >>> 112*56-5000
# 1272
# >>> 24409+43
# 24452
# >>> p(Sel(b.doc,[23144+1272]))
# Mark 6:9 But be shod with sandals; and not put on two coats.
# >>> Sel(b.doc,[5050])
# 1 verses, Deuteronomy 4:46
# >>> p(_)
# Deuteronomy 4:46 On this side Jordan, in the valley over against Bethpeor, in the land of Sihon king of the Amorites, who dwelt at Heshbon, whom Moses and the children of Israel smote, after they were come forth out of Egypt:
# >>> b.Deu[6:1].ix
# [5087]
# >>> 56*113
# 6328
# >>> _-5000
# 1328
# >>> b.Deu[5:6].ix[0]+1
# 5060
# >>> 56*112+13+7
# 6292
# >>> 
# >>> p(Sel(b.doc,[23145+1292]))
# Mark 6:30 And the apostles gathered themselves together unto Jesus, and told him all things, both what they had done, and what they had taught.
# >>> factors(1292)
# [2, 2, 17, 19]
# >>> 112*56
# 6272
# >>> p(Sel(b.doc,[23144+5060]))
# Romans 10:16 But they have not all obeyed the gospel. For Esaias saith, Lord, who hath believed our report?
# >>> b.Ex[20:1].ix[0]+1
# 2053
# >>> factors(2053)
# [2053]
# >>> whichprime(2053)
# 309
# >>> 2053/55
# 37.32727272727273
# >>> 55*37
# 2035
# >>> 2053-2035
# 18
# >>> 37*55.5
# 2053.5
# >>> 2053/37
# 55.486486486486484
# >>> b.chapters()[485]
# 9 verses, Psalms 8:1...Psalms 8:9
# >>> p(_)
# Psalms 8:1 O LORD, our Lord, how excellent is thy name in all the earth! who hast set thy glory above the heavens.
# Psalms 8:2 Out of the mouth of babes and sucklings hast thou ordained strength because of thine enemies, that thou mightest still the enemy and the avenger.
# Psalms 8:3 When I consider thy heavens, the work of thy fingers, the moon and the stars, which thou hast ordained;
# Psalms 8:4 What is man, that thou art mindful of him? and the son of man, that thou visitest him?
# Psalms 8:5 For thou hast made him a little lower than the angels, and hast crowned him with glory and honour.
# Psalms 8:6 Thou madest him to have dominion over the works of thy hands; thou hast put all things under his feet:
# Psalms 8:7 All sheep and oxen, yea, and the beasts of the field;
# Psalms 8:8 The fowl of the air, and the fish of the sea, and whatsoever passeth through the paths of the seas.
# Psalms 8:9 O LORD our Lord, how excellent is thy name in all the earth!
# >>> p(b.Ps[11:])
# Psalms 11:1 In the LORD put I my trust: how say ye to my soul, Flee as a bird to your mountain?
# Psalms 11:2 For, lo, the wicked bend their bow, they make ready their arrow upon the string, that they may privily shoot at the upright in heart.
# Psalms 11:3 If the foundations be destroyed, what can the righteous do?
# Psalms 11:4 The LORD is in his holy temple, the LORD's throne is in heaven: his eyes behold, his eyelids try, the children of men.
# Psalms 11:5 The LORD trieth the righteous: but the wicked and him that loveth violence his soul hateth.
# Psalms 11:6 Upon the wicked he shall rain snares, fire and brimstone, and an horrible tempest: this shall be the portion of their cup.
# Psalms 11:7 For the righteous LORD loveth righteousness; his countenance doth behold the upright.
# >>> b.Ps[11:].wcs()
# [20, 25, 10, 23, 16, 22, 12]
# >>> b.Ps[11:].wc()
# 128
# >>> factors(5055)
# [3, 5, 337]
# >>> 3*5*337
# 5055
# >>> b.Gen.wc()
# 38264
# >>> (b.Ex[20:]-b.Ex[30:1]).wc()
# 8577
# >>> b.Deu[5:1].ix[0]+1
# 5055
# >>> b.Deu[5:6].ix[0]+1
# 5060
# >>> factors(789629)
# [311, 2539]
# >>> b.chapters()[538]
# 8 verses, Psalms 61:1...Psalms 61:8
# >>> p(_)
# Psalms 61:1 Hear my cry, O God; attend unto my prayer.
# Psalms 61:2 From the end of the earth will I cry unto thee, when my heart is overwhelmed: lead me to the rock that is higher than I.
# Psalms 61:3 For thou hast been a shelter for me, and a strong tower from the enemy.
# Psalms 61:4 I will abide in thy tabernacle for ever: I will trust in the covert of thy wings. Selah.
# Psalms 61:5 For thou, O God, hast heard my vows: thou hast given me the heritage of those that fear thy name.
# Psalms 61:6 Thou wilt prolong the king's life: and his years as many generations.
# Psalms 61:7 He shall abide before God for ever: O prepare mercy and truth, which may preserve him.
# Psalms 61:8 So will I sing praise unto thy name for ever, that I may daily perform my vows.
# >>> p(b.Ps[62:])
# Psalms 62:1 Truly my soul waiteth upon God: from him cometh my salvation.
# Psalms 62:2 He only is my rock and my salvation; he is my defence; I shall not be greatly moved.
# Psalms 62:3 How long will ye imagine mischief against a man? ye shall be slain all of you: as a bowing wall shall ye be, and as a tottering fence.
# Psalms 62:4 They only consult to cast him down from his excellency: they delight in lies: they bless with their mouth, but they curse inwardly.  Selah.
# Psalms 62:5 My soul, wait thou only upon God; for my expectation is from him.
# Psalms 62:6 He only is my rock and my salvation: he is my defence; I shall not be moved.
# Psalms 62:7 In God is my salvation and my glory: the rock of my strength, and my refuge, is in God.
# Psalms 62:8 Trust in him at all times; ye people, pour out your heart before him: God is a refuge for us. Selah.
# Psalms 62:9 Surely men of low degree are vanity, and men of high degree are a lie: to be laid in the balance, they are altogether lighter than vanity.
# Psalms 62:10 Trust not in oppression, and become not vain in robbery: if riches increase, set not your heart upon them.
# Psalms 62:11 God hath spoken once; twice have I heard this; that power belongeth unto God.
# Psalms 62:12 Also unto thee, O Lord, belongeth mercy: for thou renderest to every man according to his work.
# >>> b.chapters()[930//2-1]
# 25 verses, Job 29:1...Job 29:25
# >>> Sel(b.doc,[31013-1])
# 1 verses, Revelation 18:19
# >>> p(_)
# Revelation 18:19 And they cast dust on their heads, and cried, weeping and wailing, saying, Alas, alas that great city, wherein were made rich all that had ships in the sea by reason of her costliness!  for in one hour is she made desolate.
# >>> 31102-31013
# 89
# >>> 31513-31102
# 411
# >>> 31102+314
# 31416
# >>> Sel(b.doc,[5000+50+10-1])
# 1 verses, Deuteronomy 5:6
# >>> b.Deu[5:]
# 33 verses, Deuteronomy 5:1...Deuteronomy 5:33
# >>> 33-5
# 28
# >>> 28-16
# 12
# >>> b.chapters()[400]
# 33 verses, 2 Chronicles 34:1...2 Chronicles 34:33
# >>> Sel(b.doc,range(23145,31102))
# 7957 verses, Matthew 1:1...Revelation 22:21
# >>> 929+260
# 1189
# >>> factors(1611)
# [3, 3, 179]
# >>> factors(1610)
# [2, 5, 7, 23]
# >>> 70*23
# 1610
# >>> 
# >>> 
