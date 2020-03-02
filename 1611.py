# >>> from bible import *
# >>> bible.midverse()
# Psalms 103:1 Bless the LORD, O my soul: and all that is within me, bless his holy name.
# Psalms 103:2 Bless the LORD, O my soul, and forget not all his benefits:
# >>> Psalms.verse(1611)
# Psalms 103:1 Bless the LORD, O my soul: and all that is within me, bless his holy name.
# >>> Genesis-Job
# Genesis 1:1-Job 42:17 (13940 verses)
# >>> 31102//2
# 15551
# >>> 15551-13940
# 1611
# >>> Psalms.verse(1611)
# Psalms 103:1 Bless the LORD, O my soul: and all that is within me, bless his holy name.
# >>> pf(1611)
# Counter({3: 2, 179: 1})
# >>> pf(1610)
# Counter({2: 1, 5: 1, 7: 1, 23: 1})
# >>> pf(1612)
# Counter({2: 2, 13: 1, 31: 1})
# >>> 4*13*31
# 1612
# >>> 26*62
# 1612
# >>> np(179)
# 41
# >>> 60+77
# 137
# >>> bible[16:11]
# Genesis 16:11;Exodus 16:11;Leviticus 16:11;Numbers 16:11;Deuteronomy 16:11;Judges 16:11;1 Samuel 16:11;2 Samuel 16:11;1 Kings 16:11;2 Kings 16:11;1 Chronicles 16:11;2 Chronicles 16:11;Job 16:11;Psalms 16:11;Proverbs 16:11;Isaiah 16:11;Jeremiah 16:11;Ezekiel 16:11;Matthew 16:11;Mark 16:11;Luke 16:11;John 16:11;Acts 16:11;Romans 16:11;1 Corinthians 16:11;Revelation 16:11 (26 verses)
# >>> p(_)
# Genesis 16:11 And the angel of the LORD said unto her, Behold, thou art with child and shalt bear a son, and shalt call his name Ishmael; because the LORD hath heard thy affliction.
# Exodus 16:11 And the LORD spake unto Moses, saying,
# Leviticus 16:11 And Aaron shall bring the bullock of the sin offering, which is for himself, and shall make an atonement for himself, and for his house, and shall kill the bullock of the sin offering which is for himself:
# Numbers 16:11 For which cause both thou and all thy company are gathered together against the LORD: and what is Aaron, that ye murmur against him?
# Deuteronomy 16:11 And thou shalt rejoice before the LORD thy God, thou, and thy son, and thy daughter, and thy manservant, and thy maidservant, and the Levite that is within thy gates, and the stranger, and the fatherless, and the widow, that are among you, in the place which the LORD thy God hath chosen to place his name there.
# Judges 16:11 And he said unto her, If they bind me fast with new ropes that never were occupied, then shall I be weak, and be as another man.
# 1 Samuel 16:11 And Samuel said unto Jesse, Are here all thy children? And he said, There remaineth yet the youngest, and, behold, he keepeth the sheep. And Samuel said unto Jesse, Send and fetch him: for we will not sit down till he come hither.
# 2 Samuel 16:11 And David said to Abishai, and to all his servants, Behold, my son, which came forth of my bowels, seeketh my life: how much more now may this Benjamite do it? let him alone, and let him curse; for the LORD hath bidden him.
# 1 Kings 16:11 And it came to pass, when he began to reign, as soon as he sat on his throne, that he slew all the house of Baasha: he left him not one that pisseth against a wall, neither of his kinsfolks, nor of his friends.
# 2 Kings 16:11 And Urijah the priest built an altar according to all that king Ahaz had sent from Damascus: so Urijah the priest made it against king Ahaz came from Damascus.
# 1 Chronicles 16:11 Seek the LORD and his strength, seek his face continually.
# 2 Chronicles 16:11 And, behold, the acts of Asa, first and last, lo, they are written in the book of the kings of Judah and Israel.
# Job 16:11 God hath delivered me to the ungodly, and turned me over into the hands of the wicked.
# Psalms 16:11 Thou wilt shew me the path of life: in thy presence is fulness of joy; at thy right hand there are pleasures for evermore.
# Proverbs 16:11 A just weight and balance are the LORD's: all the weights of the bag are his work.
# Isaiah 16:11 Wherefore my bowels shall sound like an harp for Moab, and mine inward parts for Kirharesh.
# Jeremiah 16:11 Then shalt thou say unto them, Because your fathers have forsaken me, saith the LORD, and have walked after other gods, and have served them, and have worshipped them, and have forsaken me, and have not kept my law;
# Ezekiel 16:11 I decked thee also with ornaments, and I put bracelets upon thy hands, and a chain on thy neck.
# Matthew 16:11 How is it that ye do not understand that I spake it not to you concerning bread, that ye should beware of the leaven of the Pharisees and of the Sadducees?
# Mark 16:11 And they, when they had heard that he was alive, and had been seen of her, believed not.
# Luke 16:11 If therefore ye have not been faithful in the unrighteous mammon, who will commit to your trust the true riches?
# John 16:11 Of judgment, because the prince of this world is judged.
# Acts 16:11 Therefore loosing from Troas, we came with a straight course to Samothracia, and the next day to Neapolis;
# Romans 16:11 Salute Herodion my kinsman. Greet them that be of the household of Narcissus, which are in the Lord.
# 1 Corinthians 16:11 Let no man therefore despise him: but conduct him forth in peace, that he may come unto me: for I look for him with the brethren.
# Revelation 16:11 And blasphemed the God of heaven because of their pains and their sores, and repented not of their deeds.
# >>> p(_.wc())
# 671
# >>> [v-b[b.verse(v).bookn()][1:1].vn()+1 for v in _.vns()]
# [393, 426, 467, 601, 461, 451, 394, 415, 577, 441, 579, 326, 380, 164, 451, 326, 401, 309, 539, 669, 738, 693, 571, 417, 424, 268]
# >>> p(len(_),sum(_))
# 26 11881
# >>> pf(11881)
# Counter({109: 2})
# >>> (Matthew-Revelation)
# Matthew 1:1-Revelation 22:21 (7957 verses)
# >>> factors(7957)
# [73, 109]
# >>> np(109),np(73)
# (29, 21)
# >>> prime(prime(10))*prime(21)
# 7957
# >>> Genesis-Malachi
# Genesis 1:1-Malachi 4:6 (23145 verses)
# >>> pf(23145)
# Counter({3: 1, 5: 1, 1543: 1})
# >>> 15*1543
# 23145
# >>> 3*5*prime(3**5)
# 23145
# >>> 
# >>> pp(35)*2
# 31102
# >>> sof(pp(35)*2)
# 46656
# >>> 6**6
# 46656
# >>> pp(35)*3+1
# 46654
# >>> 2*73**2-73*37
# 7957
# >>> 
# >>> nt=Matthew-Revelation
# >>> nt.verse(5256)
# 1 Corinthians 2:6 Howbeit we speak wisdom among them that are perfect: yet not the wisdom of this world, nor of the princes of this world, that come to nought:
# >>> pf(243)
# Counter({3: 5})
# >>> 
# >>> pf(393)
# Counter({3: 1, 131: 1})
# >>> 
# >>> factors(1611)
# [3, 3, 179]
# >>> np(179)
# 41
# >>> factors(1604)
# [2, 2, 401]
# >>> 2*2*ssum('את')
# 1604
# >>> factors(1611)
# [3, 3, 179]
# >>> 
# >>> 5060/math.pi
# 1610.648024089981
# >>> 5060/1611
# 3.1409062693978895
# >>> b.vi(1611)
# Exodus 4:9 And it shall come to pass, if they will not believe also these two signs, neither hearken unto thy voice, that thou shalt take of the water of the river, and pour it upon the dry land: and the water which thou takest out of the river shall become blood upon the dry land.
# >>> 
# >>> 
# >>> 
# >>> Genesis[28:12].vn()
# 786
# >>> base(23,1611)
# [3, 1, 1]
# >>> base(19,1611)
# [4, 8, 15]
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
