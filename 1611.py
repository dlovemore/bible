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
# >>> Genesis.vi(797)
# Genesis 29:1 Then Jacob went on his journey, and came into the land of the people of the east.
# >>> 
# >>> base(23,1611)
# [3, 1, 1]
# >>> base(19,1611)
# [4, 8, 15]
# >>> 
# >>> 
# >>> p(b.vi(1611)-b.vi(1614))
# Exodus 4
# 9 And it shall come to pass, if they will not believe also these two signs, neither hearken unto thy voice, that thou shalt take of the water of the river, and pour it upon the dry land: and the water which thou takest out of the river shall become blood upon the dry land.
# 10 And Moses said unto the LORD, O my LORD, I am not eloquent, neither heretofore, nor since thou hast spoken unto thy servant: but I am slow of speech, and of a slow tongue.
# 11 And the LORD said unto him, Who hath made man's mouth? or who maketh the dumb, or deaf, or the seeing, or the blind? have not I the LORD?
# 12 Now therefore go, and I will be with thy mouth, and teach thee what thou shalt say.
# >>> 
# >>> 
# >>> # 1611 in pi
# >>> b.vi(17083)-b.vi(17086)
# Proverbs 24:3-6 (4 verses)
# >>> b.vi(17936)
# Isaiah 14:7 The whole earth is at rest, and is quiet: they break forth into singing.
# >>> 
# >>> p(Proverbs[24])
# Proverbs 24
# 1 Be not thou envious against evil men, neither desire to be with them.
# 2 For their heart studieth destruction, and their lips talk of mischief.
# 3 Through wisdom is an house builded; and by understanding it is established:
# 4 And by knowledge shall the chambers be filled with all precious and pleasant riches.
# 5 A wise man is strong; yea, a man of knowledge increaseth strength.
# 6 For by wise counsel thou shalt make thy war: and in multitude of counsellors there is safety.
# 7 Wisdom is too high for a fool: he openeth not his mouth in the gate.
# 8 He that deviseth to do evil shall be called a mischievous person.
# 9 The thought of foolishness is sin: and the scorner is an abomination to men.
# 10 If thou faint in the day of adversity, thy strength is small.
# 11 If thou forbear to deliver them that are drawn unto death, and those that are ready to be slain;
# 12 If thou sayest, Behold, we knew it not; doth not he that pondereth the heart consider it? and he that keepeth thy soul, doth not he know it? and shall not he render to every man according to his works?
# 13 My son, eat thou honey, because it is good; and the honeycomb, which is sweet to thy taste:
# 14 So shall the knowledge of wisdom be unto thy soul: when thou hast found it, then there shall be a reward, and thy expectation shall not be cut off.
# 15 Lay not wait, O wicked man, against the dwelling of the righteous; spoil not his resting place:
# 16 For a just man falleth seven times, and riseth up again: but the wicked shall fall into mischief.
# 17 Rejoice not when thine enemy falleth, and let not thine heart be glad when he stumbleth:
# 18 Lest the LORD see it, and it displease him, and he turn away his wrath from him.
# 19 Fret not thyself because of evil men, neither be thou envious at the wicked:
# 20 For there shall be no reward to the evil man; the candle of the wicked shall be put out.
# 21 My son, fear thou the LORD and the king: and meddle not with them that are given to change:
# 22 For their calamity shall rise suddenly; and who knoweth the ruin of them both?
# 23 These things also belong to the wise. It is not good to have respect of persons in judgment.
# 24 He that saith unto the wicked, Thou are righteous; him shall the people curse, nations shall abhor him:
# 25 But to them that rebuke him shall be delight, and a good blessing shall come upon them.
# 26 Every man shall kiss his lips that giveth a right answer.
# 27 Prepare thy work without, and make it fit for thyself in the field; and afterwards build thine house.
# 28 Be not a witness against thy neighbour without cause; and deceive not with thy lips.
# 29 Say not, I will do so to him as he hath done to me: I will render to the man according to his work.
# 30 I went by the field of the slothful, and by the vineyard of the man void of understanding;
# 31 And, lo, it was all grown over with thorns, and nettles had covered the face thereof, and the stone wall thereof was broken down.
# 32 Then I saw, and considered it well: I looked upon it, and received instruction.
# 33 Yet a little sleep, a little slumber, a little folding of the hands to sleep:
# 34 So shall thy poverty come as one that travelleth; and thy want as an armed man.
# >>> 
