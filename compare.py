>>> from bible import *
>>> from pce import pce
>>> dir('')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> b.wc()
789629
>>> b.words()[789629//2-5:789629//2+5]
['lie', 'in', 'wait', 'for', 'my', 'soul:', 'the', 'mighty', 'are', 'gathered']
>>> b.midword()
['soul:']
>>> b/'bowshot'

>>> b/'bow shot'
Genesis 21:16 And she went, and sat her down over against him a good way off, as it were a bow shot: for she said, Let me not see the death of the child. And she sat over against him, and lift up her voice, and wept.
>>> Genesis.wc()
38264
>>> fs(_+5)
[7, 7, 11, 71]
>>> 7*7*11*71
38269
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> pce=Sel(pce)
>>> pce[1:1]
Genesis 1:1...Revelation 1:1 (66 verses)
>>> pce[1][1:1]
Genesis 1:1 IN the beginning God created the heaven and the earth.
>>> l=[i for i in span(31102) if bible.v(i).replace(',','').lower() != pce.v(i).replace('¶','').replace(',','').replace('-','').lower()]
>>> l=[i for i in span(31102) if bible.verse(i).wc() != pce.verse(i).wc()]
>>> len(l)
51
>>> l
[109, 250, 480, 495, 530, 747, 771, 829, 1812, 2168, 2468, 2520, 3383, 3536, 4134, 4265, 4331, 5312, 5921, 5979, 7446, 8320, 8769, 9638, 10035, 10088, 10235, 11398, 11572, 12817, 12823, 12966, 13683, 14207, 14564, 15300, 17740, 18055, 18797, 18811, 21089, 21235, 22064, 22343, 22362, 22791, 27284, 27301, 27385, 30401, 30574]
>>> for i in _: p(b.verse(i)); p(pce.verse(i))
... 
Genesis 5:3 And Adam lived an hundred and thirty years, and begat a son in his own likeness, and after his image; and called his name Seth:
Genesis 5:3 ¶And Adam lived an hundred and thirty years, and begat a son in his own likeness, after his image; and called his name Seth:
Genesis 10:15 And Canaan begat Sidon his first born, and Heth,
Genesis 10:15 ¶And Canaan begat Sidon his firstborn, and Heth,
Genesis 19:22 Haste thee, escape thither; for I cannot do anything till thou be come thither. Therefore the name of the city was called Zoar.
Genesis 19:22 Haste thee, escape thither; for I cannot do any thing till thou be come thither. Therefore the name of the city was called Zoar.
Genesis 19:37 And the first born bare a son, and called his name Moab: the same is the father of the Moabites unto this day.
Genesis 19:37 And the firstborn bare a son, and called his name Moab: the same is the father of the Moabites unto this day.
Genesis 21:16 And she went, and sat her down over against him a good way off, as it were a bow shot: for she said, Let me not see the death of the child. And she sat over against him, and lift up her voice, and wept.
Genesis 21:16 And she went, and sat her down over against him a good way off, as it were a bowshot: for she said, Let me not see the death of the child. And she sat over against him, and lift up her voice, and wept.
Genesis 27:19 And Jacob said unto his father, I am Esau thy first born; I have done according as thou badest me: arise, I pray thee, sit and eat of my venison, that thy soul may bless me.
Genesis 27:19 And Jacob said unto his father, I am Esau thy firstborn; I have done according as thou badest me: arise, I pray thee, sit and eat of my venison, that thy soul may bless me.
Genesis 27:43 Now therefore, my son, obey my voice; arise, flee thou to Laban my brother to Haran;
Genesis 27:43 Now therefore, my son, obey my voice; and arise, flee thou to Laban my brother to Haran;
Genesis 29:33 And she conceived again, and bare a son; and said, Because the LORD hath heard I was hated, he hath therefore given me this son also: and she called his name Simeon.
Genesis 29:33 And she conceived again, and bare a son; and said, Because the Lord hath heard that I was hated, he hath therefore given me this son also: and she called his name Simeon.
Exodus 11:5 And all the firstborn in the land of Egypt shall die, from the first born of Pharaoh that sitteth upon his throne, even unto the firstborn of the maidservant that is behind the mill; and all the firstborn of beasts.
Exodus 11:5 And all the firstborn in the land of Egypt shall die, from the firstborn of Pharaoh that sitteth upon his throne, even unto the firstborn of the maidservant that is behind the mill; and all the firstborn of beasts.
Exodus 23:23 For mine Angel shall go before thee, and bring thee in unto the Amorites, and the Hittites, and the Perizzites, and the Canaanites, the Hivites, and the Jebusites: and I will cut them off.
Exodus 23:23 For mine Angel shall go before thee, and bring thee in unto the Amorites, and the Hittites, and the Perizzites, and the Canaanites, and the Hivites, and the Jebusites: and I will cut them off.
Exodus 32:29 For Moses had said, Consecrate yourselves today to the LORD, even every man upon his son, and upon his brother; that he may bestow upon you a blessing this day.
Exodus 32:29 For Moses had said, Consecrate yourselves to day to the Lord, even every man upon his son, and upon his brother; that he may bestow upon you a blessing this day.
Exodus 34:23 Thrice in the year shall all your menchildren appear before the LORD God, the God of Israel.
Exodus 34:23 ¶Thrice in the year shall all your men children appear before the Lord God, the God of Israel.
Leviticus 22:13 But if the priest's daughter be a widow, or divorced, and have no child, and is returned unto her father's house, as in her youth, she shall eat of her father's meat: but there shall be no stranger eat thereof.
Leviticus 22:13 But if the priest's daughter be a widow, or divorced, and have no child, and is returned unto her father's house, as in her youth, she shall eat of her father's meat: but there shall no stranger eat thereof.
Leviticus 26:11 And I set my tabernacle among you: and my soul shall not abhor you.
Leviticus 26:11 And I will set my tabernacle among you: and my soul shall not abhor you.
Numbers 14:25 (Now the Amalekites and the Canaanites dwelt in the valley.) Tomorrow turn you, and get you into the wilderness by the way of the Red sea.
Numbers 14:25 (Now the Amalekites and the Canaanites dwelt in the valley.) To morrow turn you, and get you into the wilderness by the way of the Red sea.
Numbers 18:7 Therefore thou and thy sons with thee shall keep your priest's office for everything of the altar, and within the vail; and ye shall serve: I have given your priest's office unto you as a service of gift: and the stranger that cometh nigh shall be put to death.
Numbers 18:7 Therefore thou and thy sons with thee shall keep your priest's office for every thing of the altar, and within the vail; and ye shall serve: I have given your priest's office unto you as a service of gift: and the stranger that cometh nigh shall be put to death.
Numbers 20:19 And the children of Israel said unto him, We will go by the high way: and if I and my cattle drink of thy water, then I will pay for it: I will only, without doing anything else, go through on my feet.
Numbers 20:19 And the children of Israel said unto him, We will go by the high way: and if I and my cattle drink of thy water, then I will pay for it: I will only, without doing any thing else, go through on my feet.
Deuteronomy 14:21 Ye shall not eat of anything that dieth of itself: thou shalt give it unto the stranger that is in thy gates, that he may eat it; or thou mayest sell it unto an alien: for thou art an holy people unto the LORD thy God. Thou shalt not seethe a kid in his mother's milk.
Deuteronomy 14:21 ¶Ye shall not eat of any thing that dieth of itself: thou shalt give it unto the stranger that is in thy gates, that he may eat it; or thou mayest sell it unto an alien: for thou art an holy people unto the Lord thy God. Thou shalt not seethe a kid in his mother's milk.
Joshua 4:10 For the priests which bare the ark stood in the midst of Jordan, until everything was finished that the LORD commanded Joshua to speak unto the people, according to all that Moses commanded Joshua: and the people hasted and passed over.
Joshua 4:10 ¶For the priests which bare the ark stood in the midst of Jordan, until every thing was finished that the Lord commanded Joshua to speak unto the people, according to all that Moses commanded Joshua: and the people hasted and passed over.
Joshua 7:2 And Joshua sent men from Jericho to Ai, which is beside Bethaven, on the east of Bethel, and spake unto them, saying, Go up and view the country. And the men went up and viewed Ai.
Joshua 7:2 And Joshua sent men from Jericho to Ai, which is beside Beth-aven, on the east side of Beth-el, and spake unto them, saying, Go up and view the country. And the men went up and viewed Ai.
1 Samuel 10:27 But the children of Belial said, How shall this man save us? And they despised him, and brought no presents. But he held his peace.
1 Samuel 10:27 But the children of Belial said, How shall this man save us? And they despised him, and brought him no presents. But he held his peace.
2 Samuel 13:2 And Amnon was so vexed, that he fell sick for his sister Tamar; for she was a virgin; and Amnon thought it hard for him to do anything to her.
2 Samuel 13:2 And Amnon was so vexed, that he fell sick for his sister Tamar; for she was a virgin; and Amnon thought it hard for him to do any thing to her.
1 Kings 1:51 And it was told Solomon, saying, Behold, Adonijah feareth king Solomon: for, lo, he hath caught hold on the horns of the altar, saying, Let king Solomon swear unto me today that he will not slay his servant with the sword.
1 Kings 1:51 And it was told Solomon, saying, Behold, Adonijah feareth king Solomon: for, lo, he hath caught hold on the horns of the altar, saying, Let king Solomon swear unto me to day that he will not slay his servant with the sword.
2 Kings 4:34 And he went up, and lay upon the child, and put his mouth upon his mouth, and his eyes upon his eyes, and his hands upon his hands: and stretched himself upon the child; and the flesh of the child waxed warm.
2 Kings 4:34 And he went up, and lay upon the child, and put his mouth upon his mouth, and his eyes upon his eyes, and his hands upon his hands: and he stretched himself upon the child; and the flesh of the child waxed warm.
2 Kings 18:10 And at the end of three years they took it: even in the sixth year of Hezekiah, that is in the ninth year of Hoshea king of Israel, Samaria was taken.
2 Kings 18:10 And at the end of three years they took it: even in the sixth year of Hezekiah, that is the ninth year of Hoshea king of Israel, Samaria was taken.
2 Kings 19:26 Therefore their inhabitants were of small power, they were dismayed and confounded; they were as the grass of the field, and as the green herb, as the grass on the house tops, and as corn blasted before it be grown up.
2 Kings 19:26 Therefore their inhabitants were of small power, they were dismayed and confounded; they were as the grass of the field, and as the green herb, as the grass on the housetops, and as corn blasted before it be grown up.
2 Kings 25:12 But the captain of the guard left of the door of the poor of the land to be vinedressers and husbandmen.
2 Kings 25:12 But the captain of the guard left of the poor of the land to be vinedressers and husbandmen.
2 Chronicles 10:2 And it came to pass, when Jeroboam the son of Nebat, who was in Egypt, whither he fled from the presence of Solomon the king, heard it, that Jeroboam returned out of Egypt.
2 Chronicles 10:2 And it came to pass, when Jeroboam the son of Nebat, who was in Egypt, whither he had fled from the presence of Solomon the king, heard it, that Jeroboam returned out of Egypt.
2 Chronicles 18:29 And the king of Israel said unto Jehoshaphat, I will disguise myself, and I will go to the battle; but put thou on thy robes. So the king of Israel disguised himself; and they went to the battle.
2 Chronicles 18:29 And the king of Israel said unto Jehoshaphat, I will disguise myself, and will go to the battle; but put thou on thy robes. So the king of Israel disguised himself; and they went to the battle.
Esther 7:9 And Harbonah, one of the chamberlains, said before the king, Behold also, the gallows fifty cubits high, which Haman had made for Mordecai, who spoken good for the king, standeth in the house of Haman. Then the king said, Hang him thereon.
Esther 7:9 And Harbonah, one of the chamberlains, said before the king, Behold also, the gallows fifty cubits high, which Haman had made for Mordecai, who had spoken good for the king, standeth in the house of Haman. Then the king said, Hang him thereon.
Esther 8:5 And said, If it please the king, and if I have favour in his sight, and the thing seem right before the king, and I be pleasing in his eyes, let it be written to reverse the letters devised by Haman the son of Hammedatha the Agagite, which he wrote to destroy the Jews which are in all the king's provinces:
Esther 8:5 And said, If it please the king, and if I have found favour in his sight, and the thing seem right before the king, and I be pleasing in his eyes, let it be written to reverse the letters devised by Haman the son of Hammedatha the Agagite, which he wrote to destroy the Jews which are in all the king's provinces:
Job 5:14 They meet with darkness in the day time, and grope in the noonday as in the night.
Job 5:14 They meet with darkness in the daytime, and grope in the noonday as in the night.
Job 33:32 If thou hast anything to say, answer me: speak, for I desire to justify thee.
Job 33:32 If thou hast any thing to say, answer me: speak, for I desire to justify thee.
Psalms 22:2 O my God, I cry in the day time, but thou hearest not; and in the night season, and am not silent.
Pslams 22:2 O my God, I cry in the daytime, but thou hearest not; and in the night season, and am not silent.
Psalms 42:8 Yet the LORD will command his lovingkindness in the day time, and in the night his song shall be with me, and my prayer unto the God of my life.
Pslams 42:8 Yet the Lord will command his lovingkindness in the daytime, and in the night his song shall be with me, and my prayer unto the God of my life.
Psalms 86:15 But thou, O Lord, art a God full of compassion, and gracious, long suffering, and plenteous in mercy and truth.
Pslams 86:15 But thou, O Lord, art a God full of compassion, and gracious, longsuffering, and plenteous in mercy and truth.
Isaiah 4:6 And there shall be a tabernacle for a shadow in the day time from the heat, and for a place of refuge, and for a covert from storm and from rain.
Isaiah 4:6 And there shall be a tabernacle for a shadow in the daytime from the heat, and for a place of refuge, and for a covert from storm and from rain.
Isaiah 22:2 Thou that art full of stirs, a tumultuous city, joyous city: thy slain men are not slain with the sword, nor dead in battle.
Isaiah 22:2 Thou that art full of stirs, a tumultuous city, a joyous city: thy slain men are not slain with the sword, nor dead in battle.
Isaiah 58:10 And if thou draw out thy soul to the hungry, and satisfy the afflicted soul; then shall thy light rise in obscurity, and thy darkness be as the noon day:
Isaiah 58:10 And if thou draw out thy soul to the hungry, and satisfy the afflicted soul; then shall thy light rise in obscurity, and thy darkness be as the noonday:
Isaiah 59:10 We grope for the wall like the blind, and we grope as if we had no eyes: we stumble at noon day as in the night; we are in desolate places as dead men.
Isaiah 59:10 We grope for the wall like the blind, and we grope as if we had no eyes: we stumble at noonday as in the night; we are in desolate places as dead men.
Ezekiel 25:5 And I will make Rabbah a stable for camels, and the Ammonites a couching place for flocks: and ye shall know that I am the LORD.
Ezekiel 25:5 And I will make Rabbah a stable for camels, and the Ammonites a couchingplace for flocks: and ye shall know that I am the Lord.
Ezekiel 31:4 The waters made him great, the deep set him up on high with her rivers running round about his plants, and sent her little rivers unto all the trees of the field.
Ezekiel 31:4 The waters made him great, the deep set him up on high with her rivers running round about his plants, and sent out her little rivers unto all the trees of the field.
Daniel 11:27 And both of these kings' hearts shall be to do mischief, and they shall speak lies at one table; but it shall not prosper: for yet the end shall be at the time appointed.
Daniel 11:27 And both these kings' hearts shall be to do mischief, and they shall speak lies at one table; but it shall not prosper: for yet the end shall be at the time appointed.
Joel 2:31 The sun shall be turned into darkness, and the moon into blood, before the great and terrible day of the LORD come.
Joel 2:31 The sun shall be turned into darkness, and the moon into blood, before the great and the terrible day of the Lord come.
Joel 3:18 And it shall come to pass in that day, that the mountains shall drop down new wine, and the hills shall flow with milk, and all the rivers of Judah shall flow with waters, and a fountain shall come forth out of the house of the LORD, and shall water the valley of Shittim.
Joel 3:18 ¶And it shall come to pass in that day, that the mountains shall drop down new wine, and the hills shall flow with milk, and all the rivers of Judah shall flow with waters, and a fountain shall come forth of the house of the Lord, and shall water the valley of Shittim.
Zephaniah 1:3 I will consume man and beast; I will consume the fowls of the heaven, and the fishes of the sea, and the stumbling blocks with the wicked: and I will cut off man from off the land, saith the LORD.
Zephaniah 1:3 I will consume man and beast; I will consume the fowls of the heaven, and the fishes of the sea, and the stumblingblocks with the wicked; and I will cut off man from off the land, saith the Lord.
Acts 10:24 And the morrow after they entered into Caesarea. And Cornelius waited for them, and he had called together his kinsmen and near friends.
Acts 10:24 And the morrow after they entered into Cæsarea. And Cornelius waited for them, and had called together his kinsmen and near friends.
Acts 10:41 Not to all the people, but unto witnesses chosen before God, even to us, who did eat and drink with him after he rose from the dead.
Acts 10:41 Not to all the people, but unto witnesses chosen before of God, even to us, who did eat and drink with him after he rose from the dead.
Acts 13:22 And when he had removed him, he raised up unto them David to be their king; to whom also he gave their testimony, and said, I have found David the son of Jesse, a man after mine own heart, which shall fulfil all my will.
Acts 13:22 And when he had removed him, he raised up unto them David to be their king; to whom also he gave testimony, and said, I have found David the son of Jesse, a man after mine own heart, which shall fulfil all my will.
1 Peter 2:1 Wherefore laying aside all malice, and all guile, and hypocrisies, and envies, all evil speakings,
1 Peter 2:1 WHEREFORE laying aside all malice, and all guile, and hypocrisies, and envies, and all evil speakings,
1 John 2:23 Whosoever denieth the Son, the same hath not the Father: he that acknowledgeth the Son hath the Father also.
1 John 2:23 Whosoever denieth the Son, the same hath not the Father: [but] he that acknowledgeth the Son hath the Father also.
>>> 
>>> pce.v(649).lower()
>>> pce.v(649).lower()
'24:57 and they said, we will call the damsel, and inquire at her mouth.'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> tell('Sabtah Sabtechah Sabtecha')
Sabtah Sabtechah Sabtecha
    51+       67+      59 = 177
>>> a1=(b/'firstborn').vns()
>>> a2=(b/'first born').vns()
>>> aa=sorted(set(a1)|set(a2))
>>> (pce/'firstborn').vns()
[250, 489, 491, 492, 495, 569, 672, 747, 760, 822, 1035, 1056, 1126, 1127, 1247, 1324, 1395, 1466, 1470, 1477, 1624, 1625, 1670, 1812, 1829, 1846, 1870, 1881, 1883, 2143, 2517, 3695, 3705, 3706, 3733, 3734, 3735, 3736, 3738, 3739, 3743, 3956, 3957, 3958, 4273, 4765, 5463, 5464, 5465, 5554, 5976, 6277, 6740, 7372, 7558, 7632, 8084, 9318, 10266, 10282, 10310, 10320, 10332, 10334, 10349, 10357, 10363, 10377, 10390, 10430, 10432, 10483, 10577, 10606, 10615, 10621, 10647, 10652, 11080, 11082, 11088, 11628, 12586, 13290, 15165, 15354, 15643, 16184, 16207, 17959, 19701, 22656, 23056, 23170, 24981, 28146, 29481, 29484, 30201, 30236]
>>> aa==_
True
>>> 
>>> 
>>> 
>>> pce/'first born'

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
