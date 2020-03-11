from parle import *
pistr=File('pi-digits').text.replace('\n','')
pi100="3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067"

# >>> from math import *
# >>> from bible import *
# >>> from pi import *
# >>> pi
# 3.141592653589793
# >>> 31102/66/150
# 3.1416161616161618
# >>> _-pi
# 2.3508026368634916e-05
# >>> 789629/251346.71711742
# 3.141592653589799
# >>> b.chapters()[628]
# Proverbs 1:1-33 (33 verses)
# >>> len("1415926535897932384626433832795")
# 31
# >>> dep=list(map(int,'1415926535897932384626433832795'))
# >>> 137*2
# 274
# >>> base(12,411)
# [2, 10, 3]
# >>> bases(411)
# 2 [1, 1, 0, 0, 1, 1, 0, 1, 1]
# 3 [1, 2, 0, 0, 2, 0]
# 4 [1, 2, 1, 2, 3]
# 5 [3, 1, 2, 1]
# 6 [1, 5, 2, 3]
# 7 [1, 1, 2, 5]
# 8 [6, 3, 3]
# 9 [5, 0, 6]
# 10 [4, 1, 1]
# 11 [3, 4, 4]
# 12 [2, 10, 3]
# 13 [2, 5, 8]
# 14 [2, 1, 5]
# 15 [1, 12, 6]
# 16 [1, 9, 11]
# 17 [1, 7, 3]
# 18 [1, 4, 15]
# 19 [1, 2, 12]
# 20 [1, 0, 11]
# 21 [19, 12]
# 22 [18, 15]
# 23 [17, 20]
# 24 [17, 3]
# 25 [16, 11]
# 26 [15, 21]
# 27 [15, 6]
# 28 [14, 19]
# 29 [14, 5]
# 30 [13, 21]
# 31 [13, 8]
# 32 [12, 27]
# 33 [12, 15]
# 34 [12, 3]
# 35 [11, 26]
# 36 [11, 15]
# 37 [11, 4]
# 38 [10, 31]
# 39 [10, 21]
# 40 [10, 11]
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> p(_)
# [2, 10, 3]
# >>> 2433-33*8
# 2169
# >>> b.Proverbs[1:].wc()
# 519
# >>> b.Pro.wc()
# 15038
# >>> b.Pro
# Proverbs 1:1-31:31 (915 verses)
# >>> b.Gen.wc()
# 38264
# >>> b.Gen[1:].wc()
# 797
# >>> b.Gen
# Genesis 1:1-50:26 (1533 verses)
# >>> 797*2-66
# 1528
# >>> base(12, 1533)
# [10, 7, 9]
# >>> base(12, 1534)
# [10, 7, 10]
# >>> 
# >>> 
# >>> 
# >>> 19/c
# 6.337717808764889e-08
# >>> 7*17
# 119
# >>> 77*17
# 1309
# >>> factors(178)
# [2, 89]
# >>> 1189*2
# 2378
# >>> 39*2
# 78
# >>> 
# >>> c/19
# 15778550.421052631
# >>> 311/99
# 3.1414141414141414
# >>> 22/7
# 3.142857142857143
# >>> 
# >>> Genesis[1:1]-(2,3)
# Genesis 1:1-2:3 (34 verses)
# >>> _.wc()
# 864
# >>> Genesis[1].wc()
# 797
# >>> 
# >>> pistr[:1000].split('3')
# ['', '14159265', '58979', '2', '846264', '', '8', '279502884197169', '99', '75105820974944592', '078164062862089986280', '4825', '4211706798214808651', '282', '0664709', '8446095505822', '1725', '594081284811174502841027019', '85211055596446229489549', '0', '819644288109756659', '', '4461284756482', '', '78678', '16527120190914564856692', '460', '48610454', '2664821', '', '9', '60726024914127', '724587006606', '15588174881520920962829254091715', '64', '67892590', '60011', '', '05', '0548820466521', '841469519415116094', '', '057270', '6575959195', '092186117', '819', '261179', '105118548074462', '79962749567', '518857527248912279', '818', '0119491298', '', '67', '', '6244065664', '086021', '94946', '952247', '719070217986094', '7027705', '921717629', '176752', '846748184676694051', '200056812714526', '560827785771', '4275778960917', '6', '717872146844090122495', '4', '0146549585', '7105079227968925892', '5420199561121290219608640', '441815981', '629774771', '09960518707211', '49999998', '729780499510597', '17', '2816096', '18595024459455', '46908', '02642522', '0825', '', '446850', '52619', '118817101000', '1', '78', '87528865875', '', '208', '81420617177669147', '0', '59825', '4904287554687', '115956286', '882', '5', '78759', '7519577818577805', '217122680661', '001927876611195909216420198']
# >>> from table import *
# >>> Row(_)
# Row(['', '14159265', '58979', '2', '846264', '', '8', '279502884197169', '99', '75105820974944592', '078164062862089986280', '4825', '4211706798214808651', '282', '0664709', '8446095505822', '1725', '594081284811174502841027019', '85211055596446229489549', '0', '819644288109756659', '', '4461284756482', '', '78678', '16527120190914564856692', '460', '48610454', '2664821', '', '9', '60726024914127', '724587006606', '15588174881520920962829254091715', '64', '67892590', '60011', '', '05', '0548820466521', '841469519415116094', '', '057270', '6575959195', '092186117', '819', '261179', '105118548074462', '79962749567', '518857527248912279', '818', '0119491298', '', '67', '', '6244065664', '086021', '94946', '952247', '719070217986094', '7027705', '921717629', '176752', '846748184676694051', '200056812714526', '560827785771', '4275778960917', '6', '717872146844090122495', '4', '0146549585', '7105079227968925892', '5420199561121290219608640', '441815981', '629774771', '09960518707211', '49999998', '729780499510597', '17', '2816096', '18595024459455', '46908', '02642522', '0825', '', '446850', '52619', '118817101000', '1', '78', '87528865875', '', '208', '81420617177669147', '0', '59825', '4904287554687', '115956286', '882', '5', '78759', '7519577818577805', '217122680661', '001927876611195909216420198'])
# >>> _@len
# Row([0, 8, 5, 1, 6, 0, 1, 15, 2, 17, 21, 4, 19, 3, 7, 13, 4, 27, 23, 1, 18, 0, 13, 0, 5, 23, 3, 8, 7, 0, 1, 14, 12, 32, 2, 8, 5, 0, 2, 13, 18, 0, 6, 10, 9, 3, 6, 15, 11, 18, 3, 10, 0, 2, 0, 10, 6, 5, 6, 15, 7, 9, 6, 18, 15, 12, 13, 1, 21, 1, 10, 19, 25, 9, 9, 14, 8, 15, 2, 7, 14, 5, 8, 4, 0, 6, 5, 12, 1, 2, 11, 0, 3, 17, 1, 5, 13, 9, 3, 1, 5, 16, 12, 27])
# >>> from func import *
# >>> def add1(x,y): return x+y+1
# ... 
# >>> add1//_
# Row([0, 9, 15, 17, 24, 25, 27, 43, 46, 64, 86, 91, 111, 115, 123, 137, 142, 170, 194, 196, 215, 216, 230, 231, 237, 261, 265, 274, 282, 283, 285, 300, 313, 346, 349, 358, 364, 365, 368, 382, 401, 402, 409, 420, 430, 434, 441, 457, 469, 488, 492, 503, 504, 507, 508, 519, 526, 532, 539, 555, 563, 573, 580, 599, 615, 628, 642, 644, 666, 668, 679, 699, 725, 735, 745, 760, 769, 785, 788, 796, 811, 817, 826, 831, 832, 839, 845, 858, 860, 863, 875, 876, 880, 898, 900, 906, 920, 930, 934, 936, 942, 959, 972, 1000])
# >>> 
# >>> pistr[:100]
# '3141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067'
# >>> tell('King')
# K  i n  g
# 11+9+14+7=41
# >>> b[59]
# James 1:1-5:20 (108 verses)
# >>> tell('6and1')
# 6 a n  d 1
# 6+1+14+4+1=26
# >>> tell('of')
# o  f
# 15+6=21
# >>> tell('Scotland')
# S  c o  t  l  a n  d
# 19+3+15+20+12+1+14+4=88
# >>> tell('the holy bible')
# the holy bible
#  33+ 60 +  30 =123
# >>> b.chapter(535)
# Psalms 57:1-11 (11 verses)
# >>> p(_)
# Psalms 57
# 1 Be merciful unto me, O God, be merciful unto me: for my soul trusteth in thee: yea, in the shadow of thy wings will I make my refuge, until these calamities be overpast.
# 2 I will cry unto God most high; unto God that performeth all things for me.
# 3 He shall send from heaven, and save me from the reproach of him that would swallow me up. Selah. God shall send forth his mercy and his truth.
# 4 My soul is among lions: and I lie even among them that are set on fire, even the sons of men, whose teeth are spears and arrows, and their tongue a sharp sword.
# 5 Be thou exalted, O God, above the heavens; let thy glory be above all the earth.
# 6 They have prepared a net for my steps; my soul is bowed down: they have digged a pit before me, into the midst whereof they are fallen themselves. Selah.
# 7 My heart is fixed, O God, my heart is fixed: I will sing and give praise.
# 8 Awake up, my glory; awake, psaltery and harp: I myself will awake early.
# 9 I will praise thee, O Lord, among the people: I will sing unto thee among the nations.
# 10 For thy mercy is great unto the heavens, and thy truth unto the clouds.
# 11 Be thou exalted, O God, above the heavens: let thy glory be above all the earth.
# >>> pf(535)
# Counter({5: 1, 107: 1})
# >>> tell('Jacob')
# J  a c o  b
# 10+1+3+15+2=31
# >>> Row['Scotland','and','England']@sums
# Row([(88, 448), (19, 55), (57, 147)])
# >>> sums('TRUE')
# (64, 595)
# >>> middle(span(1189))
# range(595, 596)
# >>> sums('Truth')
# (87, 798)
# >>> b/'is true'
# Ruth 3:12;1 Kings 22:16;Psalms 119:160;Daniel 6:12;8:26;John 3:33;5:32;7:18,28;8:14,16-17,26;19:35;21:24;2 Corinthians 1:18;Titus 1:13;1 John 2:8;5:20;3 John 1:12;Revelation 3:7 (21 verses)
# >>> p(_)
# Ruth 3:12 And now it is true that I am thy near kinsman: howbeit there is a kinsman nearer than I.
# 1 Kings 22:16 And the king said unto him, How many times shall I adjure thee that thou tell me nothing but that which is true in the name of the LORD?
# Psalms 119:160 Thy word is true from the beginning: and every one of thy righteous judgments endureth for ever.
# Daniel 6:12 Then they came near, and spake before the king concerning the king's decree; Hast thou not signed a decree, that every man that shall ask a petition of any God or man within thirty days, save of thee, O king, shall be cast into the den of lions? The king answered and said, The thing is true, according to the law of the Medes and Persians, which altereth not.
# Daniel 8:26 And the vision of the evening and the morning which was told is true: wherefore shut thou up the vision; for it shall be for many days.
# John 3:33 He that hath received his testimony hath set to his seal that God is true.
# John 5:32 There is another that beareth witness of me; and I know that the witness which he witnesseth of me is true.
# John 7:18 He that speaketh of himself seeketh his own glory: but he that seeketh his glory that sent him, the same is true, and no unrighteousness is in him.
# John 7:28 Then cried Jesus in the temple as he taught, saying, Ye both know me, and ye know whence I am: and I am not come of myself, but he that sent me is true, whom ye know not.
# John 8
# 14 Jesus answered and said unto them, Though I bear record of myself, yet my record is true: for I know whence I came, and whither I go; but ye cannot tell whence I come, and whither I go.
# 16 And yet if I judge, my judgment is true: for I am not alone, but I and the Father that sent me.
# 17 It is also written in your law, that the testimony of two men is true.
# 26 I have many things to say and to judge of you: but he that sent me is true; and I speak to the world those things which I have heard of him.
# John 19:35 And he that saw it bare record, and his record is true: and he knoweth that he saith true, that ye might believe.
# John 21:24 This is the disciple which testifieth of these things, and wrote these things: and we know that his testimony is true.
# 2 Corinthians 1:18 But as God is true, our word toward you was not yea and nay.
# Titus 1:13 This witness is true. Wherefore rebuke them sharply, that they may be sound in the faith;
# 1 John 2:8 Again, a new commandment I write unto you, which thing is true in him and in you: because the darkness is past, and the true light now shineth.
# 1 John 5:20 And we know that the Son of God is come, and hath given us an understanding, that we may know him that is true, and we are in him that is true, even in his Son Jesus Christ. This is the true God, and eternal life.
# 3 John 1:12 Demetrius hath good report of all men, and of the truth itself: yea, and we also bear record; and ye know that our record is true.
# Revelation 3:7 And to the angel of the church in Philadelphia write; These things saith he that is holy, he that is true, he that hath the key of David, he that openeth, and no man shutteth; and shutteth, and no man openeth;
# >>> Psalm[119:160].vn()
# 16059
# >>> b.vi(2**14)
# Psalms 148:12 Both young men, and maidens; old men, and children:
# >>> _.tell()
# Both young men, and maidens; old men, and children:
#  45 +  82 + 32 + 19+   65   + 31+ 32 + 19+    73   =398
# >>> tell('love')
# l  o  v  e
# 12+15+22+5=54
# >>> tell('the stars')
# the stars
#  33+  77 =110
# >>> 
# >>> 
# >>> 
# >>> 29*2
# 58
# >>> exp(pi)
# 23.140692632779267
# >>> from decimal import Decimal
# >>> 
# >>> epi=Decimal('23.140692632779269005729086367948547380266106242600211993445046409524342350690')
# >>> pid=Decimal(pi100)
# >>> print(epi); print('',pid)
# 23.140692632779269005729086367948547380266106242600211993445046409524342350690
#  3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067
# >>> print(epi-20)
# 3.140692632779269005729086368
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 0o66
# 54
# >>> 
