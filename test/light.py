# >>> from bible import *
# >>> Genesis[1:3]
# Genesis 1:3 And God said, Let there be light: and there was light.
# >>> _.tell()
# And God said, Let there be light: and there was light.
#  19+ 26+  33 + 37+  56 +7 +  56  + 19+  56 + 43+  56  =408
# >>> _.tell()
# And God said, Let there be light: and there was light.
#  19+ 26+  33 + 37+  56 +7 +  56  + 19+  56 + 43+  56  =408
# >>> _.tell(ssum)
# And God said, Let there be light: and there was light.
#  55+ 71+ 114 +235+ 308 +7 + 254  + 55+ 308 +601+ 254  =2262
# >>> 
# >>> sums('there')
# (56, 308)
# >>> sums('be')
# (7, 7)
# >>> tell('let there be light: and there was light')
# let there be light: and there was light
#  37+  56 +7 +  56  + 19+  56 + 43+  56 =330
# >>> sums('let there be light')
# (156, 804)
# >>> sums('and there was light')
# (174, 1218)
# >>> Genesis[1:4]
# Genesis 1:4 And God saw the light, that it was good: and God divided the light from the darkness.
# >>> tell('the darkness')
# the darkness
#  33+   91   =124
# >>> tell('the darkness',ssum)
# the darkness
# 213+  370   =583
# >>> tell('the darkness',lsum)
# the darkness
#  3 +   8    =11
# >>> tell('the light')
# the light
#  33+  56 =89
# >>> fibonacci(11)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'fibonacci' is not defined
# >>> 11/89
# 0.12359550561797752
# >>> 89/124
# 0.717741935483871
# >>> factors(c)
# [2, 7, 73, 293339]
## >>> np(293339)
## 25488
# >>> 
# >>> c/1609.344*3600 # speed of light in mph
# 670616629.3843951
# >>> b.chapter(670)
# Ecclesiastes 11:1-10 (10 verses)
# >>> p(_)
# Ecclesiastes 11
# 1 Cast thy bread upon the waters: for thou shalt find it after many days.
# 2 Give a portion to seven, and also to eight; for thou knowest not what evil shall be upon the earth.
# 3 If the clouds be full of rain, they empty themselves upon the earth: and if the tree fall toward the south, or toward the north, in the place where the tree falleth, there it shall be.
# 4 He that observeth the wind shall not sow; and he that regardeth the clouds shall not reap.
# 5 As thou knowest not what is the way of the spirit, nor how the bones do grow in the womb of her that is with child: even so thou knowest not the works of God who maketh all.
# 6 In the morning sow thy seed, and in the evening withhold not thine hand: for thou knowest not whether shall prosper, either this or that, or whether they both shall be alike good.
# 7 Truly the light is sweet, and a pleasant thing it is for the eyes to behold the sun:
# 8 But if a man live many years, and rejoice in them all; yet let him remember the days of darkness; for they shall be many. All that cometh is vanity.
# 9 Rejoice, O young man, in thy youth; and let thy heart cheer thee in the days of thy youth, and walk in the ways of thine heart, and in the sight of thine eyes: but know thou, that for all these things God will bring thee into judgment.
# 10 Therefore remove sorrow from thy heart, and put away evil from thy flesh: for childhood and youth are vanity.
# >>> p(_.wcs())
# [14, 20, 36, 17, 38, 33, 18, 30, 48, 19]
# >>> p(tale(_.wcs()))
# [14, 34, 70, 87, 125, 158, 176, 206, 254, 273]
# >>> p(_.words()[160])
# light
# >>> Proverbs[1]
# Proverbs 1:1-33 (33 verses)
# >>> p(_.chn())
# 629
# >>> p(_)
# Proverbs 1
# 1 The proverbs of Solomon the son of David, king of Israel;
# 2 To know wisdom and instruction; to perceive the words of understanding;
# 3 To receive the instruction of wisdom, justice, and judgment, and equity;
# 4 To give subtilty to the simple, to the young man knowledge and discretion.
# 5 A wise man will hear, and will increase learning; and a man of understanding shall attain unto wise counsels:
# 6 To understand a proverb, and the interpretation; the words of the wise, and their dark sayings.
# 7 The fear of the LORD is the beginning of knowledge: but fools despise wisdom and instruction.
# 8 My son, hear the instruction of thy father, and forsake not the law of thy mother:
# 9 For they shall be an ornament of grace unto thy head, and chains about thy neck.
# 10 My son, if sinners entice thee, consent thou not.
# 11 If they say, Come with us, let us lay wait for blood, let us lurk privily for the innocent without cause:
# 12 Let us swallow them up alive as the grave; and whole, as those that go down into the pit:
# 13 We shall find all precious substance, we shall fill our houses with spoil:
# 14 Cast in thy lot among us; let us all have one purse:
# 15 My son, walk not thou in the way with them; refrain thy foot from their path:
# 16 For their feet run to evil, and make haste to shed blood.
# 17 Surely in vain the net is spread in the sight of any bird.
# 18 And they lay wait for their own blood; they lurk privily for their own lives.
# 19 So are the ways of every one that is greedy of gain; which taketh away the life of the owners thereof.
# 20 Wisdom crieth without; she uttereth her voice in the streets:
# 21 She crieth in the chief place of concourse, in the openings of the gates: in the city she uttereth her words, saying,
# 22 How long, ye simple ones, will ye love simplicity? and the scorners delight in their scorning, and fools hate knowledge?
# 23 Turn you at my reproof: behold, I will pour out my spirit unto you, I will make known my words unto you.
# 24 Because I have called, and ye refused; I have stretched out my hand, and no man regarded;
# 25 But ye have set at nought all my counsel, and would none of my reproof:
# 26 I also will laugh at your calamity; I will mock when your fear cometh;
# 27 When your fear cometh as desolation, and your destruction cometh as a whirlwind; when distress and anguish cometh upon you.
# 28 Then shall they call upon me, but I will not answer; they shall seek me early, but they shall not find me:
# 29 For that they hated knowledge, and did not choose the fear of the LORD:
# 30 They would none of my counsel: they despised all my reproof.
# 31 Therefore shall they eat of the fruit of their own way, and be filled with their own devices.
# 32 For the turning away of the simple shall slay them, and the prosperity of fools shall destroy them.
# 33 But whoso hearkeneth unto me shall dwell safely, and shall be quiet from fear of evil.
# >>> 
# >>> 
# >>> b.chapter(616)
# Psalms 138:1-8 (8 verses)
# >>> p(_)
# Psalms 138
# 1 I will praise thee with my whole heart: before the gods will I sing praise unto thee.
# 2 I will worship toward thy holy temple, and praise thy name for thy lovingkindness and for thy truth: for thou hast magnified thy word above all thy name.
# 3 In the day when I cried thou answeredst me, and strengthenedst me with strength in my soul.
# 4 All the kings of the earth shall praise thee, O LORD, when they hear the words of thy mouth.
# 5 Yea, they shall sing in the ways of the LORD: for great is the glory of the LORD.
# 6 Though the LORD be high, yet hath he respect unto the lowly: but the proud he knoweth afar off.
# 7 Though I walk in the midst of trouble, thou wilt revive me: thou shalt stretch forth thine hand against the wrath of mine enemies, and thy right hand shall save me.
# 8 The LORD will perfect that which concerneth me: thy mercy, O LORD, endureth for ever: forsake not the works of thine own hands.
# >>> b[61:6]
# Psalms 61:6 Thou wilt prolong the king's life: and his years as many generations.
# Isaiah 61:6 But ye shall be named the Priests of the LORD: men shall call you the Ministers of our God: ye shall eat the riches of the Gentiles, and in their glory shall ye boast yourselves.
# >>> b[6:16]
# Genesis 6:16;Exodus 6:16;Leviticus 6:16;Numbers 6:16;Deuteronomy 6:16;Joshua 6:16;Judges 6:16;1 Samuel 6:16;2 Samuel 6:16;1 Kings 6:16;2 Kings 6:16;1 Chronicles 6:16;2 Chronicles 6:16;Ezra 6:16;Nehemiah 6:16;Job 6:16;Proverbs 6:16;Jeremiah 6:16;Daniel 6:16;Micah 6:16;Matthew 6:16;Mark 6:16;Luke 6:16;John 6:16;Romans 6:16;1 Corinthians 6:16;2 Corinthians 6:16;Galatians 6:16;Ephesians 6:16;1 Timothy 6:16;Hebrews 6:16;Revelation 6:16 (32 verses)
# >>> p(_)
# Genesis 6:16 A window shalt thou make to the ark, and in a cubit shalt thou finish it above; and the door of the ark shalt thou set in the side thereof; with lower, second, and third stories shalt thou make it.
# Exodus 6:16 And these are the names of the sons of Levi according to their generations; Gershon, and Kohath, and Merari: and the years of the life of Levi were an hundred thirty and seven years.
# Leviticus 6:16 And the remainder thereof shall Aaron and his sons eat: with unleavened bread shall it be eaten in the holy place; in the court of the tabernacle of the congregation they shall eat it.
# Numbers 6:16 And the priest shall bring them before the LORD, and shall offer his sin offering, and his burnt offering:
# Deuteronomy 6:16 Ye shall not tempt the LORD your God, as ye tempted him in Massah.
# Joshua 6:16 And it came to pass at the seventh time, when the priests blew with the trumpets, Joshua said unto the people, Shout; for the LORD hath given you the city.
# Judges 6:16 And the LORD said unto him, Surely I will be with thee, and thou shalt smite the Midianites as one man.
# 1 Samuel 6:16 And when the five lords of the Philistines had seen it, they returned to Ekron the same day.
# 2 Samuel 6:16 And as the ark of the LORD came into the city of David, Michal Saul's daughter looked through a window, and saw king David leaping and dancing before the LORD; and she despised him in her heart.
# 1 Kings 6:16 And he built twenty cubits on the sides of the house, both the floor and the walls with boards of cedar: he even built them for it within, even for the oracle, even for the most holy place.
# 2 Kings 6:16 And he answered, Fear not: for they that be with us are more than they that be with them.
# 1 Chronicles 6:16 The sons of Levi; Gershom, Kohath, and Merari.
# 2 Chronicles 6:16 Now therefore, O LORD God of Israel, keep with thy servant David my father that which thou hast promised him, saying, There shall not fail thee a man in my sight to sit upon the throne of Israel; yet so that thy children take heed to their way to walk in my law, as thou hast walked before me.
# Ezra 6:16 And the children of Israel, the priests, and the Levites, and the rest of the children of the captivity, kept the dedication of this house of God with joy.
# Nehemiah 6:16 And it came to pass, that when all our enemies heard thereof, and all the heathen that were about us saw these things, they were much cast down in their own eyes: for they perceived that this work was wrought of our God.
# Job 6:16 Which are blackish by reason of the ice, and wherein the snow is hid:
# Proverbs 6:16 These six things doth the LORD hate: yea, seven are an abomination unto him:
# Jeremiah 6:16 Thus saith the LORD, Stand ye in the ways, and see, and ask for the old paths, where is the good way, and walk therein, and ye shall find rest for your souls. But they said, We will not walk therein.
# Daniel 6:16 Then the king commanded, and they brought Daniel, and cast him into the den of lions. Now the king spake and said unto Daniel, Thy God whom thou servest continually, he will deliver thee.
# Micah 6:16 For the statutes of Omri are kept, and all the works of the house of Ahab, and ye walk in their counsels; that I should make thee a desolation, and the inhabitants thereof an hissing: therefore ye shall bear the reproach of my people.
# Matthew 6:16 Moreover when ye fast, be not, as the hypocrites, of a sad countenance: for they disfigure their faces, that they may appear unto men to fast. Verily I say unto you, They have their reward.
# Mark 6:16 But when Herod heard thereof, he said, It is John, whom I beheaded: he is risen from the dead.
# Luke 6:16 And Judas the brother of James, and Judas Iscariot, which also was the traitor.
# John 6:16 And when even was now come, his disciples went down unto the sea,
# Romans 6:16 Know ye not, that to whom ye yield yourselves servants to obey, his servants ye are to whom ye obey; whether of sin unto death, or of obedience unto righteousness?
# 1 Corinthians 6:16 What? know ye not that he which is joined to an harlot is one body? for two, saith he, shall be one flesh.
# 2 Corinthians 6:16 And what agreement hath the temple of God with idols? for ye are the temple of the living God; as God hath said, I will dwell in them, and walk in them; and I will be their God, and they shall be my people.
# Galatians 6:16 And as many as walk according to this rule, peace be on them, and mercy, and upon the Israel of God.
# Ephesians 6:16 Above all, taking the shield of faith, wherewith ye shall be able to quench all the fiery darts of the wicked.
# 1 Timothy 6:16 Who only hath immortality, dwelling in the light which no man can approach unto; whom no man hath seen, nor can see: to whom be honour and power everlasting. Amen.
# Hebrews 6:16 For men verily swear by the greater: and an oath for confirmation is to them an end of all strife.
# Revelation 6:16 And said to the mountains and rocks, Fall on us, and hide us from the face of him that sitteth on the throne, and from the wrath of the Lamb:
# >>> 
# >>> b.verse(29979)
# Hebrews 2:1 Therefore we ought to give the more earnest heed to the things which we have heard, lest at any time we should let them slip.
# >>> _.tell(lsum)
# Therefore we ought to give the more earnest heed to the things which we have heard, lest at any time we should let them slip.
#     9    +2 +  5  +2 + 4  + 3 + 4  +   7   + 4  +2 + 3 +  6   +  5  +2 + 4  +  5   + 4  +2 + 3 + 4  +2 +  6   + 3 + 4  +  4  =99
# >>> _.tell()
# Therefore we ought to give the more earnest heed to the things which we have heard, lest at any time we should let them slip.
#    100   +28+  71 +35+ 43 + 33+ 51 +   82  + 22 +35+ 33+  77  +  51 +28+ 36 +  36  + 56 +21+ 40+ 47 +28+  79  + 37+ 46 +  56 =1171
# >>> 
# >>> 
# >>> 
# >>> b/'divid'/'from'
# Genesis 1:4,6-7,14,18;Leviticus 5:8;Numbers 31:42;Joshua 13:6;23:4;Isaiah 34:17;Micah 2:4;Matthew 25:32;Luke 11:22;12:52 (14 verses)
# >>> p(_)
# Genesis 1
# 4 And God saw the light, that it was good: and God divided the light from the darkness.
# 6 And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters.
# 7 And God made the firmament, and divided the waters which were under the firmament from the waters which were above the firmament: and it was so.
# 14 And God said, Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days, and years:
# 18 And to rule over the day and over the night, and to divide the light from the darkness: and God saw that it was good.
# Leviticus 5:8 And he shall bring them unto the priest, who shall offer that which is for the sin offering first, and wring off his head from his neck, but shall not divide it asunder:
# Numbers 31:42 And of the children of Israel's half, which Moses divided from the men that warred,
# Joshua 13:6 All the inhabitants of the hill country from Lebanon unto Misrephothmaim, and all the Sidonians, them will I drive out from before the children of Israel: only divide thou it by lot unto the Israelites for an inheritance, as I have commanded thee.
# Joshua 23:4 Behold, I have divided unto you by lot these nations that remain, to be an inheritance for your tribes, from Jordan, with all the nations that I have cut off, even unto the great sea westward.
# Isaiah 34:17 And he hath cast the lot for them, and his hand hath divided it unto them by line: they shall possess it for ever, from generation to generation shall they dwell therein.
# Micah 2:4 In that day shall one take up a parable against you, and lament with a doleful lamentation, and say, We be utterly spoiled: he hath changed the portion of my people: how hath he removed it from me! turning away he hath divided our fields.
# Matthew 25:32 And before him shall be gathered all nations: and he shall separate them one from another, as a shepherd divideth his sheep from the goats:
# Luke 11:22 But when a stronger than he shall come upon him, and overcome him, he taketh from him all his armour wherein he trusted, and divideth his spoils.
# Luke 12:52 For from henceforth there shall be five in one house divided, three against two, and two against three.
# >>> tell('the waters')
# the waters
#  33+  86  =119
# >>> tell('the waters which were under the firmament')
# the waters which were under the firmament
#  33+  86  +  51 + 51 +  62 + 33+    99   =415
# >>> tell('the waters which were above the firmament')
# the waters which were above the firmament
#  33+  86  +  51 + 51 +  45 + 33+    99   =398
# >>> 62+33+99
# 194
# >>> 45+33+99
# 177
# >>> tell('the day'),tell('the night')
# the day
#  33+ 30=63
# the night
#  33+  58 =91
# (None, None)
# >>> 91/63
# 1.4444444444444444
# >>> b/'one house divided'
# Luke 12:52 For from henceforth there shall be five in one house divided, three against two, and two against three.
# >>> _.tell()
# For from henceforth there shall be five in one house divided, three against two, and two against three.
#  39+ 52 +   102    +  56 +  52 +7 + 42 +23+ 34+  68 +   57   +  56 +   71  + 58 + 19+ 58+   71  +  56  =921
# >>> 
# >>> tell('one house')
# one house
#  34+  68 =102
# >>> osum('one')*3
# 102
# >>> h1=Genesis-Psalm[102]
# >>> h2=Psalm[103]-Revelation
# >>> h1
# Genesis 1:1-Psalms 102:28 (15550 verses)
# >>> h2
# Psalms 103:1-Revelation 22:21 (15552 verses)
# >>> 
# >>> 15550//5
# 3110
# >>> list(range(3110,15551,3110))
# [3110, 6220, 9330, 12440, 15550]
# >>> sum([b.verse(i,i+1) for i in range(3110,15551,3110)],b.verse(0))
# Leviticus 13:57-58;Joshua 15:17-18;1 Kings 17:12-13;Nehemiah 7:19-20;Psalms 102:28-103:1 (10 verses)
# >>> p(_)
# Leviticus 13:57 And if it appear still in the garment, either in the warp, or in the woof, or in any thing of skin; it is a spreading plague: thou shalt burn that wherein the plague is with fire.
# Leviticus 13:58 And the garment, either warp, or woof, or whatsoever thing of skin it be, which thou shalt wash, if the plague be departed from them, then it shall be washed the second time, and shall be clean.
# Joshua 15:17 And Othniel the son of Kenaz, the brother of Caleb, took it: and he gave him Achsah his daughter to wife.
# Joshua 15:18 And it came to pass, as she came unto him, that she moved him to ask of her father a field: and she lighted off her ass; and Caleb said unto her, What wouldest thou?
# 1 Kings 17:12 And she said, As the LORD thy God liveth, I have not a cake, but an handful of meal in a barrel, and a little oil in a cruse: and, behold, I am gathering two sticks, that I may go in and dress it for me and my son, that we may eat it, and die.
# 1 Kings 17:13 And Elijah said unto her, Fear not; go and do as thou hast said: but make me thereof a little cake first, and bring it unto me, and after make for thee and for thy son.
# Nehemiah 7:19 The children of Bigvai, two thousand threescore and seven.
# Nehemiah 7:20 The children of Adin, six hundred fifty and five.
# Psalms 102:28 The children of thy servants shall continue, and their seed shall be established before thee.
# Psalms 103:1 Bless the LORD, O my soul: and all that is within me, bless his holy name.
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
# >>> 
# >>> tell('the light',ssum)
# the light
# 213+ 254 =467
# >>> 124/89
# 1.3932584269662922
# >>> 583/467
# 1.2483940042826553
# >>> 89+124
# 213
# >>> 89/213
# 0.41784037558685444
# >>> 
# >>> factors(c)
# [2, 7, 73, 293339]
# >>> 2*93339
# 186678
# >>> 
# >>> 14*73
# 1022
# >>> tell('thy seed',osum,ssum)
# thy seed
#  53+ 33 = 86
# 908+114 =1022
# >>> 
# >>> 
# >>> b.verse(260)
# Genesis 10:25 And unto Eber were born two sons: the name of one was Peleg; for in his days was the earth divided; and his brother's name was Joktan.
# >>> _.tell()
# And unto Eber were born two sons: the name of one was Peleg; for in his days was the earth divided; and his brother's name was Joktan.
#  19+ 70 + 30 + 51 + 49 + 58+  67 + 33+ 33 +21+ 34+ 43+  45  + 39+23+ 36+ 49 + 43+ 33+  52 +   57   + 19+ 36+   105   + 33 + 43+   71  =1192
# >>> _.tell(ssum)
# And unto Eber were born two sons: the name of one was Peleg; for in his days was the earth divided; and his brother's name was Joktan.
#  55+610 +102 +600 +202 +760+ 310 +213+ 96 +66+115+601+ 117  +156+59+117+805 +601+213+ 304 +  435   + 55+117+   555   + 96 +601+  341  =8302
# >>> factors(341)
# [11, 31]
# >>> 156+59+117+805+osum('earth')
# 1189
# >>> sums('יקטן')
# (52, 169)
# >>> sums('פלג')
# (32, 113)
# >>> 1189+3
# 1192
# >>> 
# >>> 
# >>> 
# >>> 
# >>> [ssum(Genesis[i].vs()) for i in range(1,51)]
# [233444, 166189, 209174, 173208, 158192, 173189, 188891, 189681, 207558, 130200, 184724, 163950, 136320, 170483, 140333, 114566, 205377, 264844, 361060, 151405, 216769, 167934, 163084, 542106, 193141, 266532, 376356, 167366, 233719, 289488, 456084, 245532, 141531, 266089, 183513, 222749, 271531, 231573, 182808, 167399, 406039, 330002, 323213, 306278, 241873, 215724, 304768, 179859, 239913, 225793]
# >>> [factors(x) for x in _]
# [[2, 2, 17, 3433], [166189], [2, 7, 67, 223], [2, 2, 2, 3, 7, 1031], [2, 2, 2, 2, 9887], [173189], [188891], [3, 23, 2749], [2, 3, 3, 13, 887], [2, 2, 2, 3, 5, 5, 7, 31], [2, 2, 46181], [2, 3, 5, 5, 1093], [2, 2, 2, 2, 2, 2, 2, 3, 5, 71], [170483], [140333], [2, 57283], [3, 17, 4027], [2, 2, 73, 907], [2, 2, 5, 7, 2579], [5, 107, 283], [7, 173, 179], [2, 3, 13, 2153], [2, 2, 40771], [2, 3, 3, 3, 10039], [13, 83, 179], [2, 2, 3, 7, 19, 167], [2, 2, 3, 79, 397], [2, 67, 1249], [19, 12301], [2, 2, 2, 2, 3, 37, 163], [2, 2, 3, 3, 3, 41, 103], [2, 2, 3, 7, 37, 79], [3, 13, 19, 191], [266089], [3, 11, 67, 83], [29, 7681], [13, 20887], [3, 77191], [2, 2, 2, 3, 3, 2539], [17, 43, 229], [151, 2689], [2, 165001], [11, 29383], [2, 7, 131, 167], [241873], [2, 2, 3, 17977], [2, 2, 2, 2, 2, 2, 2, 2381], [3, 167, 359], [3, 3, 19, 23, 61], [43, 59, 89]]
# >>> 225793
# 225793
# >>> _-19,_+19
# (225774, 225812)
# >>> factors(225774)
# [2, 3, 3, 3, 37, 113]
# >>> 
# >>> tell('Pauli exclusion principle')
# Pauli exclusion principle
#   59 +   122   +   102   =283
# >>> tell('Wolfgang Ernst Pauli')
# Wolfgang Ernst Pauli
#    85   +  76 +  59 =220
# >>> for x in b/'firmament': p(x)
# ... 
# Genesis 1:6 And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters.
# Genesis 1:7 And God made the firmament, and divided the waters which were under the firmament from the waters which were above the firmament: and it was so.
# Genesis 1:8 And God called the firmament Heaven. And the evening and the morning were the second day.
# Genesis 1:14 And God said, Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days, and years:
# Genesis 1:15 And let them be for lights in the firmament of the heaven to give light upon the earth: and it was so.
# Genesis 1:17 And God set them in the firmament of the heaven to give light upon the earth,
# Genesis 1:20 And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl that may fly above the earth in the open firmament of heaven.
# Psalms 19:1 The heavens declare the glory of God; and the firmament sheweth his handywork.
# Psalms 150:1 Praise ye the LORD. Praise God in his sanctuary: praise him in the firmament of his power.
# Ezekiel 1:22 And the likeness of the firmament upon the heads of the living creature was as the colour of the terrible crystal, stretched forth over their heads above.
# Ezekiel 1:23 And under the firmament were their wings straight, the one toward the other: every one had two, which covered on this side, and every one had two, which covered on that side, their bodies.
# Ezekiel 1:25 And there was a voice from the firmament that was over their heads, when they stood, and had let down their wings.
# Ezekiel 1:26 And above the firmament that was over their heads was the likeness of a throne, as the appearance of a sapphire stone: and upon the likeness of the throne was the likeness as the appearance of a man above upon it.
# Ezekiel 10:1 Then I looked, and, behold, in the firmament that was above the head of the cherubims there appeared over them as it were a sapphire stone, as the appearance of the likeness of a throne.
# Daniel 12:3 And they that be wise shall shine as the brightness of the firmament; and they that turn many to righteousness as the stars for ever and ever.
# >>> b.count('firmament')
# 17
# >>> b.count('and')
# 51710
# >>> factors(_)
# [2, 5, 5171]
# >>> np(5171)
# 689
# >>> np(929)
# 158
# >>> npp(929)
# 20
# >>> npp(131)
# 7
# >>> pp(9)
# 181
# >>> pp(23)
# 10601
# >>> Psalm[106]
# Psalms 106:1-48 (48 verses)
# >>> p(_)
# Psalms 106
# 1 Praise ye the LORD. O give thanks unto the LORD; for he is good: for his mercy endureth for ever.
# 2 Who can utter the mighty acts of the LORD? who can shew forth all his praise?
# 3 Blessed are they that keep judgment, and he that doeth righteousness at all times.
# 4 Remember me, O LORD, with the favour that thou bearest unto thy people: O visit me with thy salvation;
# 5 That I may see the good of thy chosen, that I may rejoice in the gladness of thy nation, that I may glory with thine inheritance.
# 6 We have sinned with our fathers, we have committed iniquity, we have done wickedly.
# 7 Our fathers understood not thy wonders in Egypt; they remembered not the multitude of thy mercies; but provoked him at the sea, even at the Red sea.
# 8 Nevertheless he saved them for his name's sake, that he might make his mighty power to be known.
# 9 He rebuked the Red sea also, and it was dried up: so he led them through the depths, as through the wilderness.
# 10 And he saved them from the hand of him that hated them, and redeemed them from the hand of the enemy.
# 11 And the waters covered their enemies: there was not one of them left.
# 12 Then believed they his words; they sang his praise.
# 13 They soon forgat his works; they waited not for his counsel:
# 14 But lusted exceedingly in the wilderness, and tempted God in the desert.
# 15 And he gave them their request; but sent leanness into their soul.
# 16 They envied Moses also in the camp, and Aaron the saint of the LORD.
# 17 The earth opened and swallowed up Dathan and covered the company of Abiram.
# 18 And a fire was kindled in their company; the flame burned up the wicked.
# 19 They made a calf in Horeb, and worshipped the molten image.
# 20 Thus they changed their glory into the similitude of an ox that eateth grass.
# 21 They forgat God their saviour, which had done great things in Egypt;
# 22 Wondrous works in the land of Ham, and terrible things by the Red sea.
# 23 Therefore he said that he would destroy them, had not Moses his chosen stood before him in the breach, to turn away his wrath, lest he should destroy them.
# 24 Yea, they despised the pleasant land, they believed not his word:
# 25 But murmured in their tents, and hearkened not unto the voice of the LORD.
# 26 Therefore he lifted up his hand against them, to overthrow them in the wilderness:
# 27 To overthrow their seed also among the nations, and to scatter them in the lands.
# 28 They joined themselves also unto Baalpeor, and ate the sacrifices of the dead.
# 29 Thus they provoked him to anger with their inventions: and the plague brake in upon them.
# 30 Then stood up Phinehas, and executed judgment: and so the plague was stayed.
# 31 And that was counted unto him for righteousness unto all generations for evermore.
# 32 They angered him also at the waters of strife, so that it went ill with Moses for their sakes:
# 33 Because they provoked his spirit, so that he spake unadvisedly with his lips.
# 34 They did not destroy the nations, concerning whom the LORD commanded them:
# 35 But were mingled among the heathen, and learned their works.
# 36 And they served their idols: which were a snare unto them.
# 37 Yea, they sacrificed their sons and their daughters unto devils,
# 38 And shed innocent blood, even the blood of their sons and of their daughters, whom they sacrificed unto the idols of Canaan: and the land was polluted with blood.
# 39 Thus were they defiled with their own works, and went a whoring with their own inventions.
# 40 Therefore was the wrath of the LORD kindled against his people, insomuch that he abhorred his own inheritance.
# 41 And he gave them into the hand of the heathen; and they that hated them ruled over them.
# 42 Their enemies also oppressed them, and they were brought into subjection under their hand.
# 43 Many times did he deliver them; but they provoked him with their counsel, and were brought low for their iniquity.
# 44 Nevertheless he regarded their affliction, when he heard their cry:
# 45 And he remembered for them his covenant, and repented according to the multitude of his mercies.
# 46 He made them also to be pitied of all those that carried them captives.
# 47 Save us, O LORD our God, and gather us from among the heathen, to give thanks unto thy holy name, and to triumph in thy praise.
# 48 Blessed be the LORD God of Israel from everlasting to everlasting: and let all the people say, Amen. Praise ye the LORD.
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> pn(254)
# 1609
# >>> 
# >>> 
# >>> 
# >>> c
# 299792458
# >>> mc=c/1000
# >>> mc # speed of light in km/s
# 299792.458
# >>> c/1.609344
# 186282397.05122086
# >>> _/1000
# 186282.39705122088
# >>> 789629/_
# 4.238881464376266
# >>> 789629/mc
# 2.633918829272216
# >>> b.verse(9188)
# 1 Kings 13:3 And he gave a sign the same day, saying, This is the sign which the LORD hath spoken; Behold, the altar shall be rent, and the ashes that are upon it shall be poured out.
# >>> 
# >>> 
# >>> 10000**2/(37*37*53*106)
# 13.002139372012271
# >>> tell('ten-thousand times ten thousand')
# ten-thousand times ten thousand
#     141     +  66 + 39+  102   =348
# >>> b/'ten thousand times'
# Daniel 7:10 A fiery stream issued and came forth from before him: thousand thousands ministered unto him, and ten thousand times ten thousand stood before him: the judgment was set, and the books were opened.
# Revelation 5:11 And I beheld, and I heard the voice of many angels round about the throne and the beasts and the elders: and the number of them was ten thousand times ten thousand, and thousands of thousands;
# >>> 141**2
# 19881
# >>> factors(789629)
# [311, 2539]
# >>> np(311),np(2539)
# (64, 371)
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
# >>> 
# >>> 
# >>> 
# >>> 
# >>> pf(_)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "/home/pi/python/parle/primes.py", line 82, in pf
#     return collections.Counter(factors(n))
#   File "/home/pi/python/parle/primes.py", line 69, in factors
#     for p in (prime(j) for j in range(1,n)):
# TypeError: 'tuple' object cannot be interpreted as an integer
# >>> 37*53
# 1961
# >>> Psalm[118][8]-9
# Psalms 118:8 It is better to trust in the LORD than to put confidence in man.
# Psalms 118:9 It is better to trust in the LORD than to put confidence in princes.
# >>> _.tell()
# It is better to trust in the LORD than to put confidence in man.
# 29+28+  70  +35+  98 +23+ 33+ 49 + 43 +35+ 57+    78    +23+ 28 =629
# It is better to trust in the LORD than to put confidence in princes.
# 29+28+  70  +35+  98 +23+ 33+ 49 + 43 +35+ 57+    78    +23+   84   =685
# >>> b.chapter(629)
# Proverbs 1:1-33 (33 verses)
# >>> 
# >>> 
# >>> 
# >>> 
# >>> pf(_)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "/home/pi/python/parle/primes.py", line 82, in pf
#     return collections.Counter(factors(n))
#   File "/home/pi/python/parle/primes.py", line 69, in factors
#     for p in (prime(j) for j in range(1,n)):
# TypeError: 'Sel' object cannot be interpreted as an integer
# >>> b/"MENE"
# Daniel 5:25 And this is the writing that was written, MENE, MENE, TEKEL, UPHARSIN.
# Daniel 5:26 This is the interpretation of the thing: MENE; God hath numbered thy kingdom, and finished it.
# >>> _.verse(1).tell()
# And this is the writing that was written, MENE, MENE, TEKEL, UPHARSIN.
#  19+ 56 +28+ 33+  100  + 49 + 43+  109   +  37 +  37 +  53  +   106   =670
# >>> tell('PERES')
# P  E R  E S
# 16+5+18+5+19=63
# >>> p(Daniel[5:25]-28)
# Daniel 5
# 25 And this is the writing that was written, MENE, MENE, TEKEL, UPHARSIN.
# 26 This is the interpretation of the thing: MENE; God hath numbered thy kingdom, and finished it.
# 27 TEKEL; Thou art weighed in the balances, and art found wanting.
# 28 PERES; Thy kingdom is divided, and given to the Medes and Persians.
# >>> Daniel[5:28].tell()
# PERES; Thy kingdom is divided, and given to the Medes and Persians.
#   63  + 53+   73  +28+   57   + 19+  57 +35+ 33+  46 + 19+   101   =584
# >>> 
# >>> 
# >>> 
# >>> int(_)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# TypeError: int() argument must be a string, a bytes-like object or a number, not 'Sel'
# >>> pf(_)
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "/home/pi/python/parle/primes.py", line 82, in pf
#     return collections.Counter(factors(n))
#   File "/home/pi/python/parle/primes.py", line 69, in factors
#     for p in (prime(j) for j in range(1,n)):
# TypeError: 'Sel' object cannot be interpreted as an integer
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
# >>> 
# >>> c/_
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# TypeError: unsupported operand type(s) for /: 'int' and 'Sel'
# >>> 
# >>> 
# >>> 19/c
# 6.337717808764889e-08
# >>> osum("dna")/c
# 6.337717808764889e-08
# >>> 19*104
# 1976
# >>> factors(1947)
# [3, 11, 59]
# >>> 3*59
# 177
# >>> tell("dawkins")
# d a w  k  i n  s
# 4+1+23+11+9+14+19=81
# >>> tell("clinton richard dawkins")
# clinton richard dawkins
#    87  +   61  +   81  =229
# >>> Genesis[1:1].tell()
# In the beginning God created the heaven and the earth.
# 23+ 33+    81   + 26+   56  + 33+  55  + 19+ 33+  52  =411
# >>> Psalm[37:]
# Psalms 37:1-40 (40 verses)
# >>> 
# >>> c/77
# 3893408.5454545454
# >>> factors(38934)
# [2, 3, 3, 3, 7, 103]
# >>> factors(c)
# [2, 7, 73, 293339]
# >>> np(293339)
# 25488
# >>> pf(25488)
# Counter({2: 4, 3: 3, 59: 1})
# >>> 
# >>> bible.count(r'\blight\b')
# 272
# >>> pf(272)
# Counter({2: 4, 17: 1})
# >>> 16*17
# 272
# >>> Genesis[1:16]-17
# Genesis 1:16 And God made two great lights; the greater light to rule the day, and the lesser light to rule the night: he made the stars also.
# Genesis 1:17 And God set them in the firmament of the heaven to give light upon the earth,
# >>> _.tell(ssum)
# And God made two great lights; the greater light  to rule the day, and the lesser light  to rule the night: he made the stars also.
#  55+ 71+ 50 +760+ 303 +  354  +213+  398  + 254 +260+425 +213+705 + 55+213+ 330  + 254 +260+425 +213+ 274  +13+ 50 +213+ 491 + 191 =7043
# And God set them in the firmament of the heaven  to give light upon the earth,
#  55+ 71+305+253 +59+213+   441   +66+213+ 469  +260+421 + 254 +480 +213+ 304  =4077
# >>> 7043+4077
# 11120
# >>> c
# 299792458
# >>> Genesis[1:3].tell(lsum)
# And God said, Let there be light: and there was light.
#  3 + 3 +  4  + 3 +  5  +2 +  5   + 3 +  5  + 3 +  5   =41
# >>> c/1.60934
# 186282860.05443224
# >>> Genesis[1:3]
# Genesis 1:3 And God said, Let there be light: and there was light.
# >>> tell('lepton')
# l  e p  t  o  n
# 12+5+16+20+15+14=82
# >>> tell('let')
# l  e t
# 12+5+20=37
# >>> tell('Let there be light')
# Let there be light
#  37+  56 +7 +  56 =156
# >>> 
# >>> tell('and there was light')
# and there was light
#  19+  56 + 43+  56 =174
# >>> tell('fermions')
# f e r  m  i o  n  s
# 6+5+18+13+9+15+14+19=99
# >>> tell('firmament')
# f i r  m  a m  e n  t
# 6+9+18+13+1+13+5+14+20=99
# >>> Genesis/'firmament'
# Genesis 1:6-8,14-15,17,20 (7 verses)
# >>> p(_)
# Genesis 1
# 6 And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters.
# 7 And God made the firmament, and divided the waters which were under the firmament from the waters which were above the firmament: and it was so.
# 8 And God called the firmament Heaven. And the evening and the morning were the second day.
# 14 And God said, Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days, and years:
# 15 And let them be for lights in the firmament of the heaven to give light upon the earth: and it was so.
# 17 And God set them in the firmament of the heaven to give light upon the earth,
# 20 And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl that may fly above the earth in the open firmament of heaven.
# >>> tell('fermions')
# f e r  m  i o  n  s
# 6+5+18+13+9+15+14+19=99
# >>> tell('waters')
# w  a t  e r  s
# 23+1+20+5+18+19=86
# >>> tell('fermion baryon lepton quark')
# fermion baryon lepton quark
#    80  +  75  +  82  +  68 =305
# >>> tell('fermions baryons leptons quarks')
# fermions baryons leptons quarks
#    99   +   94  +  101  +  87  =381
# >>> Genesis[1:3].tell()
# And God said, Let there be light: and there was light.
#  19+ 26+  33 + 37+  56 +7 +  56  + 19+  56 + 43+  56  =408
# >>> c/56
# 5353436.75
# >>> b.verse(1)-b.verse(53+53)
# Genesis 1:1-4:26 (106 verses)
# >>> (_.words())[435:444],_/'open'
# (['earth', 'in', 'the', 'open', 'firmament', 'of', 'heaven.', 'And', 'God'], Genesis 1:20;3:5,7;4:11 (4 verses))
# >>> Genesis[1:20]
# Genesis 1:20 And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl that may fly above the earth in the open firmament of heaven.
# >>> _.wc()
# 29
# >>> tell('let there be light and there was light')
# let there be light and there was light
#  37+  56 +7 +  56 + 19+  56 + 43+  56 =330
# >>> c/
#   File "<console>", line 1
#     c/
#      ^
# SyntaxError: invalid syntax
# >>> 
# >>> b.chapter(436)
# Esther 10:1-3 (3 verses)
# >>> p(_)
# Esther 10
# 1 And the king Ahasuerus laid a tribute upon the land, and upon the isles of the sea.
# 2 And all the acts of his power and of his might, and the declaration of the greatness of Mordecai, whereunto the king advanced him, are they not written in the book of the chronicles of the kings of Media and Persia?
# 3 For Mordecai the Jew was next unto king Ahasuerus, and great among the Jews, and accepted of the multitude of his brethren, seeking the wealth of his people, and speaking peace to all his seed.
# >>> 
# >>> 
# >>> kk
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# NameError: name 'kk' is not defined
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> b.chapter(670)
# Ecclesiastes 11:1-10 (10 verses)
# >>> _/'light'
# Ecclesiastes 11:7 Truly the light is sweet, and a pleasant thing it is for the eyes to behold the sun:
# >>> b.chapter(616)
# Psalms 138:1-8 (8 verses)
# >>> p(_)
# Psalms 138
# 1 I will praise thee with my whole heart: before the gods will I sing praise unto thee.
# 2 I will worship toward thy holy temple, and praise thy name for thy lovingkindness and for thy truth: for thou hast magnified thy word above all thy name.
# 3 In the day when I cried thou answeredst me, and strengthenedst me with strength in my soul.
# 4 All the kings of the earth shall praise thee, O LORD, when they hear the words of thy mouth.
# 5 Yea, they shall sing in the ways of the LORD: for great is the glory of the LORD.
# 6 Though the LORD be high, yet hath he respect unto the lowly: but the proud he knoweth afar off.
# 7 Though I walk in the midst of trouble, thou wilt revive me: thou shalt stretch forth thine hand against the wrath of mine enemies, and thy right hand shall save me.
# 8 The LORD will perfect that which concerneth me: thy mercy, O LORD, endureth for ever: forsake not the works of thine own hands.
# >>> 
# >>> 
# >>> b.chapter(629)
# Proverbs 1:1-33 (33 verses)
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 14*73
# 1022
# >>> 1022*293339
# 299792458
# >>> allfactors(c)
# [1, 2, 7, 14, 73, 146, 511, 1022, 293339, 586678, 2053373, 4106746, 21413747, 42827494, 149896229, 299792458]
# >>> 
# >>> c/37
# 8102498.864864865
# >>> 37/c
# 1.2341871522331627e-07
# >>> 74/c
# 2.4683743044663253e-07
# >>> 77/c
# 2.568443533025771e-07
# >>> 515/c
# 1.717855090270483e-06
# >>> b.chapter(855)
# Daniel 5:1-31 (31 verses)
# >>> p(_)
# Daniel 5
# 1 Belshazzar the king made a great feast to a thousand of his lords, and drank wine before the thousand.
# 2 Belshazzar, whiles he tasted the wine, commanded to bring the golden and silver vessels which his father Nebuchadnezzar had taken out of the temple which was in Jerusalem; that the king, and his princes, his wives, and his concubines, might drink therein.
# 3 Then they brought the golden vessels that were taken out of the temple of the house of God which was at Jerusalem; and the king, and his princes, his wives, and his concubines, drank in them.
# 4 They drank wine, and praised the gods of gold, and of silver, of brass, of iron, of wood, and of stone.
# 5 In the same hour came forth fingers of a man's hand, and wrote over against the candlestick upon the plaister of the wall of the king's palace: and the king saw the part of the hand that wrote.
# 6 Then the king's countenance was changed, and his thoughts troubled him, so that the joints of his loins were loosed, and his knees smote one against another.
# 7 The king cried aloud to bring in the astrologers, the Chaldeans, and the soothsayers. And the king spake, and said to the wise men of Babylon, Whosoever shall read this writing, and shew me the interpretation thereof, shall be clothed with scarlet, and have a chain of gold about his neck, and shall be the third ruler in the kingdom.
# 8 Then came in all the king's wise men: but they could not read the writing, nor make known to the king the interpretation thereof.
# 9 Then was king Belshazzar greatly troubled, and his countenance was changed in him, and his lords were astonied.
# 10 Now the queen by reason of the words of the king and his lords came into the banquet house: and the queen spake and said, O king, live for ever: let not thy thoughts trouble thee, nor let thy countenance be changed:
# 11 There is a man in thy kingdom, in whom is the spirit of the holy gods; and in the days of thy father light and understanding and wisdom, like the wisdom of the gods, was found in him; whom the king Nebuchadnezzar thy father, the king, I say, thy father, made master of the magicians, astrologers, Chaldeans, and soothsayers;
# 12 Forasmuch as an excellent spirit, and knowledge, and understanding, interpreting of dreams, and shewing of hard sentences, and dissolving of doubts, were found in the same Daniel, whom the king named Belteshazzar: now let Daniel be called, and he will shew the interpretation.
# 13 Then was Daniel brought in before the king. And the king spake and said unto Daniel, Art thou that Daniel, which art of the children of the captivity of Judah, whom the king my father brought out of Jewry?
# 14 I have even heard of thee, that the spirit of the gods is in thee, and that light and understanding and excellent wisdom is found in thee.
# 15 And now the wise men, the astrologers, have been brought in before me, that they should read this writing, and make known unto me the interpretation thereof: but they could not shew the interpretation of the thing:
# 16 And I have heard of thee, that thou canst make interpretations, and dissolve doubts: now if thou canst read the writing, and make known to me the interpretation thereof, thou shalt be clothed with scarlet, and have a chain of gold about thy neck, and shalt be the third ruler in the kingdom.
# 17 Then Daniel answered and said before the king, Let thy gifts be to thyself, and give thy rewards to another; yet I will read the writing unto the king, and make known to him the interpretation.
# 18 O thou king, the most high God gave Nebuchadnezzar thy father a kingdom, and majesty, and glory, and honour:
# 19 And for the majesty that he gave him, all people, nations, and languages, trembled and feared before him: whom he would he slew; and whom he would he kept alive; and whom he would he set up; and whom he would he put down.
# 20 But when his heart was lifted up, and his mind hardened in pride, he was deposed from his kingly throne, and they took his glory from him:
# 21 And he was driven from the sons of men; and his heart was made like the beasts, and his dwelling was with the wild asses: they fed him with grass like oxen, and his body was wet with the dew of heaven; till he knew that the most high God ruled in the kingdom of men, and that he appointeth over it whomsoever he will.
# 22 And thou his son, O Belshazzar, hast not humbled thine heart, though thou knewest all this;
# 23 But hast lifted up thyself against the Lord of heaven; and they have brought the vessels of his house before thee, and thou, and thy lords, thy wives, and thy concubines, have drunk wine in them; and thou hast praised the gods of silver, and gold, of brass, iron, wood, and stone, which see not, nor hear, nor know: and the God in whose hand thy breath is, and whose are all thy ways, hast thou not glorified:
# 24 Then was the part of the hand sent from him; and this writing was written.
# 25 And this is the writing that was written, MENE, MENE, TEKEL, UPHARSIN.
# 26 This is the interpretation of the thing: MENE; God hath numbered thy kingdom, and finished it.
# 27 TEKEL; Thou art weighed in the balances, and art found wanting.
# 28 PERES; Thy kingdom is divided, and given to the Medes and Persians.
# 29 Then commanded Belshazzar, and they clothed Daniel with scarlet, and put a chain of gold about his neck, and made a proclamation concerning him, that he should be the third ruler in the kingdom.
# 30 In that night was Belshazzar the king of the Chaldeans slain.
# 31 And Darius the Median took the kingdom, being about threescore and two years old.
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
# >>> b.verse(2458)
# Exodus 32:19 And it came to pass, as soon as he came nigh unto the camp, that he saw the calf, and the dancing: and Moses' anger waxed hot, and he cast the tables out of his hands, and brake them beneath the mount.
# >>> 39*19
# 741
# >>> factors(2458)
# [2, 1229]
# >>> 1229-1189
# 40
# >>> factors(299792458)
# [2, 7, 73, 293339]
# >>> np(293339)
# 25488
# >>> pf(_)
# Counter({2: 4, 3: 3, 59: 1})
# >>> pf(93339)
# Counter({3: 3, 3457: 1})
# >>> np(3457)
# 483
# >>> pf(_)
# Counter({3: 1, 7: 1, 23: 1})
# >>> 
# >>> 29979+1123
# 31102
# >>> _+106
# 31208
# >>> b.verse(106)
# Genesis 4:26 And to Seth, to him also there was born a son; and he called his name Enos: then began men to call upon the name of the LORD.
# >>> b.verse(2458)
# Exodus 32:19 And it came to pass, as soon as he came nigh unto the camp, that he saw the calf, and the dancing: and Moses' anger waxed hot, and he cast the tables out of his hands, and brake them beneath the mount.
# >>> b.verse(1123)
# Genesis 38:3 And she conceived, and bare a son; and he called his name Er.
# >>> b.verse(29979)
# Hebrews 2:1 Therefore we ought to give the more earnest heed to the things which we have heard, lest at any time we should let them slip.
# >>> _.tell(lsum)
# Therefore we ought to give the more earnest heed to the things which we have heard, lest at any time we should let them slip.
#     9    +2 +  5  +2 + 4  + 3 + 4  +   7   + 4  +2 + 3 +  6   +  5  +2 + 4  +  5   + 4  +2 + 3 + 4  +2 +  6   + 3 + 4  +  4  =99
# >>> Hebrews.lc()
# 29322
# >>> 299792458/99
# 3028206.6464646463
# >>> Genesis[1:20].tell()
# 1:20 And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl that may fly above the earth in the open firmament of heaven.
#    0+ 19+ 26+   33+ 37+ 33+    86+   50+   67+       114+ 33+    80+      91+  49+  37+   32+ 19+  56+  49+ 39+ 43+   45+ 33+   52+23+ 33+  50+       99+21+     55 = 1404
# >>> 1404/99
# 14.181818181818182
# >>> Genesis[1:25].tell()
# 1:25 And God made the beast of the earth after his kind, and cattle after their kind, and every thing that creepeth upon the earth after his kind: and God saw that it was good.
#    0+ 19+ 26+  23+ 33+   47+21+ 33+   52+   50+ 36+   38+ 19+    61+   50+   60+   38+ 19+   75+   58+  49+      80+  66+ 33+   52+   50+ 36+   38+ 19+ 26+ 43+  49+29+ 43+   41 = 1412
# >>> 1412/99
# 14.262626262626263
# >>> Genesis.count('good')
# 56
# >>> 
# >>> 
# >>> 
# >>> 
# >>> 
