from mene import *
from func import *

multipliers={"score":20, "hundred":100, "thousand":1000, "million":1000000,}
one2nineteen='one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'
ten2ninety='ten twenty thirty forty fifty sixty seventy eighty ninety'
first2nineteenth='first second third fourth fifth sixth seventh eighth nineth tenth eleventh twelfth thirteenth fourteenth fifteenth sixteenth seventeenth eighteenth nineteenth'
tenth2ninetieth='tenth twentieth thirtieth fortieth fiftieth sixtieth seventieth eightieth ninetieth'
wordnums={v:i for i,v in enumerate(one2nineteen.split(),start=1)}
wordnums.update({v:i*10 for i,v in enumerate(ten2ninety.split(),start=1)})
wordnums.update(multipliers)
wordnums.update({w+'fold':i for w,i in wordnums.items()})
wordnums.update({v:i for i,v in enumerate(first2nineteenth.split(),start=1)})
wordnums.update({v:i*10 for i,v in enumerate(tenth2ninetieth.split(),start=1)})
multipliers.update({"hundredth":100, "thousandth":1000, "millionth":1000000,})
wordnums.update({"twoscore":40, "threescore":60, "fourscore":80})
wordnums.update({"a":0, "an":0, "and":0, })

@aslist
def word2num(ws):
    if isinstance(ws, str):
        ws=[w.lower().strip(',.;:)-') for w in ws.split(' ')]
    ns=[]
    for w in ws:
        if w not in wordnums:
            n=sum(ns)
            if n:
                yield n
                # print(n)
            ns=[]
        else:
            k=wordnums[w]
            # print(ns,k,w)
            if ns:
                while len(ns)>1 and ns[-2]<k:
                    ns[-2:]=[sum(ns[-2:])]
                if ns and k>ns[-1] and w in multipliers:
                    ns[-1]=ns[-1]*k
                    k=0
            if k: ns+=[k]
    n=sum(ns)
    if n:
        yield n
        # print(n)

# >>> from bible import *
# >>> from word2num import *
# >>> multipliers
# {'score': 20, 'hundred': 100, 'thousand': 1000, 'million': 1000000, 'hundredth': 100, 'thousandth': 1000, 'millionth': 1000000}
# >>> wordnums
# {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90, 'score': 20, 'hundred': 100, 'thousand': 1000, 'million': 1000000, 'onefold': 1, 'twofold': 2, 'threefold': 3, 'fourfold': 4, 'fivefold': 5, 'sixfold': 6, 'sevenfold': 7, 'eightfold': 8, 'ninefold': 9, 'tenfold': 10, 'elevenfold': 11, 'twelvefold': 12, 'thirteenfold': 13, 'fourteenfold': 14, 'fifteenfold': 15, 'sixteenfold': 16, 'seventeenfold': 17, 'eighteenfold': 18, 'nineteenfold': 19, 'twentyfold': 20, 'thirtyfold': 30, 'fortyfold': 40, 'fiftyfold': 50, 'sixtyfold': 60, 'seventyfold': 70, 'eightyfold': 80, 'ninetyfold': 90, 'scorefold': 20, 'hundredfold': 100, 'thousandfold': 1000, 'millionfold': 1000000, 'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5, 'sixth': 6, 'seventh': 7, 'eighth': 8, 'nineth': 9, 'tenth': 10, 'eleventh': 11, 'twelfth': 12, 'thirteenth': 13, 'fourteenth': 14, 'fifteenth': 15, 'sixteenth': 16, 'seventeenth': 17, 'eighteenth': 18, 'nineteenth': 19, 'twentieth': 20, 'thirtieth': 30, 'fortieth': 40, 'fiftieth': 50, 'sixtieth': 60, 'seventieth': 70, 'eightieth': 80, 'ninetieth': 90, 'twoscore': 40, 'threescore': 60, 'fourscore': 80, 'a': 0, 'an': 0, 'and': 0}
# >>> ns=word2num((Genesis[5:1]-31).text())
# >>> 
# >>> ns
# [130, 800, 930, 105, 807, 912, 90, 815, 905, 70, 840, 910, 65, 830, 895, 162, 800, 962, 65, 300, 365, 187, 782, 969, 182, 595, 777]
# >>> Psalm[90:10]
# Psalms 90:10 The days of our years are threescore years and ten; and if by reason of strength they be fourscore years, yet is their strength labour and sorrow; for it is soon cut off, and we fly away.
# >>> Psalm[90:10].numbers()
# [60, 10, 80]
# >>> Genesis/777
# Genesis 5:31 And all the days of Lamech were seven hundred seventy and seven years: and he died.
# >>> Genesis/60
# Genesis 25:26 And after that came his brother out, and his hand took hold on Esau's heel; and his name was called Jacob: and Isaac was threescore years old when she bare them.
# >>> 
# >>> 
# >>> b/666
# 1 Kings 10:14;2 Chronicles 9:13;Ezra 2:13;Revelation 13:18 (4 verses)
# >>> p(_)
# 1 Kings 10:14 Now the weight of gold that came to Solomon in one year was six hundred threescore and six talents of gold,
# 2 Chronicles 9:13 Now the weight of gold that came to Solomon in one year was six hundred and threescore and six talents of gold;
# Ezra 2:13 The children of Adonikam, six hundred sixty and six.
# Revelation 13:18 Here is wisdom. Let him that hath understanding count the number of the beast: for it is the number of a man; and his number is Six hundred threescore and six.
# >>> b/5000
# Joshua 8:12;Judges 20:45;1 Samuel 17:5;1 Chronicles 29:7;2 Chronicles 35:9;Ezra 2:69;Ezekiel 45:6;48:15;Matthew 14:21;16:9;Mark 6:44;8:19;Luke 9:14;John 6:10;Acts 4:4 (15 verses)
# >>> p(_)
# Joshua 8:12 And he took about five thousand men, and set them to lie in ambush between Bethel and Ai, on the west side of the city.
# Judges 20:45 And they turned and fled toward the wilderness unto the rock of Rimmon: and they gleaned of them in the highways five thousand men; and pursued hard after them unto Gidom, and slew two thousand men of them.
# 1 Samuel 17:5 And he had an helmet of brass upon his head, and he was armed with a coat of mail; and the weight of the coat was five thousand shekels of brass.
# 1 Chronicles 29:7 And gave for the service of the house of God of gold five thousand talents and ten thousand drams, and of silver ten thousand talents, and of brass eighteen thousand talents, and one hundred thousand talents of iron.
# 2 Chronicles 35:9 Conaniah also, and Shemaiah and Nethaneel, his brethren, and Hashabiah and Jeiel and Jozabad, chief of the Levites, gave unto the Levites for passover offerings five thousand small cattle, and five hundred oxen.
# Ezra 2:69 They gave after their ability unto the treasure of the work threescore and one thousand drams of gold, and five thousand pound of silver, and one hundred priests' garments.
# Ezekiel 45:6 And ye shall appoint the possession of the city five thousand broad, and five and twenty thousand long, over against the oblation of the holy portion: it shall be for the whole house of Israel.
# Ezekiel 48:15 And the five thousand, that are left in the breadth over against the five and twenty thousand, shall be a profane place for the city, for dwelling, and for suburbs: and the city shall be in the midst thereof.
# Matthew 14:21 And they that had eaten were about five thousand men, beside women and children.
# Matthew 16:9 Do ye not yet understand, neither remember the five loaves of the five thousand, and how many baskets ye took up?
# Mark 6:44 And they that did eat of the loaves were about five thousand men.
# Mark 8:19 When I brake the five loaves among five thousand, how many baskets full of fragments took ye up? They say unto him, Twelve.
# Luke 9:14 For they were about five thousand men. And he said to his disciples, Make them sit down by fifties in a company.
# John 6:10 And Jesus said, Make the men sit down. Now there was much grass in the place. So the men sat down, in number about five thousand.
# Acts 4:4 Howbeit many of them which heard the word believed; and the number of the men was about five thousand.
# >>> b/61000
# Numbers 31:34 And threescore and one thousand asses,
# Ezra 2:69 They gave after their ability unto the treasure of the work threescore and one thousand drams of gold, and five thousand pound of silver, and one hundred priests' garments.
# >>> b/77
# Genesis 4:24;Judges 8:14;Ezra 8:35 (3 verses)
# >>> b/70
# Genesis 5:12;11:26;46:27;50:3;Exodus 1:5;15:27;24:1,9;38:29;Numbers 7:13,19,25,31,37,43,49,55,61,67,73,79,85;11:16,24-25;33:9;Deuteronomy 10:22;Judges 1:7;8:30;9:2,4-5,18,24,56;12:14;2 Kings 10:1,6-7;2 Chronicles 29:32;36:21;Ezra 8:7,14;Isaiah 23:15,17;Jeremiah 25:11-12;29:10;Ezekiel 8:11;41:12;Daniel 9:2,24;Zechariah 1:12;7:5;Matthew 18:22;Luke 10:1,17;Acts 23:23 (58 verses)
# >>> 
# >>> b/60
# Genesis 25:26;Leviticus 27:3,7;Numbers 7:88;Deuteronomy 3:4;Joshua 13:30;1 Kings 4:13,22;6:2;2 Kings 25:19;1 Chronicles 2:21,23;2 Chronicles 3:3;11:21;Ezra 6:3;8:13;Psalms 90:10;Song of Solomon 3:7;6:8;Jeremiah 52:25;Ezekiel 40:14;Daniel 3:1;Matthew 13:8,23;Mark 4:8,20;Luke 24:13;1 Timothy 5:9 (28 verses)
# >>> p(_)
# Genesis 25:26 And after that came his brother out, and his hand took hold on Esau's heel; and his name was called Jacob: and Isaac was threescore years old when she bare them.
# Leviticus 27:3 And thy estimation shall be of the male from twenty years old even unto sixty years old, even thy estimation shall be fifty shekels of silver, after the shekel of the sanctuary.
# Leviticus 27:7 And if it be from sixty years old and above; if it be a male, then thy estimation shall be fifteen shekels, and for the female ten shekels.
# Numbers 7:88 And all the oxen for the sacrifice of the peace offerings were twenty and four bullocks, the rams sixty, the he goats sixty, the lambs of the first year sixty. This was the dedication of the altar, after that it was anointed.
# Deuteronomy 3:4 And we took all his cities at that time, there was not a city which we took not from them, threescore cities, all the region of Argob, the kingdom of Og in Bashan.
# Joshua 13:30 And their coast was from Mahanaim, all Bashan, all the kingdom of Og king of Bashan, and all the towns of Jair, which are in Bashan, threescore cities:
# 1 Kings 4:13 The son of Geber, in Ramothgilead; to him pertained the towns of Jair the son of Manasseh, which are in Gilead; to him also pertained the region of Argob, which is in Bashan, threescore great cities with walls and brasen bars:
# 1 Kings 4:22 And Solomon's provision for one day was thirty measures of fine flour, and threescore measures of meal,
# 1 Kings 6:2 And the house which king Solomon built for the LORD, the length thereof was threescore cubits, and the breadth thereof twenty cubits, and the height thereof thirty cubits.
# 2 Kings 25:19 And out of the city he took an officer that was set over the men of war, and five men of them that were in the king's presence, which were found in the city, and the principal scribe of the host, which mustered the people of the land, and threescore men of the people of the land that were found in the city:
# 1 Chronicles 2:21 And afterward Hezron went in to the daughter of Machir the father of Gilead, whom he married when he was threescore years old; and she bare him Segub.
# 1 Chronicles 2:23 And he took Geshur, and Aram, with the towns of Jair, from them, with Kenath, and the towns thereof, even threescore cities. All these belonged to the sons of Machir the father of Gilead.
# 2 Chronicles 3:3 Now these are the things wherein Solomon was instructed for the building of the house of God. The length by cubits after the first measure was threescore cubits, and the breadth twenty cubits.
# 2 Chronicles 11:21 And Rehoboam loved Maachah the daughter of Absalom above all his wives and his concubines: (for he took eighteen wives, and threescore concubines; and begat twenty and eight sons, and threescore daughters.)
# Ezra 6:3 In the first year of Cyrus the king the same Cyrus the king made a decree concerning the house of God at Jerusalem, Let the house be builded, the place where they offered sacrifices, and let the foundations thereof be strongly laid; the height thereof threescore cubits, and the breadth thereof threescore cubits;
# Ezra 8:13 And of the last sons of Adonikam, whose names are these, Eliphelet, Jeiel, and Shemaiah, and with them threescore males.
# Psalms 90:10 The days of our years are threescore years and ten; and if by reason of strength they be fourscore years, yet is their strength labour and sorrow; for it is soon cut off, and we fly away.
# Song of Solomon 3:7 Behold his bed, which is Solomon's; threescore valiant men are about it, of the valiant of Israel.
# Song of Solomon 6:8 There are threescore queens, and fourscore concubines, and virgins without number.
# Jeremiah 52:25 He took also out of the city an eunuch, which had the charge of the men of war; and seven men of them that were near the king's person, which were found in the city; and the principal scribe of the host, who mustered the people of the land; and threescore men of the people of the land, that were found in the midst of the city.
# Ezekiel 40:14 He made also posts of threescore cubits, even unto the post of the court round about the gate.
# Daniel 3:1 Nebuchadnezzar the king made an image of gold, whose height was threescore cubits, and the breadth thereof six cubits: he set it up in the plain of Dura, in the province of Babylon.
# Matthew 13:8 But other fell into good ground, and brought forth fruit, some an hundredfold, some sixtyfold, some thirtyfold.
# Matthew 13:23 But he that received seed into the good ground is he that heareth the word, and understandeth it; which also beareth fruit, and bringeth forth, some an hundredfold, some sixty, some thirty.
# Mark 4:8 And other fell on good ground, and did yield fruit that sprang up and increased; and brought forth, some thirty, and some sixty, and some an hundred.
# Mark 4:20 And these are they which are sown on good ground; such as hear the word, and receive it, and bring forth fruit, some thirtyfold, some sixty, and some an hundred.
# Luke 24:13 And, behold, two of them went that same day to a village called Emmaus, which was from Jerusalem about threescore furlongs.
# 1 Timothy 5:9 Let not a widow be taken into the number under threescore years old, having been the wife of one man.
# >>> [(v,v.numbers()) for v in b//'score']@p
# (Genesis 16:16 And Abram was fourscore and six years old, when Hagar bare Ishmael to Abram., [86])
# (Genesis 25:7 And these are the days of the years of Abraham's life which he lived, an hundred threescore and fifteen years., [175])
# (Genesis 25:26 And after that came his brother out, and his hand took hold on Esau's heel; and his name was called Jacob: and Isaac was threescore years old when she bare them., [60])
# (Genesis 35:28 And the days of Isaac were an hundred and fourscore years., [180])
# (Genesis 46:26 All the souls that came with Jacob into Egypt, which came out of his loins, besides Jacob's sons' wives, all the souls were threescore and six;, [66])
# (Genesis 46:27 And the sons of Joseph, which were born him in Egypt, were two souls: all the souls of the house of Jacob, which came into Egypt, were threescore and ten., [2, 70])
# (Genesis 50:3 And forty days were fulfilled for him; for so are fulfilled the days of those which are embalmed: and the Egyptians mourned for him threescore and ten days., [40, 70])
# (Exodus 7:7 And Moses was fourscore years old, and Aaron fourscore and three years old, when they spake unto Pharaoh., [80, 83])
# (Exodus 15:27 And they came to Elim, where were twelve wells of water, and threescore and ten palm trees: and they encamped there by the waters., [12, 70])
# (Exodus 38:25 And the silver of them that were numbered of the congregation was an hundred talents, and a thousand seven hundred and threescore and fifteen shekels, after the shekel of the sanctuary:, [100, 1775])
# (Leviticus 12:5 But if she bear a maid child, then she shall be unclean two weeks, as in her separation: and she shall continue in the blood of her purifying threescore and six days., [2, 66])
# (Numbers 1:27 Those that were numbered of them, even of the tribe of Judah, were threescore and fourteen thousand and six hundred., [74600])
# (Numbers 1:39 Those that were numbered of them, even of the tribe of Dan, were threescore and two thousand and seven hundred., [62700])
# (Numbers 2:4 And his host, and those that were numbered of them, were threescore and fourteen thousand and six hundred., [74600])
# (Numbers 2:9 All that were numbered in the camp of Judah were an hundred thousand and fourscore thousand and six thousand and four hundred, throughout their armies. These shall first set forth., [186400, 1])
# (Numbers 2:26 And his host, and those that were numbered of them, were threescore and two thousand and seven hundred., [62700])
# (Numbers 3:43 And all the firstborn males by the number of names, from a month old and upward, of those that were numbered of them, were twenty and two thousand two hundred and threescore and thirteen., [22273])
# (Numbers 3:46 And for those that are to be redeemed of the two hundred and threescore and thirteen of the firstborn of the children of Israel, which are more than the Levites;, [273])
# (Numbers 3:50 Of the firstborn of the children of Israel took he the money; a thousand three hundred and threescore and five shekels, after the shekel of the sanctuary:, [1365])
# (Numbers 4:48 Even those that were numbered of them, were eight thousand and five hundred and fourscore,, [8580])
# (Numbers 26:22 These are the families of Judah according to those that were numbered of them, threescore and sixteen thousand and five hundred., [76500])
# (Numbers 26:25 These are the families of Issachar according to those that were numbered of them, threescore and four thousand and three hundred., [64300])
# (Numbers 26:27 These are the families of the Zebulunites according to those that were numbered of them, threescore thousand and five hundred., [60500])
# (Numbers 26:43 All the families of the Shuhamites, according to those that were numbered of them, were threescore and four thousand and four hundred., [64400])
# (Numbers 31:33 And threescore and twelve thousand beeves,, [72000])
# (Numbers 31:34 And threescore and one thousand asses,, [61000])
# (Numbers 31:37 And the LORD's tribute of the sheep was six hundred and threescore and fifteen., [675])
# (Numbers 31:38 And the beeves were thirty and six thousand; of which the LORD's tribute was threescore and twelve., [36000, 72])
# (Numbers 31:39 And the asses were thirty thousand and five hundred; of which the LORD's tribute was threescore and one., [30500, 61])
# (Numbers 33:9 And they removed from Marah, and came unto Elim: and in Elim were twelve fountains of water, and threescore and ten palm trees; and they pitched there., [12, 70])
# (Deuteronomy 3:4 And we took all his cities at that time, there was not a city which we took not from them, threescore cities, all the region of Argob, the kingdom of Og in Bashan., [60])
# (Deuteronomy 10:22 Thy fathers went down into Egypt with threescore and ten persons; and now the LORD thy God hath made thee as the stars of heaven for multitude., [70])
# (Joshua 13:30 And their coast was from Mahanaim, all Bashan, all the kingdom of Og king of Bashan, and all the towns of Jair, which are in Bashan, threescore cities:, [60])
# (Joshua 14:10 And now, behold, the LORD hath kept me alive, as he said, these forty and five years, even since the LORD spake this word unto Moses, while the children of Israel wandered in the wilderness: and now, lo, I am this day fourscore and five years old., [45, 85])
# (Judges 1:7 And Adonibezek said, Threescore and ten kings, having their thumbs and their great toes cut off, gathered their meat under my table: as I have done, so God hath requited me. And they brought him to Jerusalem, and there he died., [70])
# (Judges 3:30 So Moab was subdued that day under the hand of Israel. And the land had rest fourscore years., [80])
# (Judges 8:14 And caught a young man of the men of Succoth, and enquired of him: and he described unto him the princes of Succoth, and the elders thereof, even threescore and seventeen men., [77])
# (Judges 8:30 And Gideon had threescore and ten sons of his body begotten: for he had many wives., [70])
# (Judges 9:2 Speak, I pray you, in the ears of all the men of Shechem, Whether is better for you, either that all the sons of Jerubbaal, which are threescore and ten persons, reign over you, or that one reign over you? remember also that I am your bone and your flesh., [70, 1])
# (Judges 9:4 And they gave him threescore and ten pieces of silver out of the house of Baalberith, wherewith Abimelech hired vain and light persons, which followed him., [70])
# (Judges 9:5 And he went unto his father's house at Ophrah, and slew his brethren the sons of Jerubbaal, being threescore and ten persons, upon one stone: notwithstanding yet Jotham the youngest son of Jerubbaal was left; for he hid himself., [70, 1])
# (Judges 9:18 And ye are risen up against my father's house this day, and have slain his sons, threescore and ten persons, upon one stone, and have made Abimelech, the son of his maidservant, king over the men of Shechem, because he is your brother;), [70, 1])
# (Judges 9:24 That the cruelty done to the threescore and ten sons of Jerubbaal might come, and their blood be laid upon Abimelech their brother, which slew them; and upon the men of Shechem, which aided him in the killing of his brethren., [70])
# (Judges 12:14 And he had forty sons and thirty nephews, that rode on threescore and ten ass colts: and he judged Israel eight years., [40, 30, 70, 8])
# (1 Samuel 6:19 And he smote the men of Bethshemesh, because they had looked into the ark of the LORD, even he smote of the people fifty thousand and threescore and ten men: and the people lamented, because the LORD had smitten many of the people with a great slaughter., [50070])
# (1 Samuel 22:18 And the king said to Doeg, Turn thou, and fall upon the priests. And Doeg the Edomite turned, and he fell upon the priests, and slew on that day fourscore and five persons that did wear a linen ephod., [85])
# (2 Samuel 2:31 But the servants of David had smitten of Benjamin, and of Abner's men, so that three hundred and threescore men died., [360])
# (2 Samuel 19:32 Now Barzillai was a very aged man, even fourscore years old: and he had provided the king of sustenance while he lay at Mahanaim; for he was a very great man., [80])
# (2 Samuel 19:35 I am this day fourscore years old: and can I discern between good and evil? can thy servant taste what I eat or what I drink? can I hear any more the voice of singing men and singing women? wherefore then should thy servant be yet a burden unto my lord the king?, [80])
# (1 Kings 4:13 The son of Geber, in Ramothgilead; to him pertained the towns of Jair the son of Manasseh, which are in Gilead; to him also pertained the region of Argob, which is in Bashan, threescore great cities with walls and brasen bars:, [60])
# (1 Kings 4:22 And Solomon's provision for one day was thirty measures of fine flour, and threescore measures of meal,, [1, 30, 60])
# (1 Kings 5:15 And Solomon had threescore and ten thousand that bare burdens, and fourscore thousand hewers in the mountains;, [70000, 80000])
# (1 Kings 6:2 And the house which king Solomon built for the LORD, the length thereof was threescore cubits, and the breadth thereof twenty cubits, and the height thereof thirty cubits., [60, 20, 30])
# (1 Kings 9:14 And Hiram sent to the king sixscore talents of gold., [])
# (1 Kings 10:14 Now the weight of gold that came to Solomon in one year was six hundred threescore and six talents of gold,, [1, 666])
# (1 Kings 12:21 And when Rehoboam was come to Jerusalem, he assembled all the house of Judah, with the tribe of Benjamin, an hundred and fourscore thousand chosen men, which were warriors, to fight against the house of Israel, to bring the kingdom again to Rehoboam the son of Solomon., [180000])
# (2 Kings 6:25 And there was a great famine in Samaria: and, behold, they besieged it, until an ass's head was sold for fourscore pieces of silver, and the fourth part of a cab of dove's dung for five pieces of silver., [80, 4, 5])
# (2 Kings 10:24 And when they went in to offer sacrifices and burnt offerings, Jehu appointed fourscore men without, and said, If any of the men whom I have brought into your hands escape, he that letteth him go, his life shall be for the life of him., [80])
# (2 Kings 19:35 And it came to pass that night, that the angel of the LORD went out, and smote in the camp of the Assyrians an hundred fourscore and five thousand: and when they arose early in the morning, behold, they were all dead corpses., [185000])
# (2 Kings 25:19 And out of the city he took an officer that was set over the men of war, and five men of them that were in the king's presence, which were found in the city, and the principal scribe of the host, which mustered the people of the land, and threescore men of the people of the land that were found in the city:, [5, 60])
# (1 Chronicles 2:21 And afterward Hezron went in to the daughter of Machir the father of Gilead, whom he married when he was threescore years old; and she bare him Segub., [60])
# (1 Chronicles 2:23 And he took Geshur, and Aram, with the towns of Jair, from them, with Kenath, and the towns thereof, even threescore cities. All these belonged to the sons of Machir the father of Gilead., [60])
# (1 Chronicles 5:18 The sons of Reuben, and the Gadites, and half the tribe of Manasseh, of valiant men, men able to bear buckler and sword, and to shoot with bow, and skilful in war, were four and forty thousand seven hundred and threescore, that went out to the war., [44760])
# (1 Chronicles 7:5 And their brethren among all the families of Issachar were valiant men of might, reckoned in all by their genealogies fourscore and seven thousand., [87000])
# (1 Chronicles 9:13 And their brethren, heads of the house of their fathers, a thousand and seven hundred and threescore; very able men for the work of the service of the house of God., [1760])
# (1 Chronicles 15:9 Of the sons of Hebron; Eliel the chief, and his brethren fourscore:, [80])
# (1 Chronicles 16:38 And Obededom with their brethren, threescore and eight; Obededom also the son of Jeduthun and Hosah to be porters:, [68])
# (1 Chronicles 21:5 And Joab gave the sum of the number of the people unto David. And all they of Israel were a thousand thousand and an hundred thousand men that drew sword: and Judah was four hundred threescore and ten thousand men that drew sword., [102000, 470000])
# (1 Chronicles 25:7 So the number of them, with their brethren that were instructed in the songs of the LORD, even all that were cunning, was two hundred fourscore and eight., [288])
# (1 Chronicles 26:8 All these of the sons of Obededom: they and their sons and their brethren, able men for strength for the service, were threescore and two of Obededom., [62])
# (2 Chronicles 2:2 And Solomon told out threescore and ten thousand men to bear burdens, and fourscore thousand to hew in the mountain, and three thousand and six hundred to oversee them., [70000, 80000, 3600])
# (2 Chronicles 2:18 And he set threescore and ten thousand of them to be bearers of burdens, and fourscore thousand to be hewers in the mountain, and three thousand and six hundred overseers to set the people a work., [70000, 80000, 3600])
# (2 Chronicles 3:3 Now these are the things wherein Solomon was instructed for the building of the house of God. The length by cubits after the first measure was threescore cubits, and the breadth twenty cubits., [1, 60, 20])
# (2 Chronicles 9:13 Now the weight of gold that came to Solomon in one year was six hundred and threescore and six talents of gold;, [1, 666])
# (2 Chronicles 11:1 And when Rehoboam was come to Jerusalem, he gathered of the house of Judah and Benjamin an hundred and fourscore thousand chosen men, which were warriors, to fight against Israel, that he might bring the kingdom again to Rehoboam., [180000])
# (2 Chronicles 11:21 And Rehoboam loved Maachah the daughter of Absalom above all his wives and his concubines: (for he took eighteen wives, and threescore concubines; and begat twenty and eight sons, and threescore daughters.), [18, 60, 28, 60])
# (2 Chronicles 12:3 With twelve hundred chariots, and threescore thousand horsemen: and the people were without number that came with him out of Egypt; the Lubims, the Sukkiims, and the Ethiopians., [1200, 60000])
# (2 Chronicles 14:8 And Asa had an army of men that bare targets and spears, out of Judah three hundred thousand; and out of Benjamin, that bare shields and drew bows, two hundred and fourscore thousand: all these were mighty men of valour., [300000, 280000])
# (2 Chronicles 17:15 And next to him was Jehohanan the captain, and with him two hundred and fourscore thousand., [280000])
# (2 Chronicles 17:18 And next him was Jehozabad, and with him an hundred and fourscore thousand ready prepared for the war., [180000])
# (2 Chronicles 26:17 And Azariah the priest went in after him, and with him fourscore priests of the LORD, that were valiant men:, [80])
# (2 Chronicles 29:32 And the number of the burnt offerings, which the congregation brought, was threescore and ten bullocks, an hundred rams, and two hundred lambs: all these were for a burnt offering to the LORD., [70, 100, 200])
# (2 Chronicles 36:21 To fulfil the word of the LORD by the mouth of Jeremiah, until the land had enjoyed her sabbaths: for as long as she lay desolate she kept sabbath, to fulfil threescore and ten years., [70])
# (Ezra 2:9 The children of Zaccai, seven hundred and threescore., [760])
# (Ezra 2:64 The whole congregation together was forty and two thousand three hundred and threescore,, [42360])
# (Ezra 2:69 They gave after their ability unto the treasure of the work threescore and one thousand drams of gold, and five thousand pound of silver, and one hundred priests' garments., [61000, 5000, 100])
# (Ezra 6:3 In the first year of Cyrus the king the same Cyrus the king made a decree concerning the house of God at Jerusalem, Let the house be builded, the place where they offered sacrifices, and let the foundations thereof be strongly laid; the height thereof threescore cubits, and the breadth thereof threescore cubits;, [1, 60, 60])
# (Ezra 8:8 And of the sons of Shephatiah; Zebadiah the son of Michael, and with him fourscore males., [80])
# (Ezra 8:10 And of the sons of Shelomith; the son of Josiphiah, and with him an hundred and threescore males., [160])
# (Ezra 8:13 And of the last sons of Adonikam, whose names are these, Eliphelet, Jeiel, and Shemaiah, and with them threescore males., [60])
# (Nehemiah 7:14 The children of Zaccai, seven hundred and threescore., [760])
# (Nehemiah 7:18 The children of Adonikam, six hundred threescore and seven., [667])
# (Nehemiah 7:19 The children of Bigvai, two thousand threescore and seven., [2067])
# (Nehemiah 7:26 The men of Bethlehem and Netophah, an hundred fourscore and eight., [188])
# (Nehemiah 7:66 The whole congregation together was forty and two thousand three hundred and threescore,, [42360])
# (Nehemiah 7:72 And that which the rest of the people gave was twenty thousand drams of gold, and two thousand pound of silver, and threescore and seven priests' garments., [20000, 2000, 67])
# (Nehemiah 11:6 All the sons of Perez that dwelt at Jerusalem were four hundred threescore and eight valiant men., [468])
# (Nehemiah 11:18 All the Levites in the holy city were two hundred fourscore and four., [284])
# (Esther 1:4 When he shewed the riches of his glorious kingdom and the honour of his excellent majesty many days, even an hundred and fourscore days., [180])
# (Psalms 90:10 The days of our years are threescore years and ten; and if by reason of strength they be fourscore years, yet is their strength labour and sorrow; for it is soon cut off, and we fly away., [60, 10, 80])
# (Song of Solomon 3:7 Behold his bed, which is Solomon's; threescore valiant men are about it, of the valiant of Israel., [60])
# (Song of Solomon 6:8 There are threescore queens, and fourscore concubines, and virgins without number., [60, 80])
# (Isaiah 7:8 For the head of Syria is Damascus, and the head of Damascus is Rezin; and within threescore and five years shall Ephraim be broken, that it be not a people., [65])
# (Isaiah 37:36 Then the angel of the LORD went forth, and smote in the camp of the Assyrians a hundred and fourscore and five thousand: and when they arose early in the morning, behold, they were all dead corpses., [185000])
# (Jeremiah 41:5 That there came certain from Shechem, from Shiloh, and from Samaria, even fourscore men, having their beards shaven, and their clothes rent, and having cut themselves, with offerings and incense in their hand, to bring them to the house of the LORD., [80])
# (Jeremiah 52:25 He took also out of the city an eunuch, which had the charge of the men of war; and seven men of them that were near the king's person, which were found in the city; and the principal scribe of the host, who mustered the people of the land; and threescore men of the people of the land, that were found in the midst of the city., [7, 60])
# (Ezekiel 40:14 He made also posts of threescore cubits, even unto the post of the court round about the gate., [60])
# (Daniel 3:1 Nebuchadnezzar the king made an image of gold, whose height was threescore cubits, and the breadth thereof six cubits: he set it up in the plain of Dura, in the province of Babylon., [60, 6])
# (Daniel 5:31 And Darius the Median took the kingdom, being about threescore and two years old., [62])
# (Daniel 9:25 Know therefore and understand, that from the going forth of the commandment to restore and to build Jerusalem unto the Messiah the Prince shall be seven weeks, and threescore and two weeks: the street shall be built again, and the wall, even in troublous times., [7, 62])
# (Daniel 9:26 And after threescore and two weeks shall Messiah be cut off, but not for himself: and the people of the prince that shall come shall destroy the city and the sanctuary; and the end thereof shall be with a flood, and unto the end of the war desolations are determined., [62])
# (Jonah 4:11 And should not I spare Nineveh, that great city, wherein are more then sixscore thousand persons that cannot discern between their right hand and their left hand; and also much cattle?, [1000])
# (Zechariah 1:12 Then the angel of the LORD answered and said, O LORD of hosts, how long wilt thou not have mercy on Jerusalem and on the cities of Judah, against which thou hast had indignation these threescore and ten years?, [70])
# (Luke 2:37 And she was a widow of about fourscore and four years, which departed not from the temple, but served God with fastings and prayers night and day., [84])
# (Luke 16:7 Then said he to another, And how much owest thou? And he said, An hundred measures of wheat. And he said unto him, Take thy bill, and write fourscore., [100, 80])
# (Luke 24:13 And, behold, two of them went that same day to a village called Emmaus, which was from Jerusalem about threescore furlongs., [2, 60])
# (Acts 7:14 Then sent Joseph, and called his father Jacob to him, and all his kindred, threescore and fifteen souls., [75])
# (Acts 23:23 And he called unto him two centurions, saying, Make ready two hundred soldiers to go to Caesarea, and horsemen threescore and ten, and spearmen two hundred, at the third hour of the night;, [2, 200, 70, 200, 3])
# (Acts 27:37 And we were in all in the ship two hundred threescore and sixteen souls., [276])
# (1 Timothy 5:9 Let not a widow be taken into the number under threescore years old, having been the wife of one man., [60, 1])
# (Revelation 11:3 And I will give power unto my two witnesses, and they shall prophesy a thousand two hundred and threescore days, clothed in sackcloth., [2, 1260])
# (Revelation 12:6 And the woman fled into the wilderness, where she hath a place prepared of God, that they should feed her there a thousand two hundred and threescore days., [1260])
# (Revelation 13:18 Here is wisdom. Let him that hath understanding count the number of the beast: for it is the number of a man; and his number is Six hundred threescore and six., [666])
# [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
# >>> 
